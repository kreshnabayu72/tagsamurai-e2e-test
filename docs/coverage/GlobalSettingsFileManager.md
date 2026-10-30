# Coverage E2E — Global Settings > File Manager

Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md` (289 TC, ID `TC-GS-FILEMGR-1`–`289`; 289 aktif, 0 retired). Suite: `specs/GlobalSettings/FileManager/`. Prefix: `GS` + `FILEMGR` (`TC-GS-FILEMGR-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 289 TC aktif masuk spec, 0 TC hanya-BE (`tc-file-manager-backend.md` memakai ID `BE-n` terpisah yang tidak merujuk ID granular; TC request langsung 248 sampai 252 dan 282 tetap di E2E, spec 071). 71 spec. Setiap TC terpetakan ke tepat satu spec (diverifikasi lewat `sourceTc`: 289 unik, tanpa duplikat, tanpa yang hilang).

Keputusan rencana (disetujui user): D-1 opsi B (klausa absence log memakai baseline jumlah entri di spec asal, tanpa spec absence tambahan), D-2 TC request langsung tetap di E2E, D-3 Setup Column dan Guided Tooltip mengikuti pola Brand (049 dan 051 mock, 050 FE+BE, 069 mock), D-4 TC-267 dan TC-284 di spec mobile 012.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-FILEMGR-E2E-001-screening-tabel-utama-layout-urutan-default-dan-tooltip | Screening Tabel Utama File Manager: Layout, Urutan Default, Row Action, dan Tooltip | FE+BE | 36 | 1, 2, 9, 10, 11 |
| TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link | Isi Sel Tabel Utama: File Format, Nama User, Format Size, Nama Panjang, dan Link File Name | FE+BE | 46 | 3, 4, 5, 6, 7, 8 |
| TC-GS-FILEMGR-E2E-003-empty-state-semua-surface-client-tanpa-data | Empty State Tabel Utama, Recycle Bin, Changelog, dan Kartu Storage Usage pada Client Tanpa Data | FE+BE | 24 | 12, 23, 30, 272 |
| TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | Resilience Baca: Loading, Error Load, dan Try Again pada Tabel, Recycle Bin, Changelog, dan Kartu Storage | FE+BE | 54 | 14, 15, 25, 32, 277, 278, 279 |
| TC-GS-FILEMGR-E2E-005-role-matrix-visibilitas-menu-dan-akses-url | Role Matrix: Visibilitas Menu File Manager dan Akses URL Langsung per Role | FE+BE | 13 | 40, 41, 42 |
| TC-GS-FILEMGR-E2E-006-role-matrix-visibilitas-kontrol-per-role | Role Matrix: Visibilitas Kontrol Tabel Utama, Recycle Bin, dan Kartu Storage per Role | FE+BE | 81 | 43, 44, 45, 46, 280 |
| TC-GS-FILEMGR-E2E-007-role-matrix-positif-download-delete-dan-permanently-delete | Role Matrix Positif: Download, Delete, dan Permanently Delete per Capability | FE+BE | 36 | 47, 200, 289 |
| TC-GS-FILEMGR-E2E-008-capability-dicabut-saat-halaman-terbuka | Capability Delete Dicabut Saat Halaman Masih Terbuka | FE+BE | 17 | 254 |
| TC-GS-FILEMGR-E2E-009-buka-file-tab-baru-dan-download-file-gambar | Buka File di Tab Baru dan Download File Gambar dari Row Action | FE+BE | 26 | 48, 50, 55 |
| TC-GS-FILEMGR-E2E-010-mobile-file-preview-bottom-sheet | Mobile: File Preview Bottom Sheet (Dimensions, Loading, Download, Tutup) | FE+BE (mobile) | 26 | 49, 51, 54, 58 |
| TC-GS-FILEMGR-E2E-011-mobile-resilience-preview-dan-download-gagal | Mobile Resilience: Gagal Memuat Gambar Preview dan Download dari Preview Gagal | FE+BE (mobile) | 18 | 52, 59 |
| TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip | Mobile: Kartu File, Recycle Bin Bottom Sheet, Kartu Storage Usage, Tanpa Bulk, dan Guided Tooltip | FE+BE (mobile) | 40 | 259, 260, 261, 267, 284 |
| TC-GS-FILEMGR-E2E-013-delete-single-dialog-screening-cancel-dan-esc | Dialog Delete Single: Screening, Cancel, Backdrop, dan Esc | FE+BE | 37 | 60, 61, 62, 63 |
| TC-GS-FILEMGR-E2E-014-delete-single-sukses-toast-dan-klik-ganda | Delete Single Berhasil: Foto Aktif, Toast Otomatis Hilang, dan Klik Ganda | FE+BE | 28 | 64, 65, 69 |
| TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | Resilience Tulis: Delete Single, Bulk Delete, Permanently Delete, Storage Tidak Terjangkau, dan Ganti Foto Gagal | FE+BE | 72 | 66, 67, 86, 92, 93, 102, 108 |
| TC-GS-FILEMGR-E2E-016-resilience-download-gagal | Resilience Download: Kegagalan Download File, Changelog, Tabel Utama, dan Recycle Bin | FE+BE | 43 | 56, 173, 196, 222 |
| TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi | Bulk Action Bar Tabel Utama: Counter, Checkbox Header, Select All, dan Retensi Seleksi | FE+BE | 56 | 71, 72, 73, 74, 77, 78 |
| TC-GS-FILEMGR-E2E-018-selection-limit-tabel-utama-dan-recycle-bin | Selection Limit: Checkbox Diblokir, Select All di-cap, dan Kosongkan Recycle Bin Beberapa Putaran | FE+BE | 28 | 75, 76, 104 |
| TC-GS-FILEMGR-E2E-019-bulk-delete-dialog-screening-cancel | Dialog Bulk Delete: Screening Homogen dan Campuran, Satu Baris, dan Cancel | FE+BE | 48 | 79, 80, 81, 83, 87 |
| TC-GS-FILEMGR-E2E-020-bulk-delete-sukses-dan-halaman-terakhir | Bulk Delete Berhasil: Campuran, Seleksi Direset, dan Pindah ke Halaman Terakhir | FE+BE | 35 | 82, 84, 153 |
| TC-GS-FILEMGR-E2E-021-bulk-delete-volume-1001-baris | Bulk Delete dan Bulk Permanently Delete dengan 1.001 Baris Terseleksi | FE+BE | 17 | 88, 105 |
| TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel | Dialog Permanently Delete Single dan Bulk: Screening, Satu Baris, Cancel, dan Bulk Action Bar Recycle Bin | FE+BE | 39 | 89, 91, 96, 97, 98, 99 |
| TC-GS-FILEMGR-E2E-023-permanently-delete-sukses-bulk-dan-kosongkan-recycle-bin | Permanently Delete Berhasil: Single, Klik Ganda, Bulk, dan Kosongkan Recycle Bin | FE+BE | 35 | 90, 95, 100, 103 |
| TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | Konflik File Tidak Tersedia: Buka, Download, Delete Single, dan Bulk Delete Setelah Diproses Pihak Lain | FE+BE | 66 | 53, 57, 68, 70, 85, 258, 263 |
| TC-GS-FILEMGR-E2E-025-konflik-file-tidak-tersedia-permanently-delete | Konflik File Tidak Tersedia: Permanently Delete Single dan Bulk Setelah Diproses Pihak Lain | FE+BE | 35 | 94, 101, 264 |
| TC-GS-FILEMGR-E2E-026-konflik-dua-admin-delete-dan-permanently-delete | Konflik Dua Admin: Delete dan Permanently Delete File yang Sama Bersamaan | FE+BE | 27 | 255, 256 |
| TC-GS-FILEMGR-E2E-027-auto-transition-ganti-dan-hapus-foto-profil | Auto-Transition: Ganti dan Hapus Foto Profil (User, My Profile, Non-Login User) Memindahkan Foto Lama ke Recycle Bin | FE+BE | 47 | 106, 107, 239, 240, 265 |
| TC-GS-FILEMGR-E2E-028-cascade-purge-delete-user-dan-non-login-user | Cascade Purge: Delete User dan Non-Login User Menghapus Permanen Seluruh File | FE+BE | 37 | 109, 110, 241, 287 |
| TC-GS-FILEMGR-E2E-029-retensi-teks-info-dan-auto-purge-in-recycle-bin | Retensi Recycle Bin: Teks Info dan Kolom Auto-Purge In Mengikuti Lifecycle Settings | FE+BE | 38 | 17, 19, 20, 21, 262 |
| TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry | Auto-Purge Job: Batas Retensi Inklusif, Floor 48 Jam, Retry, dan Balapan dengan Permanently Delete | FE+BE | 63 | 22, 111, 112, 114, 257 |
| TC-GS-FILEMGR-E2E-031-search-tabel-utama | Search Tabel Utama: Siklus Toolbar, Substring, Case-Insensitive, Size, Trim, dan Karakter Khusus | FE+BE | 58 | 13, 115, 116, 117, 119, 120 |
| TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | Filter Panel Tabel Utama: Screening, Opsi Dropdown, Chip, Indikator, dan Opsi Setelah File JPEG Dihapus | FE+BE | 59 | 122, 123, 124, 135, 136, 137, 138, 142 |
| TC-GS-FILEMGR-E2E-033-filter-nilai-size-upload-date-dan-logika-and-or | Filter Tabel Utama: Multi-Select OR, Rentang Size, Rentang Upload Date, dan Logika AND | FE+BE | 56 | 125, 126, 127, 128 |
| TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | Kombinasi Search, Filter, dan Sort Tabel Utama: Irisan, Independensi Clear, Reset Halaman, dan Pemulihan Empty State | FE+BE | 65 | 129, 130, 131, 132, 133, 140, 141 |
| TC-GS-FILEMGR-E2E-035-sort-tabel-utama | Sort Tabel Utama: Siklus 3 Tahap, Nama Lengkap, Nilai Byte, Perpindahan Kolom, dan Tie-Breaker | FE+BE | 59 | 143, 144, 145, 146, 147, 148 |
| TC-GS-FILEMGR-E2E-036-pagination-dan-retensi-state-tabel-utama | Pagination Tabel Utama dan Retensi State setelah Refresh, Tab Baru, dan Logout | FE+BE | 47 | 150, 151, 152, 154, 155 |
| TC-GS-FILEMGR-E2E-037-lintas-surface-search-tanggal-visibilitas-filter-dan-ikon-sort | Lintas Tiga Surface: Search Kolom Tanggal, Search Terikat Visibilitas Kolom, Filter Tanpa Apply, Search Dropdown Filter, dan Ikon Sort | FE+BE | 77 | 118, 121, 134, 139, 149 |
| TC-GS-FILEMGR-E2E-038-screening-recycle-bin-urutan-default-dan-tutup | Screening Modal Recycle Bin: Layout, Urutan Default, Tutup Modal, dan Tooltip | FE+BE | 34 | 16, 18, 26, 27 |
| TC-GS-FILEMGR-E2E-039-search-recycle-bin | Search Modal Recycle Bin: Siklus Toolbar, Substring Kolom, dan Size | FE+BE | 34 | 24, 201, 202, 203 |
| TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika | Filter Modal Recycle Bin: Panel, Opsi Dropdown, OR, Rentang Size, Rentang Deleted Date, dan AND | FE+BE | 38 | 204, 205, 206, 207, 208, 209 |
| TC-GS-FILEMGR-E2E-041-kombinasi-search-filter-recycle-bin | Kombinasi Search dan Filter Modal Recycle Bin: Irisan Simetris dan Independensi Clear | FE+BE | 27 | 210, 211, 212 |
| TC-GS-FILEMGR-E2E-042-sort-recycle-bin | Sort Modal Recycle Bin: File Name, File Format, Nama Lengkap, Size, Deleted Date, dan Auto-Purge In | FE+BE | 33 | 213, 214, 215, 216, 217 |
| TC-GS-FILEMGR-E2E-043-pagination-dan-buka-ulang-recycle-bin-dan-changelog | Pagination dan Reset ke Default Saat Dibuka Ulang pada Modal Recycle Bin dan Changelog | FE+BE | 36 | 218, 219 |
| TC-GS-FILEMGR-E2E-044-screening-changelog-format-sel-dan-tutup | Screening Modal Changelog: Layout, Format Sel Modified By dan Action, Tooltip, dan Tutup Modal | FE+BE | 30 | 28, 29, 33, 174 |
| TC-GS-FILEMGR-E2E-045-search-changelog | Search Modal Changelog: Siklus Toolbar, Substring Seluruh Kolom, dan Empty Hasil | FE+BE | 34 | 31, 156, 157 |
| TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | Filter Modal Changelog: Panel, Tanpa Field Field, Opsi Dropdown, Multi-Select, Rentang Date, dan AND | FE+BE | 48 | 158, 159, 160, 161, 162, 163, 266 |
| TC-GS-FILEMGR-E2E-047-kombinasi-search-filter-changelog | Kombinasi Search dan Filter Modal Changelog: Irisan, Independensi Clear, dan Pemulihan Empty State | FE+BE | 33 | 164, 165, 166, 167 |
| TC-GS-FILEMGR-E2E-048-sort-changelog | Sort Modal Changelog: Date, Action, File Name, Old Value, Modified By, dan Kolom Bernilai Sama | FE+BE | 31 | 168, 169, 170, 171 |
| TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | Setup Column Tiga Surface: Screening Overlay dan Popup, Tutup Tanpa Save, dan Guard Kolom Terakhir | mock | 52 | 175, 176, 177, 178, 179, 180, 186, 187 |
| TC-GS-FILEMGR-E2E-050-setup-column-hide-reorder-isolasi-dan-persistensi | Setup Column Tiga Surface: Hide, Reorder, Isolasi Antar Tabel, dan Persistensi setelah Refresh dan Logout | FE+BE | 42 | 181, 182, 188, 189 |
| TC-GS-FILEMGR-E2E-051-setup-column-pin-dan-reset | Setup Column Tiga Surface: Pin, Unpin, Batas Tiga Pin, dan Reset to Default | mock | 42 | 183, 184, 185 |
| TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | Download Tabel Utama dan Export Lintas Surface: Isi File CSV dan XLSX, Nama File, dan Kolom Tersembunyi | FE+BE | 62 | 190, 191, 192, 193, 194, 195, 198, 199 |
| TC-GS-FILEMGR-E2E-053-download-recycle-bin-dan-changelog-isi-file | Download Recycle Bin dan Changelog: Isi File Mengikuti Search, Filter, dan Visibilitas Kolom | FE+BE | 19 | 172, 220, 221 |
| TC-GS-FILEMGR-E2E-054-download-tabel-utama-lebih-5000-baris | Download Tabel Utama dengan 5.001 Baris | FE+BE | 6 | 197 |
| TC-GS-FILEMGR-E2E-055-log-permanently-delete-tiga-surface | Pencatatan Log Permanently Delete Single dan Bulk di Changelog File Manager, System Log, dan Activity Log | FE+BE | 39 | 223, 224, 234 |
| TC-GS-FILEMGR-E2E-056-log-delete-single-dan-foto-profil-aktif | Pencatatan Log Delete Single: Tiga Surface, Entri Photo pada Changelog User, dan File Bukan Foto Aktif | FE+BE | 31 | 225, 226, 227 |
| TC-GS-FILEMGR-E2E-057-log-auto-transition-dan-auto-purge-aktor-system | Pencatatan Log Auto-Transition dan Auto-Purge: Aktor System dan Aktor Pengguna Pelaku | FE+BE | 20 | 228, 229, 230 |
| TC-GS-FILEMGR-E2E-058-log-snapshot-nama-aktor-dan-delete-user | Pencatatan Log: Snapshot Nama Aktor setelah Rename dan Hapus Akun, serta Entri Delete User | FE+BE | 18 | 231, 232, 233 |
| TC-GS-FILEMGR-E2E-059-format-tanggal-general-settings | Format Tanggal dan Waktu General Settings pada Upload Date, Deleted Date, Date Changelog, dan Input Filter | FE+BE | 22 | 235, 236, 237 |
| TC-GS-FILEMGR-E2E-060-sync-detail-user-foto-kosong-dan-import-tanpa-file | Sinkronisasi: Detail User Foto Kosong setelah Delete dan Import Tidak Menyimpan File ke File Manager | FE+BE | 16 | 238, 242 |
| TC-GS-FILEMGR-E2E-061-plan-tier-tidak-digate | File Manager Identik pada Seluruh Tier Plan | FE+BE | 10 | 243 |
| TC-GS-FILEMGR-E2E-062-tenant-write-lockdown-suspended-expired | State Tenant: Aksi Tulis Ditolak saat Client Suspended atau Expired | FE+BE | 38 | 244, 245, 246 |
| TC-GS-FILEMGR-E2E-063-tenant-baca-tetap-tersedia | State Tenant: Aksi Baca File Manager dan Kartu Storage Tetap Tersedia saat Suspended atau Expired | FE+BE | 14 | 247, 283 |
| TC-GS-FILEMGR-E2E-064-tenant-suspended-job-latar | State Tenant: Auto-Purge dan Cascade Purge Tetap Berjalan saat Client Suspended | FE+BE | 19 | 113, 288 |
| TC-GS-FILEMGR-E2E-065-storage-screening-urutan-format-dan-baris-app | Kartu Storage Usage: Screening, Urutan Daftar App, Format Angka, dan Baris App Tanpa Aksi | FE+BE | 31 | 268, 269, 270, 286 |
| TC-GS-FILEMGR-E2E-066-storage-state-laporan-kuota-dan-batas-persentase | Kartu Storage Usage: Laporan Terlama, Kuota Belum Dialokasikan, Melewati Kuota, dan Batas Persentase | FE+BE | 30 | 271, 273, 274, 275 |
| TC-GS-FILEMGR-E2E-067-storage-perubahan-laporan-dan-topup-kuota | Kartu Storage Usage: Perubahan Angka Menunggu Laporan App Berikutnya dan Top-Up Kuota | FE+BE | 21 | 276, 285 |
| TC-GS-FILEMGR-E2E-068-storage-isolasi-client | Kartu Storage Usage Hanya Memuat Data Client Aktif | FE+BE | 8 | 281 |
| TC-GS-FILEMGR-E2E-069-guided-tooltip-konten-navigasi-keyboard | Guided Tooltip File Manager: Konten Step, Siklus Back, Next, Done, Skip, dan Keyboard | mock | 37 | 34, 37, 39 |
| TC-GS-FILEMGR-E2E-070-guided-tooltip-flag-seen-replay-dan-navigasi-keluar | Guided Tooltip File Manager: Flag Seen, Replay, dan Keluar lewat Navigasi | FE+BE | 24 | 35, 36, 38 |
| TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | Defense-in-Depth: Request Langsung Tanpa Capability, Isolasi ID Client Lain, dan Nama File Berisi Markup | FE+BE | 44 | 248, 249, 250, 251, 252, 253, 282 |

TC hanya-BE: tidak ada.

## Pembagian TC lintas spec

- **Isi file export** tabel utama (ekstensi, encoding, nama file, isi CSV/XLSX) ada di spec `052`; spec `053` memuat download Recycle Bin dan Changelog (TC-220, 221, 172) dan merujuk spec `052`; kegagalan download Recycle Bin dan Changelog ada di spec `016`.
- **Setup Column**: spec `049` (screening tiga surface, mock) merujuk spec `050` (hide, reorder, isolasi, persistensi) dan spec `051` (pin dan Reset to Default).
- **Guided Tooltip**: konten dan navigasi keyboard di spec `069` (mock); flag seen, replay, dan navigasi keluar di spec `070`; Guided Tooltip mobile (TC-267) dan kartu Storage mobile (TC-284) di spec `012`.
- **Kartu Storage Usage**: isi dan screening di spec `065` sampai `067` (TC-01 butir a.iii merujuk ke sini dari spec `001`).
- **TC-200** (download oleh role Read Only dan Manage files: Read): isi berkas tidak diasersi di spec `007`, diuji di spec `052`.
- **TC-287, 288, 289** ada di Section 1e TC (Kartu Storage Usage) tetapi dipetakan menurut topik (spec 028, 065, 007).
- **Asersi absence log (D-1 opsi B)**: klausa "tidak ada entri" pada TC fungsional (TC-22, 68, 85, 92, 94, 101, 109, 244, 245, 248, 249, 254, 263, 264, 288) tetap di spec asal dengan baseline jumlah entri sebelum aksi.

## Spec di atas sekitar 35 langkah


35 dari 71 spec melewati ±35 langkah (jumlah langkah tertulis; spec 049 sampai 051 dan 031 sampai 037 jauh lebih panjang setelah ekspansi). Alasan tiap spec ada di `## Notes` masing-masing: satu kelas harness, satu dataset, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.

| Spec | Langkah |
|---|:---:|
| TC-GS-FILEMGR-E2E-001-screening-tabel-utama-layout-urutan-default-dan-tooltip | 36 |
| TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link | 46 |
| TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | 54 |
| TC-GS-FILEMGR-E2E-006-role-matrix-visibilitas-kontrol-per-role | 81 |
| TC-GS-FILEMGR-E2E-007-role-matrix-positif-download-delete-dan-permanently-delete | 36 |
| TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip | 40 |
| TC-GS-FILEMGR-E2E-013-delete-single-dialog-screening-cancel-dan-esc | 37 |
| TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | 72 |
| TC-GS-FILEMGR-E2E-016-resilience-download-gagal | 43 |
| TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi | 56 |
| TC-GS-FILEMGR-E2E-019-bulk-delete-dialog-screening-cancel | 48 |
| TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel | 39 |
| TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | 66 |
| TC-GS-FILEMGR-E2E-027-auto-transition-ganti-dan-hapus-foto-profil | 47 |
| TC-GS-FILEMGR-E2E-028-cascade-purge-delete-user-dan-non-login-user | 37 |
| TC-GS-FILEMGR-E2E-029-retensi-teks-info-dan-auto-purge-in-recycle-bin | 38 |
| TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry | 63 |
| TC-GS-FILEMGR-E2E-031-search-tabel-utama | 58 |
| TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | 59 |
| TC-GS-FILEMGR-E2E-033-filter-nilai-size-upload-date-dan-logika-and-or | 56 |
| TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | 65 |
| TC-GS-FILEMGR-E2E-035-sort-tabel-utama | 59 |
| TC-GS-FILEMGR-E2E-036-pagination-dan-retensi-state-tabel-utama | 47 |
| TC-GS-FILEMGR-E2E-037-lintas-surface-search-tanggal-visibilitas-filter-dan-ikon-sort | 77 |
| TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika | 38 |
| TC-GS-FILEMGR-E2E-043-pagination-dan-buka-ulang-recycle-bin-dan-changelog | 36 |
| TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | 48 |
| TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | 52 |
| TC-GS-FILEMGR-E2E-050-setup-column-hide-reorder-isolasi-dan-persistensi | 42 |
| TC-GS-FILEMGR-E2E-051-setup-column-pin-dan-reset | 42 |
| TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | 62 |
| TC-GS-FILEMGR-E2E-055-log-permanently-delete-tiga-surface | 39 |
| TC-GS-FILEMGR-E2E-062-tenant-write-lockdown-suspended-expired | 38 |
| TC-GS-FILEMGR-E2E-069-guided-tooltip-konten-navigasi-keyboard | 37 |
| TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | 44 |

## Kebutuhan lingkungan (tim FE)

- Env var password didaftarkan di `spectra.config.ts` dan `.env.example`: `GS_TC_PASSWORD`, `GS_RO_PASSWORD`, `GS_FILES_READ_PASSWORD`, `GS_FILES_DELETE_PASSWORD`, `GS_NOACCESS_PASSWORD`, `GS_FILES_DELETE_CLONE_PASSWORD`, `GS_TC_EMPTY_PASSWORD`. Nilainya diisi tim FE; konfirmasi bahwa `GS_TC_PASSWORD` berlaku untuk akun `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (aktor Sinta Maharani) dan bahwa akun klon spec 008 serta akun client tanpa data (spec 003) tersedia.
- Fixture: `fixtures/file-manager.json` (identitas Tabel A2 sampai A5 dan D01 sampai D11, tanpa password/token) dibuat pada tahap script.
- Data Pre-setup: Tabel A2 (33 file aktif), A3 (16 baris Recycle Bin), A4 (14 entri Changelog), A5 (laporan Storage S1 sampai S10); data dinamis D05 sampai D10 bersufiks `{runId}-<NNN>`.
- Kemampuan teknis: seed file, Recycle Bin, dan Changelog idempotent per hook `before`; pemicu job auto-purge dan cascade purge (job dijeda atau jam dibekukan); penyimpanan file tidak terjangkau; laporan Storage dan kuota; ubah Lifecycle Settings, format tanggal, status Client, plan tier, dan capability role; client tanpa data; Android emulator (spec 010 sampai 012); membaca CSV/XLSX terunduh; klien HTTP; dua sesi; akun klon.
- Lihat `specs/GlobalSettings/FileManager/suite.md` untuk daftar state global yang dipulihkan dan hook Guided Tooltip.

## Temuan yang masih terbuka (Temuan untuk QA)

Tiap spec memuat daftar lengkap di `## Notes` bagian "Temuan untuk QA". Ringkasan pertanyaan sumber TC (Q-1 sampai Q-14 dari rencana) dan temuan baru penulis:

- **Q-1 TC-65**: "hilang otomatis setelah 4 detik" dengan pengamatan 6 detik; nilai hanya ada di `foundation/functions/toast-copy.md`, toleransi tidak didefinisikan (spec 014 mengasersi "sekitar 4 detik"). Perlu konfirmasi toleransi.
- **Q-2 TC-75, 76, 104**: "nilai terendah yang diizinkan" Selection Limit tidak diberi angka di TC; PRD Lifecycle Settings menetapkan rentang 100 sampai 5.000 (default 1.000), jadi `[Limit]` terendah = 100 > 32 dan dataset 33 baris tidak cukup: spec 018 men-seed baris tambahan (disediakan tim FE/BE). Dijawab; tidak ada keputusan terbuka (spec 017, 018).
- **Q-3 TC-19, 20, 21, 22, 111, 112**: `due-photo.png` (R04, sekarang − 31 hari) "tetap tampil sampai job auto-purge berikutnya" membuat hitungan 16 baris flaky bila job harian berjalan. Perlu keputusan: job dijeda di environment e2e atau jam dibekukan (spec 022, 023, 029, 030, 038 sampai 043, 057, 064).
- **Q-4 mekanisme "fixture BE"**: seeding Tabel A2 sampai A5, D05 sampai D10, laporan Storage, pemicu job auto-purge/cascade purge, dan storage tidak terjangkau tanpa endpoint/mekanisme di TC; semua ditulis "disediakan tim FE/BE" tanpa endpoint karangan (hampir semua spec). Spec mock 049 dan 051 tidak menyebut nama endpoint; tahap script melengkapinya dari `openapi.yaml`.
- **Q-5 TC-232, 233, 254 dan banyak TC lain**: TC mengubah/menghapus baris dan akun Pre-setup bersama (F01 sampai F05, R01 sampai R16, Sinta Maharani, Agus Wibowo), bertentangan dengan S-06; spec memakai file bersufiks dan akun klon milik spec yang disediakan tim FE. Nama pemilik klon literal belum terdaftar sebagai pengecualian S-12.
- **Q-6 TC-12, 23, 30, 272**: butuh client tanpa file, Recycle Bin kosong, Changelog kosong, dan tanpa laporan Storage; Pre-setup tidak menyebutnya (spec 003; client milik automation).
- **Q-7 hitungan "33 records"**: valid hanya bila tidak ada baris aktif lain (D05, D06, D08 menambah baris); suite serial dan dataset di-seed ulang per spec.
- **Q-8 "dihapus oleh proses lain"** (TC-53, 57, 68, 85, 94, 101, 255 sampai 257, 263, 264): pemicu tidak didefinisikan; ditulis sebagai fixture BE lewat sesi API (spec 024, 025).
- **Q-9 aksi di modul lain** (ganti/hapus foto di User, My Profile, Non-Login User, Import user, General Settings): langkah dan selektor tidak didefinisikan; ditandai "disediakan tim FE" (spec 013, 015, 020, 027, 052, 057, 060).
- **Q-10 TC-243**: daftar tier plan dan cara pindah tier tidak didefinisikan (spec 061).
- **Q-11 TC-231**: surface log pada entri Delete User tidak disebut; spec 058 mengasersi pada Changelog User dengan baseline jumlah.
- **Q-12 TC-282, 280**: TC-282 mencampur perilaku server dan UI; spec 071 mengasersi respons server saja, jalur UI toast belum punya TC.
- **Q-13 penempatan sumber**: TC-287, 288, 289 berada di Section 1e padahal isinya cascade purge dan Permanently Delete; dipetakan menurut topik. Catatan, bukan kesalahan.
- **Q-14 nilai turunan "PRD?"** (24 baris): nilai seperti `1.024 byte`, `44 days`, `100.0 MB`, `4.7 GB`, `60.0 GB` berasal dari Tabel Data Uji/fixture, bukan PRD; aritmetika diperiksa konsisten, tidak ada kontradiksi.

Temuan baru yang dicatat penulis spec:

- Spec 006: TC-44, 45, 46 menulis "File Preview terbuka dari klik File Name" dan "tutup modal preview" sedangkan PRD dan TC-48 menyatakan web tidak punya modal preview; TC-44/45 Expected b "Bulk Action Bar tidak tersedia" tanpa langkah pemicu.
- Spec 035 dan 042: tie-breaker "ID file" tidak tampil di UI dan tidak ditentukan di Tabel A2/A3 (TC-143 d/e, TC-148 b, TC-214 c/d).
- Spec 050: TC-182 Expected d (persisten setelah refresh) tidak punya langkah refresh; spec menambah F5. TC-189 "browser yang sama" bergantung penyimpanan preferensi di browser.
- Spec 051: TC-183 tidak menyebut viewport yang membuat tabel overflow horizontal; TC-185 precondition tanpa kolom/nilai konkret.
- Spec 049: TC-186 menutup popup Recycle Bin dengan Esc sedangkan surface lain dengan ikon X; TC-187 "tidak bisa di-uncheck" tanpa cara bukti selain disabled/tooltip.
- Spec 012: flag Guided Tooltip web dan Android mungkin dibagi per akun (TC-267); cara menutup walkthrough tidak disebut.
- Spec 070: cara menghapus dan membaca flag seen lewat API tidak didefinisikan (TC-35, 36, 38).
- Spec 005: TC-40/42 "halaman Global Settings mana pun" dan "URL halaman File Manager" tanpa nilai; TC-42 Expected b tidak merinci halaman setelah toast.
- Spec 024 dan 028: PRD tidak menetapkan batas atas jeda cascade purge; spec memakai batas harness 120 detik yang bukan dari TC.
- Spec 064: batas tunggu job tidak disebut TC; usulan 12 kali dengan jeda 5 detik.
- Spec 046: opsi Action filter Changelog bergantung pada Changelog seluruh client; bila spec lain menambah Action lain, asersi "tepat dua" tidak stabil.

## Disposisi pertanyaan sumber TC

Seluruh pertanyaan sumber di atas sudah diputuskan; tidak ada keputusan terbuka untuk spec e2e. Item yang menunggu perbaikan pemilik TC, PRD, konvensi, atau tim FE/BE dicatat sebagai temuan sumber dan tetap tertulis di `## Notes` bagian "Temuan untuk QA" tiap spec.

| Butir | Disposisi | Tindakan |
|---|---|---|
| Q-1 TC-65 toast 4 detik vs 6 detik | Nilai kanonik 4 detik (`foundation/functions/toast-copy.md`); 6 detik adalah jendela observasi | Spec 014 tetap mengasersi "sekitar 4 detik" |
| Q-2 TC-75, 76, 104 Selection Limit terendah | PRD Lifecycle Settings: rentang 100 sampai 5.000, default 1.000; terendah = 100 > 32 | Spec 018 men-seed baris tambahan; Notes spec 017 dan 018 memuat nilainya |
| Q-3 job auto-purge harian | Jeda job terjadwal di environment e2e dan picu manual lewat fixture; jam tidak dibekukan | Kebutuhan lingkungan tim BE/FE |
| Q-4, Q-8, Q-9, Q-10 mekanisme fixture, "dihapus proses lain", langkah modul lain, pindah tier | Tetap "disediakan tim FE/BE" tanpa endpoint karangan | Kebutuhan lingkungan |
| Q-5, Q-6 akun klon, file bersufiks, client kosong | Spec memakai akun klon dan file bersufiks | Pemilik konvensi menambah pengecualian S-06/S-12; tim FE menyediakan client kosong |
| Q-12 TC-282 | Spec 071 mengasersi respons server saja | Pemilik TC memecah TC-282 menjadi TC server dan TC toast UI |
| TC-44, 45, 46, 247 modal preview | PRD menang atas TC: web membuka tab baru | Spec 006 dan 063 menulis tab baru; pemilik TC memperbaiki TC-44/45/46/247 |
| Tie-breaker "ID file" TC-143, 148, 214 | Tidak terlihat di UI | Pemilik TC memakai kolom yang terlihat; spec mengikuti TC |
| TC-182 tanpa refresh, TC-183 tanpa viewport | Tambahan penulis dipertahankan (F5 per iterasi, viewport sebagai kemampuan teknis) | Pemilik TC melengkapi |
| Flag Guided Tooltip web dan Android | Spec 012 dan 070 menyetel dan memulihkan flag sendiri | BE mengonfirmasi apakah flag dibagi per akun |
| Spec 064 salinan `due-photo` 5 hari, bukan R04 31 hari | Dipertahankan agar job TC-113 tidak menghapusnya sebelum TC-288 | Dicatat di Notes spec 064 |

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-FILEMGR-1 | TC-GS-FILEMGR-E2E-001-screening-tabel-utama-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-FILEMGR-2 | TC-GS-FILEMGR-E2E-001-screening-tabel-utama-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-FILEMGR-3 | TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link | FE+BE |
| TC-GS-FILEMGR-4 | TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link | FE+BE |
| TC-GS-FILEMGR-5 | TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link | FE+BE |
| TC-GS-FILEMGR-6 | TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link | FE+BE |
| TC-GS-FILEMGR-7 | TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link | FE+BE |
| TC-GS-FILEMGR-8 | TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link | FE+BE |
| TC-GS-FILEMGR-9 | TC-GS-FILEMGR-E2E-001-screening-tabel-utama-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-FILEMGR-10 | TC-GS-FILEMGR-E2E-001-screening-tabel-utama-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-FILEMGR-11 | TC-GS-FILEMGR-E2E-001-screening-tabel-utama-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-FILEMGR-12 | TC-GS-FILEMGR-E2E-003-empty-state-semua-surface-client-tanpa-data | FE+BE |
| TC-GS-FILEMGR-13 | TC-GS-FILEMGR-E2E-031-search-tabel-utama | FE+BE |
| TC-GS-FILEMGR-14 | TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-FILEMGR-15 | TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-FILEMGR-16 | TC-GS-FILEMGR-E2E-038-screening-recycle-bin-urutan-default-dan-tutup | FE+BE |
| TC-GS-FILEMGR-17 | TC-GS-FILEMGR-E2E-029-retensi-teks-info-dan-auto-purge-in-recycle-bin | FE+BE |
| TC-GS-FILEMGR-18 | TC-GS-FILEMGR-E2E-038-screening-recycle-bin-urutan-default-dan-tutup | FE+BE |
| TC-GS-FILEMGR-19 | TC-GS-FILEMGR-E2E-029-retensi-teks-info-dan-auto-purge-in-recycle-bin | FE+BE |
| TC-GS-FILEMGR-20 | TC-GS-FILEMGR-E2E-029-retensi-teks-info-dan-auto-purge-in-recycle-bin | FE+BE |
| TC-GS-FILEMGR-21 | TC-GS-FILEMGR-E2E-029-retensi-teks-info-dan-auto-purge-in-recycle-bin | FE+BE |
| TC-GS-FILEMGR-22 | TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry | FE+BE |
| TC-GS-FILEMGR-23 | TC-GS-FILEMGR-E2E-003-empty-state-semua-surface-client-tanpa-data | FE+BE |
| TC-GS-FILEMGR-24 | TC-GS-FILEMGR-E2E-039-search-recycle-bin | FE+BE |
| TC-GS-FILEMGR-25 | TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-FILEMGR-26 | TC-GS-FILEMGR-E2E-038-screening-recycle-bin-urutan-default-dan-tutup | FE+BE |
| TC-GS-FILEMGR-27 | TC-GS-FILEMGR-E2E-038-screening-recycle-bin-urutan-default-dan-tutup | FE+BE |
| TC-GS-FILEMGR-28 | TC-GS-FILEMGR-E2E-044-screening-changelog-format-sel-dan-tutup | FE+BE |
| TC-GS-FILEMGR-29 | TC-GS-FILEMGR-E2E-044-screening-changelog-format-sel-dan-tutup | FE+BE |
| TC-GS-FILEMGR-30 | TC-GS-FILEMGR-E2E-003-empty-state-semua-surface-client-tanpa-data | FE+BE |
| TC-GS-FILEMGR-31 | TC-GS-FILEMGR-E2E-045-search-changelog | FE+BE |
| TC-GS-FILEMGR-32 | TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-FILEMGR-33 | TC-GS-FILEMGR-E2E-044-screening-changelog-format-sel-dan-tutup | FE+BE |
| TC-GS-FILEMGR-34 | TC-GS-FILEMGR-E2E-069-guided-tooltip-konten-navigasi-keyboard | mock |
| TC-GS-FILEMGR-35 | TC-GS-FILEMGR-E2E-070-guided-tooltip-flag-seen-replay-dan-navigasi-keluar | FE+BE |
| TC-GS-FILEMGR-36 | TC-GS-FILEMGR-E2E-070-guided-tooltip-flag-seen-replay-dan-navigasi-keluar | FE+BE |
| TC-GS-FILEMGR-37 | TC-GS-FILEMGR-E2E-069-guided-tooltip-konten-navigasi-keyboard | mock |
| TC-GS-FILEMGR-38 | TC-GS-FILEMGR-E2E-070-guided-tooltip-flag-seen-replay-dan-navigasi-keluar | FE+BE |
| TC-GS-FILEMGR-39 | TC-GS-FILEMGR-E2E-069-guided-tooltip-konten-navigasi-keyboard | mock |
| TC-GS-FILEMGR-40 | TC-GS-FILEMGR-E2E-005-role-matrix-visibilitas-menu-dan-akses-url | FE+BE |
| TC-GS-FILEMGR-41 | TC-GS-FILEMGR-E2E-005-role-matrix-visibilitas-menu-dan-akses-url | FE+BE |
| TC-GS-FILEMGR-42 | TC-GS-FILEMGR-E2E-005-role-matrix-visibilitas-menu-dan-akses-url | FE+BE |
| TC-GS-FILEMGR-43 | TC-GS-FILEMGR-E2E-006-role-matrix-visibilitas-kontrol-per-role | FE+BE |
| TC-GS-FILEMGR-44 | TC-GS-FILEMGR-E2E-006-role-matrix-visibilitas-kontrol-per-role | FE+BE |
| TC-GS-FILEMGR-45 | TC-GS-FILEMGR-E2E-006-role-matrix-visibilitas-kontrol-per-role | FE+BE |
| TC-GS-FILEMGR-46 | TC-GS-FILEMGR-E2E-006-role-matrix-visibilitas-kontrol-per-role | FE+BE |
| TC-GS-FILEMGR-47 | TC-GS-FILEMGR-E2E-007-role-matrix-positif-download-delete-dan-permanently-delete | FE+BE |
| TC-GS-FILEMGR-48 | TC-GS-FILEMGR-E2E-009-buka-file-tab-baru-dan-download-file-gambar | FE+BE |
| TC-GS-FILEMGR-49 | TC-GS-FILEMGR-E2E-010-mobile-file-preview-bottom-sheet | FE+BE (mobile) |
| TC-GS-FILEMGR-50 | TC-GS-FILEMGR-E2E-009-buka-file-tab-baru-dan-download-file-gambar | FE+BE |
| TC-GS-FILEMGR-51 | TC-GS-FILEMGR-E2E-010-mobile-file-preview-bottom-sheet | FE+BE (mobile) |
| TC-GS-FILEMGR-52 | TC-GS-FILEMGR-E2E-011-mobile-resilience-preview-dan-download-gagal | FE+BE (mobile) |
| TC-GS-FILEMGR-53 | TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | FE+BE |
| TC-GS-FILEMGR-54 | TC-GS-FILEMGR-E2E-010-mobile-file-preview-bottom-sheet | FE+BE (mobile) |
| TC-GS-FILEMGR-55 | TC-GS-FILEMGR-E2E-009-buka-file-tab-baru-dan-download-file-gambar | FE+BE |
| TC-GS-FILEMGR-56 | TC-GS-FILEMGR-E2E-016-resilience-download-gagal | FE+BE |
| TC-GS-FILEMGR-57 | TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | FE+BE |
| TC-GS-FILEMGR-58 | TC-GS-FILEMGR-E2E-010-mobile-file-preview-bottom-sheet | FE+BE (mobile) |
| TC-GS-FILEMGR-59 | TC-GS-FILEMGR-E2E-011-mobile-resilience-preview-dan-download-gagal | FE+BE (mobile) |
| TC-GS-FILEMGR-60 | TC-GS-FILEMGR-E2E-013-delete-single-dialog-screening-cancel-dan-esc | FE+BE |
| TC-GS-FILEMGR-61 | TC-GS-FILEMGR-E2E-013-delete-single-dialog-screening-cancel-dan-esc | FE+BE |
| TC-GS-FILEMGR-62 | TC-GS-FILEMGR-E2E-013-delete-single-dialog-screening-cancel-dan-esc | FE+BE |
| TC-GS-FILEMGR-63 | TC-GS-FILEMGR-E2E-013-delete-single-dialog-screening-cancel-dan-esc | FE+BE |
| TC-GS-FILEMGR-64 | TC-GS-FILEMGR-E2E-014-delete-single-sukses-toast-dan-klik-ganda | FE+BE |
| TC-GS-FILEMGR-65 | TC-GS-FILEMGR-E2E-014-delete-single-sukses-toast-dan-klik-ganda | FE+BE |
| TC-GS-FILEMGR-66 | TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | FE+BE |
| TC-GS-FILEMGR-67 | TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | FE+BE |
| TC-GS-FILEMGR-68 | TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | FE+BE |
| TC-GS-FILEMGR-69 | TC-GS-FILEMGR-E2E-014-delete-single-sukses-toast-dan-klik-ganda | FE+BE |
| TC-GS-FILEMGR-70 | TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | FE+BE |
| TC-GS-FILEMGR-71 | TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-FILEMGR-72 | TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-FILEMGR-73 | TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-FILEMGR-74 | TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-FILEMGR-75 | TC-GS-FILEMGR-E2E-018-selection-limit-tabel-utama-dan-recycle-bin | FE+BE |
| TC-GS-FILEMGR-76 | TC-GS-FILEMGR-E2E-018-selection-limit-tabel-utama-dan-recycle-bin | FE+BE |
| TC-GS-FILEMGR-77 | TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-FILEMGR-78 | TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-FILEMGR-79 | TC-GS-FILEMGR-E2E-019-bulk-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-80 | TC-GS-FILEMGR-E2E-019-bulk-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-81 | TC-GS-FILEMGR-E2E-019-bulk-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-82 | TC-GS-FILEMGR-E2E-020-bulk-delete-sukses-dan-halaman-terakhir | FE+BE |
| TC-GS-FILEMGR-83 | TC-GS-FILEMGR-E2E-019-bulk-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-84 | TC-GS-FILEMGR-E2E-020-bulk-delete-sukses-dan-halaman-terakhir | FE+BE |
| TC-GS-FILEMGR-85 | TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | FE+BE |
| TC-GS-FILEMGR-86 | TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | FE+BE |
| TC-GS-FILEMGR-87 | TC-GS-FILEMGR-E2E-019-bulk-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-88 | TC-GS-FILEMGR-E2E-021-bulk-delete-volume-1001-baris | FE+BE |
| TC-GS-FILEMGR-89 | TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-90 | TC-GS-FILEMGR-E2E-023-permanently-delete-sukses-bulk-dan-kosongkan-recycle-bin | FE+BE |
| TC-GS-FILEMGR-91 | TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-92 | TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | FE+BE |
| TC-GS-FILEMGR-93 | TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | FE+BE |
| TC-GS-FILEMGR-94 | TC-GS-FILEMGR-E2E-025-konflik-file-tidak-tersedia-permanently-delete | FE+BE |
| TC-GS-FILEMGR-95 | TC-GS-FILEMGR-E2E-023-permanently-delete-sukses-bulk-dan-kosongkan-recycle-bin | FE+BE |
| TC-GS-FILEMGR-96 | TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-97 | TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-98 | TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-99 | TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel | FE+BE |
| TC-GS-FILEMGR-100 | TC-GS-FILEMGR-E2E-023-permanently-delete-sukses-bulk-dan-kosongkan-recycle-bin | FE+BE |
| TC-GS-FILEMGR-101 | TC-GS-FILEMGR-E2E-025-konflik-file-tidak-tersedia-permanently-delete | FE+BE |
| TC-GS-FILEMGR-102 | TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | FE+BE |
| TC-GS-FILEMGR-103 | TC-GS-FILEMGR-E2E-023-permanently-delete-sukses-bulk-dan-kosongkan-recycle-bin | FE+BE |
| TC-GS-FILEMGR-104 | TC-GS-FILEMGR-E2E-018-selection-limit-tabel-utama-dan-recycle-bin | FE+BE |
| TC-GS-FILEMGR-105 | TC-GS-FILEMGR-E2E-021-bulk-delete-volume-1001-baris | FE+BE |
| TC-GS-FILEMGR-106 | TC-GS-FILEMGR-E2E-027-auto-transition-ganti-dan-hapus-foto-profil | FE+BE |
| TC-GS-FILEMGR-107 | TC-GS-FILEMGR-E2E-027-auto-transition-ganti-dan-hapus-foto-profil | FE+BE |
| TC-GS-FILEMGR-108 | TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto | FE+BE |
| TC-GS-FILEMGR-109 | TC-GS-FILEMGR-E2E-028-cascade-purge-delete-user-dan-non-login-user | FE+BE |
| TC-GS-FILEMGR-110 | TC-GS-FILEMGR-E2E-028-cascade-purge-delete-user-dan-non-login-user | FE+BE |
| TC-GS-FILEMGR-111 | TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry | FE+BE |
| TC-GS-FILEMGR-112 | TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry | FE+BE |
| TC-GS-FILEMGR-113 | TC-GS-FILEMGR-E2E-064-tenant-suspended-job-latar | FE+BE |
| TC-GS-FILEMGR-114 | TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry | FE+BE |
| TC-GS-FILEMGR-115 | TC-GS-FILEMGR-E2E-031-search-tabel-utama | FE+BE |
| TC-GS-FILEMGR-116 | TC-GS-FILEMGR-E2E-031-search-tabel-utama | FE+BE |
| TC-GS-FILEMGR-117 | TC-GS-FILEMGR-E2E-031-search-tabel-utama | FE+BE |
| TC-GS-FILEMGR-118 | TC-GS-FILEMGR-E2E-037-lintas-surface-search-tanggal-visibilitas-filter-dan-ikon-sort | FE+BE |
| TC-GS-FILEMGR-119 | TC-GS-FILEMGR-E2E-031-search-tabel-utama | FE+BE |
| TC-GS-FILEMGR-120 | TC-GS-FILEMGR-E2E-031-search-tabel-utama | FE+BE |
| TC-GS-FILEMGR-121 | TC-GS-FILEMGR-E2E-037-lintas-surface-search-tanggal-visibilitas-filter-dan-ikon-sort | FE+BE |
| TC-GS-FILEMGR-122 | TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | FE+BE |
| TC-GS-FILEMGR-123 | TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | FE+BE |
| TC-GS-FILEMGR-124 | TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | FE+BE |
| TC-GS-FILEMGR-125 | TC-GS-FILEMGR-E2E-033-filter-nilai-size-upload-date-dan-logika-and-or | FE+BE |
| TC-GS-FILEMGR-126 | TC-GS-FILEMGR-E2E-033-filter-nilai-size-upload-date-dan-logika-and-or | FE+BE |
| TC-GS-FILEMGR-127 | TC-GS-FILEMGR-E2E-033-filter-nilai-size-upload-date-dan-logika-and-or | FE+BE |
| TC-GS-FILEMGR-128 | TC-GS-FILEMGR-E2E-033-filter-nilai-size-upload-date-dan-logika-and-or | FE+BE |
| TC-GS-FILEMGR-129 | TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | FE+BE |
| TC-GS-FILEMGR-130 | TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | FE+BE |
| TC-GS-FILEMGR-131 | TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | FE+BE |
| TC-GS-FILEMGR-132 | TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | FE+BE |
| TC-GS-FILEMGR-133 | TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | FE+BE |
| TC-GS-FILEMGR-134 | TC-GS-FILEMGR-E2E-037-lintas-surface-search-tanggal-visibilitas-filter-dan-ikon-sort | FE+BE |
| TC-GS-FILEMGR-135 | TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | FE+BE |
| TC-GS-FILEMGR-136 | TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | FE+BE |
| TC-GS-FILEMGR-137 | TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | FE+BE |
| TC-GS-FILEMGR-138 | TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | FE+BE |
| TC-GS-FILEMGR-139 | TC-GS-FILEMGR-E2E-037-lintas-surface-search-tanggal-visibilitas-filter-dan-ikon-sort | FE+BE |
| TC-GS-FILEMGR-140 | TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | FE+BE |
| TC-GS-FILEMGR-141 | TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state | FE+BE |
| TC-GS-FILEMGR-142 | TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete | FE+BE |
| TC-GS-FILEMGR-143 | TC-GS-FILEMGR-E2E-035-sort-tabel-utama | FE+BE |
| TC-GS-FILEMGR-144 | TC-GS-FILEMGR-E2E-035-sort-tabel-utama | FE+BE |
| TC-GS-FILEMGR-145 | TC-GS-FILEMGR-E2E-035-sort-tabel-utama | FE+BE |
| TC-GS-FILEMGR-146 | TC-GS-FILEMGR-E2E-035-sort-tabel-utama | FE+BE |
| TC-GS-FILEMGR-147 | TC-GS-FILEMGR-E2E-035-sort-tabel-utama | FE+BE |
| TC-GS-FILEMGR-148 | TC-GS-FILEMGR-E2E-035-sort-tabel-utama | FE+BE |
| TC-GS-FILEMGR-149 | TC-GS-FILEMGR-E2E-037-lintas-surface-search-tanggal-visibilitas-filter-dan-ikon-sort | FE+BE |
| TC-GS-FILEMGR-150 | TC-GS-FILEMGR-E2E-036-pagination-dan-retensi-state-tabel-utama | FE+BE |
| TC-GS-FILEMGR-151 | TC-GS-FILEMGR-E2E-036-pagination-dan-retensi-state-tabel-utama | FE+BE |
| TC-GS-FILEMGR-152 | TC-GS-FILEMGR-E2E-036-pagination-dan-retensi-state-tabel-utama | FE+BE |
| TC-GS-FILEMGR-153 | TC-GS-FILEMGR-E2E-020-bulk-delete-sukses-dan-halaman-terakhir | FE+BE |
| TC-GS-FILEMGR-154 | TC-GS-FILEMGR-E2E-036-pagination-dan-retensi-state-tabel-utama | FE+BE |
| TC-GS-FILEMGR-155 | TC-GS-FILEMGR-E2E-036-pagination-dan-retensi-state-tabel-utama | FE+BE |
| TC-GS-FILEMGR-156 | TC-GS-FILEMGR-E2E-045-search-changelog | FE+BE |
| TC-GS-FILEMGR-157 | TC-GS-FILEMGR-E2E-045-search-changelog | FE+BE |
| TC-GS-FILEMGR-158 | TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | FE+BE |
| TC-GS-FILEMGR-159 | TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | FE+BE |
| TC-GS-FILEMGR-160 | TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | FE+BE |
| TC-GS-FILEMGR-161 | TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | FE+BE |
| TC-GS-FILEMGR-162 | TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | FE+BE |
| TC-GS-FILEMGR-163 | TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | FE+BE |
| TC-GS-FILEMGR-164 | TC-GS-FILEMGR-E2E-047-kombinasi-search-filter-changelog | FE+BE |
| TC-GS-FILEMGR-165 | TC-GS-FILEMGR-E2E-047-kombinasi-search-filter-changelog | FE+BE |
| TC-GS-FILEMGR-166 | TC-GS-FILEMGR-E2E-047-kombinasi-search-filter-changelog | FE+BE |
| TC-GS-FILEMGR-167 | TC-GS-FILEMGR-E2E-047-kombinasi-search-filter-changelog | FE+BE |
| TC-GS-FILEMGR-168 | TC-GS-FILEMGR-E2E-048-sort-changelog | FE+BE |
| TC-GS-FILEMGR-169 | TC-GS-FILEMGR-E2E-048-sort-changelog | FE+BE |
| TC-GS-FILEMGR-170 | TC-GS-FILEMGR-E2E-048-sort-changelog | FE+BE |
| TC-GS-FILEMGR-171 | TC-GS-FILEMGR-E2E-048-sort-changelog | FE+BE |
| TC-GS-FILEMGR-172 | TC-GS-FILEMGR-E2E-053-download-recycle-bin-dan-changelog-isi-file | FE+BE |
| TC-GS-FILEMGR-173 | TC-GS-FILEMGR-E2E-016-resilience-download-gagal | FE+BE |
| TC-GS-FILEMGR-174 | TC-GS-FILEMGR-E2E-044-screening-changelog-format-sel-dan-tutup | FE+BE |
| TC-GS-FILEMGR-175 | TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | mock |
| TC-GS-FILEMGR-176 | TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | mock |
| TC-GS-FILEMGR-177 | TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | mock |
| TC-GS-FILEMGR-178 | TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | mock |
| TC-GS-FILEMGR-179 | TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | mock |
| TC-GS-FILEMGR-180 | TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | mock |
| TC-GS-FILEMGR-181 | TC-GS-FILEMGR-E2E-050-setup-column-hide-reorder-isolasi-dan-persistensi | FE+BE |
| TC-GS-FILEMGR-182 | TC-GS-FILEMGR-E2E-050-setup-column-hide-reorder-isolasi-dan-persistensi | FE+BE |
| TC-GS-FILEMGR-183 | TC-GS-FILEMGR-E2E-051-setup-column-pin-dan-reset | mock |
| TC-GS-FILEMGR-184 | TC-GS-FILEMGR-E2E-051-setup-column-pin-dan-reset | mock |
| TC-GS-FILEMGR-185 | TC-GS-FILEMGR-E2E-051-setup-column-pin-dan-reset | mock |
| TC-GS-FILEMGR-186 | TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | mock |
| TC-GS-FILEMGR-187 | TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface | mock |
| TC-GS-FILEMGR-188 | TC-GS-FILEMGR-E2E-050-setup-column-hide-reorder-isolasi-dan-persistensi | FE+BE |
| TC-GS-FILEMGR-189 | TC-GS-FILEMGR-E2E-050-setup-column-hide-reorder-isolasi-dan-persistensi | FE+BE |
| TC-GS-FILEMGR-190 | TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | FE+BE |
| TC-GS-FILEMGR-191 | TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | FE+BE |
| TC-GS-FILEMGR-192 | TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | FE+BE |
| TC-GS-FILEMGR-193 | TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | FE+BE |
| TC-GS-FILEMGR-194 | TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | FE+BE |
| TC-GS-FILEMGR-195 | TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | FE+BE |
| TC-GS-FILEMGR-196 | TC-GS-FILEMGR-E2E-016-resilience-download-gagal | FE+BE |
| TC-GS-FILEMGR-197 | TC-GS-FILEMGR-E2E-054-download-tabel-utama-lebih-5000-baris | FE+BE |
| TC-GS-FILEMGR-198 | TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | FE+BE |
| TC-GS-FILEMGR-199 | TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx | FE+BE |
| TC-GS-FILEMGR-200 | TC-GS-FILEMGR-E2E-007-role-matrix-positif-download-delete-dan-permanently-delete | FE+BE |
| TC-GS-FILEMGR-201 | TC-GS-FILEMGR-E2E-039-search-recycle-bin | FE+BE |
| TC-GS-FILEMGR-202 | TC-GS-FILEMGR-E2E-039-search-recycle-bin | FE+BE |
| TC-GS-FILEMGR-203 | TC-GS-FILEMGR-E2E-039-search-recycle-bin | FE+BE |
| TC-GS-FILEMGR-204 | TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika | FE+BE |
| TC-GS-FILEMGR-205 | TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika | FE+BE |
| TC-GS-FILEMGR-206 | TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika | FE+BE |
| TC-GS-FILEMGR-207 | TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika | FE+BE |
| TC-GS-FILEMGR-208 | TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika | FE+BE |
| TC-GS-FILEMGR-209 | TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika | FE+BE |
| TC-GS-FILEMGR-210 | TC-GS-FILEMGR-E2E-041-kombinasi-search-filter-recycle-bin | FE+BE |
| TC-GS-FILEMGR-211 | TC-GS-FILEMGR-E2E-041-kombinasi-search-filter-recycle-bin | FE+BE |
| TC-GS-FILEMGR-212 | TC-GS-FILEMGR-E2E-041-kombinasi-search-filter-recycle-bin | FE+BE |
| TC-GS-FILEMGR-213 | TC-GS-FILEMGR-E2E-042-sort-recycle-bin | FE+BE |
| TC-GS-FILEMGR-214 | TC-GS-FILEMGR-E2E-042-sort-recycle-bin | FE+BE |
| TC-GS-FILEMGR-215 | TC-GS-FILEMGR-E2E-042-sort-recycle-bin | FE+BE |
| TC-GS-FILEMGR-216 | TC-GS-FILEMGR-E2E-042-sort-recycle-bin | FE+BE |
| TC-GS-FILEMGR-217 | TC-GS-FILEMGR-E2E-042-sort-recycle-bin | FE+BE |
| TC-GS-FILEMGR-218 | TC-GS-FILEMGR-E2E-043-pagination-dan-buka-ulang-recycle-bin-dan-changelog | FE+BE |
| TC-GS-FILEMGR-219 | TC-GS-FILEMGR-E2E-043-pagination-dan-buka-ulang-recycle-bin-dan-changelog | FE+BE |
| TC-GS-FILEMGR-220 | TC-GS-FILEMGR-E2E-053-download-recycle-bin-dan-changelog-isi-file | FE+BE |
| TC-GS-FILEMGR-221 | TC-GS-FILEMGR-E2E-053-download-recycle-bin-dan-changelog-isi-file | FE+BE |
| TC-GS-FILEMGR-222 | TC-GS-FILEMGR-E2E-016-resilience-download-gagal | FE+BE |
| TC-GS-FILEMGR-223 | TC-GS-FILEMGR-E2E-055-log-permanently-delete-tiga-surface | FE+BE |
| TC-GS-FILEMGR-224 | TC-GS-FILEMGR-E2E-055-log-permanently-delete-tiga-surface | FE+BE |
| TC-GS-FILEMGR-225 | TC-GS-FILEMGR-E2E-056-log-delete-single-dan-foto-profil-aktif | FE+BE |
| TC-GS-FILEMGR-226 | TC-GS-FILEMGR-E2E-056-log-delete-single-dan-foto-profil-aktif | FE+BE |
| TC-GS-FILEMGR-227 | TC-GS-FILEMGR-E2E-056-log-delete-single-dan-foto-profil-aktif | FE+BE |
| TC-GS-FILEMGR-228 | TC-GS-FILEMGR-E2E-057-log-auto-transition-dan-auto-purge-aktor-system | FE+BE |
| TC-GS-FILEMGR-229 | TC-GS-FILEMGR-E2E-057-log-auto-transition-dan-auto-purge-aktor-system | FE+BE |
| TC-GS-FILEMGR-230 | TC-GS-FILEMGR-E2E-057-log-auto-transition-dan-auto-purge-aktor-system | FE+BE |
| TC-GS-FILEMGR-231 | TC-GS-FILEMGR-E2E-058-log-snapshot-nama-aktor-dan-delete-user | FE+BE |
| TC-GS-FILEMGR-232 | TC-GS-FILEMGR-E2E-058-log-snapshot-nama-aktor-dan-delete-user | FE+BE |
| TC-GS-FILEMGR-233 | TC-GS-FILEMGR-E2E-058-log-snapshot-nama-aktor-dan-delete-user | FE+BE |
| TC-GS-FILEMGR-234 | TC-GS-FILEMGR-E2E-055-log-permanently-delete-tiga-surface | FE+BE |
| TC-GS-FILEMGR-235 | TC-GS-FILEMGR-E2E-059-format-tanggal-general-settings | FE+BE |
| TC-GS-FILEMGR-236 | TC-GS-FILEMGR-E2E-059-format-tanggal-general-settings | FE+BE |
| TC-GS-FILEMGR-237 | TC-GS-FILEMGR-E2E-059-format-tanggal-general-settings | FE+BE |
| TC-GS-FILEMGR-238 | TC-GS-FILEMGR-E2E-060-sync-detail-user-foto-kosong-dan-import-tanpa-file | FE+BE |
| TC-GS-FILEMGR-239 | TC-GS-FILEMGR-E2E-027-auto-transition-ganti-dan-hapus-foto-profil | FE+BE |
| TC-GS-FILEMGR-240 | TC-GS-FILEMGR-E2E-027-auto-transition-ganti-dan-hapus-foto-profil | FE+BE |
| TC-GS-FILEMGR-241 | TC-GS-FILEMGR-E2E-028-cascade-purge-delete-user-dan-non-login-user | FE+BE |
| TC-GS-FILEMGR-242 | TC-GS-FILEMGR-E2E-060-sync-detail-user-foto-kosong-dan-import-tanpa-file | FE+BE |
| TC-GS-FILEMGR-243 | TC-GS-FILEMGR-E2E-061-plan-tier-tidak-digate | FE+BE |
| TC-GS-FILEMGR-244 | TC-GS-FILEMGR-E2E-062-tenant-write-lockdown-suspended-expired | FE+BE |
| TC-GS-FILEMGR-245 | TC-GS-FILEMGR-E2E-062-tenant-write-lockdown-suspended-expired | FE+BE |
| TC-GS-FILEMGR-246 | TC-GS-FILEMGR-E2E-062-tenant-write-lockdown-suspended-expired | FE+BE |
| TC-GS-FILEMGR-247 | TC-GS-FILEMGR-E2E-063-tenant-baca-tetap-tersedia | FE+BE |
| TC-GS-FILEMGR-248 | TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | FE+BE |
| TC-GS-FILEMGR-249 | TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | FE+BE |
| TC-GS-FILEMGR-250 | TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | FE+BE |
| TC-GS-FILEMGR-251 | TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | FE+BE |
| TC-GS-FILEMGR-252 | TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | FE+BE |
| TC-GS-FILEMGR-253 | TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | FE+BE |
| TC-GS-FILEMGR-254 | TC-GS-FILEMGR-E2E-008-capability-dicabut-saat-halaman-terbuka | FE+BE |
| TC-GS-FILEMGR-255 | TC-GS-FILEMGR-E2E-026-konflik-dua-admin-delete-dan-permanently-delete | FE+BE |
| TC-GS-FILEMGR-256 | TC-GS-FILEMGR-E2E-026-konflik-dua-admin-delete-dan-permanently-delete | FE+BE |
| TC-GS-FILEMGR-257 | TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry | FE+BE |
| TC-GS-FILEMGR-258 | TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | FE+BE |
| TC-GS-FILEMGR-259 | TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip | FE+BE (mobile) |
| TC-GS-FILEMGR-260 | TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip | FE+BE (mobile) |
| TC-GS-FILEMGR-261 | TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip | FE+BE (mobile) |
| TC-GS-FILEMGR-262 | TC-GS-FILEMGR-E2E-029-retensi-teks-info-dan-auto-purge-in-recycle-bin | FE+BE |
| TC-GS-FILEMGR-263 | TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete | FE+BE |
| TC-GS-FILEMGR-264 | TC-GS-FILEMGR-E2E-025-konflik-file-tidak-tersedia-permanently-delete | FE+BE |
| TC-GS-FILEMGR-265 | TC-GS-FILEMGR-E2E-027-auto-transition-ganti-dan-hapus-foto-profil | FE+BE |
| TC-GS-FILEMGR-266 | TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai | FE+BE |
| TC-GS-FILEMGR-267 | TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip | FE+BE (mobile) |
| TC-GS-FILEMGR-268 | TC-GS-FILEMGR-E2E-065-storage-screening-urutan-format-dan-baris-app | FE+BE |
| TC-GS-FILEMGR-269 | TC-GS-FILEMGR-E2E-065-storage-screening-urutan-format-dan-baris-app | FE+BE |
| TC-GS-FILEMGR-270 | TC-GS-FILEMGR-E2E-065-storage-screening-urutan-format-dan-baris-app | FE+BE |
| TC-GS-FILEMGR-271 | TC-GS-FILEMGR-E2E-066-storage-state-laporan-kuota-dan-batas-persentase | FE+BE |
| TC-GS-FILEMGR-272 | TC-GS-FILEMGR-E2E-003-empty-state-semua-surface-client-tanpa-data | FE+BE |
| TC-GS-FILEMGR-273 | TC-GS-FILEMGR-E2E-066-storage-state-laporan-kuota-dan-batas-persentase | FE+BE |
| TC-GS-FILEMGR-274 | TC-GS-FILEMGR-E2E-066-storage-state-laporan-kuota-dan-batas-persentase | FE+BE |
| TC-GS-FILEMGR-275 | TC-GS-FILEMGR-E2E-066-storage-state-laporan-kuota-dan-batas-persentase | FE+BE |
| TC-GS-FILEMGR-276 | TC-GS-FILEMGR-E2E-067-storage-perubahan-laporan-dan-topup-kuota | FE+BE |
| TC-GS-FILEMGR-277 | TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-FILEMGR-278 | TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-FILEMGR-279 | TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-FILEMGR-280 | TC-GS-FILEMGR-E2E-006-role-matrix-visibilitas-kontrol-per-role | FE+BE |
| TC-GS-FILEMGR-281 | TC-GS-FILEMGR-E2E-068-storage-isolasi-client | FE+BE |
| TC-GS-FILEMGR-282 | TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss | FE+BE |
| TC-GS-FILEMGR-283 | TC-GS-FILEMGR-E2E-063-tenant-baca-tetap-tersedia | FE+BE |
| TC-GS-FILEMGR-284 | TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip | FE+BE (mobile) |
| TC-GS-FILEMGR-285 | TC-GS-FILEMGR-E2E-067-storage-perubahan-laporan-dan-topup-kuota | FE+BE |
| TC-GS-FILEMGR-286 | TC-GS-FILEMGR-E2E-065-storage-screening-urutan-format-dan-baris-app | FE+BE |
| TC-GS-FILEMGR-287 | TC-GS-FILEMGR-E2E-028-cascade-purge-delete-user-dan-non-login-user | FE+BE |
| TC-GS-FILEMGR-288 | TC-GS-FILEMGR-E2E-064-tenant-suspended-job-latar | FE+BE |
| TC-GS-FILEMGR-289 | TC-GS-FILEMGR-E2E-007-role-matrix-positif-download-delete-dan-permanently-delete | FE+BE |
