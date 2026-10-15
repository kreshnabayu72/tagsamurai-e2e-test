# Coverage E2E — Admin Console > Settings > Privacy Policy

Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md` (214 ID `TC-AC-PP-01`–`214`, semua aktif). Suite: `specs/AdminConsole/SettingsPrivacyPolicy/`. Prefix: `AC` + `PP` (`TC-AC-PP-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Tidak ada `tc-settings-privacy-policy-backend.md`.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 204 TC aktif masuk 59 spec, 10 TC hanya-BE tidak masuk spec. Setiap TC yang masuk terpetakan ke tepat satu spec (tidak ada TC yang terbelah lintas spec).

## TC hanya-BE (tidak masuk spec)

TC-AC-PP-170, 171, 172, 173, 174, 175, 176, 177, 193, 194. Seluruhnya bertanda `FE Test = -` ("pengujian murni tingkat server"): permintaan HTTP langsung yang ditolak 403/401 dan baca publik versi Active tanpa login; kolom PIC FE `-`, PIC BE `v`. Diuji di TC backend modul ini. TC-170, 171, dan 177 memuat satu langkah cek UI sebagai Total Control, tetapi inti ujinya respons server sehingga tetap diperlakukan hanya-BE (keputusan user pada rencana spec).

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-PP-E2E-001-screening-halaman-utama-dan-tabel | Screening Halaman Utama Privacy Policy: Layout Tabel Version History, Badge Active, Format Sel, dan Row Action | FE+BE | 66 | 1, 2, 3, 5, 6, 79, 163 |
| TC-AC-PP-E2E-002-published-by-seed-satu-kata-akun-dihapus | Published By: Nilai Seed System, Nama Satu Kata, dan Snapshot Akun Dihapus pada Tampil, Search, Filter, dan Sort | FE+BE | 29 | 4, 105, 107, 124 |
| TC-AC-PP-E2E-003-first-time-screening-empty-state-read-only | First-time Setup: Screening Empty State dan Read Only Tanpa Tombol Create | FE+BE | 19 | 10, 20 |
| TC-AC-PP-E2E-004-first-time-create-screening-dan-validasi-v01 | First-time Create Privacy Policy: Screening Modal, Validasi V-01 Diblokir, dan Clear Field | mock | 36 | 34, 36, 37, 38 |
| TC-AC-PP-E2E-005-first-time-create-penutupan-modal | First-time Create Privacy Policy: Penutupan Modal Dirty dan Bersih | mock | 41 | 39, 40, 197, 198 |
| TC-AC-PP-E2E-006-first-time-publish-pertama-dan-log | Publish Pertama pada First-time Setup Menghasilkan Version 1 Active dan Entri Log Publish | FE+BE | 27 | 35, 156 |
| TC-AC-PP-E2E-007-resilience-baca-tabel-dan-export | Resilience Baca Tabel Version History: Loading, Error Load, Try Again, dan Kegagalan Download | FE+BE | 34 | 7, 8, 9, 141 |
| TC-AC-PP-E2E-008-resilience-baca-modal-view-edit | Resilience Baca Konten di Modal View dan Edit: Loading, Error Load, Try Again, dan Penutupan | FE+BE | 95 | 31, 32, 44, 45, 46, 70 |
| TC-AC-PP-E2E-009-role-matrix-visibilitas-elemen | Role Matrix: Visibilitas Elemen Halaman Privacy Policy per Role | FE+BE | 66 | 13, 17, 18, 19, 21, 22 |
| TC-AC-PP-E2E-010-role-matrix-negatif-tanpa-capability | Role Matrix Negatif: Principal Tanpa Capability Tidak Melihat Menu dan Akses Langsung Ditolak | FE+BE | 9 | 12, 14 |
| TC-AC-PP-E2E-011-role-matrix-negatif-entity-gate | Role Matrix Negatif: Entity Gate Distributor, Partner, dan Client Tidak Mengakses Privacy Policy | FE+BE | 25 | 15, 16 |
| TC-AC-PP-E2E-012-role-matrix-positif-read-only-detail-download | Role Matrix Positif: Read Only Mengeksekusi Detail Versi dan Download CSV | FE+BE | 17 | 23, 24 |
| TC-AC-PP-E2E-013-role-matrix-positif-default-user-publish | Role Matrix Positif: Default User Mengeksekusi Publish New Version | FE+BE | 13 | 25 |
| TC-AC-PP-E2E-014-capability-dicabut-saat-aksi-berjalan | Capability Update Dicabut Setelah Modal Edit Terbuka: Publish Ditolak 403 | FE+BE | 25 | 84 |
| TC-AC-PP-E2E-015-modal-view-screening-dan-penutupan | Modal View: Screening Versi Active dan Superseded, Jalur Buka, serta Penutupan | FE+BE | 51 | 26, 27, 28, 30 |
| TC-AC-PP-E2E-016-modal-view-konten-200-paragraf | Modal View: Konten 200 Paragraf Dirender Penuh dengan Scroll | FE+BE | 8 | 33 |
| TC-AC-PP-E2E-017-edit-screening-dan-jalur-masuk | Screening Modal State Edit dan Dua Jalur Masuk ke State Edit | FE+BE | 43 | 41, 42, 43 |
| TC-AC-PP-E2E-018-edit-active-berubah-oleh-admin-lain | Versi Active Berubah oleh Admin Lain Saat Modal Edit Dibuka atau Sedang Terbuka | FE+BE | 46 | 47, 48, 95 |
| TC-AC-PP-E2E-019-editor-undo-redo-dan-aksesibilitas | Editor: Undo dan Redo serta Aksesibilitas Area Editor dan Toolbar | mock | 32 | 52, 53 |
| TC-AC-PP-E2E-020-editor-insert-link | Editor Insert Link: Screening Popover, Validasi URL, Penyisipan, Cancel, Esc, dan Tautan Existing | mock | 138 | 54, 55, 56, 57, 58, 209 |
| TC-AC-PP-E2E-021-editor-format-dan-paste-tersimpan | Editor: Format Teks, Daftar, dan Paste Tersimpan serta Dirender Setelah Publish | FE+BE | 75 | 49, 50, 51, 59, 60 |
| TC-AC-PP-E2E-022-edit-clear-field-dan-unsaved-changes | Edit: Clear Field dan Dialog Unsaved Changes pada Modal State Edit | FE+BE | 76 | 61, 62, 63, 65, 66, 72 |
| TC-AC-PP-E2E-023-edit-penutupan-modal-esc-klik-luar-navigasi | Edit: Penutupan Modal lewat Esc, Klik Luar, Navigasi Sidebar, Browser Back, dan Reload | FE+BE | 86 | 64, 67, 68, 69, 71 |
| TC-AC-PP-E2E-024-dialog-publish-confirm-dan-validasi-v01-edit | Validasi V-01 pada Edit dan Dialog Publish Confirm: Screening, Cancel, Esc, Back, dan Klik Luar | FE+BE | 48 | 73, 74, 88 |
| TC-AC-PP-E2E-025-publish-berhasil-immutability | Publish New Version Berhasil: Badge Active Berpindah, Jalur View, Tiga Publikasi, dan Pemulihan Manual | FE+BE | 74 | 75, 76, 77, 78 |
| TC-AC-PP-E2E-026-publish-saving-state-klik-ganda-filter-aktif | Publish: State Publishing, Klik Ganda [Publish], dan Versi Baru Saat Filter Aktif | FE+BE | 54 | 80, 81, 200 |
| TC-AC-PP-E2E-027-publish-no-op-dan-normalisasi | Publish Tanpa Perubahan (No-Op) dan Normalisasi Pembanding Konten | FE+BE | 82 | 89, 90, 195, 196, 211 |
| TC-AC-PP-E2E-028-defense-konten-kosong-ditolak-server | Defense-in-Depth: Server Menolak Konten Kosong, Konten Hanya Sanitasi, dan Konten &nbsp; pada Publish | FE+BE | 39 | 85, 86, 87 |
| TC-AC-PP-E2E-029-resilience-tulis-publish-5xx-jaringan-401-429 | Resilience Tulis Publish: Gangguan Jaringan, 429, 400, 413, Sesi Berakhir 401, dan Server Error 5xx | FE+BE | 98 | 82, 83, 204, 205 |
| TC-AC-PP-E2E-030-idempotency-timeout-30-detik-dan-retry | Idempotency Publish: Timeout 30 Detik, Respons Dibuang atau Ditahan, dan Pengiriman Ulang | FE+BE | 118 | 91, 203, 206, 213, 214 |
| TC-AC-PP-E2E-031-idempotency-key-bentrok-409-dialog-d03 | Idempotency Publish: Key Bentrok 409 dan Dialog Konteks Unable to Publish | FE+BE | 80 | 92, 93, 202 |
| TC-AC-PP-E2E-032-idempotency-masa-berlaku-24-jam | Idempotency Publish: Masa Berlaku Key 24 Jam dan Batas Tepat 24 Jam | FE+BE | 39 | 94, 212 |
| TC-AC-PP-E2E-033-search-version-history | Search Version History: Siklus Interaksi dan Pencocokan Kolom | FE+BE | 73 | 11, 96, 97, 98, 100, 101, 102 |
| TC-AC-PP-E2E-034-filter-screening-dropdown-dan-chip | Filter Panel: Screening, Dropdown Published By, dan Penghapusan Chip | FE+BE | 35 | 106, 108, 109, 110 |
| TC-AC-PP-E2E-035-filter-rentang-and-apply-clear-indikator | Filter Panel: Rentang Tanggal, Logika AND, Apply, Clear Field, dan Indikator | FE+BE | 69 | 112, 113, 114, 116, 117, 118, 119 |
| TC-AC-PP-E2E-036-filter-overflow-chip-more | Filter Published By: Overflow Chip Diringkas Menjadi +N more | FE+BE | 10 | 201 |
| TC-AC-PP-E2E-037-filter-published-by-or | Filter Published By dengan Dua Opsi Memakai Logika OR | FE+BE | 11 | 111 |
| TC-AC-PP-E2E-038-sort-default-dan-siklus-tiga-klik | Sort Tabel Version History: Urutan Default, Siklus Tiga Klik, dan Header Actions | FE+BE | 27 | 120, 123, 125, 127 |
| TC-AC-PP-E2E-039-sort-tie-breaker-published-at-sama | Sort Tie-Breaker: Dua Versi dengan Published At Sama Diurutkan Menurut Nomor Versi | FE+BE | 8 | 121 |
| TC-AC-PP-E2E-040-search-dan-sort-dataset-besar | Search dan Sort Version History pada Dataset Besar (Riwayat B) | FE+BE | 39 | 99, 104, 122, 126 |
| TC-AC-PP-E2E-041-pagination-preservasi-state-dan-modal | Pagination, Preservasi State, dan Reset Tabel Version History | FE+BE | 64 | 29, 148, 149, 150, 151, 152, 153 |
| TC-AC-PP-E2E-042-kombinasi-search-filter-sort-page-size | Kombinasi Search, Filter, Sort, dan Page Size pada Version History | FE+BE | 28 | 115, 199 |
| TC-AC-PP-E2E-043-setup-column-screening-hide-guard-tutup | Setup Column dan Column Visibility: Screening, Hide, Guard, dan Tutup Tanpa Save | mock | 55 | 128, 129, 130, 134, 136 |
| TC-AC-PP-E2E-044-setup-column-reorder-pin-reset-persist | Setup Column: Hide, Reorder, Pin, Reset, dan Persistensi Konfigurasi | FE+BE | 66 | 131, 132, 133, 135, 137 |
| TC-AC-PP-E2E-045-download-screening-dan-isi-file | Download Version History: Screening Overlay, Nama File, dan Isi File CSV dan XLSX | FE+BE | 52 | 138, 139, 140, 142, 145, 146, 147 |
| TC-AC-PP-E2E-046-download-mengikuti-search-dan-filter | Download Mengikuti Search dan Filter Aktif lintas Halaman (Riwayat B) | FE+BE | 20 | 143, 144 |
| TC-AC-PP-E2E-047-download-volume-5001-baris | Download CSV Lebih dari 5.000 Baris Diproses Sinkron (Riwayat D) | FE+BE | 10 | 207 |
| TC-AC-PP-E2E-048-format-tanggal-dan-time-zone | Published At Mengikuti Date Format, Time Zone, dan Time Format General Settings | FE+BE | 50 | 166, 167, 168, 210 |
| TC-AC-PP-E2E-049-log-publish-activity-dan-system-log | Entri Log Publish pada Activity Log dan System Log Aktor | FE+BE | 89 | 154, 155, 157, 162, 164 |
| TC-AC-PP-E2E-050-log-snapshot-nama-aktor | Snapshot Nama Aktor pada Published By dan Activity Log Setelah Akun Diganti Nama atau Dihapus | FE+BE | 19 | 161 |
| TC-AC-PP-E2E-051-log-absence-tanpa-pencatatan | Aksi Tanpa Pencatatan: View, Search, Download, Publish Gagal, dan Versi Seed Tidak Menulis Log | FE+BE | 43 | 158, 159, 160 |
| TC-AC-PP-E2E-052-sesi-pengguna-lain-tidak-terganggu | Publish Tidak Mengganggu Sesi Pengguna Lain dan Tidak Mengirim Notifikasi | FE+BE | 15 | 165 |
| TC-AC-PP-E2E-053-sanitasi-elemen-dan-atribut-berbahaya | Sanitasi Server: Penghapusan Script, Atribut Event, Style, dan Tautan Berskema Berbahaya | FE+BE | 47 | 178, 179, 180, 181, 183 |
| TC-AC-PP-E2E-054-sanitasi-whitelist-tautan-dan-paste | Sanitasi Server: Unwrap Tag, Tautan Aman, Whitelist Utuh, dan Paste Berbahaya dari Editor | FE+BE | 48 | 182, 184, 185, 186 |
| TC-AC-PP-E2E-055-konkurensi-dua-admin-publish | Konkurensi Dua Admin Mem-publish Bersamaan pada Versi Active dan First-time Setup | FE+BE | 39 | 187, 188 |
| TC-AC-PP-E2E-056-android-back-sistem-dialog-popover | Android: Back Sistem pada Modal, Dialog Publish Confirm, dan Popover Insert Link | FE+BE | 45 | 189, 190, 191 |
| TC-AC-PP-E2E-057-android-download-dan-sort-bottom-sheet | Android: Download Susunan Kolom Default dan Sort lewat Bottom Sheet | FE+BE | 33 | 192, 208 |
| TC-AC-PP-E2E-058-defense-search-payload-script-dan-karakter-literal | Defense-in-Depth Search: Karakter Pola dan Payload Script Diperlakukan sebagai Teks Literal | FE+BE | 22 | 103 |
| TC-AC-PP-E2E-059-capability-diberikan-dan-dicabut-akses-menu | Pemberian dan Pencabutan Capability Manage Privacy Policy Mengubah Akses Menu | FE+BE | 24 | 169 |

Spec 056 dan 057 memakai `coverage.mobile: automated` (aplikasi native Android); spec lain `coverage.web: automated`.

## Pembagian TC lintas spec

- Tidak ada TC yang terbelah lintas spec.
- Asersi absence log murni (kelas g) hanya di spec `051` (TC-158, 159, 160). Asersi jumlah entri log (tepat 1 entri per Publish, tanpa entri consent) berada di spec fungsional `049` (TC-157) karena bukan kelas g.
- TC-156 (entri log Publish pertama) dijalankan bersama TC-35 di spec `006` karena keduanya berbagi aksi Publish pada Riwayat C.
- TC-146 (Download tanpa baris) berada di spec `045` (kelas f) pada dataset Riwayat C yang di-seed ulang di akhir spec.
- TC-103 (payload script di Search) ada di spec `058` (kelas a), dipindah dari `033`.

## Kebutuhan lingkungan (tim FE)

- Env var password yang dipakai spec (hanya `AC_TC_PASSWORD` yang sudah terdaftar; sisanya belum didaftarkan di `spectra.config.ts` dan `.env.example`; berkas itu tidak diubah oleh generate spec): `AC_TC_PASSWORD`, `AC_RO_PASSWORD`, `AC_DU_PASSWORD`, `AC_NOCAP_PASSWORD`, `AC_DIST_PASSWORD`, `AC_PARTNER_PASSWORD`, `AC_CLIENT_PASSWORD`, `AC_TC2_PASSWORD`, `AC_SNAP_PASSWORD`, `AC_INDROLE_PASSWORD`, `AC_MAYA_PASSWORD`, `AC_BUDI_PASSWORD`.
- Fixture `fixtures/privacyPolicy.json` (belum ada): `urlHalamanPrivacyPolicy`, `jumlahParagrafKontenPanjang` (016), `kontenVersi4AdminLain` (018), `kontenSanitasiScript`, `kontenSanitasiEvent`, `kontenSanitasiStyleClass`, `kontenSanitasiTagStyle`, `kontenSanitasiSkemaTautan` (053), `kontenSanitasiUnwrap`, `kontenSanitasiTautanAman`, `kontenSanitasiWhitelist`, `clipboardPasteBerbahaya` (054).
- Fixture BE: membuat ulang dataset Riwayat A, B, C, D (5.001 versi), S, T, V dan varian isi Riwayat A (200 paragraf, teks `Important` bertag `strong`, Published By Version 120 `Budi Santoso`); membuat admin lain publish (pemicu); membuat akun sekali pakai (Pre-setup 17, 18); memberi/mencabut capability "Manage privacy policy" termasuk untuk Distributor, Partner, Client; menyetujui Version 3 untuk Budi Aditya (spec 052).
- Kemampuan teknis: `Spectra.intercept()` (500, 401, 429, 400, 413, 409, 422, timeout, respons dibuang/ditahan, penggantian body Publish); klien HTTP (Publish langsung, TC-212 dan spec 053/054); jam server dan fixture waktu (spec 032, 048); pengubah General Settings (Date Format, Time Zone, Time Format); dua sesi/browser paralel (014, 050, 052, 055, 018); tunggu nyata 30 detik (spec 030, 031) dan 10 detik (spec 029); penangkap unduhan CSV/XLSX; penanganan dialog `beforeunload` dan deteksi dialog `alert`; clipboard HTML; pengubah lebar viewport; mail-catcher (spec 052); aplikasi native Android dan mekanisme intercept jaringannya (spec 056, 057).
- Suite berjalan serial (`parallel: false`): dokumen Privacy Policy tunggal platform-wide dan Publish/seeding mengubah state global.
- Environment automation harus terisolasi dari aktivitas pengguna lain.

## Temuan yang masih terbuka

Temuan TC sumber (ambigu, kontradiktif, kurang precondition) dicatat per spec di `## Notes` butir "Temuan untuk QA". Yang paling berdampak:

- TC-17 melabeli Version 2 "Superseded", padahal TC-02 menyatakan tidak ada badge Superseded.
- TC-98: keyword `john d` dinyatakan cocok dengan nama lengkap, tetapi sel tabel hanya menampilkan `John D`.
- TC-209 menulis `[↶]` sedangkan tooltip toolbar di TC-34/NC-15 adalah "Undo".
- TC-71: judul menyebut "tutup tab" tetapi hanya reload yang diuji.
- TC-80: Expected b memisahkan Esc modal dan Esc dialog padahal hanya satu tombol Esc.
- TC-93: aksi klik `[Clear Field]`/`[✕]`/area gelap pada Expected b tidak ada di kolom Langkah Uji.
- TC-94 dan TC-212: sarana kirim ulang (UI atau klien HTTP) dan jenis manipulasi jam server tidak dinyatakan.
- TC-91, 92, 203, 206, 213, 214: kesamaan idempotency key tidak teramati lewat UI dan nama header tidak ada di TC/openapi (NC-02).
- TC-153: precondition tidak menyebut page size; TC-157/162: cara mencatat baseline log tidak ditentukan; TC-187 Expected e tidak teramati sampai detik di UI.
- TC-165, 187, 188 bertanda Manual Only; tetap ditulis sebagai spec dengan kebutuhan teknis di Prerequisites (bagian 2 konvensi).
- Spec yang melewati batas ±35 langkah dengan satu kelas harness (alasan tertulis di `## Notes` tiap spec: tiap klausa Expected menjadi satu `Verifikasi` (S-01), bagian TC berdiri sendiri setelah reseed, dan tidak dipecah; saran pemecahan 023 dan 029 diserahkan ke tim FE): 001 (66), 004 (36), 005 (41), 008 (95), 009 (66), 015 (51), 017 (43), 018 (46), 020 (138), 021 (75), 022 (76), 023 (86), 024 (48), 025 (74), 026 (54), 027 (82), 028 (39), 029 (98), 030 (118), 031 (80), 032 (39), 033 (73), 035 (69), 040 (39), 041 (64), 043 (55), 044 (66), 045 (52), 048 (50), 049 (89), 051 (43), 053 (47), 054 (48), 055 (39), 056 (45).
- Spec 044 bermode FE+BE (bukan mock) karena TC-137 login ulang sungguhan. Spec bermode mock: 004, 005, 019, 020, 043 (kebutuhan mock sesi/izin Total Control tertulis di Prerequisites; login nyata hanya untuk run non-mock).
- Perubahan pasca-audit e2e: TC-146 dipindah dari spec 003 ke 045 (kelas f), TC-103 dipindah dari 033 ke spec baru 058 (kelas a), spec 014 dipecah (TC-84 tetap di 014, TC-169 menjadi spec baru 059). Akun `AC_PRINCIPAL_PP_PASSWORD` yang sudah terdaftar di `spectra.config.ts` belum dipetakan ke Pre-setup TC; menunggu konfirmasi tim FE.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-PP-1 | TC-AC-PP-E2E-001 | FE+BE |
| TC-AC-PP-2 | TC-AC-PP-E2E-001 | FE+BE |
| TC-AC-PP-3 | TC-AC-PP-E2E-001 | FE+BE |
| TC-AC-PP-4 | TC-AC-PP-E2E-002 | FE+BE |
| TC-AC-PP-5 | TC-AC-PP-E2E-001 | FE+BE |
| TC-AC-PP-6 | TC-AC-PP-E2E-001 | FE+BE |
| TC-AC-PP-7 | TC-AC-PP-E2E-007 | FE+BE |
| TC-AC-PP-8 | TC-AC-PP-E2E-007 | FE+BE |
| TC-AC-PP-9 | TC-AC-PP-E2E-007 | FE+BE |
| TC-AC-PP-10 | TC-AC-PP-E2E-003 | FE+BE |
| TC-AC-PP-11 | TC-AC-PP-E2E-033 | FE+BE |
| TC-AC-PP-12 | TC-AC-PP-E2E-010 | FE+BE |
| TC-AC-PP-13 | TC-AC-PP-E2E-009 | FE+BE |
| TC-AC-PP-14 | TC-AC-PP-E2E-010 | FE+BE |
| TC-AC-PP-15 | TC-AC-PP-E2E-011 | FE+BE |
| TC-AC-PP-16 | TC-AC-PP-E2E-011 | FE+BE |
| TC-AC-PP-17 | TC-AC-PP-E2E-009 | FE+BE |
| TC-AC-PP-18 | TC-AC-PP-E2E-009 | FE+BE |
| TC-AC-PP-19 | TC-AC-PP-E2E-009 | FE+BE |
| TC-AC-PP-20 | TC-AC-PP-E2E-003 | FE+BE |
| TC-AC-PP-21 | TC-AC-PP-E2E-009 | FE+BE |
| TC-AC-PP-22 | TC-AC-PP-E2E-009 | FE+BE |
| TC-AC-PP-23 | TC-AC-PP-E2E-012 | FE+BE |
| TC-AC-PP-24 | TC-AC-PP-E2E-012 | FE+BE |
| TC-AC-PP-25 | TC-AC-PP-E2E-013 | FE+BE |
| TC-AC-PP-26 | TC-AC-PP-E2E-015 | FE+BE |
| TC-AC-PP-27 | TC-AC-PP-E2E-015 | FE+BE |
| TC-AC-PP-28 | TC-AC-PP-E2E-015 | FE+BE |
| TC-AC-PP-29 | TC-AC-PP-E2E-041 | FE+BE |
| TC-AC-PP-30 | TC-AC-PP-E2E-015 | FE+BE |
| TC-AC-PP-31 | TC-AC-PP-E2E-008 | FE+BE |
| TC-AC-PP-32 | TC-AC-PP-E2E-008 | FE+BE |
| TC-AC-PP-33 | TC-AC-PP-E2E-016 | FE+BE |
| TC-AC-PP-34 | TC-AC-PP-E2E-004 | mock |
| TC-AC-PP-35 | TC-AC-PP-E2E-006 | FE+BE |
| TC-AC-PP-36 | TC-AC-PP-E2E-004 | mock |
| TC-AC-PP-37 | TC-AC-PP-E2E-004 | mock |
| TC-AC-PP-38 | TC-AC-PP-E2E-004 | mock |
| TC-AC-PP-39 | TC-AC-PP-E2E-005 | mock |
| TC-AC-PP-40 | TC-AC-PP-E2E-005 | mock |
| TC-AC-PP-41 | TC-AC-PP-E2E-017 | FE+BE |
| TC-AC-PP-42 | TC-AC-PP-E2E-017 | FE+BE |
| TC-AC-PP-43 | TC-AC-PP-E2E-017 | FE+BE |
| TC-AC-PP-44 | TC-AC-PP-E2E-008 | FE+BE |
| TC-AC-PP-45 | TC-AC-PP-E2E-008 | FE+BE |
| TC-AC-PP-46 | TC-AC-PP-E2E-008 | FE+BE |
| TC-AC-PP-47 | TC-AC-PP-E2E-018 | FE+BE |
| TC-AC-PP-48 | TC-AC-PP-E2E-018 | FE+BE |
| TC-AC-PP-49 | TC-AC-PP-E2E-021 | FE+BE |
| TC-AC-PP-50 | TC-AC-PP-E2E-021 | FE+BE |
| TC-AC-PP-51 | TC-AC-PP-E2E-021 | FE+BE |
| TC-AC-PP-52 | TC-AC-PP-E2E-019 | mock |
| TC-AC-PP-53 | TC-AC-PP-E2E-019 | mock |
| TC-AC-PP-54 | TC-AC-PP-E2E-020 | mock |
| TC-AC-PP-55 | TC-AC-PP-E2E-020 | mock |
| TC-AC-PP-56 | TC-AC-PP-E2E-020 | mock |
| TC-AC-PP-57 | TC-AC-PP-E2E-020 | mock |
| TC-AC-PP-58 | TC-AC-PP-E2E-020 | mock |
| TC-AC-PP-59 | TC-AC-PP-E2E-021 | FE+BE |
| TC-AC-PP-60 | TC-AC-PP-E2E-021 | FE+BE |
| TC-AC-PP-61 | TC-AC-PP-E2E-022 | FE+BE |
| TC-AC-PP-62 | TC-AC-PP-E2E-022 | FE+BE |
| TC-AC-PP-63 | TC-AC-PP-E2E-022 | FE+BE |
| TC-AC-PP-64 | TC-AC-PP-E2E-023 | FE+BE |
| TC-AC-PP-65 | TC-AC-PP-E2E-022 | FE+BE |
| TC-AC-PP-66 | TC-AC-PP-E2E-022 | FE+BE |
| TC-AC-PP-67 | TC-AC-PP-E2E-023 | FE+BE |
| TC-AC-PP-68 | TC-AC-PP-E2E-023 | FE+BE |
| TC-AC-PP-69 | TC-AC-PP-E2E-023 | FE+BE |
| TC-AC-PP-70 | TC-AC-PP-E2E-008 | FE+BE |
| TC-AC-PP-71 | TC-AC-PP-E2E-023 | FE+BE |
| TC-AC-PP-72 | TC-AC-PP-E2E-022 | FE+BE |
| TC-AC-PP-73 | TC-AC-PP-E2E-024 | FE+BE |
| TC-AC-PP-74 | TC-AC-PP-E2E-024 | FE+BE |
| TC-AC-PP-75 | TC-AC-PP-E2E-025 | FE+BE |
| TC-AC-PP-76 | TC-AC-PP-E2E-025 | FE+BE |
| TC-AC-PP-77 | TC-AC-PP-E2E-025 | FE+BE |
| TC-AC-PP-78 | TC-AC-PP-E2E-025 | FE+BE |
| TC-AC-PP-79 | TC-AC-PP-E2E-001 | FE+BE |
| TC-AC-PP-80 | TC-AC-PP-E2E-026 | FE+BE |
| TC-AC-PP-81 | TC-AC-PP-E2E-026 | FE+BE |
| TC-AC-PP-82 | TC-AC-PP-E2E-029 | FE+BE |
| TC-AC-PP-83 | TC-AC-PP-E2E-029 | FE+BE |
| TC-AC-PP-84 | TC-AC-PP-E2E-014 | FE+BE |
| TC-AC-PP-85 | TC-AC-PP-E2E-028 | FE+BE |
| TC-AC-PP-86 | TC-AC-PP-E2E-028 | FE+BE |
| TC-AC-PP-87 | TC-AC-PP-E2E-028 | FE+BE |
| TC-AC-PP-88 | TC-AC-PP-E2E-024 | FE+BE |
| TC-AC-PP-89 | TC-AC-PP-E2E-027 | FE+BE |
| TC-AC-PP-90 | TC-AC-PP-E2E-027 | FE+BE |
| TC-AC-PP-91 | TC-AC-PP-E2E-030 | FE+BE |
| TC-AC-PP-92 | TC-AC-PP-E2E-031 | FE+BE |
| TC-AC-PP-93 | TC-AC-PP-E2E-031 | FE+BE |
| TC-AC-PP-94 | TC-AC-PP-E2E-032 | FE+BE |
| TC-AC-PP-95 | TC-AC-PP-E2E-018 | FE+BE |
| TC-AC-PP-96 | TC-AC-PP-E2E-033 | FE+BE |
| TC-AC-PP-97 | TC-AC-PP-E2E-033 | FE+BE |
| TC-AC-PP-98 | TC-AC-PP-E2E-033 | FE+BE |
| TC-AC-PP-99 | TC-AC-PP-E2E-040 | FE+BE |
| TC-AC-PP-100 | TC-AC-PP-E2E-033 | FE+BE |
| TC-AC-PP-101 | TC-AC-PP-E2E-033 | FE+BE |
| TC-AC-PP-102 | TC-AC-PP-E2E-033 | FE+BE |
| TC-AC-PP-103 | TC-AC-PP-E2E-058 | FE+BE |
| TC-AC-PP-104 | TC-AC-PP-E2E-040 | FE+BE |
| TC-AC-PP-105 | TC-AC-PP-E2E-002 | FE+BE |
| TC-AC-PP-106 | TC-AC-PP-E2E-034 | FE+BE |
| TC-AC-PP-107 | TC-AC-PP-E2E-002 | FE+BE |
| TC-AC-PP-108 | TC-AC-PP-E2E-034 | FE+BE |
| TC-AC-PP-109 | TC-AC-PP-E2E-034 | FE+BE |
| TC-AC-PP-110 | TC-AC-PP-E2E-034 | FE+BE |
| TC-AC-PP-111 | TC-AC-PP-E2E-037 | FE+BE |
| TC-AC-PP-112 | TC-AC-PP-E2E-035 | FE+BE |
| TC-AC-PP-113 | TC-AC-PP-E2E-035 | FE+BE |
| TC-AC-PP-114 | TC-AC-PP-E2E-035 | FE+BE |
| TC-AC-PP-115 | TC-AC-PP-E2E-042 | FE+BE |
| TC-AC-PP-116 | TC-AC-PP-E2E-035 | FE+BE |
| TC-AC-PP-117 | TC-AC-PP-E2E-035 | FE+BE |
| TC-AC-PP-118 | TC-AC-PP-E2E-035 | FE+BE |
| TC-AC-PP-119 | TC-AC-PP-E2E-035 | FE+BE |
| TC-AC-PP-120 | TC-AC-PP-E2E-038 | FE+BE |
| TC-AC-PP-121 | TC-AC-PP-E2E-039 | FE+BE |
| TC-AC-PP-122 | TC-AC-PP-E2E-040 | FE+BE |
| TC-AC-PP-123 | TC-AC-PP-E2E-038 | FE+BE |
| TC-AC-PP-124 | TC-AC-PP-E2E-002 | FE+BE |
| TC-AC-PP-125 | TC-AC-PP-E2E-038 | FE+BE |
| TC-AC-PP-126 | TC-AC-PP-E2E-040 | FE+BE |
| TC-AC-PP-127 | TC-AC-PP-E2E-038 | FE+BE |
| TC-AC-PP-128 | TC-AC-PP-E2E-043 | mock |
| TC-AC-PP-129 | TC-AC-PP-E2E-043 | mock |
| TC-AC-PP-130 | TC-AC-PP-E2E-043 | mock |
| TC-AC-PP-131 | TC-AC-PP-E2E-044 | FE+BE |
| TC-AC-PP-132 | TC-AC-PP-E2E-044 | FE+BE |
| TC-AC-PP-133 | TC-AC-PP-E2E-044 | FE+BE |
| TC-AC-PP-134 | TC-AC-PP-E2E-043 | mock |
| TC-AC-PP-135 | TC-AC-PP-E2E-044 | FE+BE |
| TC-AC-PP-136 | TC-AC-PP-E2E-043 | mock |
| TC-AC-PP-137 | TC-AC-PP-E2E-044 | FE+BE |
| TC-AC-PP-138 | TC-AC-PP-E2E-045 | FE+BE |
| TC-AC-PP-139 | TC-AC-PP-E2E-045 | FE+BE |
| TC-AC-PP-140 | TC-AC-PP-E2E-045 | FE+BE |
| TC-AC-PP-141 | TC-AC-PP-E2E-007 | FE+BE |
| TC-AC-PP-142 | TC-AC-PP-E2E-045 | FE+BE |
| TC-AC-PP-143 | TC-AC-PP-E2E-046 | FE+BE |
| TC-AC-PP-144 | TC-AC-PP-E2E-046 | FE+BE |
| TC-AC-PP-145 | TC-AC-PP-E2E-045 | FE+BE |
| TC-AC-PP-146 | TC-AC-PP-E2E-045 | FE+BE |
| TC-AC-PP-147 | TC-AC-PP-E2E-045 | FE+BE |
| TC-AC-PP-148 | TC-AC-PP-E2E-041 | FE+BE |
| TC-AC-PP-149 | TC-AC-PP-E2E-041 | FE+BE |
| TC-AC-PP-150 | TC-AC-PP-E2E-041 | FE+BE |
| TC-AC-PP-151 | TC-AC-PP-E2E-041 | FE+BE |
| TC-AC-PP-152 | TC-AC-PP-E2E-041 | FE+BE |
| TC-AC-PP-153 | TC-AC-PP-E2E-041 | FE+BE |
| TC-AC-PP-154 | TC-AC-PP-E2E-049 | FE+BE |
| TC-AC-PP-155 | TC-AC-PP-E2E-049 | FE+BE |
| TC-AC-PP-156 | TC-AC-PP-E2E-006 | FE+BE |
| TC-AC-PP-157 | TC-AC-PP-E2E-049 | FE+BE |
| TC-AC-PP-158 | TC-AC-PP-E2E-051 | FE+BE |
| TC-AC-PP-159 | TC-AC-PP-E2E-051 | FE+BE |
| TC-AC-PP-160 | TC-AC-PP-E2E-051 | FE+BE |
| TC-AC-PP-161 | TC-AC-PP-E2E-050 | FE+BE |
| TC-AC-PP-162 | TC-AC-PP-E2E-049 | FE+BE |
| TC-AC-PP-163 | TC-AC-PP-E2E-001 | FE+BE |
| TC-AC-PP-164 | TC-AC-PP-E2E-049 | FE+BE |
| TC-AC-PP-165 | TC-AC-PP-E2E-052 | FE+BE |
| TC-AC-PP-166 | TC-AC-PP-E2E-048 | FE+BE |
| TC-AC-PP-167 | TC-AC-PP-E2E-048 | FE+BE |
| TC-AC-PP-168 | TC-AC-PP-E2E-048 | FE+BE |
| TC-AC-PP-169 | TC-AC-PP-E2E-059 | FE+BE |
| TC-AC-PP-178 | TC-AC-PP-E2E-053 | FE+BE |
| TC-AC-PP-179 | TC-AC-PP-E2E-053 | FE+BE |
| TC-AC-PP-180 | TC-AC-PP-E2E-053 | FE+BE |
| TC-AC-PP-181 | TC-AC-PP-E2E-053 | FE+BE |
| TC-AC-PP-182 | TC-AC-PP-E2E-054 | FE+BE |
| TC-AC-PP-183 | TC-AC-PP-E2E-053 | FE+BE |
| TC-AC-PP-184 | TC-AC-PP-E2E-054 | FE+BE |
| TC-AC-PP-185 | TC-AC-PP-E2E-054 | FE+BE |
| TC-AC-PP-186 | TC-AC-PP-E2E-054 | FE+BE |
| TC-AC-PP-187 | TC-AC-PP-E2E-055 | FE+BE |
| TC-AC-PP-188 | TC-AC-PP-E2E-055 | FE+BE |
| TC-AC-PP-189 | TC-AC-PP-E2E-056 | FE+BE |
| TC-AC-PP-190 | TC-AC-PP-E2E-056 | FE+BE |
| TC-AC-PP-191 | TC-AC-PP-E2E-056 | FE+BE |
| TC-AC-PP-192 | TC-AC-PP-E2E-057 | FE+BE |
| TC-AC-PP-195 | TC-AC-PP-E2E-027 | FE+BE |
| TC-AC-PP-196 | TC-AC-PP-E2E-027 | FE+BE |
| TC-AC-PP-197 | TC-AC-PP-E2E-005 | mock |
| TC-AC-PP-198 | TC-AC-PP-E2E-005 | mock |
| TC-AC-PP-199 | TC-AC-PP-E2E-042 | FE+BE |
| TC-AC-PP-200 | TC-AC-PP-E2E-026 | FE+BE |
| TC-AC-PP-201 | TC-AC-PP-E2E-036 | FE+BE |
| TC-AC-PP-202 | TC-AC-PP-E2E-031 | FE+BE |
| TC-AC-PP-203 | TC-AC-PP-E2E-030 | FE+BE |
| TC-AC-PP-204 | TC-AC-PP-E2E-029 | FE+BE |
| TC-AC-PP-205 | TC-AC-PP-E2E-029 | FE+BE |
| TC-AC-PP-206 | TC-AC-PP-E2E-030 | FE+BE |
| TC-AC-PP-207 | TC-AC-PP-E2E-047 | FE+BE |
| TC-AC-PP-208 | TC-AC-PP-E2E-057 | FE+BE |
| TC-AC-PP-209 | TC-AC-PP-E2E-020 | mock |
| TC-AC-PP-210 | TC-AC-PP-E2E-048 | FE+BE |
| TC-AC-PP-211 | TC-AC-PP-E2E-027 | FE+BE |
| TC-AC-PP-212 | TC-AC-PP-E2E-032 | FE+BE |
| TC-AC-PP-213 | TC-AC-PP-E2E-030 | FE+BE |
| TC-AC-PP-214 | TC-AC-PP-E2E-030 | FE+BE |
