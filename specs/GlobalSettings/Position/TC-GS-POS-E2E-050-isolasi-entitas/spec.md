---
id: TC-GS-POS-E2E-050-isolasi-entitas
title: "Isolasi Entitas: Position Client Lain Tidak Terlihat di Tabel, Changelog, dan Validasi Nama"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-267
coverage:
  web: automated
---

# Isolasi Entitas: Position Client Lain Tidak Terlihat di Tabel, Changelog, dan Validasi Nama

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` dan berada di Global Settings > User > Position pada entitas aktif (Client A). Password tidak ditulis di spec atau fixture.
- Akun Total Control `Client Lain` (Pre-setup 19) dipakai hanya di hook `before` untuk memastikan Position `Regional Sales Lead` ada di entitas `Client Lain`, kredensial `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Data Pre-setup: Position `Regional Sales Lead` milik entitas `Client Lain` (Pre-setup 19), tidak diubah atau dihapus spec ini sehingga tidak bersuffix. Hook `before` memastikan entitas aktif (Client A) tidak memiliki Position bernama `Regional Sales Lead`.
- Data Dinamis: tidak ada. Spec tidak membuat data (submit Create tidak pernah dilakukan).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` untuk akun aktor spec ini (Total Control) dan hook `after` memulihkannya; lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): kembalikan sesi ke akun Total Control default suite.
- Hook `beforeEach`: membuka Global Settings > User > Position pada entitas aktif; spec tidak menguji navigasi sehingga tidak mengulang langkah buka layar di `## Test Steps`.
- Kemampuan teknis: membaca keberadaan Position di entitas `Client Lain` dan entitas aktif (disediakan tim FE/BE; mekanisme tidak didefinisikan di TC, PRD, atau LLD).
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-POS-267: Isolasi entitas, Position entitas lain tidak terlihat

1. Ketik `Regional Sales Lead` pada Search tabel Position lalu tekan Enter
2. Verifikasi tabel menampilkan "No results found"
3. Klik `←` pada kotak Search tabel Position (menutup input dan mereset tabel)
4. Klik ikon Changelog
5. Ketik `Regional Sales Lead` pada Search Popup Changelog lalu tekan Enter
6. Verifikasi Popup Changelog menampilkan "No results found"
7. Tutup Popup Changelog dengan klik `✕` di header
8. Klik `[+ Position]`
9. Ketik `Regional Sales Lead` pada field Position Name
10. Tunggu ±500 ms (debounce pengecekan keunikan)
11. Verifikasi tidak ada error inline "Position Name already exists" pada field Position Name
12. Klik `✕` di header Popup Create Position
13. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
14. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Kelas harness: state tenant (isolasi entitas, hanya baca).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 (menutup input Search tabel dan mereset tabel), 7 (menutup Popup Changelog), serta langkah 12 dan 14 (aksi `✕` dan `[Leave]`). Langkah 13 adalah `Verifikasi` tambahan agar penutupan form Create yang dirty deterministik (S-08); teks dialog dari PRD §4.2d Dialog 5 dan dialog diasersi sebagai satu elemen (judul, body, dan tombol disebut utuh).
- Spec memuat satu pembukaan form Create dan satu kejadian menutup form (langkah 8 dan 12 sampai 14).
- Placeholder Search Popup Changelog `Search changelog...` (NC-16) tidak diasersi di spec ini.
- Temuan untuk QA:
  - TC-GS-POS-267 tidak menyebut email dan env var akun Total Control `Client Lain` (Pre-setup 19); env var `GS_CLIENTB_TC_PASSWORD` terdaftar di `spectra.config.ts` dan `.env.example`, tetapi email akun `Client Lain` perlu ditetapkan.
  - TC-GS-POS-267 langkah 2 tidak menyebut apakah Search Popup Changelog dieksekusi dengan Enter; spec memakai Enter seperti langkah 1.
  - TC-GS-POS-267 tidak menyebut cara memastikan entitas aktif tidak memiliki `Regional Sales Lead`; spec menuliskannya sebagai pengecekan di hook `before` yang disediakan tim FE/BE.
