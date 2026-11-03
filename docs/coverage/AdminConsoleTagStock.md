# Coverage E2E — Admin Console > Tag Stock

Sumber: `admin-console/tag-stock/TestCases/tc-tag-stock.md` (936 ID unik `TC-AC-ACTS-1`–`995`, bernomor tidak kontigu). Suite: `specs/AdminConsole/TagStock/`. Prefix: `AC` + `ACTS` (`TC-AC-ACTS-E2E-*`). Status semua spec: `draft`, belum diaudit.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 936 TC masuk 266 spec; tidak ada TC hanya-BE (`tc-tag-stock-backend.md` tidak ada). Setiap TC terpetakan ke tepat satu spec.

## TC hanya-BE (tidak masuk spec)

Tidak ada.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-ACTS-E2E-001-screening-stock-list-breadcrumb-header-kolom-dan-footer | Screening Stock List: Breadcrumb, Header, Kolom, Footer, Urutan Default, Tanpa Checkbox, dan Aria-Label Tabel | FE+BE | 24 | 1, 15, 33, 34, 35, 812 |
| TC-AC-ACTS-E2E-002-isi-sel-stock-list-tanpa-kuota-icon-tag-type-badge-dan-device-name-panjang | Isi Sel Stock List: Tanpa Kuota Allocated, Icon TAG Type, Badge Brand dan Model Terpotong, Device Name Panjang, dan Header Tidak Wrap | FE+BE | 42 | 14, 20, 21, 22, 23, 854 |
| TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | Metrik Stock List: SKU Tanpa Unit, Total Registered, Available, Damaged/Missing, Add Stock pada SKU Kosong, dan Sort Last Updated | FE+BE | 28 | 2, 3, 9, 10, 11, 12, 13, 888 |
| TC-AC-ACTS-E2E-004-navigasi-stock-list-detail-sku-dan-add-stock-per-tag-type | Navigasi dari Stock List: Klik Device Name, Row Action Detail, Add Stock per TAG Type, dan Ctrl+Klik Tab Baru | FE+BE | 38 | 5, 6, 7, 8, 752, 753 |
| TC-AC-ACTS-E2E-005-distributor-stock-list-metrik-di-scope-unit-sendiri | Distributor di Stock List: Total Registered, Available, Damaged/Missing, In Use, dan Last Updated di-Scope ke Unit Sendiri | FE+BE | 29 | 16, 17, 18, 19, 890 |
| TC-AC-ACTS-E2E-006-stock-list-mengikuti-aksi-delete-audit-dan-sku-baru | Stock List Mengikuti Aksi: Available Mengikuti Transisi Status, Mutasi saat Terfilter, Urutan Deterministik, dan Last Updated Setelah Delete Unit Terakhir | FE+BE | 37 | 4, 97, 99, 889 |
| TC-AC-ACTS-E2E-007-guided-tooltip-stock-list-empat-step-navigasi-flag-dan-keyboard | Guided Tooltip Stock List: Empat Step, Navigasi Next/Back/Done/Skip, Flag Seen, Keluar Tanpa Selesai, dan Keyboard | FE+BE | 47 | 24, 25, 26, 27, 28 |
| TC-AC-ACTS-E2E-008-retensi-state-stock-list-back-refresh-reset-menu-dan-cache-setup-column | Retensi State Stock List: Back dari Detail SKU, Refresh F5, Reset Klik Menu Sidebar, dan Cache Setup Column Independen | FE+BE | 32 | 30, 31, 32, 112, 113 |
| TC-AC-ACTS-E2E-009-sort-stock-list-kelas-teks-dan-label | Sort Stock List: Kelas Teks (Device Name, SKU, Type) dan Kelas Label (TAG Type, Brand, Model/Type) | FE+BE | 14 | 36, 37 |
| TC-AC-ACTS-E2E-010-sort-stock-list-kelas-numerik-tanggal-dan-kolom-non-sortable | Sort Stock List: Kelas Numerik, Kelas Tanggal Last Updated, dan Kolom Photo Non-Sortable | FE+BE | 18 | 38, 39, 40 |
| TC-AC-ACTS-E2E-011-search-stock-list-siklus-kelas-teks-dan-kolom-tanpa-search | Search Stock List: Siklus Toolbar, Kelas Teks, dan Kolom Photo/Last Updated Tanpa Search | FE+BE | 41 | 41, 42, 46 |
| TC-AC-ACTS-E2E-012-search-stock-list-badge-enum-dan-visibilitas-kolom-brand | Search Stock List: Kelas Badge, Kelas Enum, dan Search Terikat Visibilitas Kolom Brand | FE+BE | 33 | 43, 44, 47, 48 |
| TC-AC-ACTS-E2E-013-search-stock-list-numerik-dan-alur-search-filter | Search Stock List: Kelas Numerik serta Alur Search lalu Filter dan Filter lalu Search | FE+BE | 18 | 45, 49, 50 |
| TC-AC-ACTS-E2E-014-filter-stock-list-screening-panel-range-dan-field-sku | Filter Stock List: Screening Panel, Field SKU Tidak Ada, Numeric Range, dan Min/Max Inklusif | FE+BE | 26 | 51, 54, 91, 92, 853 |
| TC-AC-ACTS-E2E-015-filter-stock-list-dropdown-date-range-dan-opsi-distinct | Filter Stock List: Dropdown Multi-Select, Date Range, dan Opsi Dropdown Distinct | FE+BE | 19 | 52, 53, 55 |
| TC-AC-ACTS-E2E-016-filter-stock-list-kombinasi-and-dan-independen-dari-column-visibility | Filter Stock List: Kombinasi AND dan Filter Independen dari Column Visibility | FE+BE | 14 | 56, 790 |
| TC-AC-ACTS-E2E-017-setup-column-stock-list-screening-satu-kolom-tersisa-dan-pin-ke-4 | Setup Column Stock List: Screening Overlay dan Popup, Satu Kolom Tersisa, dan Pin ke-4 Diblokir | FE+BE | 23 | 57, 58, 64, 65 |
| TC-AC-ACTS-E2E-018-setup-column-stock-list-ceklis-dan-unceklis-kolom | Setup Column Stock List: Ceklis dan Unceklis Dua Belas Kolom | FE+BE | 13 | 59 |
| TC-AC-ACTS-E2E-019-setup-column-stock-list-urutan-pin-reset-dan-tutup | Setup Column Stock List: Geser Urutan, Pin dan Unpin, Reset to Default, serta Tutup dengan (X) atau Esc | FE+BE | 26 | 60, 61, 62, 63 |
| TC-AC-ACTS-E2E-020-pagination-dan-state-stock-list-kosong-error-dan-loading | State Stock List: Empty State, Empty-Filtered, Error Load, dan Loading | FE+BE | 17 | 67, 68, 69, 70 |
| TC-AC-ACTS-E2E-021-download-stock-list-csv-dan-xlsx-nama-berkas | Download Stock List: Nama Berkas CSV dan XLSX | FE+BE | 8 | 71, 72 |
| TC-AC-ACTS-E2E-022-lintas-permukaan-tooltip-table-tools-dan-search-spasi-tepi | Lintas Enam Permukaan: Tooltip Table Tools dan Column Visibility serta Search dengan Spasi di Tepi | FE+BE | 24 | 74, 75 |
| TC-AC-ACTS-E2E-023-lintas-permukaan-search-literal-dan-spasi-tengah | Lintas Enam Permukaan: Search Teks Literal (Payload Script dan Karakter Pola) dan Spasi di Tengah Query | FE+BE | 11 | 76, 77 |
| TC-AC-ACTS-E2E-024-lintas-permukaan-pagination-halaman-tidak-valid-page-size-dan-sort | Lintas Enam Permukaan: Pagination Nomor Halaman Tidak Valid, Ganti Page Size, dan Ganti Sort | FE+BE | 15 | 78, 79, 80 |
| TC-AC-ACTS-E2E-025-lintas-permukaan-search-dan-apply-filter-reset-halaman | Lintas Enam Permukaan: Search dan Apply Filter di Halaman Lebih dari 1 Kembali ke Halaman 1 | FE+BE | 10 | 81 |
| TC-AC-ACTS-E2E-026-lintas-permukaan-independensi-clear-filter-dan-clear-search | Lintas Enam Permukaan: Independensi Kontrol, Clear Filter Menjaga Search dan Sort serta Clear Search Menjaga Filter dan Sort | FE+BE | 13 | 93, 94 |
| TC-AC-ACTS-E2E-027-lintas-permukaan-independensi-ganti-sort-dan-pemulihan-empty-state | Lintas Enam Permukaan: Independensi Ganti Kolom Sort dan Pemulihan Empty State saat Kontrol Dilepas | FE+BE | 13 | 95, 96 |
| TC-AC-ACTS-E2E-028-role-matrix-visibilitas-elemen-total-control-dan-default-user | Role Matrix: Visibilitas Elemen TAG > Stock oleh Total Control dan Default User | FE+BE | 43 | 114, 115 |
| TC-AC-ACTS-E2E-029-role-matrix-visibilitas-elemen-read-only-dan-additional-approver | Role Matrix: Visibilitas Elemen TAG > Stock oleh Read Only dan Additional Approver Tanpa Capability | FE+BE | 36 | 116, 117 |
| TC-AC-ACTS-E2E-030-role-matrix-visibilitas-elemen-manage-tag-stock-create-dan-update | Role Matrix: Visibilitas Elemen TAG > Stock oleh Pemegang Manage TAG Stock Read+Create dan Read+Update | FE+BE | 37 | 118, 119 |
| TC-AC-ACTS-E2E-031-role-matrix-visibilitas-elemen-manage-tag-stock-delete-dan-read | Role Matrix: Visibilitas Elemen TAG > Stock oleh Pemegang Manage TAG Stock Read+Delete dan Read Saja | FE+BE | 37 | 120, 121 |
| TC-AC-ACTS-E2E-032-role-matrix-visibilitas-elemen-distributor-toggle-on-dan-off | Role Matrix: Visibilitas Elemen TAG > Stock oleh Distributor dengan Toggle Local Registration ON dan OFF | FE+BE | 37 | 122, 123 |
| TC-AC-ACTS-E2E-033-role-matrix-negatif-tanpa-akses-tag-stock-dan-sidebar | Role Matrix Negatif: Tanpa Akses TAG > Stock (Distributor Tanpa Role, Partner, Client, Role Lain), Direct URL Detail SKU, dan Menu Approvals > TAG Stock Hidden untuk Distributor | FE+BE | 34 | 124, 125, 126, 127, 136, 137 |
| TC-AC-ACTS-E2E-034-role-matrix-positif-eksekusi-add-stock-audit-dan-scan-distributor | Role Matrix Positif: Eksekusi Add Stock oleh Read+Create, Audit oleh Read+Update, serta Add Stock dan Audit oleh Distributor Toggle ON dan OFF, dan Item Sidebar TAG > Stock untuk Aktor Read | FE+BE | 36 | 128, 129, 130, 133, 134, 724 |
| TC-AC-ACTS-E2E-035-role-matrix-positif-delete-dan-approval-manage-delete-distributor-dan-additional-approver | Role Matrix Positif: Delete oleh Read+Delete dan Distributor serta Approve oleh Additional Approver | FE+BE | 17 | 131, 132, 135 |
| TC-AC-ACTS-E2E-036-role-matrix-read-only-dan-capability-parsial-aksi-tulis-hidden | Role Matrix: Aksi Tulis Hidden untuk Read Only dan Capability Parsial (Toolbar Tab Available, Delete by Scan, Checkbox, Bulk Bar, Review Approvals, TAG Log) | FE+BE | 34 | 296, 387, 816, 983 |
| TC-AC-ACTS-E2E-037-download-stock-list-isi-sel-xlsx | Download Stock List: Isi Sel XLSX per Tipe Kolom | FE+BE | 11 | 73 |
| TC-AC-ACTS-E2E-039-lintas-permukaan-filter-search-di-dalam-dropdown | Lintas Enam Permukaan: Filter, Search di Dalam Dropdown Mempersempit Opsi | FE+BE | 12 | 82 |
| TC-AC-ACTS-E2E-040-lintas-permukaan-filter-chip-dan-hapus-lewat-x | Lintas Enam Permukaan: Filter, Opsi Terpilih Tampil sebagai Chip dan Dihapus Lewat (X) | FE+BE | 13 | 83 |
| TC-AC-ACTS-E2E-041-lintas-permukaan-filter-uncheck-opsi-menghapus-chip | Lintas Enam Permukaan: Filter, Uncheck Opsi di Dropdown Menghapus Chip | FE+BE | 10 | 84 |
| TC-AC-ACTS-E2E-042-lintas-permukaan-filter-hapus-chip-lalu-apply | Lintas Enam Permukaan: Filter, Menghapus Chip lalu Apply Menyaring Ulang Tabel | FE+BE | 11 | 85 |
| TC-AC-ACTS-E2E-043-lintas-permukaan-filter-chip-more-saat-melebihi-lebar | Lintas Enam Permukaan: Filter, Opsi Melebihi Lebar Field Diringkas Chip +N more | FE+BE | 10 | 86 |
| TC-AC-ACTS-E2E-044-lintas-permukaan-filter-dropdown-loading-kosong-dan-stale | Lintas Enam Permukaan: Filter, Dropdown Loading, No options available, dan Nilai Stale | FE+BE | 18 | 87 |
| TC-AC-ACTS-E2E-045-lintas-permukaan-filter-tutup-panel-tanpa-apply-membuang-draft | Lintas Enam Permukaan: Filter, Menutup Panel Tanpa Apply Membuang Draft | FE+BE | 10 | 88 |
| TC-AC-ACTS-E2E-046-lintas-permukaan-filter-titik-aktif-pada-ikon-filter | Lintas Enam Permukaan: Filter, Ikon Filter Menampilkan Titik Aktif | FE+BE | 11 | 89 |
| TC-AC-ACTS-E2E-047-lintas-permukaan-filter-clear-field-mengosongkan-semua-field | Lintas Enam Permukaan: Filter, Tombol Clear Field Mengosongkan Semua Field | FE+BE | 10 | 90 |
| TC-AC-ACTS-E2E-048-add-stock-rfid-screening-sesi-scan-mengunci-halaman-dan-baris-ok | Add Stock RFID: Screening Idle, Sesi Scan Mengunci Halaman dengan Widget, Scan Baru Menjadi Baris OK, dan Mode Scan Terkunci | FE+BE | 35 | 139, 140, 141, 154 |
| TC-AC-ACTS-E2E-049-add-stock-rfid-duplikat-dalam-sesi-dan-baris-scan-tidak-lengkap | Add Stock RFID: Duplikat EPC atau UID dalam Sesi (Toast T-01) dan Baris Scan yang Hanya Membawa EPC atau UID (Toast T-22) | FE+BE | 32 | 142, 143, 149, 150 |
| TC-AC-ACTS-E2E-050-add-stock-rfid-remove-by-scan-disabled-hapus-baris-dan-toast | Add Stock RFID: Remove by Scan Disabled saat List Kosong, Hapus Baris yang Ada, dan TAG yang Tidak di List | FE+BE | 32 | 151, 152, 153 |
| TC-AC-ACTS-E2E-051-add-stock-rfid-checkbox-select-all-dan-dialog-remove | Add Stock RFID: Kolom Checkbox, Select All dan Unselect All, Bulk Action Bar Remove, serta Dialog Remove TAG dan TAGs | FE+BE | 42 | 868, 869, 870, 871 |
| TC-AC-ACTS-E2E-052-add-stock-rfid-remove-sukses-baris-waiting-dan-bar-non-interaktif | Add Stock RFID: Remove Sukses, Remove Baris Waiting for Approval, dan Checkbox serta Bulk Bar Non-Interaktif selama Sesi Scan | FE+BE | 52 | 872, 873, 874 |
| TC-AC-ACTS-E2E-053-add-stock-rfid-cancel-dan-meninggalkan-halaman-dengan-list | Add Stock RFID: Cancel dan Meninggalkan Halaman dengan List Berisi atau Kosong (Dialog Unsaved Changes, Leave dan Cancel) | FE+BE | 40 | 155, 156, 157, 158, 893, 894 |
| TC-AC-ACTS-E2E-054-add-stock-rfid-reload-back-fisik-dan-pindah-tab-saat-sesi-aktif | Add Stock RFID: Reload atau Tutup Tab, Back Fisik (Modal RFID Scan Stopped), dan Pindah Tab Browser saat List Berisi atau Sesi Aktif | FE+BE | 26 | 159, 160, 161, 162, 796 |
| TC-AC-ACTS-E2E-055-add-stock-rfid-reader-tidak-terhubung-putus-saat-sesi-dan-idle | Add Stock RFID: Reader Tidak Terhubung (Toast V-03), Putus di Tengah Sesi, Putus saat Idle, dan Satu dari Dua Reader Putus | FE+BE | 33 | 163, 164, 165, 166 |
| TC-AC-ACTS-E2E-056-add-stock-rfid-submit-ok-kosong-klik-ganda-sku-tidak-valid-dan-tanpa-batas | Add Stock RFID: Submit List Kosong (V-05), Semua OK, Kembali ke Detail SKU, Klik Ganda, dan SKU Tidak Valid saat Submit | FE+BE | 52 | 167, 168, 174, 720, 744 |
| TC-AC-ACTS-E2E-057-add-stock-rfid-match-existing-waiting-for-approval-per-identifier | Add Stock RFID: Scan Cocok Unit Existing Menjadi Waiting for Approval (EPC Saja, UID Saja, Keduanya, Dua Unit Berbeda) | FE+BE | 30 | 144, 145, 146, 147, 148 |
| TC-AC-ACTS-E2E-058-add-stock-rfid-submit-waiting-partial-register-dan-bentuk-tunggal-jamak | Add Stock RFID: Submit Semua Waiting, Campuran OK dan Waiting (Dialog Partial Register), Cancel dan Continue, serta Bentuk Tunggal dan Jamak | FE+BE | 59 | 169, 170, 171, 172, 746, 761 |
| TC-AC-ACTS-E2E-059-add-stock-rfid-normalisasi-identifier-unit-rejected-dan-submit-ulang | Add Stock RFID: Normalisasi Identifier, Identifier Unit Rejected Terdaftar sebagai Unit Baru, dan Submit Ulang Batch yang Sama | FE+BE | 56 | 176, 740, 745 |
| TC-AC-ACTS-E2E-060-add-stock-rfid-bypass-e2a-total-control-pada-batch-campuran | Add Stock RFID: Bypass E2a oleh Total Control, Tidak Menampilkan Waiting, dan Unit Bypass Tidak Masuk Quantity dan Success Event Log | FE+BE | 32 | 181, 778 |
| TC-AC-ACTS-E2E-061-add-stock-rfid-detail-ui-aria-live-tooltip-badge-kartu-sku-dan-saving-state | Add Stock RFID: Detail UI (Widget aria-live, Badge OK Tanpa Tooltip, Kartu SKU Terpotong, dan Saving State Submit) | FE+BE | 27 | 177, 179, 180, 857 |
| TC-AC-ACTS-E2E-062-add-stock-rfid-navigasi-breadcrumb-url-gps-dan-dialog-modul | Add Stock: Breadcrumb Stock dan Detail, URL Add Stock Scan untuk SKU GPS Ditolak, serta Dialog Konfirmasi Modul (Backdrop dan Esc) | FE+BE | 59 | 721, 722, 803 |
| TC-AC-ACTS-E2E-063-add-stock-nfc-screening-sesi-scan-baris-ok-dan-mode-terkunci | Add Stock NFC: Screening Idle, Sesi Scan Mengunci Halaman, Scan Baru Menjadi OK, dan Mode Scan Terkunci | FE+BE | 35 | 182, 183, 184, 190 |
| TC-AC-ACTS-E2E-064-add-stock-nfc-duplikat-uid-waiting-dan-remove-by-scan | Add Stock NFC: Duplikat UID Code (T-01), Scan Cocok Unit Existing Menjadi Waiting, dan Remove by Scan | FE+BE | 54 | 185, 186, 187, 188, 189 |
| TC-AC-ACTS-E2E-065-add-stock-nfc-cancel-dan-meninggalkan-halaman-dengan-list | Add Stock NFC: Cancel dan Meninggalkan Halaman dengan List Berisi atau Kosong | FE+BE | 40 | 191, 192, 193, 194, 895, 896 |
| TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble | Add Stock NFC: Reload, Back Fisik, Pindah Tab, Reader Tidak Terhubung atau Putus, serta Remove Manual dan Remove by Scan NFC dan BLE | FE+BE | 61 | 195, 196, 197, 198, 199, 797, 877 |
| TC-AC-ACTS-E2E-067-add-stock-nfc-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | Add Stock NFC: Submit List Kosong, Semua OK, Klik Ganda, Normalisasi Identifier, dan Saving State | FE+BE | 46 | 200, 201, 207, 210 |
| TC-AC-ACTS-E2E-068-add-stock-nfc-submit-waiting-dan-partial-register | Add Stock NFC: Submit Semua Waiting, Campuran OK dan Waiting (Partial Register), Cancel dan Continue, serta Normalisasi | FE+BE | 57 | 202, 203, 204, 205, 209 |
| TC-AC-ACTS-E2E-069-add-stock-ble-screening-sesi-scan-baris-ok-dan-mode-terkunci | Add Stock BLE: Screening Idle, Sesi Scan Mengunci Halaman, Scan Baru Menjadi OK, dan Mode Scan Terkunci | FE+BE | 35 | 211, 212, 213, 219 |
| TC-AC-ACTS-E2E-070-add-stock-ble-duplikat-mac-waiting-dan-remove-by-scan | Add Stock BLE: Duplikat MAC Address (T-01), Scan Cocok Unit Existing Menjadi Waiting, dan Remove by Scan | FE+BE | 54 | 214, 215, 216, 217, 218 |
| TC-AC-ACTS-E2E-071-add-stock-ble-cancel-dan-meninggalkan-halaman-dengan-list | Add Stock BLE: Cancel dan Meninggalkan Halaman dengan List Berisi atau Kosong | FE+BE | 40 | 220, 221, 222, 223, 897, 898 |
| TC-AC-ACTS-E2E-072-add-stock-ble-reload-back-fisik-pindah-tab-scanner-tidak-terhubung-dan-putus | Add Stock BLE: Reload, Back Fisik, Pindah Tab, Scanner Tidak Terhubung (Toast V-04), Putus di Tengah Sesi, dan Putus saat Idle | FE+BE | 42 | 224, 225, 226, 227, 228, 798 |
| TC-AC-ACTS-E2E-073-add-stock-ble-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | Add Stock BLE: Submit List Kosong, Semua OK, Klik Ganda, Normalisasi Identifier, dan Saving State | FE+BE | 55 | 229, 230, 236, 238, 239 |
| TC-AC-ACTS-E2E-074-add-stock-ble-submit-waiting-dan-partial-register | Add Stock BLE: Submit Semua Waiting, Campuran OK dan Waiting (Partial Register), serta Cancel dan Continue | FE+BE | 41 | 231, 232, 233, 234 |
| TC-AC-ACTS-E2E-075-resilience-add-stock-submit-gagal-dan-timeout-rfid-nfc-ble-gps | Resilience Add Stock: Submit Gagal (Toast T-03) pada RFID, NFC, BLE, dan GPS serta Submit RFID Tanpa Respons (Toast T-24) | FE+BE | 71 | 173, 206, 235, 265, 811 |
| TC-AC-ACTS-E2E-076-konkurensi-add-stock-toggle-local-registration-dimatikan-saat-sesi | Konkurensi Add Stock: Toggle Local Registration Dimatikan saat Sesi RFID, NFC, BLE, dan GPS | FE+BE | 58 | 175, 208, 237, 267 |
| TC-AC-ACTS-E2E-077-absence-add-stock-bypass-seluruh-batch-preview-read-only-dan-remove-tanpa-tulis | Absence Add Stock: Batch Seluruhnya Bypass Tanpa Entri Add Stock, Batch Seluruhnya Bypass Tanpa Baris Event Log, Cek Match Preview GPS Read-Only, dan Remove Tanpa Request atau Log | FE+BE | 67 | 773, 779, 878, 946 |
| TC-AC-ACTS-E2E-078-konkurensi-add-stock-dua-sesi-submit-identifier-sama-dan-hasil-commit-berbeda | Konkurensi Add Stock: Dua Sesi Submit Identifier Sama (RFID dan GPS) dan Hasil Commit Berbeda dari Badge | FE+BE | 51 | 178, 715, 727 |
| TC-AC-ACTS-E2E-079-add-stock-rfid-remove-by-scan-beruntun-dan-kode-tidak-dikenal | Add Stock RFID: Remove by Scan Beruntun Tanpa Jeda, TAG Tidak di List, dan Kode Tidak Dikenal | FE+BE | 39 | 875, 876 |
| TC-AC-ACTS-E2E-080-lintas-permukaan-download-seluruh-baris-dan-hasil-search-filter | Lintas Enam Permukaan: Download Tanpa Search/Filter Mengekspor Seluruh Baris dan dengan Search/Filter Hanya yang Cocok | FE+BE | 14 | 102, 103 |
| TC-AC-ACTS-E2E-081-lintas-permukaan-download-kolom-hide-dan-unhide | Lintas Enam Permukaan: Download Mengikuti Kolom yang Tampil, Kolom Di-Hide Tidak Ikut dan Di-Unhide Ikut | FE+BE | 13 | 104, 105 |
| TC-AC-ACTS-E2E-082-lintas-permukaan-download-tanpa-toast-gagal-dan-xlsx-sheet1 | Lintas Enam Permukaan: Download Sukses Tanpa Toast, Gagal dengan Toast Error, dan Workbook XLSX Satu Sheet | FE+BE | 12 | 106, 107, 110 |
| TC-AC-ACTS-E2E-083-lintas-permukaan-download-hasil-kosong-dan-csv-pemisah-bom-kutip | Lintas Enam Permukaan: Download Hasil Filter Kosong Berisi Header Saja dan CSV Pemisah Koma, UTF-8 BOM, serta Kutip | FE+BE | 16 | 108, 109 |
| TC-AC-ACTS-E2E-084-add-stock-gps-screening-upload-csv-xlsx-manual-entry-dan-preview-bersama | Add Stock GPS: Screening, Upload CSV dan XLSX Valid dengan Empat Status, Manual Entry, dan Satu Preview Bersama | FE+BE | 34 | 241, 242, 243, 244, 245 |
| TC-AC-ACTS-E2E-085-add-stock-gps-validasi-imei-duplicate-dan-hapus-baris-preview | Add Stock GPS: Validasi IMEI 15 Digit, Duplicate in File/List, Hapus Baris Preview, dan Re-evaluasi Kemunculan Pertama | FE+BE | 39 | 246, 247, 248, 249, 763 |
| TC-AC-ACTS-E2E-086-add-stock-gps-match-existing-ringkasan-manual-entry-dan-invalid-berulang | Add Stock GPS: IMEI Cocok Unit Existing (Waiting), Ringkasan A/B/C/D, Manual Entry Satu IMEI, Placeholder, Bentuk Tunggal, dan Invalid Format Berulang | FE+BE | 41 | 250, 268, 272, 748, 749, 783 |
| TC-AC-ACTS-E2E-087-add-stock-gps-berkas-header-salah-tipe-template-dan-batas-1-mb | Add Stock GPS: Header Berkas Salah (V-06), Tipe Tidak Didukung (V-08), Download Template, serta Batas 1 MB (V-10, Tepat 1 MB, Preview Tak Berubah) | FE+BE | 24 | 251, 252, 253, 737, 738, 739 |
| TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview | Add Stock GPS: Cancel dan Meninggalkan Halaman dengan Preview Berisi atau Kosong, Reload, serta Pilih Cancel Tetap di Halaman | FE+BE | 42 | 254, 255, 256, 257, 258, 899, 900 |
| TC-AC-ACTS-E2E-089-add-stock-gps-submit-ok-waiting-partial-register-dan-bentuk-tunggal | Add Stock GPS: Submit Tanpa Baris Valid (V-07), Semua OK, serta Campuran OK dan Waiting dengan Dialog Partial Register dan Cancel | FE+BE | 30 | 259, 260, 261, 262 |
| TC-AC-ACTS-E2E-090-add-stock-gps-klik-ganda-bypass-e2a-dan-identifier-rejected | Add Stock GPS: Klik Ganda Submit, Bypass E2a oleh Total Control, dan IMEI Hanya Dipegang Unit Rejected | FE+BE | 38 | 266, 734, 741 |
| TC-AC-ACTS-E2E-091-add-stock-gps-volume-5000-baris-sinkron-dan-background | Add Stock GPS Volume: Tepat 5.000 Baris Sinkron, Lebih dari 5.000 Baris di Background (Toast T-23 dan Notifikasi), Campuran Partial Register, dan Tanpa Baris OK | FE+BE | 43 | 269, 270, 769, 770 |
| TC-AC-ACTS-E2E-092-add-stock-gps-volume-job-background-gagal-ambang-lintas-upload-dan-remove-ke-5000 | Add Stock GPS Volume: Kegagalan Job Background, Ambang 5.000 Lintas Upload Berurutan, Remove Menurunkan Total ke 5.000, dan Bar Non-Interaktif saat Parse | FE+BE | 44 | 771, 772, 885, 887 |
| TC-AC-ACTS-E2E-093-add-stock-gps-checkbox-select-all-dan-dialog-remove-imei | Add Stock GPS: Kolom Checkbox, Select All dan Unselect All, Bulk Action Bar Remove, serta Dialog Remove IMEI dan IMEIs | FE+BE | 35 | 880, 881, 882 |
| TC-AC-ACTS-E2E-094-add-stock-gps-remove-sukses-reevaluasi-preview-dan-ikon-hapus | Add Stock GPS: Remove Sukses (T-37) dengan Ringkasan Dihitung Ulang, Re-evaluasi IMEI Kembar, dan Ikon Hapus per Baris | FE+BE | 32 | 883, 884, 886 |
| TC-AC-ACTS-E2E-095-approvals-duplicate-dialog-review-register-duplicate-activation-collision-dan-byo | Approvals Duplicate: Dialog Review Register Duplicate, Activation Collision, Client BYO Tanpa SKU, dan Label Registered by/at dari Import GPS | FE+BE | 25 | 273, 274, 275, 728 |
| TC-AC-ACTS-E2E-096-approvals-duplicate-existing-record-label-matched-identifier-dan-approval-note | Approvals Duplicate: Nama User Dengan Hover, Placeholder Approval Note, Existing Record Deleted, Label Stock/Client, dan Matched Identifier RFID, NFC, BLE, GPS | FE+BE | 37 | 300, 301, 302, 729, 750, 764 |
| TC-AC-ACTS-E2E-097-approvals-duplicate-radio-validasi-reject-batas-note-cancel-dan-klik-ganda | Approvals Duplicate: Radio Approve/Reject, Reject Tanpa Note (V-09), Batas 360 Karakter, Cancel Tanpa Commit, dan Klik Ganda Submit | FE+BE | 39 | 276, 279, 280, 283, 284, 294 |
| TC-AC-ACTS-E2E-098-approvals-duplicate-approve-register-duplicate-activation-collision-dan-unit-tidak-tampil | Approvals Duplicate: Approve Register Duplicate dan Activation Collision, Unit Rejected Tidak Masuk Stok, dan Total Registered Tidak Berubah saat Pending | FE+BE | 39 | 277, 278, 298, 879 |
| TC-AC-ACTS-E2E-099-approvals-duplicate-reject-register-duplicate-dan-activation-collision | Approvals Duplicate: Reject Register Duplicate (Unit Rejected Tidak Masuk Stok) dan Reject Activation Collision (Alasan Tidak Diteruskan ke Client) | FE+BE | 27 | 281, 282 |
| TC-AC-ACTS-E2E-100-approvals-duplicate-scan-ulang-identifier-rejected-dan-constraint-unique-status-live | Approvals Duplicate: Scan Ulang Identifier Unit Rejected Terdaftar sebagai Unit Baru dan Constraint UNIQUE Hanya untuk Status Live | FE+BE | 37 | 303, 742 |
| TC-AC-ACTS-E2E-101-approvals-duplicate-requester-distributor-dua-subject-dan-bypass-e2a-default-user | Approvals Duplicate: Bypass E2a Total Control dan Default User, Requester Distributor Diputuskan Principal, serta Dua Subject Satu Existing Record | FE+BE | 46 | 285, 286, 297, 299 |
| TC-AC-ACTS-E2E-102-approvals-duplicate-e4-additional-approver-subject-sendiri-disembunyikan | Approvals Duplicate: E4 Additional Approver, Subject Sendiri Tersembunyi di Tab Active, Tampil di Tab History, Approve Langsung Ditolak, dan Activation Collision Tanpa E4 | FE+BE | 39 | 287, 288, 289, 768, 806 |
| TC-AC-ACTS-E2E-103-approvals-duplicate-konkurensi-dua-approver-dan-dialog-nested | Approvals Duplicate Konkurensi: Dua Approver Approve Subject yang Sama, Approve dan Reject Bersamaan, Reject Pertama Mengunci, serta Esc pada Dialog Nested | FE+BE | 51 | 290, 291, 808, 809 |
| TC-AC-ACTS-E2E-104-approvals-duplicate-activation-collision-dibatalkan-event-delete-tag-dan-no-op | Approvals Duplicate: Activation Collision Canceled Otomatis oleh Event Delete TAG, Event Diterima Ulang No-Op, Register Duplicate Tanpa Pembatalan, dan Tanpa Timeout | FE+BE | 42 | 292, 304, 305, 306, 307, 308 |
| TC-AC-ACTS-E2E-105-resilience-approvals-error-detail-gagal-muat-timeout-dan-download-gagal | Resilience Approvals: Approve atau Reject Gagal 5xx, Detail Approval Gagal Dimuat, Tanpa Respons (T-24), Detail History Gagal Dimuat, dan Download Gagal dengan Nama Sub-Menu | FE+BE | 44 | 293, 295, 730, 776, 810 |
| TC-AC-ACTS-E2E-106-lintas-modul-activate-tag-jalur-a-dan-b-menambah-in-use-dan-tidak-mengubah-total | Lintas Modul: Activate TAG Jalur A dan B Memindahkan Unit ke Tab In Use, Menaikkan In Use, dan Jalur B Tanpa SKU Tidak Tampil | FE+BE | 28 | 673, 674, 675, 676 |
| TC-AC-ACTS-E2E-107-lintas-modul-delete-tag-jalur-a-dan-b-dan-auto-resolve-activate | Lintas Modul: Delete TAG Jalur A dan B, Activate TAG Cocok Unit Available Auto-Resolve, dan Activate TAG Cocok Unit In Use Membuat Activation Collision | FE+BE | 28 | 677, 678, 679, 680 |
| TC-AC-ACTS-E2E-108-lintas-modul-event-condition-combine-separate-dan-no-op | Lintas Modul: Event Condition Mengubah Status Tab In Use, Combine dan Separate, Event atau Delete TAG No-Op, dan Status Kembali Kosong setelah Delete TAG Jalur A | FE+BE | 38 | 681, 682, 683, 684, 781, 782 |
| TC-AC-ACTS-E2E-109-lintas-modul-stock-ledger-device-allocation-add-approve-delete-dan-batch-waiting | Lintas Modul: Saldo Stock Ledger di Device Allocation (Add Stock, Approve, Delete), Batch Seluruhnya Waiting, dan Baris Ledger Pertama | FE+BE | 44 | 685, 686, 687, 725, 726 |
| TC-AC-ACTS-E2E-110-lintas-modul-notifikasi-permintaan-hasil-keputusan-dan-gagal-kirim | Lintas Modul: Notifikasi Permintaan Approval ke Pool, Hasil Keputusan ke Requester, Auto-Read, dan Notifikasi Gagal Terkirim Tidak Menggagalkan Approve | FE+BE | 36 | 688, 689, 690, 813 |
| TC-AC-ACTS-E2E-111-lintas-modul-format-tanggal-waktu-general-settings-enam-permukaan | Lintas Modul: Format Tanggal dan Waktu Mengikuti General Settings di Stock List, Tab Available, Tab In Use, Event Log, dan Approvals Tab Active dan History | FE+BE | 25 | 691, 692, 693, 694, 696, 697 |
| TC-AC-ACTS-E2E-112-lintas-modul-qr-tidak-tampil-last-updated-dan-aksi-pengaruhnya | Lintas Modul: QR Tidak Tampil di Stock List, Last Updated Naik setelah Mark Damaged/Missing, Waiting, Approve, Reject, Cancel, dan Delete | FE+BE | 30 | 698, 699, 700 |
| TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off | Defense-in-Depth: Request Tulis Langsung Tanpa Capability, Partner atau Client, Distributor Approve, Audit, Delete Unit Bukan Miliknya, Toggle OFF, Isolasi Entitas, dan Endpoint QR | FE+BE | 27 | 701, 702, 703, 704, 705, 707, 708 |
| TC-AC-ACTS-E2E-114-defense-in-depth-distributor-suspended-read-only-capability-parsial-dan-payload-note | Defense-in-Depth: Distributor Suspended Request Tulis Ditolak, Read Only, Capability Parsial, Pemegang Update Tidak Dapat Approve atau Reject, dan Payload XSS/SQL di Approval Note | FE+BE | 36 | 706, 709, 784, 785, 786 |
| TC-AC-ACTS-E2E-115-popup-tag-log-row-action-header-per-tag-type-dan-urutan-kronologis | Popup TAG Log: Row Action di Tab Available dan In Use, Header Per TAG Type, dan Urutan Kronologis dengan Judul Kalimat | FE+BE | 34 | 952, 953, 954, 955 |
| TC-AC-ACTS-E2E-116-popup-tag-log-format-tanggal-empty-state-read-only-gagal-muat-dan-scope-distributor | Popup TAG Log: Format Tanggal Mengikuti General Settings, Unit Tanpa Entri (S-29), Read-Only Tanpa Tombol Close, Gagal Dimuat, dan Distributor Hanya Unit Batch Miliknya | FE+BE | 36 | 956, 957, 958, 959, 982 |
| TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit | Popup TAG Log Entri: Registered (Add Stock Scan, Import GPS, Bypass E2a), Waiting lalu Approved, Activated, Unit Ditolak dan Canceled Tanpa Log | FE+BE | 37 | 960, 961, 962, 963, 964, 965, 966 |
| TC-AC-ACTS-E2E-118-popup-tag-log-entri-audit-verified-not-found-dilewati-dan-sibling-combined | Popup TAG Log Entri Audit: Verified dengan Recovery, Not Found dengan dan Tanpa Centang, Unit Dilewati Tanpa Entri, dan Sibling Combined Tanpa Entri | FE+BE | 36 | 967, 968, 969, 972 |
| TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable | Popup TAG Log Entri Lintas Modul: Activated, Returned to Stock, Delete Jalur B, Status Synced, Combined dan Separated, Delete Stock, dan Entri Immutable | FE+BE | 49 | 973, 974, 975, 976, 978, 979, 980 |
| TC-AC-ACTS-E2E-120-add-stock-gps-partial-register-bentuk-tunggal-continue-dan-semua-waiting | Add Stock GPS: Dialog Partial Register Bentuk Tunggal, Continue Mendaftarkan OK dan Mengirim Waiting, serta Submit Semua Waiting | FE+BE | 18 | 263, 264, 807 |
| TC-AC-ACTS-E2E-121-approvals-duplicate-existing-record-unit-paling-awal-saat-dua-unit-live-berbagi-identifier | Approvals Duplicate: Existing Record Menunjuk Unit Paling Awal Terdaftar bila Dua Unit Live Berbagi Identifier | FE+BE | 14 | 780 |
| TC-AC-ACTS-E2E-122-audit-rfid-screening-popup-start-scan-dan-verified-di-tempat | Audit RFID: Screening Popup Idle, Start Scan Mengunci Popup, TAG Cocok Menjadi Verified, dan TAG Tidak di Tabel Diabaikan Tanpa Toast | FE+BE | 38 | 309, 310, 311, 312 |
| TC-AC-ACTS-E2E-123-audit-rfid-scan-ulang-prioritas-uid-identifier-stop-dan-sesi-berikutnya | Audit RFID: Scan Ulang Tidak Menambah Counter, UID Menang, Kolom Identifier EPC/UID, Stop Membuka Kunci, dan Sesi Berikutnya Mempertahankan Verified | FE+BE | 46 | 313, 314, 315, 316, 317 |
| TC-AC-ACTS-E2E-124-audit-rfid-submit-dialog-konfirmasi-dan-confirm-dengan-checkbox | Audit RFID: Submit Sebelum Scan, Tanpa Not Scanned Commit Langsung (T-05), Dialog Konfirmasi, dan Confirm dengan Checkbox Menandai Not Scanned | FE+BE | 41 | 318, 319, 321, 322 |
| TC-AC-ACTS-E2E-125-audit-rfid-confirm-tanpa-centang-cancel-dialog-recovery-d03-dan-toast-gabungan | Audit RFID: Confirm Tanpa Centang, Cancel Dialog, Baris Damaged/Missing Tak Ter-Scan Masuk Hitungan D-03, dan Toast Gabungan dengan Klausa Recovery | FE+BE | 48 | 323, 324, 325, 326 |
| TC-AC-ACTS-E2E-126-audit-rfid-toast-netral-t20-bentuk-tunggal-counter-dan-badge-severity | Audit RFID: Submit Tanpa Perubahan Status (Toast Netral T-20), Dialog Konfirmasi Bentuk Tunggal, Counter Widget Tunggal dan Jamak, dan Badge Audit Status | FE+BE | 48 | 320, 756, 765, 774 |
| TC-AC-ACTS-E2E-127-audit-rfid-unit-combined-in-use-waiting-empty-state-dan-tag-code-tidak-berubah | Audit RFID: Unit Combined Tetap Eligible, In Use dan Waiting Tidak Ditawarkan, Tanpa Unit Eligible (Empty State), Gagal Memuat Daftar, dan TAG Code Tidak Berubah | FE+BE | 47 | 328, 329, 330, 331, 733 |
| TC-AC-ACTS-E2E-128-audit-rfid-tutup-popup-d06-leave-cancel-dan-tanpa-verified | Audit RFID: Tutup Popup Setelah Stop dengan Baris Verified (D-06 Leave dan Cancel) dan Tutup Popup Tanpa Verified Langsung Tertutup | FE+BE | 27 | 332, 333, 334 |
| TC-AC-ACTS-E2E-129-audit-rfid-klik-ganda-tanpa-stock-ledger-event-log-dan-start-scan-tanpa-reader | Audit RFID: Klik Ganda Submit Diproses Sekali, Audit Tidak Menulis Stock Ledger, Pencatatan Perubahan di Event Log, dan Start Scan Tanpa Reader (V-03) | FE+BE | 45 | 340, 341, 342, 716 |
| TC-AC-ACTS-E2E-130-audit-rfid-scan-kode-belum-terdaftar-bukan-eligible-dan-format-tidak-valid | Audit RFID: Scan Kode Belum Terdaftar (Toast T-38), Kode Terdaftar Bukan Unit Eligible Diabaikan, dan Teks Berformat Tidak Valid Diabaikan | FE+BE | 31 | 948, 949, 950 |
| TC-AC-ACTS-E2E-131-audit-rfid-konkurensi-status-unit-berubah-oleh-sesi-lain-di-tengah-sesi | Audit RFID Konkurensi: Unit Berubah Status oleh Sesi Lain Di-Skip (T-08 Tunggal dan Jamak) dan Nol Perubahan dengan Unit Di-Skip | FE+BE | 37 | 327, 762, 767 |
| TC-AC-ACTS-E2E-132-audit-nfc-screening-start-scan-verified-stop-dan-submit-dialog | Audit NFC: Screening Popup Idle, Start Scan Mengunci Popup, Verified di Tempat, Stop, dan Submit dengan Not Scanned Membuka Dialog | FE+BE | 50 | 343, 344, 345, 346, 347 |
| TC-AC-ACTS-E2E-133-audit-nfc-confirm-cancel-recovery-combined-dan-in-use | Audit NFC: Confirm dengan dan Tanpa Centang, Cancel Dialog, Recovery Damaged/Missing, Unit Combined Eligible, dan Unit In Use Tidak Ditawarkan | FE+BE | 55 | 348, 349, 350, 351, 352, 353 |
| TC-AC-ACTS-E2E-134-audit-nfc-start-scan-tanpa-reader-d06-leave-cancel-dan-scan-uid-belum-terdaftar | Audit NFC: Start Scan Tanpa Reader (V-03), Tutup Popup Setelah Stop (D-06 Leave dan Cancel), dan Scan UID Belum Terdaftar (T-38) | FE+BE | 38 | 717, 718, 719, 951 |
| TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr | Audit TAG Tidak Tersedia: Hidden untuk SKU BLE dan GPS, Request Langsung Ditolak, QR Tanpa Audit, Unit BLE Pra-Aktivasi Tanpa Jalur Damaged/Missing, dan Status BLE di Tab In Use | FE+BE | 34 | 240, 271, 355, 356, 357, 358, 359 |
| TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger | Delete Unit: Dialog Delete Unit, Cancel, Unit Waiting Tanpa Delete, Guard Combined (D-07) dan Existing Record (D-08), Urutan Evaluasi Guard, dan Saldo Ledger Negatif (T-16) | FE+BE | 46 | 360, 363, 364, 366, 367, 368, 369 |
| TC-AC-ACTS-E2E-137-delete-unit-konfirmasi-damaged-missing-klik-ganda-distributor-dan-unit-terakhir-sku | Delete Unit: Konfirmasi Delete Mengurangi Total Registered dan Ledger, Delete Damaged/Missing, Klik Ganda, Distributor Hanya Unit Miliknya, dan Hapus Unit Terakhir SKU | FE+BE | 44 | 361, 362, 371, 372, 373 |
| TC-AC-ACTS-E2E-138-delete-by-scan-screening-toolbar-visibilitas-sku-gps-dan-tanpa-reader | Delete by Scan: Toolbar Tab Available RFID, Tab In Use Tanpa Delete by Scan, SKU GPS Hanya Bulk Delete, dan Klik Tanpa Reader (V-03 atau V-04) | FE+BE | 31 | 815, 817, 818, 819 |
| TC-AC-ACTS-E2E-139-bulk-delete-screening-checkbox-select-all-dan-kolom-checkbox | Bulk Delete: Screening Bulk Action Bar, Checkbox Semua Baris Tab Available, Select All dan Unselect All, serta Kolom Checkbox (Pinned, Bukan Setup Column, Tidak Ikut Download) | FE+BE | 35 | 838, 839, 840, 851 |
| TC-AC-ACTS-E2E-140-bulk-delete-seleksi-lintas-halaman-selection-limit-dan-dialog-delete-units | Bulk Delete: Checkbox Header Halaman Aktif, Select All Lintas Halaman, Seleksi Bertahan, Selection Limit, dan Dialog Delete Units | FE+BE | 38 | 841, 842, 843, 845 |
| TC-AC-ACTS-E2E-141-delete-by-scan-sesi-terkunci-hapus-langsung-beruntun-dan-damaged-missing | Delete by Scan: Sesi Terkunci dengan Widget Deleting TAGs, Scan Eligible Langsung Terhapus, Scan Beruntun, dan Unit Damaged/Missing | FE+BE | 43 | 820, 821, 822, 823 |
| TC-AC-ACTS-E2E-142-delete-by-scan-penolakan-sku-lain-status-combined-dan-existing-record | Delete by Scan: Penolakan Unit SKU Lain (T-26), Waiting, In Use, Tidak di Stok, Combined (T-27), dan Existing Record Pending (T-28) | FE+BE | 37 | 824, 825, 826, 827 |
| TC-AC-ACTS-E2E-143-delete-by-scan-kode-tidak-dikenal-sesi-berlanjut-nfc-ble-dan-scan-ulang | Delete by Scan: Kode Bukan Identifier (T-29), Penolakan Tidak Menghentikan Sesi, SKU NFC dan BLE, dan Scan Ulang Kode yang Sudah Terhapus (T-31) | FE+BE | 49 | 828, 829, 830, 858 |
| TC-AC-ACTS-E2E-144-delete-by-scan-reader-putus-pindah-halaman-log-sesi-dan-distributor | Delete by Scan: Reader Terputus, Meninggalkan Halaman (Modal RFID Scan Stopped), Log Sesi Level-Sesi, dan Distributor Hanya Menghapus Stok Sendiri | FE+BE | 44 | 833, 834, 835, 836 |
| TC-AC-ACTS-E2E-145-bulk-delete-sukses-sebagian-dilewati-collapse-satu-baris-dan-distributor | Bulk Delete: Seleksi Satu Baris Collapse ke Dialog Single, Sukses (T-15), Sebagian Dilewati (Delete Result), dan Distributor Menghapus Unit Sendiri | FE+BE | 44 | 844, 846, 847, 852 |
| TC-AC-ACTS-E2E-146-konkurensi-audit-dan-delete-bersamaan-dua-sesi-ui | Konkurensi Audit dan Delete: Dua Sesi Audit pada Unit yang Sama, Delete Dua Kali, dan Delete Bersamaan dengan Audit | FE+BE | 39 | 710, 711, 714 |
| TC-AC-ACTS-E2E-147-konkurensi-delete-by-scan-dan-bulk-delete-bersamaan-sesi-lain | Konkurensi Delete: Unit Berubah Status oleh Sesi Lain (T-17, D-05, T-32), Bulk Delete Tidak Eligible (T-30), dan Bulk Delete Bersamaan dengan Sesi Lain | FE+BE | 60 | 365, 759, 831, 848, 850 |
| TC-AC-ACTS-E2E-148-resilience-delete-dan-audit-gagal-5xx-dan-timeout | Resilience Delete dan Audit: Audit Submit Gagal (T-09), Delete Gagal 5xx (T-16), Delete by Scan Gagal dan Timeout (T-16, T-24), dan Bulk Delete Tanpa Respons (T-24) | FE+BE | 41 | 339, 370, 832, 849 |
| TC-AC-ACTS-E2E-149-state-tenant-distributor-suspended-aksi-tulis-ditolak-dan-plan-gating-tidak-ada | State Tenant: Distributor Suspended (Aksi Tulis Ditolak Server, Import GPS, Delete Scan dan Bulk, Aksi Sistem Tanpa Aktor Tidak Diblokir) dan Plan Gating Tidak Ada | FE+BE | 49 | 138, 736, 758, 760, 837 |
| TC-AC-ACTS-E2E-150-absence-log-audit-tanpa-perubahan-dan-delete-tanpa-entri-event-log-tag-log | Absence Log: Audit Tanpa Perubahan Tidak Menulis Log, Tanpa Baris Event Log, Tanpa Entri Audit TAG Log, dan Bulk Delete Tanpa Penghapusan Tanpa Baris Event Log | FE+BE | 43 | 670, 930, 947, 970, 971 |
| TC-AC-ACTS-E2E-151-absence-log-delete-by-scan-tanpa-penghapusan-usage-event-dan-status-synced | Absence Log: Delete by Scan Tanpa Penghapusan Tanpa Log dan Usage Event, Usage Event Tidak Tercatat tanpa Reader dan untuk Aksi Lain, serta Event Condition No-Op Tanpa Status Synced | FE+BE | 48 | 859, 863, 864, 865, 977 |
| TC-AC-ACTS-E2E-152-usage-event-handheld-reader-add-stock-audit-delete-by-scan-dan-kegagalan-tulis | Usage Event Handheld Reader: Satu Event per Sesi Add Stock, Audit, dan Delete by Scan serta Kegagalan Menulis Usage Event pada Submit Add Stock dan Delete by Scan | FE+BE | 42 | 860, 861, 862, 866, 867 |
| TC-AC-ACTS-E2E-153-pencatatan-log-add-stock-via-scan-import-gps-waiting-dan-batch-waiting | Pencatatan Log: Add Stock via Scan, Import GPS, dan Waiting for Approval di System Log, Activity Log, dan Event Log; Entri Level SKU; Batch Seluruhnya Waiting | FE+BE | 43 | 521, 655, 656, 657, 669 |
| TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | Pencatatan Log: Mark as Damaged/Missing dan Available, Duplicate Approved (Register Duplicate, Activation Collision, Bypass E2a), Rejected, Canceled oleh Sistem, dan Delete Stock | FE+BE | 48 | 658, 659, 660, 661, 662, 663, 664, 665 |
| TC-AC-ACTS-E2E-155-pencatatan-log-field-delete-stock-sync-condition-kolom-modified-by-dan-tanpa-duplikat | Pencatatan Log: Entri Delete Stock Satuan, Sync Condition, Kolom Modified By Activity Log, Tanpa Entri Ganda atau Nyasar, Isolasi Log Distributor, dan Scope Activity Log Tanpa Event Global Settings | FE+BE | 35 | 522, 525, 526, 666, 667, 668 |
| TC-AC-ACTS-E2E-156-pencatatan-log-snapshot-audit-level-sesi-dan-activation-collision-waiting | Pencatatan Log: Audit Multi-Unit Satu Entri per Unit, Snapshot Log Tidak Berubah, Activation Collision Waiting dengan Aktor Client, dan Log Audit Level Sesi | FE+BE | 37 | 671, 672, 751, 777 |
| TC-AC-ACTS-E2E-157-detail-sku-screening-header-summary-bar-tab-dan-tag-type-icon | Detail SKU: Screening Header, Summary Bar, Tab, Toolbar Tab Available SKU GPS dan BLE, dan Icon TAG Type di Header | FE+BE | 35 | 374, 375, 856 |
| TC-AC-ACTS-E2E-158-detail-sku-retensi-state-per-sub-tab-hapus-baris-terakhir-dan-identifier-non-rfid | Detail SKU: State Per Sub-Tab, Refresh F5, Hapus Baris Terakhir di Halaman Terakhir, dan Kolom Identifier (UID, RFID) Kosong untuk Non-RFID | FE+BE | 42 | 787, 789, 795, 801 |
| TC-AC-ACTS-E2E-159-detail-sku-aria-label-sort-tag-code-mutasi-terfilter-siklus-toast-dan-ikon-combined | Detail SKU Tab Available: Aria-Label Tabel, Sort TAG Code Tanpa Nilai Kosong dan Ikon Combined, Mutasi saat Terfilter, dan Siklus Toast | FE+BE | 37 | 29, 98, 101, 804, 901 |
| TC-AC-ACTS-E2E-160-detail-sku-realtime-tab-available-opsi-filter-banner-dan-approval | Detail SKU Realtime: Unit Menjadi In Use, Keputusan Approval, Opsi Dropdown Filter, dan Banner Waiting for Approval Tanpa Reload | FE+BE | 31 | 386, 731, 735, 991 |
| TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval | Detail SKU: Summary Bar Card Available, Perubahan setelah Delete, dan Banner Waiting for Approval (Jamak, Tunggal, Tidak Tampil, Bukan Collision, Link Review) | FE+BE | 37 | 891, 892, 984, 985, 986, 987, 988 |
| TC-AC-ACTS-E2E-162-detail-sku-banner-waiting-for-approval-non-approver-distributor-dan-state-tabel | Detail SKU Banner: Non-Approver (Teks Tanpa Link), Distributor Hanya Batch Sendiri, Tidak Terpengaruh Search/Filter/Sort, Tidak Tampil di Tab In Use, Loading, Error, dan Tidak Dapat Ditutup | FE+BE | 39 | 989, 990, 992, 993, 994 |
| TC-AC-ACTS-E2E-163-audit-rfid-sesi-scan-aktif-back-fisik-reader-putus-pindah-tab-dan-reload | Audit RFID: Sesi Scan Aktif Ditinggalkan (Back Fisik, Semua Reader Putus, Pindah Tab, dan Reload) | FE+BE | 37 | 335, 336, 799, 800 |
| TC-AC-ACTS-E2E-164-konkurensi-audit-dan-delete-unit-in-use-dan-approve-subject-via-sesi-api | Konkurensi Audit dan Delete: Unit Menjadi In Use di Tengah Audit dan Delete Bersamaan dengan Approve Subject | FE+BE | 20 | 712, 713 |
| TC-AC-ACTS-E2E-165-detail-sku-tab-available-badge-status-filter-status-dan-ikon-combined | Detail SKU Tab Available: Badge Status, Filter Status, Ikon Combined, dan Popup Combined TAG Read-Only | FE+BE | 20 | 376, 377, 379, 380, 381 |
| TC-AC-ACTS-E2E-166-detail-sku-tab-available-unit-waiting-rejected-byo-registered-by-dan-row-action-tag-log | Detail SKU Tab Available: Unit Waiting, Rejected, dan BYO Tidak Tampil, Registered By Terisi, dan Row Action TAG Log | FE+BE | 24 | 378, 382, 383, 384, 385, 814 |
| TC-AC-ACTS-E2E-167-detail-sku-tab-available-screening-urutan | Detail SKU Tab Available: Screening Header, Kolom, Footer dan Urutan Default | FE+BE | 10 | 388, 389 |
| TC-AC-ACTS-E2E-168-detail-sku-tab-available-sort-bagian-1 | Detail SKU Tab Available: Sort 3-State Per Kelas Kolom (Bagian 1) | FE+BE | 21 | 390, 391, 392 |
| TC-AC-ACTS-E2E-169-detail-sku-tab-available-sort-bagian-2-hover-user-siklus-search | Detail SKU Tab Available: Sort 3-State Per Kelas Kolom (Bagian 2), Siklus Search Toolbar, dan Hover Nama User | FE+BE | 33 | 393, 394, 425 |
| TC-AC-ACTS-E2E-170-detail-sku-tab-available-search-kolom-bagian-1 | Detail SKU Tab Available: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1) | FE+BE | 9 | 395, 396, 397 |
| TC-AC-ACTS-E2E-171-detail-sku-tab-available-search-kolom-bagian-2-search-visibilitas | Detail SKU Tab Available: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom | FE+BE | 18 | 398, 399, 400 |
| TC-AC-ACTS-E2E-172-detail-sku-tab-available-alur-search-filter | Detail SKU Tab Available: Alur Search lalu Filter dan Filter lalu Search | FE+BE | 23 | 401, 402 |
| TC-AC-ACTS-E2E-173-detail-sku-tab-available-filter-bagian-1 | Detail SKU Tab Available: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1) | FE+BE | 33 | 403, 404, 405 |
| TC-AC-ACTS-E2E-174-detail-sku-tab-available-filter-bagian-2-sc-screening | Detail SKU Tab Available: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup | FE+BE | 30 | 406, 407, 408, 409 |
| TC-AC-ACTS-E2E-175-detail-sku-tab-available-sc-ceklis | Detail SKU Tab Available: Setup Column: Ceklis dan Unceklis Kolom | FE+BE | 18 | 410 |
| TC-AC-ACTS-E2E-176-detail-sku-tab-available-sc-urutan-pin | Detail SKU Tab Available: Setup Column: Geser Urutan serta Pin dan Unpin | FE+BE | 21 | 411, 412 |
| TC-AC-ACTS-E2E-177-detail-sku-tab-available-sc-reset-tutup-bagian-1 | Detail SKU Tab Available: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1) | FE+BE | 31 | 413, 414, 415 |
| TC-AC-ACTS-E2E-178-detail-sku-tab-available-sc-reset-tutup-bagian-2-pagination | Detail SKU Tab Available: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2) | FE+BE | 10 | 416 |
| TC-AC-ACTS-E2E-179-detail-sku-tab-available-state | Detail SKU Tab Available: State Kosong, Empty-Filtered, Error Load, dan Loading | FE+BE | 21 | 418, 419, 420, 421 |
| TC-AC-ACTS-E2E-180-detail-sku-tab-available-download | Detail SKU Tab Available: Download CSV dan XLSX | FE+BE | 9 | 422, 423 |
| TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku | Tab In Use: Screening Read-Only Tanpa Toolbar Tulis, Row Action TAG Log, Badge Status, Status Kosong, Registered By BYO, dan Unit Tanpa SKU | FE+BE | 32 | 426, 427, 428, 429, 430, 431, 432 |
| TC-AC-ACTS-E2E-182-tab-in-use-screening-urutan | Detail SKU Tab In Use: Screening Header, Kolom, Footer dan Urutan Default | FE+BE | 8 | 433, 434 |
| TC-AC-ACTS-E2E-183-tab-in-use-sort-bagian-1 | Detail SKU Tab In Use: Sort 3-State Per Kelas Kolom (Bagian 1) | FE+BE | 15 | 435, 436 |
| TC-AC-ACTS-E2E-184-tab-in-use-sort-bagian-2 | Detail SKU Tab In Use: Sort 3-State Per Kelas Kolom (Bagian 2) | FE+BE | 20 | 437, 438 |
| TC-AC-ACTS-E2E-185-tab-in-use-search-kolom-bagian-1 | Detail SKU Tab In Use: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1) | FE+BE | 9 | 440, 441, 442 |
| TC-AC-ACTS-E2E-186-tab-in-use-search-kolom-bagian-2-search-visibilitas | Detail SKU Tab In Use: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom | FE+BE | 24 | 443, 444, 445, 446 |
| TC-AC-ACTS-E2E-187-tab-in-use-alur-search-filter | Detail SKU Tab In Use: Alur Search lalu Filter dan Filter lalu Search | FE+BE | 25 | 447, 448 |
| TC-AC-ACTS-E2E-188-tab-in-use-filter-bagian-1 | Detail SKU Tab In Use: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1) | FE+BE | 28 | 449, 450, 451 |
| TC-AC-ACTS-E2E-189-tab-in-use-filter-bagian-2-sc-screening | Detail SKU Tab In Use: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup | FE+BE | 30 | 452, 453, 454, 455 |
| TC-AC-ACTS-E2E-190-tab-in-use-sc-ceklis | Detail SKU Tab In Use: Setup Column: Ceklis dan Unceklis Kolom | FE+BE | 18 | 456 |
| TC-AC-ACTS-E2E-191-tab-in-use-sc-urutan-pin | Detail SKU Tab In Use: Setup Column: Geser Urutan serta Pin dan Unpin | FE+BE | 21 | 457, 458 |
| TC-AC-ACTS-E2E-192-tab-in-use-sc-reset-tutup-bagian-1 | Detail SKU Tab In Use: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1) | FE+BE | 31 | 459, 460, 461 |
| TC-AC-ACTS-E2E-193-tab-in-use-sc-reset-tutup-bagian-2-pagination | Detail SKU Tab In Use: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2) | FE+BE | 10 | 462 |
| TC-AC-ACTS-E2E-194-tab-in-use-state | Detail SKU Tab In Use: State Kosong, Empty-Filtered, Error Load, dan Loading | FE+BE | 21 | 464, 465, 466, 467 |
| TC-AC-ACTS-E2E-195-tab-in-use-download-hover-user | Detail SKU Tab In Use: Download CSV dan XLSX; Hover Nama User | FE+BE | 12 | 468, 469, 471 |
| TC-AC-ACTS-E2E-196-approvals-tab-history-screening-badge-approval-approver-tag-code-dan-baris-canceled | Approvals Tab History: Badge Approval Tiga Severity, Approver dan TAG Code Kosong Sesuai Status, Detail Read-Only, dan Baris Canceled Tanpa Keputusan | FE+BE | 28 | 610, 611, 612, 613, 614 |
| TC-AC-ACTS-E2E-197-approvals-tab-history-screening-urutan-sort-bagian-1 | Approvals Tab History: Screening Header, Kolom, Footer dan Urutan Default; Sort 3-State Per Kelas Kolom (Bagian 1) | FE+BE | 21 | 615, 616, 617 |
| TC-AC-ACTS-E2E-198-approvals-tab-history-sort-bagian-2 | Approvals Tab History: Sort 3-State Per Kelas Kolom (Bagian 2) | FE+BE | 15 | 618, 619 |
| TC-AC-ACTS-E2E-199-approvals-tab-history-sort-bagian-3-siklus-search | Approvals Tab History: Sort 3-State Per Kelas Kolom (Bagian 3); Siklus Search Toolbar | FE+BE | 36 | 620, 621 |
| TC-AC-ACTS-E2E-200-approvals-tab-history-search-kolom-bagian-1 | Approvals Tab History: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1) | FE+BE | 9 | 622, 623, 624 |
| TC-AC-ACTS-E2E-201-approvals-tab-history-search-kolom-bagian-2-search-visibilitas | Approvals Tab History: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom | FE+BE | 27 | 625, 626, 627, 628, 629 |
| TC-AC-ACTS-E2E-202-approvals-tab-history-alur-search-filter | Approvals Tab History: Alur Search lalu Filter dan Filter lalu Search | FE+BE | 25 | 630, 631 |
| TC-AC-ACTS-E2E-203-approvals-tab-history-filter-bagian-1 | Approvals Tab History: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1) | FE+BE | 16 | 632, 633 |
| TC-AC-ACTS-E2E-204-approvals-tab-history-filter-bagian-2 | Approvals Tab History: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2) | FE+BE | 25 | 634, 635, 636 |
| TC-AC-ACTS-E2E-205-approvals-tab-history-sc-screening | Approvals Tab History: Setup Column: Screening Overlay dan Popup | FE+BE | 18 | 637, 638 |
| TC-AC-ACTS-E2E-206-approvals-tab-history-sc-ceklis | Approvals Tab History: Setup Column: Ceklis dan Unceklis Kolom | FE+BE | 18 | 639 |
| TC-AC-ACTS-E2E-207-approvals-tab-history-sc-urutan-pin | Approvals Tab History: Setup Column: Geser Urutan serta Pin dan Unpin | FE+BE | 21 | 640, 641 |
| TC-AC-ACTS-E2E-208-approvals-tab-history-sc-reset-tutup-bagian-1 | Approvals Tab History: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1) | FE+BE | 31 | 642, 643, 644 |
| TC-AC-ACTS-E2E-209-approvals-tab-history-sc-reset-tutup-bagian-2-pagination | Approvals Tab History: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2) | FE+BE | 10 | 645 |
| TC-AC-ACTS-E2E-210-approvals-tab-history-state | Approvals Tab History: State Kosong, Empty-Filtered, Error Load, dan Loading | FE+BE | 23 | 647, 648, 649, 650 |
| TC-AC-ACTS-E2E-211-approvals-tab-history-download-hover-user | Approvals Tab History: Download CSV dan XLSX; Hover Nama User | FE+BE | 12 | 651, 652, 654 |
| TC-AC-ACTS-E2E-212-detail-sku-tab-available-registered-at-hasil-approve | Detail SKU Tab Available: Registered At Unit Hasil Approve Register Duplicate Tetap Waktu Scan, Berpasangan dengan Registered By | FE+BE | 16 | 805 |
| TC-AC-ACTS-E2E-213-tab-in-use-siklus-search | Detail SKU Tab In Use: Siklus Search Toolbar | FE+BE | 24 | 439 |
| TC-AC-ACTS-E2E-214-modal-event-log-buka-default-tab-add-stock-tutup-sesi-sku-ini-dan-popup-audit-tanpa-ikon | Modal Event Log: Buka di Tab Add Stock, Screening, Tutup (X), Esc, dan Backdrop, Hanya Sesi SKU Ini, serta Popup Audit TAG Tanpa Ikon Event Log | FE+BE | 41 | 472, 478, 479, 902, 903, 904 |
| TC-AC-ACTS-E2E-215-modal-event-log-kolom-actions-detail-dan-popup-detail-sesi-add-stock-delete-bulk-dan-scan | Modal Event Log: Kolom Actions Detail per Baris serta Popup Detail Sesi Add Stock, Delete Stock Bulk Parsial, dan Delete by Scan | FE+BE | 40 | 905, 933, 934, 935 |
| TC-AC-ACTS-E2E-216-modal-event-log-popup-detail-sesi-audit-snapshot-section-kosong-dan-empty-state | Modal Event Log: Popup Detail Sesi Audit, Snapshot Unit Terhapus, Section Tanpa Baris Disembunyikan, dan Empty State S-28 | FE+BE | 44 | 936, 937, 938, 939 |
| TC-AC-ACTS-E2E-217-modal-event-log-popup-detail-read-only-scroll-internal-dan-error-load | Modal Event Log: Popup Detail Read-Only dengan Scroll Internal dan Error Load Popup Detail | FE+BE | 20 | 940, 941 |
| TC-AC-ACTS-E2E-218-modal-event-log-penulisan-sesi-add-stock-delete-satuan-bulk-delete-parsial-dan-tanpa-keputusan-duplicate-approval | Modal Event Log: Penulisan Sesi Add Stock (Success dan Waiting), Delete Satuan, Bulk Delete Parsial, dan Tanpa Keputusan Duplicate Approval | FE+BE | 38 | 473, 474, 475, 477 |
| TC-AC-ACTS-E2E-219-modal-event-log-angka-success-per-tag-hardware-dan-unit-bypass | Modal Event Log: Angka Success Add Stock RFID Satu dan Dua TAG, Hardware Kosong untuk Import GPS, serta Unit Bypass E2a Tidak Dihitung | FE+BE | 39 | 766, 775, 944 |
| TC-AC-ACTS-E2E-220-modal-event-log-tab-audit-tag-penulisan-found-not-found-dan-recovery | Modal Event Log Tab Audit TAG: Penulisan Sesi dengan D-03 Dicentang dan Tidak serta Semua Verified dengan Recovery | FE+BE | 28 | 927, 928, 929 |
| TC-AC-ACTS-E2E-221-modal-event-log-batch-seluruhnya-waiting-menulis-baris-success-0 | Modal Event Log: Batch Add Stock Seluruhnya Waiting Menulis Baris dengan Success 0 | FE+BE | 13 | 945 |
| TC-AC-ACTS-E2E-222-modal-event-log-distributor-hanya-batch-sendiri-dan-tanpa-duplicate-canceled-global-settings | Modal Event Log: Distributor Hanya Melihat Sesi Batch Miliknya pada Kedua Tab dan Tanpa Duplicate Canceled dari Event Delete TAG Global Settings | FE+BE | 32 | 942, 943 |
| TC-AC-ACTS-E2E-223-modal-event-log-download-lebih-dari-5000-baris-loading-screen | Modal Event Log: Download Lebih dari 5.000 Baris Memakai Loading Screen lalu Langsung Terunduh | FE+BE | 8 | 111 |
| TC-AC-ACTS-E2E-224-modal-event-log-tab-add-stock-screening-urutan | Modal Event Log Tab Add Stock: Screening Header, Kolom, Footer dan Urutan Default | FE+BE | 11 | 480, 481 |
| TC-AC-ACTS-E2E-225-modal-event-log-tab-add-stock-sort-bagian-1 | Modal Event Log Tab Add Stock: Sort 3-State Per Kelas Kolom (Bagian 1) | FE+BE | 22 | 482, 483, 484 |
| TC-AC-ACTS-E2E-226-modal-event-log-tab-add-stock-sort-bagian-2-siklus-search | Modal Event Log Tab Add Stock: Sort 3-State Per Kelas Kolom (Bagian 2); Siklus Search Toolbar | FE+BE | 33 | 100, 485, 486 |
| TC-AC-ACTS-E2E-227-modal-event-log-tab-add-stock-search-kolom | Modal Event Log Tab Add Stock: Search Per Kelas Kolom dan Kolom Tanpa Search | FE+BE | 33 | 487, 488, 489, 490 |
| TC-AC-ACTS-E2E-228-modal-event-log-tab-add-stock-search-visibilitas-alur-search-filter | Modal Event Log Tab Add Stock: Search Terikat Visibilitas Kolom; Alur Search lalu Filter dan Filter lalu Search | FE+BE | 27 | 491, 492, 493, 494 |
| TC-AC-ACTS-E2E-229-modal-event-log-tab-add-stock-filter-bagian-1 | Modal Event Log Tab Add Stock: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1) | FE+BE | 20 | 495, 496, 497 |
| TC-AC-ACTS-E2E-230-modal-event-log-tab-add-stock-filter-bagian-2-sc-screening | Modal Event Log Tab Add Stock: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup | FE+BE | 20 | 498, 499, 500, 501 |
| TC-AC-ACTS-E2E-231-modal-event-log-tab-add-stock-sc-ceklis | Modal Event Log Tab Add Stock: Setup Column: Ceklis dan Unceklis Kolom | FE+BE | 17 | 502 |
| TC-AC-ACTS-E2E-232-modal-event-log-tab-add-stock-sc-urutan-pin | Modal Event Log Tab Add Stock: Setup Column: Geser Urutan serta Pin dan Unpin | FE+BE | 21 | 503, 504 |
| TC-AC-ACTS-E2E-233-modal-event-log-tab-add-stock-sc-reset-tutup-bagian-1 | Modal Event Log Tab Add Stock: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1) | FE+BE | 30 | 505, 506, 507 |
| TC-AC-ACTS-E2E-234-modal-event-log-tab-add-stock-sc-reset-tutup-bagian-2-pagination | Modal Event Log Tab Add Stock: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2) | FE+BE | 12 | 508 |
| TC-AC-ACTS-E2E-235-modal-event-log-tab-add-stock-state | Modal Event Log Tab Add Stock: State Kosong, Empty-Filtered, Error Load, dan Loading | FE+BE | 27 | 510, 511, 512, 513 |
| TC-AC-ACTS-E2E-236-modal-event-log-tab-add-stock-download-hover-user | Modal Event Log Tab Add Stock: Download CSV dan XLSX; Hover Nama User | FE+BE | 12 | 514, 515, 517 |
| TC-AC-ACTS-E2E-237-modal-event-log-tab-audit-tag-screening-urutan | Modal Event Log Tab Audit TAG: Screening Header, Kolom, Footer dan Urutan Default | FE+BE | 13 | 906, 907 |
| TC-AC-ACTS-E2E-238-modal-event-log-tab-audit-tag-sort-bagian-1 | Modal Event Log Tab Audit TAG: Sort 3-State Per Kelas Kolom (Bagian 1) | FE+BE | 23 | 908, 909, 910 |
| TC-AC-ACTS-E2E-239-modal-event-log-tab-audit-tag-sort-bagian-2-search-kolom | Modal Event Log Tab Audit TAG: Sort 3-State Per Kelas Kolom (Bagian 2); Search Per Kelas Kolom dan Kolom Tanpa Search | FE+BE | 31 | 911, 912, 913 |
| TC-AC-ACTS-E2E-240-modal-event-log-tab-audit-tag-filter | Modal Event Log Tab Audit TAG: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND | FE+BE | 27 | 914, 915, 916 |
| TC-AC-ACTS-E2E-241-modal-event-log-tab-audit-tag-sc-screening-sc-ceklis | Modal Event Log Tab Audit TAG: Setup Column: Screening Overlay dan Popup; Setup Column: Ceklis dan Unceklis Kolom | FE+BE | 25 | 917, 918 |
| TC-AC-ACTS-E2E-242-modal-event-log-tab-audit-tag-pagination | Modal Event Log Tab Audit TAG: Pagination | FE+BE | 14 | 919 |
| TC-AC-ACTS-E2E-243-modal-event-log-tab-audit-tag-state | Modal Event Log Tab Audit TAG: State Kosong, Empty-Filtered, Error Load, dan Loading | FE+BE | 28 | 920, 921, 922, 923 |
| TC-AC-ACTS-E2E-244-modal-event-log-tab-audit-tag-download | Modal Event Log Tab Audit TAG: Download CSV dan XLSX | FE+BE | 10 | 924, 925 |
| TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review | Approvals Tab Active: Screening, Satu Tabel Dua Type, Sel Device Name dan Category BYO Tanpa SKU, Requested By, Row Action Review, dan Subject Canceled Tidak Tampil | FE+BE | 36 | 566, 567, 568, 569, 570, 571, 572 |
| TC-AC-ACTS-E2E-246-approvals-tab-active-screening-urutan | Approvals Tab Active: Screening Header, Kolom, Footer dan Urutan Default | FE+BE | 10 | 573, 574 |
| TC-AC-ACTS-E2E-247-approvals-tab-active-sort-bagian-1 | Approvals Tab Active: Sort 3-State Per Kelas Kolom (Bagian 1) | FE+BE | 15 | 575, 576 |
| TC-AC-ACTS-E2E-248-approvals-tab-active-sort-bagian-2-siklus-search | Approvals Tab Active: Sort 3-State Per Kelas Kolom (Bagian 2); Siklus Search Toolbar | FE+BE | 30 | 577, 578 |
| TC-AC-ACTS-E2E-249-approvals-tab-active-search-kolom-bagian-1 | Approvals Tab Active: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1) | FE+BE | 42 | 579, 580, 581, 582 |
| TC-AC-ACTS-E2E-250-approvals-tab-active-search-kolom-bagian-2-search-visibilitas-alur-search-filter | Approvals Tab Active: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom; Alur Search lalu Filter dan Filter lalu Search | FE+BE | 33 | 583, 584, 585, 586, 587 |
| TC-AC-ACTS-E2E-251-approvals-tab-active-filter-bagian-1 | Approvals Tab Active: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1) | FE+BE | 18 | 588, 589, 590 |
| TC-AC-ACTS-E2E-252-approvals-tab-active-filter-bagian-2-sc-screening | Approvals Tab Active: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup | FE+BE | 19 | 591, 592, 593, 594 |
| TC-AC-ACTS-E2E-253-approvals-tab-active-sc-ceklis | Approvals Tab Active: Setup Column: Ceklis dan Unceklis Kolom | FE+BE | 16 | 595 |
| TC-AC-ACTS-E2E-254-approvals-tab-active-sc-urutan-pin | Approvals Tab Active: Setup Column: Geser Urutan serta Pin dan Unpin | FE+BE | 20 | 596, 597 |
| TC-AC-ACTS-E2E-255-approvals-tab-active-sc-reset-tutup-bagian-1 | Approvals Tab Active: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1) | FE+BE | 29 | 598, 599, 600 |
| TC-AC-ACTS-E2E-256-approvals-tab-active-sc-reset-tutup-bagian-2-pagination | Approvals Tab Active: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2) | FE+BE | 11 | 601 |
| TC-AC-ACTS-E2E-257-approvals-tab-active-state | Approvals Tab Active: State Kosong, Empty-Filtered, Error Load, dan Loading | FE+BE | 26 | 603, 604, 605, 606 |
| TC-AC-ACTS-E2E-258-approvals-tab-active-download | Approvals Tab Active: Download CSV dan XLSX | FE+BE | 8 | 607, 608 |
| TC-AC-ACTS-E2E-259-approvals-tab-active-dan-history-state-per-sub-tab-dan-refresh-f5 | Approvals Tab Active dan Tab History: State Search, Filter, Sort, dan Paginasi Per Sub-Tab serta Dipertahankan saat Refresh F5 | FE+BE | 40 | 788, 802 |
| TC-AC-ACTS-E2E-260-modal-event-log-dan-approvals-tab-active-isi-sel-berkas-xlsx | Modal Event Log (Tab Add Stock dan Tab Audit TAG) serta Approvals Tab Active: Isi Sel Berkas XLSX per Tipe Kolom | FE+BE | 34 | 516, 609, 926 |
| TC-AC-ACTS-E2E-261-modal-event-log-penulisan-sesi-delete-by-scan-unit-dilewati-audit-dan-kolom-hardware | Modal Event Log: Penulisan Sesi Delete by Scan, Unit Dilewati pada Sesi Audit TAG, dan Kolom Hardware Tab Audit TAG | FE+BE | 36 | 476, 931, 932 |
| TC-AC-ACTS-E2E-262-volume-pagination-stock-list-dan-detail-sku-tab-available-dan-in-use-101-baris | Volume Pagination (101 Baris atau Lebih): Stock List, Detail SKU Tab Available, dan Detail SKU Tab In Use | FE+BE | 39 | 66, 417, 463 |
| TC-AC-ACTS-E2E-263-volume-pagination-modal-event-log-tab-add-stock-dan-approvals-tab-active-dan-history-101-baris | Volume Pagination (101 Baris atau Lebih): Modal Event Log Tab Add Stock serta Approvals Tab Active dan Tab History | FE+BE | 43 | 509, 602, 646 |
| TC-AC-ACTS-E2E-264-volume-add-stock-rfid-1001-tag-tanpa-field-notes-dan-tanpa-batas-unit | Volume Add Stock RFID 1.001 TAG dalam Satu Sesi Scan: Tanpa Field Notes dan Tanpa Batas Jumlah Unit | FE+BE | 15 | 732 |
| TC-AC-ACTS-E2E-265-isi-sel-detail-sku-tab-available-tab-in-use-dan-approvals-tab-history-berkas-xlsx | Detail SKU Tab Available dan Tab In Use serta Approvals Tab History: Isi Sel Berkas XLSX per Tipe Kolom | FE+BE | 24 | 424, 470, 653 |
| TC-AC-ACTS-E2E-266-resilience-add-stock-rfid-kegagalan-menulis-tag-log-membatalkan-transaksi | Resilience Add Stock RFID: Kegagalan Menulis Entri TAG Log Membatalkan Transaksi Kejadiannya | FE+BE | 9 | 981 |
| TC-AC-ACTS-E2E-267-detail-sku-banner-waiting-for-approval-hilang-tanpa-reload-setelah-reject-unit-terakhir | Detail SKU Realtime: Banner Waiting for Approval Hilang Tanpa Reload Setelah Unit Terakhir Di-Reject | FE+BE | 10 | 995 |

## Lapisan per TC

| TC | Spec | Mode |
|---|---|:---:|
| TC-AC-ACTS-1 | TC-AC-ACTS-E2E-001-screening-stock-list-breadcrumb-header-kolom-dan-footer | FE+BE |
| TC-AC-ACTS-2 | TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | FE+BE |
| TC-AC-ACTS-3 | TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | FE+BE |
| TC-AC-ACTS-4 | TC-AC-ACTS-E2E-006-stock-list-mengikuti-aksi-delete-audit-dan-sku-baru | FE+BE |
| TC-AC-ACTS-5 | TC-AC-ACTS-E2E-004-navigasi-stock-list-detail-sku-dan-add-stock-per-tag-type | FE+BE |
| TC-AC-ACTS-6 | TC-AC-ACTS-E2E-004-navigasi-stock-list-detail-sku-dan-add-stock-per-tag-type | FE+BE |
| TC-AC-ACTS-7 | TC-AC-ACTS-E2E-004-navigasi-stock-list-detail-sku-dan-add-stock-per-tag-type | FE+BE |
| TC-AC-ACTS-8 | TC-AC-ACTS-E2E-004-navigasi-stock-list-detail-sku-dan-add-stock-per-tag-type | FE+BE |
| TC-AC-ACTS-9 | TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | FE+BE |
| TC-AC-ACTS-10 | TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | FE+BE |
| TC-AC-ACTS-11 | TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | FE+BE |
| TC-AC-ACTS-12 | TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | FE+BE |
| TC-AC-ACTS-13 | TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | FE+BE |
| TC-AC-ACTS-14 | TC-AC-ACTS-E2E-002-isi-sel-stock-list-tanpa-kuota-icon-tag-type-badge-dan-device-name-panjang | FE+BE |
| TC-AC-ACTS-15 | TC-AC-ACTS-E2E-001-screening-stock-list-breadcrumb-header-kolom-dan-footer | FE+BE |
| TC-AC-ACTS-16 | TC-AC-ACTS-E2E-005-distributor-stock-list-metrik-di-scope-unit-sendiri | FE+BE |
| TC-AC-ACTS-17 | TC-AC-ACTS-E2E-005-distributor-stock-list-metrik-di-scope-unit-sendiri | FE+BE |
| TC-AC-ACTS-18 | TC-AC-ACTS-E2E-005-distributor-stock-list-metrik-di-scope-unit-sendiri | FE+BE |
| TC-AC-ACTS-19 | TC-AC-ACTS-E2E-005-distributor-stock-list-metrik-di-scope-unit-sendiri | FE+BE |
| TC-AC-ACTS-20 | TC-AC-ACTS-E2E-002-isi-sel-stock-list-tanpa-kuota-icon-tag-type-badge-dan-device-name-panjang | FE+BE |
| TC-AC-ACTS-21 | TC-AC-ACTS-E2E-002-isi-sel-stock-list-tanpa-kuota-icon-tag-type-badge-dan-device-name-panjang | FE+BE |
| TC-AC-ACTS-22 | TC-AC-ACTS-E2E-002-isi-sel-stock-list-tanpa-kuota-icon-tag-type-badge-dan-device-name-panjang | FE+BE |
| TC-AC-ACTS-23 | TC-AC-ACTS-E2E-002-isi-sel-stock-list-tanpa-kuota-icon-tag-type-badge-dan-device-name-panjang | FE+BE |
| TC-AC-ACTS-24 | TC-AC-ACTS-E2E-007-guided-tooltip-stock-list-empat-step-navigasi-flag-dan-keyboard | FE+BE |
| TC-AC-ACTS-25 | TC-AC-ACTS-E2E-007-guided-tooltip-stock-list-empat-step-navigasi-flag-dan-keyboard | FE+BE |
| TC-AC-ACTS-26 | TC-AC-ACTS-E2E-007-guided-tooltip-stock-list-empat-step-navigasi-flag-dan-keyboard | FE+BE |
| TC-AC-ACTS-27 | TC-AC-ACTS-E2E-007-guided-tooltip-stock-list-empat-step-navigasi-flag-dan-keyboard | FE+BE |
| TC-AC-ACTS-28 | TC-AC-ACTS-E2E-007-guided-tooltip-stock-list-empat-step-navigasi-flag-dan-keyboard | FE+BE |
| TC-AC-ACTS-29 | TC-AC-ACTS-E2E-159-detail-sku-aria-label-sort-tag-code-mutasi-terfilter-siklus-toast-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-30 | TC-AC-ACTS-E2E-008-retensi-state-stock-list-back-refresh-reset-menu-dan-cache-setup-column | FE+BE |
| TC-AC-ACTS-31 | TC-AC-ACTS-E2E-008-retensi-state-stock-list-back-refresh-reset-menu-dan-cache-setup-column | FE+BE |
| TC-AC-ACTS-32 | TC-AC-ACTS-E2E-008-retensi-state-stock-list-back-refresh-reset-menu-dan-cache-setup-column | FE+BE |
| TC-AC-ACTS-33 | TC-AC-ACTS-E2E-001-screening-stock-list-breadcrumb-header-kolom-dan-footer | FE+BE |
| TC-AC-ACTS-34 | TC-AC-ACTS-E2E-001-screening-stock-list-breadcrumb-header-kolom-dan-footer | FE+BE |
| TC-AC-ACTS-35 | TC-AC-ACTS-E2E-001-screening-stock-list-breadcrumb-header-kolom-dan-footer | FE+BE |
| TC-AC-ACTS-36 | TC-AC-ACTS-E2E-009-sort-stock-list-kelas-teks-dan-label | FE+BE |
| TC-AC-ACTS-37 | TC-AC-ACTS-E2E-009-sort-stock-list-kelas-teks-dan-label | FE+BE |
| TC-AC-ACTS-38 | TC-AC-ACTS-E2E-010-sort-stock-list-kelas-numerik-tanggal-dan-kolom-non-sortable | FE+BE |
| TC-AC-ACTS-39 | TC-AC-ACTS-E2E-010-sort-stock-list-kelas-numerik-tanggal-dan-kolom-non-sortable | FE+BE |
| TC-AC-ACTS-40 | TC-AC-ACTS-E2E-010-sort-stock-list-kelas-numerik-tanggal-dan-kolom-non-sortable | FE+BE |
| TC-AC-ACTS-41 | TC-AC-ACTS-E2E-011-search-stock-list-siklus-kelas-teks-dan-kolom-tanpa-search | FE+BE |
| TC-AC-ACTS-42 | TC-AC-ACTS-E2E-011-search-stock-list-siklus-kelas-teks-dan-kolom-tanpa-search | FE+BE |
| TC-AC-ACTS-43 | TC-AC-ACTS-E2E-012-search-stock-list-badge-enum-dan-visibilitas-kolom-brand | FE+BE |
| TC-AC-ACTS-44 | TC-AC-ACTS-E2E-012-search-stock-list-badge-enum-dan-visibilitas-kolom-brand | FE+BE |
| TC-AC-ACTS-45 | TC-AC-ACTS-E2E-013-search-stock-list-numerik-dan-alur-search-filter | FE+BE |
| TC-AC-ACTS-46 | TC-AC-ACTS-E2E-011-search-stock-list-siklus-kelas-teks-dan-kolom-tanpa-search | FE+BE |
| TC-AC-ACTS-47 | TC-AC-ACTS-E2E-012-search-stock-list-badge-enum-dan-visibilitas-kolom-brand | FE+BE |
| TC-AC-ACTS-48 | TC-AC-ACTS-E2E-012-search-stock-list-badge-enum-dan-visibilitas-kolom-brand | FE+BE |
| TC-AC-ACTS-49 | TC-AC-ACTS-E2E-013-search-stock-list-numerik-dan-alur-search-filter | FE+BE |
| TC-AC-ACTS-50 | TC-AC-ACTS-E2E-013-search-stock-list-numerik-dan-alur-search-filter | FE+BE |
| TC-AC-ACTS-51 | TC-AC-ACTS-E2E-014-filter-stock-list-screening-panel-range-dan-field-sku | FE+BE |
| TC-AC-ACTS-52 | TC-AC-ACTS-E2E-015-filter-stock-list-dropdown-date-range-dan-opsi-distinct | FE+BE |
| TC-AC-ACTS-53 | TC-AC-ACTS-E2E-015-filter-stock-list-dropdown-date-range-dan-opsi-distinct | FE+BE |
| TC-AC-ACTS-54 | TC-AC-ACTS-E2E-014-filter-stock-list-screening-panel-range-dan-field-sku | FE+BE |
| TC-AC-ACTS-55 | TC-AC-ACTS-E2E-015-filter-stock-list-dropdown-date-range-dan-opsi-distinct | FE+BE |
| TC-AC-ACTS-56 | TC-AC-ACTS-E2E-016-filter-stock-list-kombinasi-and-dan-independen-dari-column-visibility | FE+BE |
| TC-AC-ACTS-57 | TC-AC-ACTS-E2E-017-setup-column-stock-list-screening-satu-kolom-tersisa-dan-pin-ke-4 | FE+BE |
| TC-AC-ACTS-58 | TC-AC-ACTS-E2E-017-setup-column-stock-list-screening-satu-kolom-tersisa-dan-pin-ke-4 | FE+BE |
| TC-AC-ACTS-59 | TC-AC-ACTS-E2E-018-setup-column-stock-list-ceklis-dan-unceklis-kolom | FE+BE |
| TC-AC-ACTS-60 | TC-AC-ACTS-E2E-019-setup-column-stock-list-urutan-pin-reset-dan-tutup | FE+BE |
| TC-AC-ACTS-61 | TC-AC-ACTS-E2E-019-setup-column-stock-list-urutan-pin-reset-dan-tutup | FE+BE |
| TC-AC-ACTS-62 | TC-AC-ACTS-E2E-019-setup-column-stock-list-urutan-pin-reset-dan-tutup | FE+BE |
| TC-AC-ACTS-63 | TC-AC-ACTS-E2E-019-setup-column-stock-list-urutan-pin-reset-dan-tutup | FE+BE |
| TC-AC-ACTS-64 | TC-AC-ACTS-E2E-017-setup-column-stock-list-screening-satu-kolom-tersisa-dan-pin-ke-4 | FE+BE |
| TC-AC-ACTS-65 | TC-AC-ACTS-E2E-017-setup-column-stock-list-screening-satu-kolom-tersisa-dan-pin-ke-4 | FE+BE |
| TC-AC-ACTS-66 | TC-AC-ACTS-E2E-262-volume-pagination-stock-list-dan-detail-sku-tab-available-dan-in-use-101-baris | FE+BE |
| TC-AC-ACTS-67 | TC-AC-ACTS-E2E-020-pagination-dan-state-stock-list-kosong-error-dan-loading | FE+BE |
| TC-AC-ACTS-68 | TC-AC-ACTS-E2E-020-pagination-dan-state-stock-list-kosong-error-dan-loading | FE+BE |
| TC-AC-ACTS-69 | TC-AC-ACTS-E2E-020-pagination-dan-state-stock-list-kosong-error-dan-loading | FE+BE |
| TC-AC-ACTS-70 | TC-AC-ACTS-E2E-020-pagination-dan-state-stock-list-kosong-error-dan-loading | FE+BE |
| TC-AC-ACTS-71 | TC-AC-ACTS-E2E-021-download-stock-list-csv-dan-xlsx-nama-berkas | FE+BE |
| TC-AC-ACTS-72 | TC-AC-ACTS-E2E-021-download-stock-list-csv-dan-xlsx-nama-berkas | FE+BE |
| TC-AC-ACTS-73 | TC-AC-ACTS-E2E-037-download-stock-list-isi-sel-xlsx | FE+BE |
| TC-AC-ACTS-74 | TC-AC-ACTS-E2E-022-lintas-permukaan-tooltip-table-tools-dan-search-spasi-tepi | FE+BE |
| TC-AC-ACTS-75 | TC-AC-ACTS-E2E-022-lintas-permukaan-tooltip-table-tools-dan-search-spasi-tepi | FE+BE |
| TC-AC-ACTS-76 | TC-AC-ACTS-E2E-023-lintas-permukaan-search-literal-dan-spasi-tengah | FE+BE |
| TC-AC-ACTS-77 | TC-AC-ACTS-E2E-023-lintas-permukaan-search-literal-dan-spasi-tengah | FE+BE |
| TC-AC-ACTS-78 | TC-AC-ACTS-E2E-024-lintas-permukaan-pagination-halaman-tidak-valid-page-size-dan-sort | FE+BE |
| TC-AC-ACTS-79 | TC-AC-ACTS-E2E-024-lintas-permukaan-pagination-halaman-tidak-valid-page-size-dan-sort | FE+BE |
| TC-AC-ACTS-80 | TC-AC-ACTS-E2E-024-lintas-permukaan-pagination-halaman-tidak-valid-page-size-dan-sort | FE+BE |
| TC-AC-ACTS-81 | TC-AC-ACTS-E2E-025-lintas-permukaan-search-dan-apply-filter-reset-halaman | FE+BE |
| TC-AC-ACTS-82 | TC-AC-ACTS-E2E-039-lintas-permukaan-filter-search-di-dalam-dropdown | FE+BE |
| TC-AC-ACTS-83 | TC-AC-ACTS-E2E-040-lintas-permukaan-filter-chip-dan-hapus-lewat-x | FE+BE |
| TC-AC-ACTS-84 | TC-AC-ACTS-E2E-041-lintas-permukaan-filter-uncheck-opsi-menghapus-chip | FE+BE |
| TC-AC-ACTS-85 | TC-AC-ACTS-E2E-042-lintas-permukaan-filter-hapus-chip-lalu-apply | FE+BE |
| TC-AC-ACTS-86 | TC-AC-ACTS-E2E-043-lintas-permukaan-filter-chip-more-saat-melebihi-lebar | FE+BE |
| TC-AC-ACTS-87 | TC-AC-ACTS-E2E-044-lintas-permukaan-filter-dropdown-loading-kosong-dan-stale | FE+BE |
| TC-AC-ACTS-88 | TC-AC-ACTS-E2E-045-lintas-permukaan-filter-tutup-panel-tanpa-apply-membuang-draft | FE+BE |
| TC-AC-ACTS-89 | TC-AC-ACTS-E2E-046-lintas-permukaan-filter-titik-aktif-pada-ikon-filter | FE+BE |
| TC-AC-ACTS-90 | TC-AC-ACTS-E2E-047-lintas-permukaan-filter-clear-field-mengosongkan-semua-field | FE+BE |
| TC-AC-ACTS-91 | TC-AC-ACTS-E2E-014-filter-stock-list-screening-panel-range-dan-field-sku | FE+BE |
| TC-AC-ACTS-92 | TC-AC-ACTS-E2E-014-filter-stock-list-screening-panel-range-dan-field-sku | FE+BE |
| TC-AC-ACTS-93 | TC-AC-ACTS-E2E-026-lintas-permukaan-independensi-clear-filter-dan-clear-search | FE+BE |
| TC-AC-ACTS-94 | TC-AC-ACTS-E2E-026-lintas-permukaan-independensi-clear-filter-dan-clear-search | FE+BE |
| TC-AC-ACTS-95 | TC-AC-ACTS-E2E-027-lintas-permukaan-independensi-ganti-sort-dan-pemulihan-empty-state | FE+BE |
| TC-AC-ACTS-96 | TC-AC-ACTS-E2E-027-lintas-permukaan-independensi-ganti-sort-dan-pemulihan-empty-state | FE+BE |
| TC-AC-ACTS-97 | TC-AC-ACTS-E2E-006-stock-list-mengikuti-aksi-delete-audit-dan-sku-baru | FE+BE |
| TC-AC-ACTS-98 | TC-AC-ACTS-E2E-159-detail-sku-aria-label-sort-tag-code-mutasi-terfilter-siklus-toast-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-99 | TC-AC-ACTS-E2E-006-stock-list-mengikuti-aksi-delete-audit-dan-sku-baru | FE+BE |
| TC-AC-ACTS-100 | TC-AC-ACTS-E2E-226-modal-event-log-tab-add-stock-sort-bagian-2-siklus-search | FE+BE |
| TC-AC-ACTS-101 | TC-AC-ACTS-E2E-159-detail-sku-aria-label-sort-tag-code-mutasi-terfilter-siklus-toast-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-102 | TC-AC-ACTS-E2E-080-lintas-permukaan-download-seluruh-baris-dan-hasil-search-filter | FE+BE |
| TC-AC-ACTS-103 | TC-AC-ACTS-E2E-080-lintas-permukaan-download-seluruh-baris-dan-hasil-search-filter | FE+BE |
| TC-AC-ACTS-104 | TC-AC-ACTS-E2E-081-lintas-permukaan-download-kolom-hide-dan-unhide | FE+BE |
| TC-AC-ACTS-105 | TC-AC-ACTS-E2E-081-lintas-permukaan-download-kolom-hide-dan-unhide | FE+BE |
| TC-AC-ACTS-106 | TC-AC-ACTS-E2E-082-lintas-permukaan-download-tanpa-toast-gagal-dan-xlsx-sheet1 | FE+BE |
| TC-AC-ACTS-107 | TC-AC-ACTS-E2E-082-lintas-permukaan-download-tanpa-toast-gagal-dan-xlsx-sheet1 | FE+BE |
| TC-AC-ACTS-108 | TC-AC-ACTS-E2E-083-lintas-permukaan-download-hasil-kosong-dan-csv-pemisah-bom-kutip | FE+BE |
| TC-AC-ACTS-109 | TC-AC-ACTS-E2E-083-lintas-permukaan-download-hasil-kosong-dan-csv-pemisah-bom-kutip | FE+BE |
| TC-AC-ACTS-110 | TC-AC-ACTS-E2E-082-lintas-permukaan-download-tanpa-toast-gagal-dan-xlsx-sheet1 | FE+BE |
| TC-AC-ACTS-111 | TC-AC-ACTS-E2E-223-modal-event-log-download-lebih-dari-5000-baris-loading-screen | FE+BE |
| TC-AC-ACTS-112 | TC-AC-ACTS-E2E-008-retensi-state-stock-list-back-refresh-reset-menu-dan-cache-setup-column | FE+BE |
| TC-AC-ACTS-113 | TC-AC-ACTS-E2E-008-retensi-state-stock-list-back-refresh-reset-menu-dan-cache-setup-column | FE+BE |
| TC-AC-ACTS-114 | TC-AC-ACTS-E2E-028-role-matrix-visibilitas-elemen-total-control-dan-default-user | FE+BE |
| TC-AC-ACTS-115 | TC-AC-ACTS-E2E-028-role-matrix-visibilitas-elemen-total-control-dan-default-user | FE+BE |
| TC-AC-ACTS-116 | TC-AC-ACTS-E2E-029-role-matrix-visibilitas-elemen-read-only-dan-additional-approver | FE+BE |
| TC-AC-ACTS-117 | TC-AC-ACTS-E2E-029-role-matrix-visibilitas-elemen-read-only-dan-additional-approver | FE+BE |
| TC-AC-ACTS-118 | TC-AC-ACTS-E2E-030-role-matrix-visibilitas-elemen-manage-tag-stock-create-dan-update | FE+BE |
| TC-AC-ACTS-119 | TC-AC-ACTS-E2E-030-role-matrix-visibilitas-elemen-manage-tag-stock-create-dan-update | FE+BE |
| TC-AC-ACTS-120 | TC-AC-ACTS-E2E-031-role-matrix-visibilitas-elemen-manage-tag-stock-delete-dan-read | FE+BE |
| TC-AC-ACTS-121 | TC-AC-ACTS-E2E-031-role-matrix-visibilitas-elemen-manage-tag-stock-delete-dan-read | FE+BE |
| TC-AC-ACTS-122 | TC-AC-ACTS-E2E-032-role-matrix-visibilitas-elemen-distributor-toggle-on-dan-off | FE+BE |
| TC-AC-ACTS-123 | TC-AC-ACTS-E2E-032-role-matrix-visibilitas-elemen-distributor-toggle-on-dan-off | FE+BE |
| TC-AC-ACTS-124 | TC-AC-ACTS-E2E-033-role-matrix-negatif-tanpa-akses-tag-stock-dan-sidebar | FE+BE |
| TC-AC-ACTS-125 | TC-AC-ACTS-E2E-033-role-matrix-negatif-tanpa-akses-tag-stock-dan-sidebar | FE+BE |
| TC-AC-ACTS-126 | TC-AC-ACTS-E2E-033-role-matrix-negatif-tanpa-akses-tag-stock-dan-sidebar | FE+BE |
| TC-AC-ACTS-127 | TC-AC-ACTS-E2E-033-role-matrix-negatif-tanpa-akses-tag-stock-dan-sidebar | FE+BE |
| TC-AC-ACTS-128 | TC-AC-ACTS-E2E-034-role-matrix-positif-eksekusi-add-stock-audit-dan-scan-distributor | FE+BE |
| TC-AC-ACTS-129 | TC-AC-ACTS-E2E-034-role-matrix-positif-eksekusi-add-stock-audit-dan-scan-distributor | FE+BE |
| TC-AC-ACTS-130 | TC-AC-ACTS-E2E-034-role-matrix-positif-eksekusi-add-stock-audit-dan-scan-distributor | FE+BE |
| TC-AC-ACTS-131 | TC-AC-ACTS-E2E-035-role-matrix-positif-delete-dan-approval-manage-delete-distributor-dan-additional-approver | FE+BE |
| TC-AC-ACTS-132 | TC-AC-ACTS-E2E-035-role-matrix-positif-delete-dan-approval-manage-delete-distributor-dan-additional-approver | FE+BE |
| TC-AC-ACTS-133 | TC-AC-ACTS-E2E-034-role-matrix-positif-eksekusi-add-stock-audit-dan-scan-distributor | FE+BE |
| TC-AC-ACTS-134 | TC-AC-ACTS-E2E-034-role-matrix-positif-eksekusi-add-stock-audit-dan-scan-distributor | FE+BE |
| TC-AC-ACTS-135 | TC-AC-ACTS-E2E-035-role-matrix-positif-delete-dan-approval-manage-delete-distributor-dan-additional-approver | FE+BE |
| TC-AC-ACTS-136 | TC-AC-ACTS-E2E-033-role-matrix-negatif-tanpa-akses-tag-stock-dan-sidebar | FE+BE |
| TC-AC-ACTS-137 | TC-AC-ACTS-E2E-033-role-matrix-negatif-tanpa-akses-tag-stock-dan-sidebar | FE+BE |
| TC-AC-ACTS-138 | TC-AC-ACTS-E2E-149-state-tenant-distributor-suspended-aksi-tulis-ditolak-dan-plan-gating-tidak-ada | FE+BE |
| TC-AC-ACTS-139 | TC-AC-ACTS-E2E-048-add-stock-rfid-screening-sesi-scan-mengunci-halaman-dan-baris-ok | FE+BE |
| TC-AC-ACTS-140 | TC-AC-ACTS-E2E-048-add-stock-rfid-screening-sesi-scan-mengunci-halaman-dan-baris-ok | FE+BE |
| TC-AC-ACTS-141 | TC-AC-ACTS-E2E-048-add-stock-rfid-screening-sesi-scan-mengunci-halaman-dan-baris-ok | FE+BE |
| TC-AC-ACTS-142 | TC-AC-ACTS-E2E-049-add-stock-rfid-duplikat-dalam-sesi-dan-baris-scan-tidak-lengkap | FE+BE |
| TC-AC-ACTS-143 | TC-AC-ACTS-E2E-049-add-stock-rfid-duplikat-dalam-sesi-dan-baris-scan-tidak-lengkap | FE+BE |
| TC-AC-ACTS-144 | TC-AC-ACTS-E2E-057-add-stock-rfid-match-existing-waiting-for-approval-per-identifier | FE+BE |
| TC-AC-ACTS-145 | TC-AC-ACTS-E2E-057-add-stock-rfid-match-existing-waiting-for-approval-per-identifier | FE+BE |
| TC-AC-ACTS-146 | TC-AC-ACTS-E2E-057-add-stock-rfid-match-existing-waiting-for-approval-per-identifier | FE+BE |
| TC-AC-ACTS-147 | TC-AC-ACTS-E2E-057-add-stock-rfid-match-existing-waiting-for-approval-per-identifier | FE+BE |
| TC-AC-ACTS-148 | TC-AC-ACTS-E2E-057-add-stock-rfid-match-existing-waiting-for-approval-per-identifier | FE+BE |
| TC-AC-ACTS-149 | TC-AC-ACTS-E2E-049-add-stock-rfid-duplikat-dalam-sesi-dan-baris-scan-tidak-lengkap | FE+BE |
| TC-AC-ACTS-150 | TC-AC-ACTS-E2E-049-add-stock-rfid-duplikat-dalam-sesi-dan-baris-scan-tidak-lengkap | FE+BE |
| TC-AC-ACTS-151 | TC-AC-ACTS-E2E-050-add-stock-rfid-remove-by-scan-disabled-hapus-baris-dan-toast | FE+BE |
| TC-AC-ACTS-152 | TC-AC-ACTS-E2E-050-add-stock-rfid-remove-by-scan-disabled-hapus-baris-dan-toast | FE+BE |
| TC-AC-ACTS-153 | TC-AC-ACTS-E2E-050-add-stock-rfid-remove-by-scan-disabled-hapus-baris-dan-toast | FE+BE |
| TC-AC-ACTS-154 | TC-AC-ACTS-E2E-048-add-stock-rfid-screening-sesi-scan-mengunci-halaman-dan-baris-ok | FE+BE |
| TC-AC-ACTS-155 | TC-AC-ACTS-E2E-053-add-stock-rfid-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-156 | TC-AC-ACTS-E2E-053-add-stock-rfid-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-157 | TC-AC-ACTS-E2E-053-add-stock-rfid-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-158 | TC-AC-ACTS-E2E-053-add-stock-rfid-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-159 | TC-AC-ACTS-E2E-054-add-stock-rfid-reload-back-fisik-dan-pindah-tab-saat-sesi-aktif | FE+BE |
| TC-AC-ACTS-160 | TC-AC-ACTS-E2E-054-add-stock-rfid-reload-back-fisik-dan-pindah-tab-saat-sesi-aktif | FE+BE |
| TC-AC-ACTS-161 | TC-AC-ACTS-E2E-054-add-stock-rfid-reload-back-fisik-dan-pindah-tab-saat-sesi-aktif | FE+BE |
| TC-AC-ACTS-162 | TC-AC-ACTS-E2E-054-add-stock-rfid-reload-back-fisik-dan-pindah-tab-saat-sesi-aktif | FE+BE |
| TC-AC-ACTS-163 | TC-AC-ACTS-E2E-055-add-stock-rfid-reader-tidak-terhubung-putus-saat-sesi-dan-idle | FE+BE |
| TC-AC-ACTS-164 | TC-AC-ACTS-E2E-055-add-stock-rfid-reader-tidak-terhubung-putus-saat-sesi-dan-idle | FE+BE |
| TC-AC-ACTS-165 | TC-AC-ACTS-E2E-055-add-stock-rfid-reader-tidak-terhubung-putus-saat-sesi-dan-idle | FE+BE |
| TC-AC-ACTS-166 | TC-AC-ACTS-E2E-055-add-stock-rfid-reader-tidak-terhubung-putus-saat-sesi-dan-idle | FE+BE |
| TC-AC-ACTS-167 | TC-AC-ACTS-E2E-056-add-stock-rfid-submit-ok-kosong-klik-ganda-sku-tidak-valid-dan-tanpa-batas | FE+BE |
| TC-AC-ACTS-168 | TC-AC-ACTS-E2E-056-add-stock-rfid-submit-ok-kosong-klik-ganda-sku-tidak-valid-dan-tanpa-batas | FE+BE |
| TC-AC-ACTS-169 | TC-AC-ACTS-E2E-058-add-stock-rfid-submit-waiting-partial-register-dan-bentuk-tunggal-jamak | FE+BE |
| TC-AC-ACTS-170 | TC-AC-ACTS-E2E-058-add-stock-rfid-submit-waiting-partial-register-dan-bentuk-tunggal-jamak | FE+BE |
| TC-AC-ACTS-171 | TC-AC-ACTS-E2E-058-add-stock-rfid-submit-waiting-partial-register-dan-bentuk-tunggal-jamak | FE+BE |
| TC-AC-ACTS-172 | TC-AC-ACTS-E2E-058-add-stock-rfid-submit-waiting-partial-register-dan-bentuk-tunggal-jamak | FE+BE |
| TC-AC-ACTS-173 | TC-AC-ACTS-E2E-075-resilience-add-stock-submit-gagal-dan-timeout-rfid-nfc-ble-gps | FE+BE |
| TC-AC-ACTS-174 | TC-AC-ACTS-E2E-056-add-stock-rfid-submit-ok-kosong-klik-ganda-sku-tidak-valid-dan-tanpa-batas | FE+BE |
| TC-AC-ACTS-175 | TC-AC-ACTS-E2E-076-konkurensi-add-stock-toggle-local-registration-dimatikan-saat-sesi | FE+BE |
| TC-AC-ACTS-176 | TC-AC-ACTS-E2E-059-add-stock-rfid-normalisasi-identifier-unit-rejected-dan-submit-ulang | FE+BE |
| TC-AC-ACTS-177 | TC-AC-ACTS-E2E-061-add-stock-rfid-detail-ui-aria-live-tooltip-badge-kartu-sku-dan-saving-state | FE+BE |
| TC-AC-ACTS-178 | TC-AC-ACTS-E2E-078-konkurensi-add-stock-dua-sesi-submit-identifier-sama-dan-hasil-commit-berbeda | FE+BE |
| TC-AC-ACTS-179 | TC-AC-ACTS-E2E-061-add-stock-rfid-detail-ui-aria-live-tooltip-badge-kartu-sku-dan-saving-state | FE+BE |
| TC-AC-ACTS-180 | TC-AC-ACTS-E2E-061-add-stock-rfid-detail-ui-aria-live-tooltip-badge-kartu-sku-dan-saving-state | FE+BE |
| TC-AC-ACTS-181 | TC-AC-ACTS-E2E-060-add-stock-rfid-bypass-e2a-total-control-pada-batch-campuran | FE+BE |
| TC-AC-ACTS-182 | TC-AC-ACTS-E2E-063-add-stock-nfc-screening-sesi-scan-baris-ok-dan-mode-terkunci | FE+BE |
| TC-AC-ACTS-183 | TC-AC-ACTS-E2E-063-add-stock-nfc-screening-sesi-scan-baris-ok-dan-mode-terkunci | FE+BE |
| TC-AC-ACTS-184 | TC-AC-ACTS-E2E-063-add-stock-nfc-screening-sesi-scan-baris-ok-dan-mode-terkunci | FE+BE |
| TC-AC-ACTS-185 | TC-AC-ACTS-E2E-064-add-stock-nfc-duplikat-uid-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-186 | TC-AC-ACTS-E2E-064-add-stock-nfc-duplikat-uid-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-187 | TC-AC-ACTS-E2E-064-add-stock-nfc-duplikat-uid-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-188 | TC-AC-ACTS-E2E-064-add-stock-nfc-duplikat-uid-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-189 | TC-AC-ACTS-E2E-064-add-stock-nfc-duplikat-uid-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-190 | TC-AC-ACTS-E2E-063-add-stock-nfc-screening-sesi-scan-baris-ok-dan-mode-terkunci | FE+BE |
| TC-AC-ACTS-191 | TC-AC-ACTS-E2E-065-add-stock-nfc-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-192 | TC-AC-ACTS-E2E-065-add-stock-nfc-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-193 | TC-AC-ACTS-E2E-065-add-stock-nfc-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-194 | TC-AC-ACTS-E2E-065-add-stock-nfc-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-195 | TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble | FE+BE |
| TC-AC-ACTS-196 | TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble | FE+BE |
| TC-AC-ACTS-197 | TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble | FE+BE |
| TC-AC-ACTS-198 | TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble | FE+BE |
| TC-AC-ACTS-199 | TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble | FE+BE |
| TC-AC-ACTS-200 | TC-AC-ACTS-E2E-067-add-stock-nfc-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-201 | TC-AC-ACTS-E2E-067-add-stock-nfc-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-202 | TC-AC-ACTS-E2E-068-add-stock-nfc-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-203 | TC-AC-ACTS-E2E-068-add-stock-nfc-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-204 | TC-AC-ACTS-E2E-068-add-stock-nfc-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-205 | TC-AC-ACTS-E2E-068-add-stock-nfc-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-206 | TC-AC-ACTS-E2E-075-resilience-add-stock-submit-gagal-dan-timeout-rfid-nfc-ble-gps | FE+BE |
| TC-AC-ACTS-207 | TC-AC-ACTS-E2E-067-add-stock-nfc-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-208 | TC-AC-ACTS-E2E-076-konkurensi-add-stock-toggle-local-registration-dimatikan-saat-sesi | FE+BE |
| TC-AC-ACTS-209 | TC-AC-ACTS-E2E-068-add-stock-nfc-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-210 | TC-AC-ACTS-E2E-067-add-stock-nfc-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-211 | TC-AC-ACTS-E2E-069-add-stock-ble-screening-sesi-scan-baris-ok-dan-mode-terkunci | FE+BE |
| TC-AC-ACTS-212 | TC-AC-ACTS-E2E-069-add-stock-ble-screening-sesi-scan-baris-ok-dan-mode-terkunci | FE+BE |
| TC-AC-ACTS-213 | TC-AC-ACTS-E2E-069-add-stock-ble-screening-sesi-scan-baris-ok-dan-mode-terkunci | FE+BE |
| TC-AC-ACTS-214 | TC-AC-ACTS-E2E-070-add-stock-ble-duplikat-mac-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-215 | TC-AC-ACTS-E2E-070-add-stock-ble-duplikat-mac-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-216 | TC-AC-ACTS-E2E-070-add-stock-ble-duplikat-mac-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-217 | TC-AC-ACTS-E2E-070-add-stock-ble-duplikat-mac-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-218 | TC-AC-ACTS-E2E-070-add-stock-ble-duplikat-mac-waiting-dan-remove-by-scan | FE+BE |
| TC-AC-ACTS-219 | TC-AC-ACTS-E2E-069-add-stock-ble-screening-sesi-scan-baris-ok-dan-mode-terkunci | FE+BE |
| TC-AC-ACTS-220 | TC-AC-ACTS-E2E-071-add-stock-ble-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-221 | TC-AC-ACTS-E2E-071-add-stock-ble-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-222 | TC-AC-ACTS-E2E-071-add-stock-ble-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-223 | TC-AC-ACTS-E2E-071-add-stock-ble-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-224 | TC-AC-ACTS-E2E-072-add-stock-ble-reload-back-fisik-pindah-tab-scanner-tidak-terhubung-dan-putus | FE+BE |
| TC-AC-ACTS-225 | TC-AC-ACTS-E2E-072-add-stock-ble-reload-back-fisik-pindah-tab-scanner-tidak-terhubung-dan-putus | FE+BE |
| TC-AC-ACTS-226 | TC-AC-ACTS-E2E-072-add-stock-ble-reload-back-fisik-pindah-tab-scanner-tidak-terhubung-dan-putus | FE+BE |
| TC-AC-ACTS-227 | TC-AC-ACTS-E2E-072-add-stock-ble-reload-back-fisik-pindah-tab-scanner-tidak-terhubung-dan-putus | FE+BE |
| TC-AC-ACTS-228 | TC-AC-ACTS-E2E-072-add-stock-ble-reload-back-fisik-pindah-tab-scanner-tidak-terhubung-dan-putus | FE+BE |
| TC-AC-ACTS-229 | TC-AC-ACTS-E2E-073-add-stock-ble-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-230 | TC-AC-ACTS-E2E-073-add-stock-ble-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-231 | TC-AC-ACTS-E2E-074-add-stock-ble-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-232 | TC-AC-ACTS-E2E-074-add-stock-ble-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-233 | TC-AC-ACTS-E2E-074-add-stock-ble-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-234 | TC-AC-ACTS-E2E-074-add-stock-ble-submit-waiting-dan-partial-register | FE+BE |
| TC-AC-ACTS-235 | TC-AC-ACTS-E2E-075-resilience-add-stock-submit-gagal-dan-timeout-rfid-nfc-ble-gps | FE+BE |
| TC-AC-ACTS-236 | TC-AC-ACTS-E2E-073-add-stock-ble-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-237 | TC-AC-ACTS-E2E-076-konkurensi-add-stock-toggle-local-registration-dimatikan-saat-sesi | FE+BE |
| TC-AC-ACTS-238 | TC-AC-ACTS-E2E-073-add-stock-ble-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-239 | TC-AC-ACTS-E2E-073-add-stock-ble-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state | FE+BE |
| TC-AC-ACTS-240 | TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr | FE+BE |
| TC-AC-ACTS-241 | TC-AC-ACTS-E2E-084-add-stock-gps-screening-upload-csv-xlsx-manual-entry-dan-preview-bersama | FE+BE |
| TC-AC-ACTS-242 | TC-AC-ACTS-E2E-084-add-stock-gps-screening-upload-csv-xlsx-manual-entry-dan-preview-bersama | FE+BE |
| TC-AC-ACTS-243 | TC-AC-ACTS-E2E-084-add-stock-gps-screening-upload-csv-xlsx-manual-entry-dan-preview-bersama | FE+BE |
| TC-AC-ACTS-244 | TC-AC-ACTS-E2E-084-add-stock-gps-screening-upload-csv-xlsx-manual-entry-dan-preview-bersama | FE+BE |
| TC-AC-ACTS-245 | TC-AC-ACTS-E2E-084-add-stock-gps-screening-upload-csv-xlsx-manual-entry-dan-preview-bersama | FE+BE |
| TC-AC-ACTS-246 | TC-AC-ACTS-E2E-085-add-stock-gps-validasi-imei-duplicate-dan-hapus-baris-preview | FE+BE |
| TC-AC-ACTS-247 | TC-AC-ACTS-E2E-085-add-stock-gps-validasi-imei-duplicate-dan-hapus-baris-preview | FE+BE |
| TC-AC-ACTS-248 | TC-AC-ACTS-E2E-085-add-stock-gps-validasi-imei-duplicate-dan-hapus-baris-preview | FE+BE |
| TC-AC-ACTS-249 | TC-AC-ACTS-E2E-085-add-stock-gps-validasi-imei-duplicate-dan-hapus-baris-preview | FE+BE |
| TC-AC-ACTS-250 | TC-AC-ACTS-E2E-086-add-stock-gps-match-existing-ringkasan-manual-entry-dan-invalid-berulang | FE+BE |
| TC-AC-ACTS-251 | TC-AC-ACTS-E2E-087-add-stock-gps-berkas-header-salah-tipe-template-dan-batas-1-mb | FE+BE |
| TC-AC-ACTS-252 | TC-AC-ACTS-E2E-087-add-stock-gps-berkas-header-salah-tipe-template-dan-batas-1-mb | FE+BE |
| TC-AC-ACTS-253 | TC-AC-ACTS-E2E-087-add-stock-gps-berkas-header-salah-tipe-template-dan-batas-1-mb | FE+BE |
| TC-AC-ACTS-254 | TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview | FE+BE |
| TC-AC-ACTS-255 | TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview | FE+BE |
| TC-AC-ACTS-256 | TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview | FE+BE |
| TC-AC-ACTS-257 | TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview | FE+BE |
| TC-AC-ACTS-258 | TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview | FE+BE |
| TC-AC-ACTS-259 | TC-AC-ACTS-E2E-089-add-stock-gps-submit-ok-waiting-partial-register-dan-bentuk-tunggal | FE+BE |
| TC-AC-ACTS-260 | TC-AC-ACTS-E2E-089-add-stock-gps-submit-ok-waiting-partial-register-dan-bentuk-tunggal | FE+BE |
| TC-AC-ACTS-261 | TC-AC-ACTS-E2E-089-add-stock-gps-submit-ok-waiting-partial-register-dan-bentuk-tunggal | FE+BE |
| TC-AC-ACTS-262 | TC-AC-ACTS-E2E-089-add-stock-gps-submit-ok-waiting-partial-register-dan-bentuk-tunggal | FE+BE |
| TC-AC-ACTS-263 | TC-AC-ACTS-E2E-120-add-stock-gps-partial-register-bentuk-tunggal-continue-dan-semua-waiting | FE+BE |
| TC-AC-ACTS-264 | TC-AC-ACTS-E2E-120-add-stock-gps-partial-register-bentuk-tunggal-continue-dan-semua-waiting | FE+BE |
| TC-AC-ACTS-265 | TC-AC-ACTS-E2E-075-resilience-add-stock-submit-gagal-dan-timeout-rfid-nfc-ble-gps | FE+BE |
| TC-AC-ACTS-266 | TC-AC-ACTS-E2E-090-add-stock-gps-klik-ganda-bypass-e2a-dan-identifier-rejected | FE+BE |
| TC-AC-ACTS-267 | TC-AC-ACTS-E2E-076-konkurensi-add-stock-toggle-local-registration-dimatikan-saat-sesi | FE+BE |
| TC-AC-ACTS-268 | TC-AC-ACTS-E2E-086-add-stock-gps-match-existing-ringkasan-manual-entry-dan-invalid-berulang | FE+BE |
| TC-AC-ACTS-269 | TC-AC-ACTS-E2E-091-add-stock-gps-volume-5000-baris-sinkron-dan-background | FE+BE |
| TC-AC-ACTS-270 | TC-AC-ACTS-E2E-091-add-stock-gps-volume-5000-baris-sinkron-dan-background | FE+BE |
| TC-AC-ACTS-271 | TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr | FE+BE |
| TC-AC-ACTS-272 | TC-AC-ACTS-E2E-086-add-stock-gps-match-existing-ringkasan-manual-entry-dan-invalid-berulang | FE+BE |
| TC-AC-ACTS-273 | TC-AC-ACTS-E2E-095-approvals-duplicate-dialog-review-register-duplicate-activation-collision-dan-byo | FE+BE |
| TC-AC-ACTS-274 | TC-AC-ACTS-E2E-095-approvals-duplicate-dialog-review-register-duplicate-activation-collision-dan-byo | FE+BE |
| TC-AC-ACTS-275 | TC-AC-ACTS-E2E-095-approvals-duplicate-dialog-review-register-duplicate-activation-collision-dan-byo | FE+BE |
| TC-AC-ACTS-276 | TC-AC-ACTS-E2E-097-approvals-duplicate-radio-validasi-reject-batas-note-cancel-dan-klik-ganda | FE+BE |
| TC-AC-ACTS-277 | TC-AC-ACTS-E2E-098-approvals-duplicate-approve-register-duplicate-activation-collision-dan-unit-tidak-tampil | FE+BE |
| TC-AC-ACTS-278 | TC-AC-ACTS-E2E-098-approvals-duplicate-approve-register-duplicate-activation-collision-dan-unit-tidak-tampil | FE+BE |
| TC-AC-ACTS-279 | TC-AC-ACTS-E2E-097-approvals-duplicate-radio-validasi-reject-batas-note-cancel-dan-klik-ganda | FE+BE |
| TC-AC-ACTS-280 | TC-AC-ACTS-E2E-097-approvals-duplicate-radio-validasi-reject-batas-note-cancel-dan-klik-ganda | FE+BE |
| TC-AC-ACTS-281 | TC-AC-ACTS-E2E-099-approvals-duplicate-reject-register-duplicate-dan-activation-collision | FE+BE |
| TC-AC-ACTS-282 | TC-AC-ACTS-E2E-099-approvals-duplicate-reject-register-duplicate-dan-activation-collision | FE+BE |
| TC-AC-ACTS-283 | TC-AC-ACTS-E2E-097-approvals-duplicate-radio-validasi-reject-batas-note-cancel-dan-klik-ganda | FE+BE |
| TC-AC-ACTS-284 | TC-AC-ACTS-E2E-097-approvals-duplicate-radio-validasi-reject-batas-note-cancel-dan-klik-ganda | FE+BE |
| TC-AC-ACTS-285 | TC-AC-ACTS-E2E-101-approvals-duplicate-requester-distributor-dua-subject-dan-bypass-e2a-default-user | FE+BE |
| TC-AC-ACTS-286 | TC-AC-ACTS-E2E-101-approvals-duplicate-requester-distributor-dua-subject-dan-bypass-e2a-default-user | FE+BE |
| TC-AC-ACTS-287 | TC-AC-ACTS-E2E-102-approvals-duplicate-e4-additional-approver-subject-sendiri-disembunyikan | FE+BE |
| TC-AC-ACTS-288 | TC-AC-ACTS-E2E-102-approvals-duplicate-e4-additional-approver-subject-sendiri-disembunyikan | FE+BE |
| TC-AC-ACTS-289 | TC-AC-ACTS-E2E-102-approvals-duplicate-e4-additional-approver-subject-sendiri-disembunyikan | FE+BE |
| TC-AC-ACTS-290 | TC-AC-ACTS-E2E-103-approvals-duplicate-konkurensi-dua-approver-dan-dialog-nested | FE+BE |
| TC-AC-ACTS-291 | TC-AC-ACTS-E2E-103-approvals-duplicate-konkurensi-dua-approver-dan-dialog-nested | FE+BE |
| TC-AC-ACTS-292 | TC-AC-ACTS-E2E-104-approvals-duplicate-activation-collision-dibatalkan-event-delete-tag-dan-no-op | FE+BE |
| TC-AC-ACTS-293 | TC-AC-ACTS-E2E-105-resilience-approvals-error-detail-gagal-muat-timeout-dan-download-gagal | FE+BE |
| TC-AC-ACTS-294 | TC-AC-ACTS-E2E-097-approvals-duplicate-radio-validasi-reject-batas-note-cancel-dan-klik-ganda | FE+BE |
| TC-AC-ACTS-295 | TC-AC-ACTS-E2E-105-resilience-approvals-error-detail-gagal-muat-timeout-dan-download-gagal | FE+BE |
| TC-AC-ACTS-296 | TC-AC-ACTS-E2E-036-role-matrix-read-only-dan-capability-parsial-aksi-tulis-hidden | FE+BE |
| TC-AC-ACTS-297 | TC-AC-ACTS-E2E-101-approvals-duplicate-requester-distributor-dua-subject-dan-bypass-e2a-default-user | FE+BE |
| TC-AC-ACTS-298 | TC-AC-ACTS-E2E-098-approvals-duplicate-approve-register-duplicate-activation-collision-dan-unit-tidak-tampil | FE+BE |
| TC-AC-ACTS-299 | TC-AC-ACTS-E2E-101-approvals-duplicate-requester-distributor-dua-subject-dan-bypass-e2a-default-user | FE+BE |
| TC-AC-ACTS-300 | TC-AC-ACTS-E2E-096-approvals-duplicate-existing-record-label-matched-identifier-dan-approval-note | FE+BE |
| TC-AC-ACTS-301 | TC-AC-ACTS-E2E-096-approvals-duplicate-existing-record-label-matched-identifier-dan-approval-note | FE+BE |
| TC-AC-ACTS-302 | TC-AC-ACTS-E2E-096-approvals-duplicate-existing-record-label-matched-identifier-dan-approval-note | FE+BE |
| TC-AC-ACTS-303 | TC-AC-ACTS-E2E-100-approvals-duplicate-scan-ulang-identifier-rejected-dan-constraint-unique-status-live | FE+BE |
| TC-AC-ACTS-304 | TC-AC-ACTS-E2E-104-approvals-duplicate-activation-collision-dibatalkan-event-delete-tag-dan-no-op | FE+BE |
| TC-AC-ACTS-305 | TC-AC-ACTS-E2E-104-approvals-duplicate-activation-collision-dibatalkan-event-delete-tag-dan-no-op | FE+BE |
| TC-AC-ACTS-306 | TC-AC-ACTS-E2E-104-approvals-duplicate-activation-collision-dibatalkan-event-delete-tag-dan-no-op | FE+BE |
| TC-AC-ACTS-307 | TC-AC-ACTS-E2E-104-approvals-duplicate-activation-collision-dibatalkan-event-delete-tag-dan-no-op | FE+BE |
| TC-AC-ACTS-308 | TC-AC-ACTS-E2E-104-approvals-duplicate-activation-collision-dibatalkan-event-delete-tag-dan-no-op | FE+BE |
| TC-AC-ACTS-309 | TC-AC-ACTS-E2E-122-audit-rfid-screening-popup-start-scan-dan-verified-di-tempat | FE+BE |
| TC-AC-ACTS-310 | TC-AC-ACTS-E2E-122-audit-rfid-screening-popup-start-scan-dan-verified-di-tempat | FE+BE |
| TC-AC-ACTS-311 | TC-AC-ACTS-E2E-122-audit-rfid-screening-popup-start-scan-dan-verified-di-tempat | FE+BE |
| TC-AC-ACTS-312 | TC-AC-ACTS-E2E-122-audit-rfid-screening-popup-start-scan-dan-verified-di-tempat | FE+BE |
| TC-AC-ACTS-313 | TC-AC-ACTS-E2E-123-audit-rfid-scan-ulang-prioritas-uid-identifier-stop-dan-sesi-berikutnya | FE+BE |
| TC-AC-ACTS-314 | TC-AC-ACTS-E2E-123-audit-rfid-scan-ulang-prioritas-uid-identifier-stop-dan-sesi-berikutnya | FE+BE |
| TC-AC-ACTS-315 | TC-AC-ACTS-E2E-123-audit-rfid-scan-ulang-prioritas-uid-identifier-stop-dan-sesi-berikutnya | FE+BE |
| TC-AC-ACTS-316 | TC-AC-ACTS-E2E-123-audit-rfid-scan-ulang-prioritas-uid-identifier-stop-dan-sesi-berikutnya | FE+BE |
| TC-AC-ACTS-317 | TC-AC-ACTS-E2E-123-audit-rfid-scan-ulang-prioritas-uid-identifier-stop-dan-sesi-berikutnya | FE+BE |
| TC-AC-ACTS-318 | TC-AC-ACTS-E2E-124-audit-rfid-submit-dialog-konfirmasi-dan-confirm-dengan-checkbox | FE+BE |
| TC-AC-ACTS-319 | TC-AC-ACTS-E2E-124-audit-rfid-submit-dialog-konfirmasi-dan-confirm-dengan-checkbox | FE+BE |
| TC-AC-ACTS-320 | TC-AC-ACTS-E2E-126-audit-rfid-toast-netral-t20-bentuk-tunggal-counter-dan-badge-severity | FE+BE |
| TC-AC-ACTS-321 | TC-AC-ACTS-E2E-124-audit-rfid-submit-dialog-konfirmasi-dan-confirm-dengan-checkbox | FE+BE |
| TC-AC-ACTS-322 | TC-AC-ACTS-E2E-124-audit-rfid-submit-dialog-konfirmasi-dan-confirm-dengan-checkbox | FE+BE |
| TC-AC-ACTS-323 | TC-AC-ACTS-E2E-125-audit-rfid-confirm-tanpa-centang-cancel-dialog-recovery-d03-dan-toast-gabungan | FE+BE |
| TC-AC-ACTS-324 | TC-AC-ACTS-E2E-125-audit-rfid-confirm-tanpa-centang-cancel-dialog-recovery-d03-dan-toast-gabungan | FE+BE |
| TC-AC-ACTS-325 | TC-AC-ACTS-E2E-125-audit-rfid-confirm-tanpa-centang-cancel-dialog-recovery-d03-dan-toast-gabungan | FE+BE |
| TC-AC-ACTS-326 | TC-AC-ACTS-E2E-125-audit-rfid-confirm-tanpa-centang-cancel-dialog-recovery-d03-dan-toast-gabungan | FE+BE |
| TC-AC-ACTS-327 | TC-AC-ACTS-E2E-131-audit-rfid-konkurensi-status-unit-berubah-oleh-sesi-lain-di-tengah-sesi | FE+BE |
| TC-AC-ACTS-328 | TC-AC-ACTS-E2E-127-audit-rfid-unit-combined-in-use-waiting-empty-state-dan-tag-code-tidak-berubah | FE+BE |
| TC-AC-ACTS-329 | TC-AC-ACTS-E2E-127-audit-rfid-unit-combined-in-use-waiting-empty-state-dan-tag-code-tidak-berubah | FE+BE |
| TC-AC-ACTS-330 | TC-AC-ACTS-E2E-127-audit-rfid-unit-combined-in-use-waiting-empty-state-dan-tag-code-tidak-berubah | FE+BE |
| TC-AC-ACTS-331 | TC-AC-ACTS-E2E-127-audit-rfid-unit-combined-in-use-waiting-empty-state-dan-tag-code-tidak-berubah | FE+BE |
| TC-AC-ACTS-332 | TC-AC-ACTS-E2E-128-audit-rfid-tutup-popup-d06-leave-cancel-dan-tanpa-verified | FE+BE |
| TC-AC-ACTS-333 | TC-AC-ACTS-E2E-128-audit-rfid-tutup-popup-d06-leave-cancel-dan-tanpa-verified | FE+BE |
| TC-AC-ACTS-334 | TC-AC-ACTS-E2E-128-audit-rfid-tutup-popup-d06-leave-cancel-dan-tanpa-verified | FE+BE |
| TC-AC-ACTS-335 | TC-AC-ACTS-E2E-163-audit-rfid-sesi-scan-aktif-back-fisik-reader-putus-pindah-tab-dan-reload | FE+BE |
| TC-AC-ACTS-336 | TC-AC-ACTS-E2E-163-audit-rfid-sesi-scan-aktif-back-fisik-reader-putus-pindah-tab-dan-reload | FE+BE |
| TC-AC-ACTS-339 | TC-AC-ACTS-E2E-148-resilience-delete-dan-audit-gagal-5xx-dan-timeout | FE+BE |
| TC-AC-ACTS-340 | TC-AC-ACTS-E2E-129-audit-rfid-klik-ganda-tanpa-stock-ledger-event-log-dan-start-scan-tanpa-reader | FE+BE |
| TC-AC-ACTS-341 | TC-AC-ACTS-E2E-129-audit-rfid-klik-ganda-tanpa-stock-ledger-event-log-dan-start-scan-tanpa-reader | FE+BE |
| TC-AC-ACTS-342 | TC-AC-ACTS-E2E-129-audit-rfid-klik-ganda-tanpa-stock-ledger-event-log-dan-start-scan-tanpa-reader | FE+BE |
| TC-AC-ACTS-343 | TC-AC-ACTS-E2E-132-audit-nfc-screening-start-scan-verified-stop-dan-submit-dialog | FE+BE |
| TC-AC-ACTS-344 | TC-AC-ACTS-E2E-132-audit-nfc-screening-start-scan-verified-stop-dan-submit-dialog | FE+BE |
| TC-AC-ACTS-345 | TC-AC-ACTS-E2E-132-audit-nfc-screening-start-scan-verified-stop-dan-submit-dialog | FE+BE |
| TC-AC-ACTS-346 | TC-AC-ACTS-E2E-132-audit-nfc-screening-start-scan-verified-stop-dan-submit-dialog | FE+BE |
| TC-AC-ACTS-347 | TC-AC-ACTS-E2E-132-audit-nfc-screening-start-scan-verified-stop-dan-submit-dialog | FE+BE |
| TC-AC-ACTS-348 | TC-AC-ACTS-E2E-133-audit-nfc-confirm-cancel-recovery-combined-dan-in-use | FE+BE |
| TC-AC-ACTS-349 | TC-AC-ACTS-E2E-133-audit-nfc-confirm-cancel-recovery-combined-dan-in-use | FE+BE |
| TC-AC-ACTS-350 | TC-AC-ACTS-E2E-133-audit-nfc-confirm-cancel-recovery-combined-dan-in-use | FE+BE |
| TC-AC-ACTS-351 | TC-AC-ACTS-E2E-133-audit-nfc-confirm-cancel-recovery-combined-dan-in-use | FE+BE |
| TC-AC-ACTS-352 | TC-AC-ACTS-E2E-133-audit-nfc-confirm-cancel-recovery-combined-dan-in-use | FE+BE |
| TC-AC-ACTS-353 | TC-AC-ACTS-E2E-133-audit-nfc-confirm-cancel-recovery-combined-dan-in-use | FE+BE |
| TC-AC-ACTS-355 | TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr | FE+BE |
| TC-AC-ACTS-356 | TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr | FE+BE |
| TC-AC-ACTS-357 | TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr | FE+BE |
| TC-AC-ACTS-358 | TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr | FE+BE |
| TC-AC-ACTS-359 | TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr | FE+BE |
| TC-AC-ACTS-360 | TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger | FE+BE |
| TC-AC-ACTS-361 | TC-AC-ACTS-E2E-137-delete-unit-konfirmasi-damaged-missing-klik-ganda-distributor-dan-unit-terakhir-sku | FE+BE |
| TC-AC-ACTS-362 | TC-AC-ACTS-E2E-137-delete-unit-konfirmasi-damaged-missing-klik-ganda-distributor-dan-unit-terakhir-sku | FE+BE |
| TC-AC-ACTS-363 | TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger | FE+BE |
| TC-AC-ACTS-364 | TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger | FE+BE |
| TC-AC-ACTS-365 | TC-AC-ACTS-E2E-147-konkurensi-delete-by-scan-dan-bulk-delete-bersamaan-sesi-lain | FE+BE |
| TC-AC-ACTS-366 | TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger | FE+BE |
| TC-AC-ACTS-367 | TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger | FE+BE |
| TC-AC-ACTS-368 | TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger | FE+BE |
| TC-AC-ACTS-369 | TC-AC-ACTS-E2E-136-delete-unit-guard-dialog-blok-combined-existing-record-urutan-evaluasi-dan-saldo-ledger | FE+BE |
| TC-AC-ACTS-370 | TC-AC-ACTS-E2E-148-resilience-delete-dan-audit-gagal-5xx-dan-timeout | FE+BE |
| TC-AC-ACTS-371 | TC-AC-ACTS-E2E-137-delete-unit-konfirmasi-damaged-missing-klik-ganda-distributor-dan-unit-terakhir-sku | FE+BE |
| TC-AC-ACTS-372 | TC-AC-ACTS-E2E-137-delete-unit-konfirmasi-damaged-missing-klik-ganda-distributor-dan-unit-terakhir-sku | FE+BE |
| TC-AC-ACTS-373 | TC-AC-ACTS-E2E-137-delete-unit-konfirmasi-damaged-missing-klik-ganda-distributor-dan-unit-terakhir-sku | FE+BE |
| TC-AC-ACTS-374 | TC-AC-ACTS-E2E-157-detail-sku-screening-header-summary-bar-tab-dan-tag-type-icon | FE+BE |
| TC-AC-ACTS-375 | TC-AC-ACTS-E2E-157-detail-sku-screening-header-summary-bar-tab-dan-tag-type-icon | FE+BE |
| TC-AC-ACTS-376 | TC-AC-ACTS-E2E-165-detail-sku-tab-available-badge-status-filter-status-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-377 | TC-AC-ACTS-E2E-165-detail-sku-tab-available-badge-status-filter-status-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-378 | TC-AC-ACTS-E2E-166-detail-sku-tab-available-unit-waiting-rejected-byo-registered-by-dan-row-action-tag-log | FE+BE |
| TC-AC-ACTS-379 | TC-AC-ACTS-E2E-165-detail-sku-tab-available-badge-status-filter-status-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-380 | TC-AC-ACTS-E2E-165-detail-sku-tab-available-badge-status-filter-status-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-381 | TC-AC-ACTS-E2E-165-detail-sku-tab-available-badge-status-filter-status-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-382 | TC-AC-ACTS-E2E-166-detail-sku-tab-available-unit-waiting-rejected-byo-registered-by-dan-row-action-tag-log | FE+BE |
| TC-AC-ACTS-383 | TC-AC-ACTS-E2E-166-detail-sku-tab-available-unit-waiting-rejected-byo-registered-by-dan-row-action-tag-log | FE+BE |
| TC-AC-ACTS-384 | TC-AC-ACTS-E2E-166-detail-sku-tab-available-unit-waiting-rejected-byo-registered-by-dan-row-action-tag-log | FE+BE |
| TC-AC-ACTS-385 | TC-AC-ACTS-E2E-166-detail-sku-tab-available-unit-waiting-rejected-byo-registered-by-dan-row-action-tag-log | FE+BE |
| TC-AC-ACTS-386 | TC-AC-ACTS-E2E-160-detail-sku-realtime-tab-available-opsi-filter-banner-dan-approval | FE+BE |
| TC-AC-ACTS-387 | TC-AC-ACTS-E2E-036-role-matrix-read-only-dan-capability-parsial-aksi-tulis-hidden | FE+BE |
| TC-AC-ACTS-388 | TC-AC-ACTS-E2E-167-detail-sku-tab-available-screening-urutan | FE+BE |
| TC-AC-ACTS-389 | TC-AC-ACTS-E2E-167-detail-sku-tab-available-screening-urutan | FE+BE |
| TC-AC-ACTS-390 | TC-AC-ACTS-E2E-168-detail-sku-tab-available-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-391 | TC-AC-ACTS-E2E-168-detail-sku-tab-available-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-392 | TC-AC-ACTS-E2E-168-detail-sku-tab-available-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-393 | TC-AC-ACTS-E2E-169-detail-sku-tab-available-sort-bagian-2-hover-user-siklus-search | FE+BE |
| TC-AC-ACTS-394 | TC-AC-ACTS-E2E-169-detail-sku-tab-available-sort-bagian-2-hover-user-siklus-search | FE+BE |
| TC-AC-ACTS-395 | TC-AC-ACTS-E2E-170-detail-sku-tab-available-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-396 | TC-AC-ACTS-E2E-170-detail-sku-tab-available-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-397 | TC-AC-ACTS-E2E-170-detail-sku-tab-available-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-398 | TC-AC-ACTS-E2E-171-detail-sku-tab-available-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-399 | TC-AC-ACTS-E2E-171-detail-sku-tab-available-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-400 | TC-AC-ACTS-E2E-171-detail-sku-tab-available-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-401 | TC-AC-ACTS-E2E-172-detail-sku-tab-available-alur-search-filter | FE+BE |
| TC-AC-ACTS-402 | TC-AC-ACTS-E2E-172-detail-sku-tab-available-alur-search-filter | FE+BE |
| TC-AC-ACTS-403 | TC-AC-ACTS-E2E-173-detail-sku-tab-available-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-404 | TC-AC-ACTS-E2E-173-detail-sku-tab-available-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-405 | TC-AC-ACTS-E2E-173-detail-sku-tab-available-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-406 | TC-AC-ACTS-E2E-174-detail-sku-tab-available-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-407 | TC-AC-ACTS-E2E-174-detail-sku-tab-available-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-408 | TC-AC-ACTS-E2E-174-detail-sku-tab-available-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-409 | TC-AC-ACTS-E2E-174-detail-sku-tab-available-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-410 | TC-AC-ACTS-E2E-175-detail-sku-tab-available-sc-ceklis | FE+BE |
| TC-AC-ACTS-411 | TC-AC-ACTS-E2E-176-detail-sku-tab-available-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-412 | TC-AC-ACTS-E2E-176-detail-sku-tab-available-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-413 | TC-AC-ACTS-E2E-177-detail-sku-tab-available-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-414 | TC-AC-ACTS-E2E-177-detail-sku-tab-available-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-415 | TC-AC-ACTS-E2E-177-detail-sku-tab-available-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-416 | TC-AC-ACTS-E2E-178-detail-sku-tab-available-sc-reset-tutup-bagian-2-pagination | FE+BE |
| TC-AC-ACTS-417 | TC-AC-ACTS-E2E-262-volume-pagination-stock-list-dan-detail-sku-tab-available-dan-in-use-101-baris | FE+BE |
| TC-AC-ACTS-418 | TC-AC-ACTS-E2E-179-detail-sku-tab-available-state | FE+BE |
| TC-AC-ACTS-419 | TC-AC-ACTS-E2E-179-detail-sku-tab-available-state | FE+BE |
| TC-AC-ACTS-420 | TC-AC-ACTS-E2E-179-detail-sku-tab-available-state | FE+BE |
| TC-AC-ACTS-421 | TC-AC-ACTS-E2E-179-detail-sku-tab-available-state | FE+BE |
| TC-AC-ACTS-422 | TC-AC-ACTS-E2E-180-detail-sku-tab-available-download | FE+BE |
| TC-AC-ACTS-423 | TC-AC-ACTS-E2E-180-detail-sku-tab-available-download | FE+BE |
| TC-AC-ACTS-424 | TC-AC-ACTS-E2E-265-isi-sel-detail-sku-tab-available-tab-in-use-dan-approvals-tab-history-berkas-xlsx | FE+BE |
| TC-AC-ACTS-425 | TC-AC-ACTS-E2E-169-detail-sku-tab-available-sort-bagian-2-hover-user-siklus-search | FE+BE |
| TC-AC-ACTS-426 | TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku | FE+BE |
| TC-AC-ACTS-427 | TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku | FE+BE |
| TC-AC-ACTS-428 | TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku | FE+BE |
| TC-AC-ACTS-429 | TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku | FE+BE |
| TC-AC-ACTS-430 | TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku | FE+BE |
| TC-AC-ACTS-431 | TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku | FE+BE |
| TC-AC-ACTS-432 | TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku | FE+BE |
| TC-AC-ACTS-433 | TC-AC-ACTS-E2E-182-tab-in-use-screening-urutan | FE+BE |
| TC-AC-ACTS-434 | TC-AC-ACTS-E2E-182-tab-in-use-screening-urutan | FE+BE |
| TC-AC-ACTS-435 | TC-AC-ACTS-E2E-183-tab-in-use-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-436 | TC-AC-ACTS-E2E-183-tab-in-use-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-437 | TC-AC-ACTS-E2E-184-tab-in-use-sort-bagian-2 | FE+BE |
| TC-AC-ACTS-438 | TC-AC-ACTS-E2E-184-tab-in-use-sort-bagian-2 | FE+BE |
| TC-AC-ACTS-439 | TC-AC-ACTS-E2E-213-tab-in-use-siklus-search | FE+BE |
| TC-AC-ACTS-440 | TC-AC-ACTS-E2E-185-tab-in-use-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-441 | TC-AC-ACTS-E2E-185-tab-in-use-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-442 | TC-AC-ACTS-E2E-185-tab-in-use-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-443 | TC-AC-ACTS-E2E-186-tab-in-use-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-444 | TC-AC-ACTS-E2E-186-tab-in-use-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-445 | TC-AC-ACTS-E2E-186-tab-in-use-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-446 | TC-AC-ACTS-E2E-186-tab-in-use-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-447 | TC-AC-ACTS-E2E-187-tab-in-use-alur-search-filter | FE+BE |
| TC-AC-ACTS-448 | TC-AC-ACTS-E2E-187-tab-in-use-alur-search-filter | FE+BE |
| TC-AC-ACTS-449 | TC-AC-ACTS-E2E-188-tab-in-use-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-450 | TC-AC-ACTS-E2E-188-tab-in-use-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-451 | TC-AC-ACTS-E2E-188-tab-in-use-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-452 | TC-AC-ACTS-E2E-189-tab-in-use-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-453 | TC-AC-ACTS-E2E-189-tab-in-use-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-454 | TC-AC-ACTS-E2E-189-tab-in-use-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-455 | TC-AC-ACTS-E2E-189-tab-in-use-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-456 | TC-AC-ACTS-E2E-190-tab-in-use-sc-ceklis | FE+BE |
| TC-AC-ACTS-457 | TC-AC-ACTS-E2E-191-tab-in-use-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-458 | TC-AC-ACTS-E2E-191-tab-in-use-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-459 | TC-AC-ACTS-E2E-192-tab-in-use-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-460 | TC-AC-ACTS-E2E-192-tab-in-use-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-461 | TC-AC-ACTS-E2E-192-tab-in-use-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-462 | TC-AC-ACTS-E2E-193-tab-in-use-sc-reset-tutup-bagian-2-pagination | FE+BE |
| TC-AC-ACTS-463 | TC-AC-ACTS-E2E-262-volume-pagination-stock-list-dan-detail-sku-tab-available-dan-in-use-101-baris | FE+BE |
| TC-AC-ACTS-464 | TC-AC-ACTS-E2E-194-tab-in-use-state | FE+BE |
| TC-AC-ACTS-465 | TC-AC-ACTS-E2E-194-tab-in-use-state | FE+BE |
| TC-AC-ACTS-466 | TC-AC-ACTS-E2E-194-tab-in-use-state | FE+BE |
| TC-AC-ACTS-467 | TC-AC-ACTS-E2E-194-tab-in-use-state | FE+BE |
| TC-AC-ACTS-468 | TC-AC-ACTS-E2E-195-tab-in-use-download-hover-user | FE+BE |
| TC-AC-ACTS-469 | TC-AC-ACTS-E2E-195-tab-in-use-download-hover-user | FE+BE |
| TC-AC-ACTS-470 | TC-AC-ACTS-E2E-265-isi-sel-detail-sku-tab-available-tab-in-use-dan-approvals-tab-history-berkas-xlsx | FE+BE |
| TC-AC-ACTS-471 | TC-AC-ACTS-E2E-195-tab-in-use-download-hover-user | FE+BE |
| TC-AC-ACTS-472 | TC-AC-ACTS-E2E-214-modal-event-log-buka-default-tab-add-stock-tutup-sesi-sku-ini-dan-popup-audit-tanpa-ikon | FE+BE |
| TC-AC-ACTS-473 | TC-AC-ACTS-E2E-218-modal-event-log-penulisan-sesi-add-stock-delete-satuan-bulk-delete-parsial-dan-tanpa-keputusan-duplicate-approval | FE+BE |
| TC-AC-ACTS-474 | TC-AC-ACTS-E2E-218-modal-event-log-penulisan-sesi-add-stock-delete-satuan-bulk-delete-parsial-dan-tanpa-keputusan-duplicate-approval | FE+BE |
| TC-AC-ACTS-475 | TC-AC-ACTS-E2E-218-modal-event-log-penulisan-sesi-add-stock-delete-satuan-bulk-delete-parsial-dan-tanpa-keputusan-duplicate-approval | FE+BE |
| TC-AC-ACTS-476 | TC-AC-ACTS-E2E-261-modal-event-log-penulisan-sesi-delete-by-scan-unit-dilewati-audit-dan-kolom-hardware | FE+BE |
| TC-AC-ACTS-477 | TC-AC-ACTS-E2E-218-modal-event-log-penulisan-sesi-add-stock-delete-satuan-bulk-delete-parsial-dan-tanpa-keputusan-duplicate-approval | FE+BE |
| TC-AC-ACTS-478 | TC-AC-ACTS-E2E-214-modal-event-log-buka-default-tab-add-stock-tutup-sesi-sku-ini-dan-popup-audit-tanpa-ikon | FE+BE |
| TC-AC-ACTS-479 | TC-AC-ACTS-E2E-214-modal-event-log-buka-default-tab-add-stock-tutup-sesi-sku-ini-dan-popup-audit-tanpa-ikon | FE+BE |
| TC-AC-ACTS-480 | TC-AC-ACTS-E2E-224-modal-event-log-tab-add-stock-screening-urutan | FE+BE |
| TC-AC-ACTS-481 | TC-AC-ACTS-E2E-224-modal-event-log-tab-add-stock-screening-urutan | FE+BE |
| TC-AC-ACTS-482 | TC-AC-ACTS-E2E-225-modal-event-log-tab-add-stock-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-483 | TC-AC-ACTS-E2E-225-modal-event-log-tab-add-stock-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-484 | TC-AC-ACTS-E2E-225-modal-event-log-tab-add-stock-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-485 | TC-AC-ACTS-E2E-226-modal-event-log-tab-add-stock-sort-bagian-2-siklus-search | FE+BE |
| TC-AC-ACTS-486 | TC-AC-ACTS-E2E-226-modal-event-log-tab-add-stock-sort-bagian-2-siklus-search | FE+BE |
| TC-AC-ACTS-487 | TC-AC-ACTS-E2E-227-modal-event-log-tab-add-stock-search-kolom | FE+BE |
| TC-AC-ACTS-488 | TC-AC-ACTS-E2E-227-modal-event-log-tab-add-stock-search-kolom | FE+BE |
| TC-AC-ACTS-489 | TC-AC-ACTS-E2E-227-modal-event-log-tab-add-stock-search-kolom | FE+BE |
| TC-AC-ACTS-490 | TC-AC-ACTS-E2E-227-modal-event-log-tab-add-stock-search-kolom | FE+BE |
| TC-AC-ACTS-491 | TC-AC-ACTS-E2E-228-modal-event-log-tab-add-stock-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-492 | TC-AC-ACTS-E2E-228-modal-event-log-tab-add-stock-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-493 | TC-AC-ACTS-E2E-228-modal-event-log-tab-add-stock-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-494 | TC-AC-ACTS-E2E-228-modal-event-log-tab-add-stock-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-495 | TC-AC-ACTS-E2E-229-modal-event-log-tab-add-stock-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-496 | TC-AC-ACTS-E2E-229-modal-event-log-tab-add-stock-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-497 | TC-AC-ACTS-E2E-229-modal-event-log-tab-add-stock-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-498 | TC-AC-ACTS-E2E-230-modal-event-log-tab-add-stock-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-499 | TC-AC-ACTS-E2E-230-modal-event-log-tab-add-stock-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-500 | TC-AC-ACTS-E2E-230-modal-event-log-tab-add-stock-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-501 | TC-AC-ACTS-E2E-230-modal-event-log-tab-add-stock-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-502 | TC-AC-ACTS-E2E-231-modal-event-log-tab-add-stock-sc-ceklis | FE+BE |
| TC-AC-ACTS-503 | TC-AC-ACTS-E2E-232-modal-event-log-tab-add-stock-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-504 | TC-AC-ACTS-E2E-232-modal-event-log-tab-add-stock-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-505 | TC-AC-ACTS-E2E-233-modal-event-log-tab-add-stock-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-506 | TC-AC-ACTS-E2E-233-modal-event-log-tab-add-stock-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-507 | TC-AC-ACTS-E2E-233-modal-event-log-tab-add-stock-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-508 | TC-AC-ACTS-E2E-234-modal-event-log-tab-add-stock-sc-reset-tutup-bagian-2-pagination | FE+BE |
| TC-AC-ACTS-509 | TC-AC-ACTS-E2E-263-volume-pagination-modal-event-log-tab-add-stock-dan-approvals-tab-active-dan-history-101-baris | FE+BE |
| TC-AC-ACTS-510 | TC-AC-ACTS-E2E-235-modal-event-log-tab-add-stock-state | FE+BE |
| TC-AC-ACTS-511 | TC-AC-ACTS-E2E-235-modal-event-log-tab-add-stock-state | FE+BE |
| TC-AC-ACTS-512 | TC-AC-ACTS-E2E-235-modal-event-log-tab-add-stock-state | FE+BE |
| TC-AC-ACTS-513 | TC-AC-ACTS-E2E-235-modal-event-log-tab-add-stock-state | FE+BE |
| TC-AC-ACTS-514 | TC-AC-ACTS-E2E-236-modal-event-log-tab-add-stock-download-hover-user | FE+BE |
| TC-AC-ACTS-515 | TC-AC-ACTS-E2E-236-modal-event-log-tab-add-stock-download-hover-user | FE+BE |
| TC-AC-ACTS-516 | TC-AC-ACTS-E2E-260-modal-event-log-dan-approvals-tab-active-isi-sel-berkas-xlsx | FE+BE |
| TC-AC-ACTS-517 | TC-AC-ACTS-E2E-236-modal-event-log-tab-add-stock-download-hover-user | FE+BE |
| TC-AC-ACTS-521 | TC-AC-ACTS-E2E-153-pencatatan-log-add-stock-via-scan-import-gps-waiting-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-522 | TC-AC-ACTS-E2E-155-pencatatan-log-field-delete-stock-sync-condition-kolom-modified-by-dan-tanpa-duplikat | FE+BE |
| TC-AC-ACTS-525 | TC-AC-ACTS-E2E-155-pencatatan-log-field-delete-stock-sync-condition-kolom-modified-by-dan-tanpa-duplikat | FE+BE |
| TC-AC-ACTS-526 | TC-AC-ACTS-E2E-155-pencatatan-log-field-delete-stock-sync-condition-kolom-modified-by-dan-tanpa-duplikat | FE+BE |
| TC-AC-ACTS-566 | TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review | FE+BE |
| TC-AC-ACTS-567 | TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review | FE+BE |
| TC-AC-ACTS-568 | TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review | FE+BE |
| TC-AC-ACTS-569 | TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review | FE+BE |
| TC-AC-ACTS-570 | TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review | FE+BE |
| TC-AC-ACTS-571 | TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review | FE+BE |
| TC-AC-ACTS-572 | TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review | FE+BE |
| TC-AC-ACTS-573 | TC-AC-ACTS-E2E-246-approvals-tab-active-screening-urutan | FE+BE |
| TC-AC-ACTS-574 | TC-AC-ACTS-E2E-246-approvals-tab-active-screening-urutan | FE+BE |
| TC-AC-ACTS-575 | TC-AC-ACTS-E2E-247-approvals-tab-active-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-576 | TC-AC-ACTS-E2E-247-approvals-tab-active-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-577 | TC-AC-ACTS-E2E-248-approvals-tab-active-sort-bagian-2-siklus-search | FE+BE |
| TC-AC-ACTS-578 | TC-AC-ACTS-E2E-248-approvals-tab-active-sort-bagian-2-siklus-search | FE+BE |
| TC-AC-ACTS-579 | TC-AC-ACTS-E2E-249-approvals-tab-active-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-580 | TC-AC-ACTS-E2E-249-approvals-tab-active-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-581 | TC-AC-ACTS-E2E-249-approvals-tab-active-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-582 | TC-AC-ACTS-E2E-249-approvals-tab-active-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-583 | TC-AC-ACTS-E2E-250-approvals-tab-active-search-kolom-bagian-2-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-584 | TC-AC-ACTS-E2E-250-approvals-tab-active-search-kolom-bagian-2-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-585 | TC-AC-ACTS-E2E-250-approvals-tab-active-search-kolom-bagian-2-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-586 | TC-AC-ACTS-E2E-250-approvals-tab-active-search-kolom-bagian-2-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-587 | TC-AC-ACTS-E2E-250-approvals-tab-active-search-kolom-bagian-2-search-visibilitas-alur-search-filter | FE+BE |
| TC-AC-ACTS-588 | TC-AC-ACTS-E2E-251-approvals-tab-active-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-589 | TC-AC-ACTS-E2E-251-approvals-tab-active-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-590 | TC-AC-ACTS-E2E-251-approvals-tab-active-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-591 | TC-AC-ACTS-E2E-252-approvals-tab-active-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-592 | TC-AC-ACTS-E2E-252-approvals-tab-active-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-593 | TC-AC-ACTS-E2E-252-approvals-tab-active-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-594 | TC-AC-ACTS-E2E-252-approvals-tab-active-filter-bagian-2-sc-screening | FE+BE |
| TC-AC-ACTS-595 | TC-AC-ACTS-E2E-253-approvals-tab-active-sc-ceklis | FE+BE |
| TC-AC-ACTS-596 | TC-AC-ACTS-E2E-254-approvals-tab-active-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-597 | TC-AC-ACTS-E2E-254-approvals-tab-active-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-598 | TC-AC-ACTS-E2E-255-approvals-tab-active-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-599 | TC-AC-ACTS-E2E-255-approvals-tab-active-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-600 | TC-AC-ACTS-E2E-255-approvals-tab-active-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-601 | TC-AC-ACTS-E2E-256-approvals-tab-active-sc-reset-tutup-bagian-2-pagination | FE+BE |
| TC-AC-ACTS-602 | TC-AC-ACTS-E2E-263-volume-pagination-modal-event-log-tab-add-stock-dan-approvals-tab-active-dan-history-101-baris | FE+BE |
| TC-AC-ACTS-603 | TC-AC-ACTS-E2E-257-approvals-tab-active-state | FE+BE |
| TC-AC-ACTS-604 | TC-AC-ACTS-E2E-257-approvals-tab-active-state | FE+BE |
| TC-AC-ACTS-605 | TC-AC-ACTS-E2E-257-approvals-tab-active-state | FE+BE |
| TC-AC-ACTS-606 | TC-AC-ACTS-E2E-257-approvals-tab-active-state | FE+BE |
| TC-AC-ACTS-607 | TC-AC-ACTS-E2E-258-approvals-tab-active-download | FE+BE |
| TC-AC-ACTS-608 | TC-AC-ACTS-E2E-258-approvals-tab-active-download | FE+BE |
| TC-AC-ACTS-609 | TC-AC-ACTS-E2E-260-modal-event-log-dan-approvals-tab-active-isi-sel-berkas-xlsx | FE+BE |
| TC-AC-ACTS-610 | TC-AC-ACTS-E2E-196-approvals-tab-history-screening-badge-approval-approver-tag-code-dan-baris-canceled | FE+BE |
| TC-AC-ACTS-611 | TC-AC-ACTS-E2E-196-approvals-tab-history-screening-badge-approval-approver-tag-code-dan-baris-canceled | FE+BE |
| TC-AC-ACTS-612 | TC-AC-ACTS-E2E-196-approvals-tab-history-screening-badge-approval-approver-tag-code-dan-baris-canceled | FE+BE |
| TC-AC-ACTS-613 | TC-AC-ACTS-E2E-196-approvals-tab-history-screening-badge-approval-approver-tag-code-dan-baris-canceled | FE+BE |
| TC-AC-ACTS-614 | TC-AC-ACTS-E2E-196-approvals-tab-history-screening-badge-approval-approver-tag-code-dan-baris-canceled | FE+BE |
| TC-AC-ACTS-615 | TC-AC-ACTS-E2E-197-approvals-tab-history-screening-urutan-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-616 | TC-AC-ACTS-E2E-197-approvals-tab-history-screening-urutan-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-617 | TC-AC-ACTS-E2E-197-approvals-tab-history-screening-urutan-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-618 | TC-AC-ACTS-E2E-198-approvals-tab-history-sort-bagian-2 | FE+BE |
| TC-AC-ACTS-619 | TC-AC-ACTS-E2E-198-approvals-tab-history-sort-bagian-2 | FE+BE |
| TC-AC-ACTS-620 | TC-AC-ACTS-E2E-199-approvals-tab-history-sort-bagian-3-siklus-search | FE+BE |
| TC-AC-ACTS-621 | TC-AC-ACTS-E2E-199-approvals-tab-history-sort-bagian-3-siklus-search | FE+BE |
| TC-AC-ACTS-622 | TC-AC-ACTS-E2E-200-approvals-tab-history-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-623 | TC-AC-ACTS-E2E-200-approvals-tab-history-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-624 | TC-AC-ACTS-E2E-200-approvals-tab-history-search-kolom-bagian-1 | FE+BE |
| TC-AC-ACTS-625 | TC-AC-ACTS-E2E-201-approvals-tab-history-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-626 | TC-AC-ACTS-E2E-201-approvals-tab-history-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-627 | TC-AC-ACTS-E2E-201-approvals-tab-history-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-628 | TC-AC-ACTS-E2E-201-approvals-tab-history-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-629 | TC-AC-ACTS-E2E-201-approvals-tab-history-search-kolom-bagian-2-search-visibilitas | FE+BE |
| TC-AC-ACTS-630 | TC-AC-ACTS-E2E-202-approvals-tab-history-alur-search-filter | FE+BE |
| TC-AC-ACTS-631 | TC-AC-ACTS-E2E-202-approvals-tab-history-alur-search-filter | FE+BE |
| TC-AC-ACTS-632 | TC-AC-ACTS-E2E-203-approvals-tab-history-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-633 | TC-AC-ACTS-E2E-203-approvals-tab-history-filter-bagian-1 | FE+BE |
| TC-AC-ACTS-634 | TC-AC-ACTS-E2E-204-approvals-tab-history-filter-bagian-2 | FE+BE |
| TC-AC-ACTS-635 | TC-AC-ACTS-E2E-204-approvals-tab-history-filter-bagian-2 | FE+BE |
| TC-AC-ACTS-636 | TC-AC-ACTS-E2E-204-approvals-tab-history-filter-bagian-2 | FE+BE |
| TC-AC-ACTS-637 | TC-AC-ACTS-E2E-205-approvals-tab-history-sc-screening | FE+BE |
| TC-AC-ACTS-638 | TC-AC-ACTS-E2E-205-approvals-tab-history-sc-screening | FE+BE |
| TC-AC-ACTS-639 | TC-AC-ACTS-E2E-206-approvals-tab-history-sc-ceklis | FE+BE |
| TC-AC-ACTS-640 | TC-AC-ACTS-E2E-207-approvals-tab-history-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-641 | TC-AC-ACTS-E2E-207-approvals-tab-history-sc-urutan-pin | FE+BE |
| TC-AC-ACTS-642 | TC-AC-ACTS-E2E-208-approvals-tab-history-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-643 | TC-AC-ACTS-E2E-208-approvals-tab-history-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-644 | TC-AC-ACTS-E2E-208-approvals-tab-history-sc-reset-tutup-bagian-1 | FE+BE |
| TC-AC-ACTS-645 | TC-AC-ACTS-E2E-209-approvals-tab-history-sc-reset-tutup-bagian-2-pagination | FE+BE |
| TC-AC-ACTS-646 | TC-AC-ACTS-E2E-263-volume-pagination-modal-event-log-tab-add-stock-dan-approvals-tab-active-dan-history-101-baris | FE+BE |
| TC-AC-ACTS-647 | TC-AC-ACTS-E2E-210-approvals-tab-history-state | FE+BE |
| TC-AC-ACTS-648 | TC-AC-ACTS-E2E-210-approvals-tab-history-state | FE+BE |
| TC-AC-ACTS-649 | TC-AC-ACTS-E2E-210-approvals-tab-history-state | FE+BE |
| TC-AC-ACTS-650 | TC-AC-ACTS-E2E-210-approvals-tab-history-state | FE+BE |
| TC-AC-ACTS-651 | TC-AC-ACTS-E2E-211-approvals-tab-history-download-hover-user | FE+BE |
| TC-AC-ACTS-652 | TC-AC-ACTS-E2E-211-approvals-tab-history-download-hover-user | FE+BE |
| TC-AC-ACTS-653 | TC-AC-ACTS-E2E-265-isi-sel-detail-sku-tab-available-tab-in-use-dan-approvals-tab-history-berkas-xlsx | FE+BE |
| TC-AC-ACTS-654 | TC-AC-ACTS-E2E-211-approvals-tab-history-download-hover-user | FE+BE |
| TC-AC-ACTS-655 | TC-AC-ACTS-E2E-153-pencatatan-log-add-stock-via-scan-import-gps-waiting-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-656 | TC-AC-ACTS-E2E-153-pencatatan-log-add-stock-via-scan-import-gps-waiting-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-657 | TC-AC-ACTS-E2E-153-pencatatan-log-add-stock-via-scan-import-gps-waiting-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-658 | TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | FE+BE |
| TC-AC-ACTS-659 | TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | FE+BE |
| TC-AC-ACTS-660 | TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | FE+BE |
| TC-AC-ACTS-661 | TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | FE+BE |
| TC-AC-ACTS-662 | TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | FE+BE |
| TC-AC-ACTS-663 | TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | FE+BE |
| TC-AC-ACTS-664 | TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | FE+BE |
| TC-AC-ACTS-665 | TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock | FE+BE |
| TC-AC-ACTS-666 | TC-AC-ACTS-E2E-155-pencatatan-log-field-delete-stock-sync-condition-kolom-modified-by-dan-tanpa-duplikat | FE+BE |
| TC-AC-ACTS-667 | TC-AC-ACTS-E2E-155-pencatatan-log-field-delete-stock-sync-condition-kolom-modified-by-dan-tanpa-duplikat | FE+BE |
| TC-AC-ACTS-668 | TC-AC-ACTS-E2E-155-pencatatan-log-field-delete-stock-sync-condition-kolom-modified-by-dan-tanpa-duplikat | FE+BE |
| TC-AC-ACTS-669 | TC-AC-ACTS-E2E-153-pencatatan-log-add-stock-via-scan-import-gps-waiting-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-670 | TC-AC-ACTS-E2E-150-absence-log-audit-tanpa-perubahan-dan-delete-tanpa-entri-event-log-tag-log | FE+BE |
| TC-AC-ACTS-671 | TC-AC-ACTS-E2E-156-pencatatan-log-snapshot-audit-level-sesi-dan-activation-collision-waiting | FE+BE |
| TC-AC-ACTS-672 | TC-AC-ACTS-E2E-156-pencatatan-log-snapshot-audit-level-sesi-dan-activation-collision-waiting | FE+BE |
| TC-AC-ACTS-673 | TC-AC-ACTS-E2E-106-lintas-modul-activate-tag-jalur-a-dan-b-menambah-in-use-dan-tidak-mengubah-total | FE+BE |
| TC-AC-ACTS-674 | TC-AC-ACTS-E2E-106-lintas-modul-activate-tag-jalur-a-dan-b-menambah-in-use-dan-tidak-mengubah-total | FE+BE |
| TC-AC-ACTS-675 | TC-AC-ACTS-E2E-106-lintas-modul-activate-tag-jalur-a-dan-b-menambah-in-use-dan-tidak-mengubah-total | FE+BE |
| TC-AC-ACTS-676 | TC-AC-ACTS-E2E-106-lintas-modul-activate-tag-jalur-a-dan-b-menambah-in-use-dan-tidak-mengubah-total | FE+BE |
| TC-AC-ACTS-677 | TC-AC-ACTS-E2E-107-lintas-modul-delete-tag-jalur-a-dan-b-dan-auto-resolve-activate | FE+BE |
| TC-AC-ACTS-678 | TC-AC-ACTS-E2E-107-lintas-modul-delete-tag-jalur-a-dan-b-dan-auto-resolve-activate | FE+BE |
| TC-AC-ACTS-679 | TC-AC-ACTS-E2E-107-lintas-modul-delete-tag-jalur-a-dan-b-dan-auto-resolve-activate | FE+BE |
| TC-AC-ACTS-680 | TC-AC-ACTS-E2E-107-lintas-modul-delete-tag-jalur-a-dan-b-dan-auto-resolve-activate | FE+BE |
| TC-AC-ACTS-681 | TC-AC-ACTS-E2E-108-lintas-modul-event-condition-combine-separate-dan-no-op | FE+BE |
| TC-AC-ACTS-682 | TC-AC-ACTS-E2E-108-lintas-modul-event-condition-combine-separate-dan-no-op | FE+BE |
| TC-AC-ACTS-683 | TC-AC-ACTS-E2E-108-lintas-modul-event-condition-combine-separate-dan-no-op | FE+BE |
| TC-AC-ACTS-684 | TC-AC-ACTS-E2E-108-lintas-modul-event-condition-combine-separate-dan-no-op | FE+BE |
| TC-AC-ACTS-685 | TC-AC-ACTS-E2E-109-lintas-modul-stock-ledger-device-allocation-add-approve-delete-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-686 | TC-AC-ACTS-E2E-109-lintas-modul-stock-ledger-device-allocation-add-approve-delete-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-687 | TC-AC-ACTS-E2E-109-lintas-modul-stock-ledger-device-allocation-add-approve-delete-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-688 | TC-AC-ACTS-E2E-110-lintas-modul-notifikasi-permintaan-hasil-keputusan-dan-gagal-kirim | FE+BE |
| TC-AC-ACTS-689 | TC-AC-ACTS-E2E-110-lintas-modul-notifikasi-permintaan-hasil-keputusan-dan-gagal-kirim | FE+BE |
| TC-AC-ACTS-690 | TC-AC-ACTS-E2E-110-lintas-modul-notifikasi-permintaan-hasil-keputusan-dan-gagal-kirim | FE+BE |
| TC-AC-ACTS-691 | TC-AC-ACTS-E2E-111-lintas-modul-format-tanggal-waktu-general-settings-enam-permukaan | FE+BE |
| TC-AC-ACTS-692 | TC-AC-ACTS-E2E-111-lintas-modul-format-tanggal-waktu-general-settings-enam-permukaan | FE+BE |
| TC-AC-ACTS-693 | TC-AC-ACTS-E2E-111-lintas-modul-format-tanggal-waktu-general-settings-enam-permukaan | FE+BE |
| TC-AC-ACTS-694 | TC-AC-ACTS-E2E-111-lintas-modul-format-tanggal-waktu-general-settings-enam-permukaan | FE+BE |
| TC-AC-ACTS-696 | TC-AC-ACTS-E2E-111-lintas-modul-format-tanggal-waktu-general-settings-enam-permukaan | FE+BE |
| TC-AC-ACTS-697 | TC-AC-ACTS-E2E-111-lintas-modul-format-tanggal-waktu-general-settings-enam-permukaan | FE+BE |
| TC-AC-ACTS-698 | TC-AC-ACTS-E2E-112-lintas-modul-qr-tidak-tampil-last-updated-dan-aksi-pengaruhnya | FE+BE |
| TC-AC-ACTS-699 | TC-AC-ACTS-E2E-112-lintas-modul-qr-tidak-tampil-last-updated-dan-aksi-pengaruhnya | FE+BE |
| TC-AC-ACTS-700 | TC-AC-ACTS-E2E-112-lintas-modul-qr-tidak-tampil-last-updated-dan-aksi-pengaruhnya | FE+BE |
| TC-AC-ACTS-701 | TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off | FE+BE |
| TC-AC-ACTS-702 | TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off | FE+BE |
| TC-AC-ACTS-703 | TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off | FE+BE |
| TC-AC-ACTS-704 | TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off | FE+BE |
| TC-AC-ACTS-705 | TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off | FE+BE |
| TC-AC-ACTS-706 | TC-AC-ACTS-E2E-114-defense-in-depth-distributor-suspended-read-only-capability-parsial-dan-payload-note | FE+BE |
| TC-AC-ACTS-707 | TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off | FE+BE |
| TC-AC-ACTS-708 | TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off | FE+BE |
| TC-AC-ACTS-709 | TC-AC-ACTS-E2E-114-defense-in-depth-distributor-suspended-read-only-capability-parsial-dan-payload-note | FE+BE |
| TC-AC-ACTS-710 | TC-AC-ACTS-E2E-146-konkurensi-audit-dan-delete-bersamaan-dua-sesi-ui | FE+BE |
| TC-AC-ACTS-711 | TC-AC-ACTS-E2E-146-konkurensi-audit-dan-delete-bersamaan-dua-sesi-ui | FE+BE |
| TC-AC-ACTS-712 | TC-AC-ACTS-E2E-164-konkurensi-audit-dan-delete-unit-in-use-dan-approve-subject-via-sesi-api | FE+BE |
| TC-AC-ACTS-713 | TC-AC-ACTS-E2E-164-konkurensi-audit-dan-delete-unit-in-use-dan-approve-subject-via-sesi-api | FE+BE |
| TC-AC-ACTS-714 | TC-AC-ACTS-E2E-146-konkurensi-audit-dan-delete-bersamaan-dua-sesi-ui | FE+BE |
| TC-AC-ACTS-715 | TC-AC-ACTS-E2E-078-konkurensi-add-stock-dua-sesi-submit-identifier-sama-dan-hasil-commit-berbeda | FE+BE |
| TC-AC-ACTS-716 | TC-AC-ACTS-E2E-129-audit-rfid-klik-ganda-tanpa-stock-ledger-event-log-dan-start-scan-tanpa-reader | FE+BE |
| TC-AC-ACTS-717 | TC-AC-ACTS-E2E-134-audit-nfc-start-scan-tanpa-reader-d06-leave-cancel-dan-scan-uid-belum-terdaftar | FE+BE |
| TC-AC-ACTS-718 | TC-AC-ACTS-E2E-134-audit-nfc-start-scan-tanpa-reader-d06-leave-cancel-dan-scan-uid-belum-terdaftar | FE+BE |
| TC-AC-ACTS-719 | TC-AC-ACTS-E2E-134-audit-nfc-start-scan-tanpa-reader-d06-leave-cancel-dan-scan-uid-belum-terdaftar | FE+BE |
| TC-AC-ACTS-720 | TC-AC-ACTS-E2E-056-add-stock-rfid-submit-ok-kosong-klik-ganda-sku-tidak-valid-dan-tanpa-batas | FE+BE |
| TC-AC-ACTS-721 | TC-AC-ACTS-E2E-062-add-stock-rfid-navigasi-breadcrumb-url-gps-dan-dialog-modul | FE+BE |
| TC-AC-ACTS-722 | TC-AC-ACTS-E2E-062-add-stock-rfid-navigasi-breadcrumb-url-gps-dan-dialog-modul | FE+BE |
| TC-AC-ACTS-724 | TC-AC-ACTS-E2E-034-role-matrix-positif-eksekusi-add-stock-audit-dan-scan-distributor | FE+BE |
| TC-AC-ACTS-725 | TC-AC-ACTS-E2E-109-lintas-modul-stock-ledger-device-allocation-add-approve-delete-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-726 | TC-AC-ACTS-E2E-109-lintas-modul-stock-ledger-device-allocation-add-approve-delete-dan-batch-waiting | FE+BE |
| TC-AC-ACTS-727 | TC-AC-ACTS-E2E-078-konkurensi-add-stock-dua-sesi-submit-identifier-sama-dan-hasil-commit-berbeda | FE+BE |
| TC-AC-ACTS-728 | TC-AC-ACTS-E2E-095-approvals-duplicate-dialog-review-register-duplicate-activation-collision-dan-byo | FE+BE |
| TC-AC-ACTS-729 | TC-AC-ACTS-E2E-096-approvals-duplicate-existing-record-label-matched-identifier-dan-approval-note | FE+BE |
| TC-AC-ACTS-730 | TC-AC-ACTS-E2E-105-resilience-approvals-error-detail-gagal-muat-timeout-dan-download-gagal | FE+BE |
| TC-AC-ACTS-731 | TC-AC-ACTS-E2E-160-detail-sku-realtime-tab-available-opsi-filter-banner-dan-approval | FE+BE |
| TC-AC-ACTS-732 | TC-AC-ACTS-E2E-264-volume-add-stock-rfid-1001-tag-tanpa-field-notes-dan-tanpa-batas-unit | FE+BE |
| TC-AC-ACTS-733 | TC-AC-ACTS-E2E-127-audit-rfid-unit-combined-in-use-waiting-empty-state-dan-tag-code-tidak-berubah | FE+BE |
| TC-AC-ACTS-734 | TC-AC-ACTS-E2E-090-add-stock-gps-klik-ganda-bypass-e2a-dan-identifier-rejected | FE+BE |
| TC-AC-ACTS-735 | TC-AC-ACTS-E2E-160-detail-sku-realtime-tab-available-opsi-filter-banner-dan-approval | FE+BE |
| TC-AC-ACTS-736 | TC-AC-ACTS-E2E-149-state-tenant-distributor-suspended-aksi-tulis-ditolak-dan-plan-gating-tidak-ada | FE+BE |
| TC-AC-ACTS-737 | TC-AC-ACTS-E2E-087-add-stock-gps-berkas-header-salah-tipe-template-dan-batas-1-mb | FE+BE |
| TC-AC-ACTS-738 | TC-AC-ACTS-E2E-087-add-stock-gps-berkas-header-salah-tipe-template-dan-batas-1-mb | FE+BE |
| TC-AC-ACTS-739 | TC-AC-ACTS-E2E-087-add-stock-gps-berkas-header-salah-tipe-template-dan-batas-1-mb | FE+BE |
| TC-AC-ACTS-740 | TC-AC-ACTS-E2E-059-add-stock-rfid-normalisasi-identifier-unit-rejected-dan-submit-ulang | FE+BE |
| TC-AC-ACTS-741 | TC-AC-ACTS-E2E-090-add-stock-gps-klik-ganda-bypass-e2a-dan-identifier-rejected | FE+BE |
| TC-AC-ACTS-742 | TC-AC-ACTS-E2E-100-approvals-duplicate-scan-ulang-identifier-rejected-dan-constraint-unique-status-live | FE+BE |
| TC-AC-ACTS-744 | TC-AC-ACTS-E2E-056-add-stock-rfid-submit-ok-kosong-klik-ganda-sku-tidak-valid-dan-tanpa-batas | FE+BE |
| TC-AC-ACTS-745 | TC-AC-ACTS-E2E-059-add-stock-rfid-normalisasi-identifier-unit-rejected-dan-submit-ulang | FE+BE |
| TC-AC-ACTS-746 | TC-AC-ACTS-E2E-058-add-stock-rfid-submit-waiting-partial-register-dan-bentuk-tunggal-jamak | FE+BE |
| TC-AC-ACTS-748 | TC-AC-ACTS-E2E-086-add-stock-gps-match-existing-ringkasan-manual-entry-dan-invalid-berulang | FE+BE |
| TC-AC-ACTS-749 | TC-AC-ACTS-E2E-086-add-stock-gps-match-existing-ringkasan-manual-entry-dan-invalid-berulang | FE+BE |
| TC-AC-ACTS-750 | TC-AC-ACTS-E2E-096-approvals-duplicate-existing-record-label-matched-identifier-dan-approval-note | FE+BE |
| TC-AC-ACTS-751 | TC-AC-ACTS-E2E-156-pencatatan-log-snapshot-audit-level-sesi-dan-activation-collision-waiting | FE+BE |
| TC-AC-ACTS-752 | TC-AC-ACTS-E2E-004-navigasi-stock-list-detail-sku-dan-add-stock-per-tag-type | FE+BE |
| TC-AC-ACTS-753 | TC-AC-ACTS-E2E-004-navigasi-stock-list-detail-sku-dan-add-stock-per-tag-type | FE+BE |
| TC-AC-ACTS-756 | TC-AC-ACTS-E2E-126-audit-rfid-toast-netral-t20-bentuk-tunggal-counter-dan-badge-severity | FE+BE |
| TC-AC-ACTS-758 | TC-AC-ACTS-E2E-149-state-tenant-distributor-suspended-aksi-tulis-ditolak-dan-plan-gating-tidak-ada | FE+BE |
| TC-AC-ACTS-759 | TC-AC-ACTS-E2E-147-konkurensi-delete-by-scan-dan-bulk-delete-bersamaan-sesi-lain | FE+BE |
| TC-AC-ACTS-760 | TC-AC-ACTS-E2E-149-state-tenant-distributor-suspended-aksi-tulis-ditolak-dan-plan-gating-tidak-ada | FE+BE |
| TC-AC-ACTS-761 | TC-AC-ACTS-E2E-058-add-stock-rfid-submit-waiting-partial-register-dan-bentuk-tunggal-jamak | FE+BE |
| TC-AC-ACTS-762 | TC-AC-ACTS-E2E-131-audit-rfid-konkurensi-status-unit-berubah-oleh-sesi-lain-di-tengah-sesi | FE+BE |
| TC-AC-ACTS-763 | TC-AC-ACTS-E2E-085-add-stock-gps-validasi-imei-duplicate-dan-hapus-baris-preview | FE+BE |
| TC-AC-ACTS-764 | TC-AC-ACTS-E2E-096-approvals-duplicate-existing-record-label-matched-identifier-dan-approval-note | FE+BE |
| TC-AC-ACTS-765 | TC-AC-ACTS-E2E-126-audit-rfid-toast-netral-t20-bentuk-tunggal-counter-dan-badge-severity | FE+BE |
| TC-AC-ACTS-766 | TC-AC-ACTS-E2E-219-modal-event-log-angka-success-per-tag-hardware-dan-unit-bypass | FE+BE |
| TC-AC-ACTS-767 | TC-AC-ACTS-E2E-131-audit-rfid-konkurensi-status-unit-berubah-oleh-sesi-lain-di-tengah-sesi | FE+BE |
| TC-AC-ACTS-768 | TC-AC-ACTS-E2E-102-approvals-duplicate-e4-additional-approver-subject-sendiri-disembunyikan | FE+BE |
| TC-AC-ACTS-769 | TC-AC-ACTS-E2E-091-add-stock-gps-volume-5000-baris-sinkron-dan-background | FE+BE |
| TC-AC-ACTS-770 | TC-AC-ACTS-E2E-091-add-stock-gps-volume-5000-baris-sinkron-dan-background | FE+BE |
| TC-AC-ACTS-771 | TC-AC-ACTS-E2E-092-add-stock-gps-volume-job-background-gagal-ambang-lintas-upload-dan-remove-ke-5000 | FE+BE |
| TC-AC-ACTS-772 | TC-AC-ACTS-E2E-092-add-stock-gps-volume-job-background-gagal-ambang-lintas-upload-dan-remove-ke-5000 | FE+BE |
| TC-AC-ACTS-773 | TC-AC-ACTS-E2E-077-absence-add-stock-bypass-seluruh-batch-preview-read-only-dan-remove-tanpa-tulis | FE+BE |
| TC-AC-ACTS-774 | TC-AC-ACTS-E2E-126-audit-rfid-toast-netral-t20-bentuk-tunggal-counter-dan-badge-severity | FE+BE |
| TC-AC-ACTS-775 | TC-AC-ACTS-E2E-219-modal-event-log-angka-success-per-tag-hardware-dan-unit-bypass | FE+BE |
| TC-AC-ACTS-776 | TC-AC-ACTS-E2E-105-resilience-approvals-error-detail-gagal-muat-timeout-dan-download-gagal | FE+BE |
| TC-AC-ACTS-777 | TC-AC-ACTS-E2E-156-pencatatan-log-snapshot-audit-level-sesi-dan-activation-collision-waiting | FE+BE |
| TC-AC-ACTS-778 | TC-AC-ACTS-E2E-060-add-stock-rfid-bypass-e2a-total-control-pada-batch-campuran | FE+BE |
| TC-AC-ACTS-779 | TC-AC-ACTS-E2E-077-absence-add-stock-bypass-seluruh-batch-preview-read-only-dan-remove-tanpa-tulis | FE+BE |
| TC-AC-ACTS-780 | TC-AC-ACTS-E2E-121-approvals-duplicate-existing-record-unit-paling-awal-saat-dua-unit-live-berbagi-identifier | FE+BE |
| TC-AC-ACTS-781 | TC-AC-ACTS-E2E-108-lintas-modul-event-condition-combine-separate-dan-no-op | FE+BE |
| TC-AC-ACTS-782 | TC-AC-ACTS-E2E-108-lintas-modul-event-condition-combine-separate-dan-no-op | FE+BE |
| TC-AC-ACTS-783 | TC-AC-ACTS-E2E-086-add-stock-gps-match-existing-ringkasan-manual-entry-dan-invalid-berulang | FE+BE |
| TC-AC-ACTS-784 | TC-AC-ACTS-E2E-114-defense-in-depth-distributor-suspended-read-only-capability-parsial-dan-payload-note | FE+BE |
| TC-AC-ACTS-785 | TC-AC-ACTS-E2E-114-defense-in-depth-distributor-suspended-read-only-capability-parsial-dan-payload-note | FE+BE |
| TC-AC-ACTS-786 | TC-AC-ACTS-E2E-114-defense-in-depth-distributor-suspended-read-only-capability-parsial-dan-payload-note | FE+BE |
| TC-AC-ACTS-787 | TC-AC-ACTS-E2E-158-detail-sku-retensi-state-per-sub-tab-hapus-baris-terakhir-dan-identifier-non-rfid | FE+BE |
| TC-AC-ACTS-788 | TC-AC-ACTS-E2E-259-approvals-tab-active-dan-history-state-per-sub-tab-dan-refresh-f5 | FE+BE |
| TC-AC-ACTS-789 | TC-AC-ACTS-E2E-158-detail-sku-retensi-state-per-sub-tab-hapus-baris-terakhir-dan-identifier-non-rfid | FE+BE |
| TC-AC-ACTS-790 | TC-AC-ACTS-E2E-016-filter-stock-list-kombinasi-and-dan-independen-dari-column-visibility | FE+BE |
| TC-AC-ACTS-795 | TC-AC-ACTS-E2E-158-detail-sku-retensi-state-per-sub-tab-hapus-baris-terakhir-dan-identifier-non-rfid | FE+BE |
| TC-AC-ACTS-796 | TC-AC-ACTS-E2E-054-add-stock-rfid-reload-back-fisik-dan-pindah-tab-saat-sesi-aktif | FE+BE |
| TC-AC-ACTS-797 | TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble | FE+BE |
| TC-AC-ACTS-798 | TC-AC-ACTS-E2E-072-add-stock-ble-reload-back-fisik-pindah-tab-scanner-tidak-terhubung-dan-putus | FE+BE |
| TC-AC-ACTS-799 | TC-AC-ACTS-E2E-163-audit-rfid-sesi-scan-aktif-back-fisik-reader-putus-pindah-tab-dan-reload | FE+BE |
| TC-AC-ACTS-800 | TC-AC-ACTS-E2E-163-audit-rfid-sesi-scan-aktif-back-fisik-reader-putus-pindah-tab-dan-reload | FE+BE |
| TC-AC-ACTS-801 | TC-AC-ACTS-E2E-158-detail-sku-retensi-state-per-sub-tab-hapus-baris-terakhir-dan-identifier-non-rfid | FE+BE |
| TC-AC-ACTS-802 | TC-AC-ACTS-E2E-259-approvals-tab-active-dan-history-state-per-sub-tab-dan-refresh-f5 | FE+BE |
| TC-AC-ACTS-803 | TC-AC-ACTS-E2E-062-add-stock-rfid-navigasi-breadcrumb-url-gps-dan-dialog-modul | FE+BE |
| TC-AC-ACTS-804 | TC-AC-ACTS-E2E-159-detail-sku-aria-label-sort-tag-code-mutasi-terfilter-siklus-toast-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-805 | TC-AC-ACTS-E2E-212-detail-sku-tab-available-registered-at-hasil-approve | FE+BE |
| TC-AC-ACTS-806 | TC-AC-ACTS-E2E-102-approvals-duplicate-e4-additional-approver-subject-sendiri-disembunyikan | FE+BE |
| TC-AC-ACTS-807 | TC-AC-ACTS-E2E-120-add-stock-gps-partial-register-bentuk-tunggal-continue-dan-semua-waiting | FE+BE |
| TC-AC-ACTS-808 | TC-AC-ACTS-E2E-103-approvals-duplicate-konkurensi-dua-approver-dan-dialog-nested | FE+BE |
| TC-AC-ACTS-809 | TC-AC-ACTS-E2E-103-approvals-duplicate-konkurensi-dua-approver-dan-dialog-nested | FE+BE |
| TC-AC-ACTS-810 | TC-AC-ACTS-E2E-105-resilience-approvals-error-detail-gagal-muat-timeout-dan-download-gagal | FE+BE |
| TC-AC-ACTS-811 | TC-AC-ACTS-E2E-075-resilience-add-stock-submit-gagal-dan-timeout-rfid-nfc-ble-gps | FE+BE |
| TC-AC-ACTS-812 | TC-AC-ACTS-E2E-001-screening-stock-list-breadcrumb-header-kolom-dan-footer | FE+BE |
| TC-AC-ACTS-813 | TC-AC-ACTS-E2E-110-lintas-modul-notifikasi-permintaan-hasil-keputusan-dan-gagal-kirim | FE+BE |
| TC-AC-ACTS-814 | TC-AC-ACTS-E2E-166-detail-sku-tab-available-unit-waiting-rejected-byo-registered-by-dan-row-action-tag-log | FE+BE |
| TC-AC-ACTS-815 | TC-AC-ACTS-E2E-138-delete-by-scan-screening-toolbar-visibilitas-sku-gps-dan-tanpa-reader | FE+BE |
| TC-AC-ACTS-816 | TC-AC-ACTS-E2E-036-role-matrix-read-only-dan-capability-parsial-aksi-tulis-hidden | FE+BE |
| TC-AC-ACTS-817 | TC-AC-ACTS-E2E-138-delete-by-scan-screening-toolbar-visibilitas-sku-gps-dan-tanpa-reader | FE+BE |
| TC-AC-ACTS-818 | TC-AC-ACTS-E2E-138-delete-by-scan-screening-toolbar-visibilitas-sku-gps-dan-tanpa-reader | FE+BE |
| TC-AC-ACTS-819 | TC-AC-ACTS-E2E-138-delete-by-scan-screening-toolbar-visibilitas-sku-gps-dan-tanpa-reader | FE+BE |
| TC-AC-ACTS-820 | TC-AC-ACTS-E2E-141-delete-by-scan-sesi-terkunci-hapus-langsung-beruntun-dan-damaged-missing | FE+BE |
| TC-AC-ACTS-821 | TC-AC-ACTS-E2E-141-delete-by-scan-sesi-terkunci-hapus-langsung-beruntun-dan-damaged-missing | FE+BE |
| TC-AC-ACTS-822 | TC-AC-ACTS-E2E-141-delete-by-scan-sesi-terkunci-hapus-langsung-beruntun-dan-damaged-missing | FE+BE |
| TC-AC-ACTS-823 | TC-AC-ACTS-E2E-141-delete-by-scan-sesi-terkunci-hapus-langsung-beruntun-dan-damaged-missing | FE+BE |
| TC-AC-ACTS-824 | TC-AC-ACTS-E2E-142-delete-by-scan-penolakan-sku-lain-status-combined-dan-existing-record | FE+BE |
| TC-AC-ACTS-825 | TC-AC-ACTS-E2E-142-delete-by-scan-penolakan-sku-lain-status-combined-dan-existing-record | FE+BE |
| TC-AC-ACTS-826 | TC-AC-ACTS-E2E-142-delete-by-scan-penolakan-sku-lain-status-combined-dan-existing-record | FE+BE |
| TC-AC-ACTS-827 | TC-AC-ACTS-E2E-142-delete-by-scan-penolakan-sku-lain-status-combined-dan-existing-record | FE+BE |
| TC-AC-ACTS-828 | TC-AC-ACTS-E2E-143-delete-by-scan-kode-tidak-dikenal-sesi-berlanjut-nfc-ble-dan-scan-ulang | FE+BE |
| TC-AC-ACTS-829 | TC-AC-ACTS-E2E-143-delete-by-scan-kode-tidak-dikenal-sesi-berlanjut-nfc-ble-dan-scan-ulang | FE+BE |
| TC-AC-ACTS-830 | TC-AC-ACTS-E2E-143-delete-by-scan-kode-tidak-dikenal-sesi-berlanjut-nfc-ble-dan-scan-ulang | FE+BE |
| TC-AC-ACTS-831 | TC-AC-ACTS-E2E-147-konkurensi-delete-by-scan-dan-bulk-delete-bersamaan-sesi-lain | FE+BE |
| TC-AC-ACTS-832 | TC-AC-ACTS-E2E-148-resilience-delete-dan-audit-gagal-5xx-dan-timeout | FE+BE |
| TC-AC-ACTS-833 | TC-AC-ACTS-E2E-144-delete-by-scan-reader-putus-pindah-halaman-log-sesi-dan-distributor | FE+BE |
| TC-AC-ACTS-834 | TC-AC-ACTS-E2E-144-delete-by-scan-reader-putus-pindah-halaman-log-sesi-dan-distributor | FE+BE |
| TC-AC-ACTS-835 | TC-AC-ACTS-E2E-144-delete-by-scan-reader-putus-pindah-halaman-log-sesi-dan-distributor | FE+BE |
| TC-AC-ACTS-836 | TC-AC-ACTS-E2E-144-delete-by-scan-reader-putus-pindah-halaman-log-sesi-dan-distributor | FE+BE |
| TC-AC-ACTS-837 | TC-AC-ACTS-E2E-149-state-tenant-distributor-suspended-aksi-tulis-ditolak-dan-plan-gating-tidak-ada | FE+BE |
| TC-AC-ACTS-838 | TC-AC-ACTS-E2E-139-bulk-delete-screening-checkbox-select-all-dan-kolom-checkbox | FE+BE |
| TC-AC-ACTS-839 | TC-AC-ACTS-E2E-139-bulk-delete-screening-checkbox-select-all-dan-kolom-checkbox | FE+BE |
| TC-AC-ACTS-840 | TC-AC-ACTS-E2E-139-bulk-delete-screening-checkbox-select-all-dan-kolom-checkbox | FE+BE |
| TC-AC-ACTS-841 | TC-AC-ACTS-E2E-140-bulk-delete-seleksi-lintas-halaman-selection-limit-dan-dialog-delete-units | FE+BE |
| TC-AC-ACTS-842 | TC-AC-ACTS-E2E-140-bulk-delete-seleksi-lintas-halaman-selection-limit-dan-dialog-delete-units | FE+BE |
| TC-AC-ACTS-843 | TC-AC-ACTS-E2E-140-bulk-delete-seleksi-lintas-halaman-selection-limit-dan-dialog-delete-units | FE+BE |
| TC-AC-ACTS-844 | TC-AC-ACTS-E2E-145-bulk-delete-sukses-sebagian-dilewati-collapse-satu-baris-dan-distributor | FE+BE |
| TC-AC-ACTS-845 | TC-AC-ACTS-E2E-140-bulk-delete-seleksi-lintas-halaman-selection-limit-dan-dialog-delete-units | FE+BE |
| TC-AC-ACTS-846 | TC-AC-ACTS-E2E-145-bulk-delete-sukses-sebagian-dilewati-collapse-satu-baris-dan-distributor | FE+BE |
| TC-AC-ACTS-847 | TC-AC-ACTS-E2E-145-bulk-delete-sukses-sebagian-dilewati-collapse-satu-baris-dan-distributor | FE+BE |
| TC-AC-ACTS-848 | TC-AC-ACTS-E2E-147-konkurensi-delete-by-scan-dan-bulk-delete-bersamaan-sesi-lain | FE+BE |
| TC-AC-ACTS-849 | TC-AC-ACTS-E2E-148-resilience-delete-dan-audit-gagal-5xx-dan-timeout | FE+BE |
| TC-AC-ACTS-850 | TC-AC-ACTS-E2E-147-konkurensi-delete-by-scan-dan-bulk-delete-bersamaan-sesi-lain | FE+BE |
| TC-AC-ACTS-851 | TC-AC-ACTS-E2E-139-bulk-delete-screening-checkbox-select-all-dan-kolom-checkbox | FE+BE |
| TC-AC-ACTS-852 | TC-AC-ACTS-E2E-145-bulk-delete-sukses-sebagian-dilewati-collapse-satu-baris-dan-distributor | FE+BE |
| TC-AC-ACTS-853 | TC-AC-ACTS-E2E-014-filter-stock-list-screening-panel-range-dan-field-sku | FE+BE |
| TC-AC-ACTS-854 | TC-AC-ACTS-E2E-002-isi-sel-stock-list-tanpa-kuota-icon-tag-type-badge-dan-device-name-panjang | FE+BE |
| TC-AC-ACTS-856 | TC-AC-ACTS-E2E-157-detail-sku-screening-header-summary-bar-tab-dan-tag-type-icon | FE+BE |
| TC-AC-ACTS-857 | TC-AC-ACTS-E2E-061-add-stock-rfid-detail-ui-aria-live-tooltip-badge-kartu-sku-dan-saving-state | FE+BE |
| TC-AC-ACTS-858 | TC-AC-ACTS-E2E-143-delete-by-scan-kode-tidak-dikenal-sesi-berlanjut-nfc-ble-dan-scan-ulang | FE+BE |
| TC-AC-ACTS-859 | TC-AC-ACTS-E2E-151-absence-log-delete-by-scan-tanpa-penghapusan-usage-event-dan-status-synced | FE+BE |
| TC-AC-ACTS-860 | TC-AC-ACTS-E2E-152-usage-event-handheld-reader-add-stock-audit-delete-by-scan-dan-kegagalan-tulis | FE+BE |
| TC-AC-ACTS-861 | TC-AC-ACTS-E2E-152-usage-event-handheld-reader-add-stock-audit-delete-by-scan-dan-kegagalan-tulis | FE+BE |
| TC-AC-ACTS-862 | TC-AC-ACTS-E2E-152-usage-event-handheld-reader-add-stock-audit-delete-by-scan-dan-kegagalan-tulis | FE+BE |
| TC-AC-ACTS-863 | TC-AC-ACTS-E2E-151-absence-log-delete-by-scan-tanpa-penghapusan-usage-event-dan-status-synced | FE+BE |
| TC-AC-ACTS-864 | TC-AC-ACTS-E2E-151-absence-log-delete-by-scan-tanpa-penghapusan-usage-event-dan-status-synced | FE+BE |
| TC-AC-ACTS-865 | TC-AC-ACTS-E2E-151-absence-log-delete-by-scan-tanpa-penghapusan-usage-event-dan-status-synced | FE+BE |
| TC-AC-ACTS-866 | TC-AC-ACTS-E2E-152-usage-event-handheld-reader-add-stock-audit-delete-by-scan-dan-kegagalan-tulis | FE+BE |
| TC-AC-ACTS-867 | TC-AC-ACTS-E2E-152-usage-event-handheld-reader-add-stock-audit-delete-by-scan-dan-kegagalan-tulis | FE+BE |
| TC-AC-ACTS-868 | TC-AC-ACTS-E2E-051-add-stock-rfid-checkbox-select-all-dan-dialog-remove | FE+BE |
| TC-AC-ACTS-869 | TC-AC-ACTS-E2E-051-add-stock-rfid-checkbox-select-all-dan-dialog-remove | FE+BE |
| TC-AC-ACTS-870 | TC-AC-ACTS-E2E-051-add-stock-rfid-checkbox-select-all-dan-dialog-remove | FE+BE |
| TC-AC-ACTS-871 | TC-AC-ACTS-E2E-051-add-stock-rfid-checkbox-select-all-dan-dialog-remove | FE+BE |
| TC-AC-ACTS-872 | TC-AC-ACTS-E2E-052-add-stock-rfid-remove-sukses-baris-waiting-dan-bar-non-interaktif | FE+BE |
| TC-AC-ACTS-873 | TC-AC-ACTS-E2E-052-add-stock-rfid-remove-sukses-baris-waiting-dan-bar-non-interaktif | FE+BE |
| TC-AC-ACTS-874 | TC-AC-ACTS-E2E-052-add-stock-rfid-remove-sukses-baris-waiting-dan-bar-non-interaktif | FE+BE |
| TC-AC-ACTS-875 | TC-AC-ACTS-E2E-079-add-stock-rfid-remove-by-scan-beruntun-dan-kode-tidak-dikenal | FE+BE |
| TC-AC-ACTS-876 | TC-AC-ACTS-E2E-079-add-stock-rfid-remove-by-scan-beruntun-dan-kode-tidak-dikenal | FE+BE |
| TC-AC-ACTS-877 | TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble | FE+BE |
| TC-AC-ACTS-878 | TC-AC-ACTS-E2E-077-absence-add-stock-bypass-seluruh-batch-preview-read-only-dan-remove-tanpa-tulis | FE+BE |
| TC-AC-ACTS-879 | TC-AC-ACTS-E2E-098-approvals-duplicate-approve-register-duplicate-activation-collision-dan-unit-tidak-tampil | FE+BE |
| TC-AC-ACTS-880 | TC-AC-ACTS-E2E-093-add-stock-gps-checkbox-select-all-dan-dialog-remove-imei | FE+BE |
| TC-AC-ACTS-881 | TC-AC-ACTS-E2E-093-add-stock-gps-checkbox-select-all-dan-dialog-remove-imei | FE+BE |
| TC-AC-ACTS-882 | TC-AC-ACTS-E2E-093-add-stock-gps-checkbox-select-all-dan-dialog-remove-imei | FE+BE |
| TC-AC-ACTS-883 | TC-AC-ACTS-E2E-094-add-stock-gps-remove-sukses-reevaluasi-preview-dan-ikon-hapus | FE+BE |
| TC-AC-ACTS-884 | TC-AC-ACTS-E2E-094-add-stock-gps-remove-sukses-reevaluasi-preview-dan-ikon-hapus | FE+BE |
| TC-AC-ACTS-885 | TC-AC-ACTS-E2E-092-add-stock-gps-volume-job-background-gagal-ambang-lintas-upload-dan-remove-ke-5000 | FE+BE |
| TC-AC-ACTS-886 | TC-AC-ACTS-E2E-094-add-stock-gps-remove-sukses-reevaluasi-preview-dan-ikon-hapus | FE+BE |
| TC-AC-ACTS-887 | TC-AC-ACTS-E2E-092-add-stock-gps-volume-job-background-gagal-ambang-lintas-upload-dan-remove-ke-5000 | FE+BE |
| TC-AC-ACTS-888 | TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available | FE+BE |
| TC-AC-ACTS-889 | TC-AC-ACTS-E2E-006-stock-list-mengikuti-aksi-delete-audit-dan-sku-baru | FE+BE |
| TC-AC-ACTS-890 | TC-AC-ACTS-E2E-005-distributor-stock-list-metrik-di-scope-unit-sendiri | FE+BE |
| TC-AC-ACTS-891 | TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval | FE+BE |
| TC-AC-ACTS-892 | TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval | FE+BE |
| TC-AC-ACTS-893 | TC-AC-ACTS-E2E-053-add-stock-rfid-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-894 | TC-AC-ACTS-E2E-053-add-stock-rfid-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-895 | TC-AC-ACTS-E2E-065-add-stock-nfc-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-896 | TC-AC-ACTS-E2E-065-add-stock-nfc-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-897 | TC-AC-ACTS-E2E-071-add-stock-ble-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-898 | TC-AC-ACTS-E2E-071-add-stock-ble-cancel-dan-meninggalkan-halaman-dengan-list | FE+BE |
| TC-AC-ACTS-899 | TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview | FE+BE |
| TC-AC-ACTS-900 | TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview | FE+BE |
| TC-AC-ACTS-901 | TC-AC-ACTS-E2E-159-detail-sku-aria-label-sort-tag-code-mutasi-terfilter-siklus-toast-dan-ikon-combined | FE+BE |
| TC-AC-ACTS-902 | TC-AC-ACTS-E2E-214-modal-event-log-buka-default-tab-add-stock-tutup-sesi-sku-ini-dan-popup-audit-tanpa-ikon | FE+BE |
| TC-AC-ACTS-903 | TC-AC-ACTS-E2E-214-modal-event-log-buka-default-tab-add-stock-tutup-sesi-sku-ini-dan-popup-audit-tanpa-ikon | FE+BE |
| TC-AC-ACTS-904 | TC-AC-ACTS-E2E-214-modal-event-log-buka-default-tab-add-stock-tutup-sesi-sku-ini-dan-popup-audit-tanpa-ikon | FE+BE |
| TC-AC-ACTS-905 | TC-AC-ACTS-E2E-215-modal-event-log-kolom-actions-detail-dan-popup-detail-sesi-add-stock-delete-bulk-dan-scan | FE+BE |
| TC-AC-ACTS-906 | TC-AC-ACTS-E2E-237-modal-event-log-tab-audit-tag-screening-urutan | FE+BE |
| TC-AC-ACTS-907 | TC-AC-ACTS-E2E-237-modal-event-log-tab-audit-tag-screening-urutan | FE+BE |
| TC-AC-ACTS-908 | TC-AC-ACTS-E2E-238-modal-event-log-tab-audit-tag-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-909 | TC-AC-ACTS-E2E-238-modal-event-log-tab-audit-tag-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-910 | TC-AC-ACTS-E2E-238-modal-event-log-tab-audit-tag-sort-bagian-1 | FE+BE |
| TC-AC-ACTS-911 | TC-AC-ACTS-E2E-239-modal-event-log-tab-audit-tag-sort-bagian-2-search-kolom | FE+BE |
| TC-AC-ACTS-912 | TC-AC-ACTS-E2E-239-modal-event-log-tab-audit-tag-sort-bagian-2-search-kolom | FE+BE |
| TC-AC-ACTS-913 | TC-AC-ACTS-E2E-239-modal-event-log-tab-audit-tag-sort-bagian-2-search-kolom | FE+BE |
| TC-AC-ACTS-914 | TC-AC-ACTS-E2E-240-modal-event-log-tab-audit-tag-filter | FE+BE |
| TC-AC-ACTS-915 | TC-AC-ACTS-E2E-240-modal-event-log-tab-audit-tag-filter | FE+BE |
| TC-AC-ACTS-916 | TC-AC-ACTS-E2E-240-modal-event-log-tab-audit-tag-filter | FE+BE |
| TC-AC-ACTS-917 | TC-AC-ACTS-E2E-241-modal-event-log-tab-audit-tag-sc-screening-sc-ceklis | FE+BE |
| TC-AC-ACTS-918 | TC-AC-ACTS-E2E-241-modal-event-log-tab-audit-tag-sc-screening-sc-ceklis | FE+BE |
| TC-AC-ACTS-919 | TC-AC-ACTS-E2E-242-modal-event-log-tab-audit-tag-pagination | FE+BE |
| TC-AC-ACTS-920 | TC-AC-ACTS-E2E-243-modal-event-log-tab-audit-tag-state | FE+BE |
| TC-AC-ACTS-921 | TC-AC-ACTS-E2E-243-modal-event-log-tab-audit-tag-state | FE+BE |
| TC-AC-ACTS-922 | TC-AC-ACTS-E2E-243-modal-event-log-tab-audit-tag-state | FE+BE |
| TC-AC-ACTS-923 | TC-AC-ACTS-E2E-243-modal-event-log-tab-audit-tag-state | FE+BE |
| TC-AC-ACTS-924 | TC-AC-ACTS-E2E-244-modal-event-log-tab-audit-tag-download | FE+BE |
| TC-AC-ACTS-925 | TC-AC-ACTS-E2E-244-modal-event-log-tab-audit-tag-download | FE+BE |
| TC-AC-ACTS-926 | TC-AC-ACTS-E2E-260-modal-event-log-dan-approvals-tab-active-isi-sel-berkas-xlsx | FE+BE |
| TC-AC-ACTS-927 | TC-AC-ACTS-E2E-220-modal-event-log-tab-audit-tag-penulisan-found-not-found-dan-recovery | FE+BE |
| TC-AC-ACTS-928 | TC-AC-ACTS-E2E-220-modal-event-log-tab-audit-tag-penulisan-found-not-found-dan-recovery | FE+BE |
| TC-AC-ACTS-929 | TC-AC-ACTS-E2E-220-modal-event-log-tab-audit-tag-penulisan-found-not-found-dan-recovery | FE+BE |
| TC-AC-ACTS-930 | TC-AC-ACTS-E2E-150-absence-log-audit-tanpa-perubahan-dan-delete-tanpa-entri-event-log-tag-log | FE+BE |
| TC-AC-ACTS-931 | TC-AC-ACTS-E2E-261-modal-event-log-penulisan-sesi-delete-by-scan-unit-dilewati-audit-dan-kolom-hardware | FE+BE |
| TC-AC-ACTS-932 | TC-AC-ACTS-E2E-261-modal-event-log-penulisan-sesi-delete-by-scan-unit-dilewati-audit-dan-kolom-hardware | FE+BE |
| TC-AC-ACTS-933 | TC-AC-ACTS-E2E-215-modal-event-log-kolom-actions-detail-dan-popup-detail-sesi-add-stock-delete-bulk-dan-scan | FE+BE |
| TC-AC-ACTS-934 | TC-AC-ACTS-E2E-215-modal-event-log-kolom-actions-detail-dan-popup-detail-sesi-add-stock-delete-bulk-dan-scan | FE+BE |
| TC-AC-ACTS-935 | TC-AC-ACTS-E2E-215-modal-event-log-kolom-actions-detail-dan-popup-detail-sesi-add-stock-delete-bulk-dan-scan | FE+BE |
| TC-AC-ACTS-936 | TC-AC-ACTS-E2E-216-modal-event-log-popup-detail-sesi-audit-snapshot-section-kosong-dan-empty-state | FE+BE |
| TC-AC-ACTS-937 | TC-AC-ACTS-E2E-216-modal-event-log-popup-detail-sesi-audit-snapshot-section-kosong-dan-empty-state | FE+BE |
| TC-AC-ACTS-938 | TC-AC-ACTS-E2E-216-modal-event-log-popup-detail-sesi-audit-snapshot-section-kosong-dan-empty-state | FE+BE |
| TC-AC-ACTS-939 | TC-AC-ACTS-E2E-216-modal-event-log-popup-detail-sesi-audit-snapshot-section-kosong-dan-empty-state | FE+BE |
| TC-AC-ACTS-940 | TC-AC-ACTS-E2E-217-modal-event-log-popup-detail-read-only-scroll-internal-dan-error-load | FE+BE |
| TC-AC-ACTS-941 | TC-AC-ACTS-E2E-217-modal-event-log-popup-detail-read-only-scroll-internal-dan-error-load | FE+BE |
| TC-AC-ACTS-942 | TC-AC-ACTS-E2E-222-modal-event-log-distributor-hanya-batch-sendiri-dan-tanpa-duplicate-canceled-global-settings | FE+BE |
| TC-AC-ACTS-943 | TC-AC-ACTS-E2E-222-modal-event-log-distributor-hanya-batch-sendiri-dan-tanpa-duplicate-canceled-global-settings | FE+BE |
| TC-AC-ACTS-944 | TC-AC-ACTS-E2E-219-modal-event-log-angka-success-per-tag-hardware-dan-unit-bypass | FE+BE |
| TC-AC-ACTS-945 | TC-AC-ACTS-E2E-221-modal-event-log-batch-seluruhnya-waiting-menulis-baris-success-0 | FE+BE |
| TC-AC-ACTS-946 | TC-AC-ACTS-E2E-077-absence-add-stock-bypass-seluruh-batch-preview-read-only-dan-remove-tanpa-tulis | FE+BE |
| TC-AC-ACTS-947 | TC-AC-ACTS-E2E-150-absence-log-audit-tanpa-perubahan-dan-delete-tanpa-entri-event-log-tag-log | FE+BE |
| TC-AC-ACTS-948 | TC-AC-ACTS-E2E-130-audit-rfid-scan-kode-belum-terdaftar-bukan-eligible-dan-format-tidak-valid | FE+BE |
| TC-AC-ACTS-949 | TC-AC-ACTS-E2E-130-audit-rfid-scan-kode-belum-terdaftar-bukan-eligible-dan-format-tidak-valid | FE+BE |
| TC-AC-ACTS-950 | TC-AC-ACTS-E2E-130-audit-rfid-scan-kode-belum-terdaftar-bukan-eligible-dan-format-tidak-valid | FE+BE |
| TC-AC-ACTS-951 | TC-AC-ACTS-E2E-134-audit-nfc-start-scan-tanpa-reader-d06-leave-cancel-dan-scan-uid-belum-terdaftar | FE+BE |
| TC-AC-ACTS-952 | TC-AC-ACTS-E2E-115-popup-tag-log-row-action-header-per-tag-type-dan-urutan-kronologis | FE+BE |
| TC-AC-ACTS-953 | TC-AC-ACTS-E2E-115-popup-tag-log-row-action-header-per-tag-type-dan-urutan-kronologis | FE+BE |
| TC-AC-ACTS-954 | TC-AC-ACTS-E2E-115-popup-tag-log-row-action-header-per-tag-type-dan-urutan-kronologis | FE+BE |
| TC-AC-ACTS-955 | TC-AC-ACTS-E2E-115-popup-tag-log-row-action-header-per-tag-type-dan-urutan-kronologis | FE+BE |
| TC-AC-ACTS-956 | TC-AC-ACTS-E2E-116-popup-tag-log-format-tanggal-empty-state-read-only-gagal-muat-dan-scope-distributor | FE+BE |
| TC-AC-ACTS-957 | TC-AC-ACTS-E2E-116-popup-tag-log-format-tanggal-empty-state-read-only-gagal-muat-dan-scope-distributor | FE+BE |
| TC-AC-ACTS-958 | TC-AC-ACTS-E2E-116-popup-tag-log-format-tanggal-empty-state-read-only-gagal-muat-dan-scope-distributor | FE+BE |
| TC-AC-ACTS-959 | TC-AC-ACTS-E2E-116-popup-tag-log-format-tanggal-empty-state-read-only-gagal-muat-dan-scope-distributor | FE+BE |
| TC-AC-ACTS-960 | TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit | FE+BE |
| TC-AC-ACTS-961 | TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit | FE+BE |
| TC-AC-ACTS-962 | TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit | FE+BE |
| TC-AC-ACTS-963 | TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit | FE+BE |
| TC-AC-ACTS-964 | TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit | FE+BE |
| TC-AC-ACTS-965 | TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit | FE+BE |
| TC-AC-ACTS-966 | TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit | FE+BE |
| TC-AC-ACTS-967 | TC-AC-ACTS-E2E-118-popup-tag-log-entri-audit-verified-not-found-dilewati-dan-sibling-combined | FE+BE |
| TC-AC-ACTS-968 | TC-AC-ACTS-E2E-118-popup-tag-log-entri-audit-verified-not-found-dilewati-dan-sibling-combined | FE+BE |
| TC-AC-ACTS-969 | TC-AC-ACTS-E2E-118-popup-tag-log-entri-audit-verified-not-found-dilewati-dan-sibling-combined | FE+BE |
| TC-AC-ACTS-970 | TC-AC-ACTS-E2E-150-absence-log-audit-tanpa-perubahan-dan-delete-tanpa-entri-event-log-tag-log | FE+BE |
| TC-AC-ACTS-971 | TC-AC-ACTS-E2E-150-absence-log-audit-tanpa-perubahan-dan-delete-tanpa-entri-event-log-tag-log | FE+BE |
| TC-AC-ACTS-972 | TC-AC-ACTS-E2E-118-popup-tag-log-entri-audit-verified-not-found-dilewati-dan-sibling-combined | FE+BE |
| TC-AC-ACTS-973 | TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable | FE+BE |
| TC-AC-ACTS-974 | TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable | FE+BE |
| TC-AC-ACTS-975 | TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable | FE+BE |
| TC-AC-ACTS-976 | TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable | FE+BE |
| TC-AC-ACTS-977 | TC-AC-ACTS-E2E-151-absence-log-delete-by-scan-tanpa-penghapusan-usage-event-dan-status-synced | FE+BE |
| TC-AC-ACTS-978 | TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable | FE+BE |
| TC-AC-ACTS-979 | TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable | FE+BE |
| TC-AC-ACTS-980 | TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable | FE+BE |
| TC-AC-ACTS-981 | TC-AC-ACTS-E2E-266-resilience-add-stock-rfid-kegagalan-menulis-tag-log-membatalkan-transaksi | FE+BE |
| TC-AC-ACTS-982 | TC-AC-ACTS-E2E-116-popup-tag-log-format-tanggal-empty-state-read-only-gagal-muat-dan-scope-distributor | FE+BE |
| TC-AC-ACTS-983 | TC-AC-ACTS-E2E-036-role-matrix-read-only-dan-capability-parsial-aksi-tulis-hidden | FE+BE |
| TC-AC-ACTS-984 | TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval | FE+BE |
| TC-AC-ACTS-985 | TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval | FE+BE |
| TC-AC-ACTS-986 | TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval | FE+BE |
| TC-AC-ACTS-987 | TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval | FE+BE |
| TC-AC-ACTS-988 | TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval | FE+BE |
| TC-AC-ACTS-989 | TC-AC-ACTS-E2E-162-detail-sku-banner-waiting-for-approval-non-approver-distributor-dan-state-tabel | FE+BE |
| TC-AC-ACTS-990 | TC-AC-ACTS-E2E-162-detail-sku-banner-waiting-for-approval-non-approver-distributor-dan-state-tabel | FE+BE |
| TC-AC-ACTS-991 | TC-AC-ACTS-E2E-160-detail-sku-realtime-tab-available-opsi-filter-banner-dan-approval | FE+BE |
| TC-AC-ACTS-992 | TC-AC-ACTS-E2E-162-detail-sku-banner-waiting-for-approval-non-approver-distributor-dan-state-tabel | FE+BE |
| TC-AC-ACTS-993 | TC-AC-ACTS-E2E-162-detail-sku-banner-waiting-for-approval-non-approver-distributor-dan-state-tabel | FE+BE |
| TC-AC-ACTS-994 | TC-AC-ACTS-E2E-162-detail-sku-banner-waiting-for-approval-non-approver-distributor-dan-state-tabel | FE+BE |
| TC-AC-ACTS-995 | TC-AC-ACTS-E2E-267-detail-sku-banner-waiting-for-approval-hilang-tanpa-reload-setelah-reject-unit-terakhir | FE+BE |

## Catatan

- Semua spec `Mode: FE+BE`: modul tanpa folder `API/` tidak punya openapi atau LLD, sehingga mock tidak dapat memenuhi R-15 dan S-13.
- Kemampuan yang dinyatakan "disediakan tim FE/BE": simulator reader RFID/NFC/BLE dan Handheld Reader USB, pelaku kedua (Admin B, Principal pengubah toggle, Client), pemicu lintas modul, injeksi kegagalan BE, serta fixture `Fixture.tagStock` (`fixtures/tag-stock.json`, belum ada).
- Env var akun yang perlu didaftarkan tim FE di `spectra.config.ts` dan `.env.example`: `AC_AA_PASSWORD`, `AC_AA_CREATE_PASSWORD`, `AC_TC2_PASSWORD`, `AC_TS_CREATE_PASSWORD`, `AC_TS_UPDATE_PASSWORD`, `AC_TS_DELETE_PASSWORD`, `AC_TS_READ_PASSWORD`, `AC_DIST_ON_PASSWORD`, `AC_DIST_OFF_PASSWORD`, `AC_DIST_NOROLE_PASSWORD`, `AC_DIST_SUSP_PASSWORD`, `AC_ROLELAIN_PASSWORD`, `AC_PARTNER_PASSWORD`, `AC_CLIENT_PASSWORD`.
- Spec melewati ~35 langkah: 99 spec; alasan tertulis di Notes tiap spec (satu kelas harness dan satu dataset, atau idiom 8b butir 7 untuk langkah berulang per kolom/permukaan).
- Penempatan TC berkelas harness: pagination volume 101 baris atau lebih di spec 242 (TC 919), 262 (TC 66, 417, 463), dan 263 (TC 509, 602, 646); volume 1.001 TAG di spec 264 (TC 732); isi sel berkas (kelas f) di spec 037, 260, dan 265 (TC 424, 470, 653); resilience kegagalan penulisan TAG Log di spec 266 (TC 981); banner Waiting for Approval hilang setelah Reject di spec 267 (TC 995; pasangan TC 991 di spec 160). Role Matrix: TC 136 (negatif) di spec 033 dan TC 128 (positif) di spec 034.
- Temuan untuk QA (TC sumber ambigu atau saling bertentangan) ditulis di Notes tiap spec. Yang paling berdampak: jumlah TC di registri (814) lebih sedikit dari TC aktual; TC 56 vs 51/853 (field `SKU` Filter Panel); TC 821 vs 835/858 (log Delete by Scan); TC 312 vs 948 (toast TAG tak terdaftar); TC 868–876 dan 880–886 (baris Waiting pada Total Control yang bypass, TC 181/734); email Total Control di Pre-setup berbeda dari `.env.example`.
