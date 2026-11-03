---
id: TC-FA-PREF-E2E-109-changelog-column-visibility-dan-screening-setup-column
title: "Changelog Column Visibility dan screening modal Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-332
  - TC-FA-PREF-333
  - TC-FA-PREF-334
coverage:
  web: automated
---

# Changelog Column Visibility dan screening modal Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 9 entri contoh (PB-C1); dipakai sebagai precondition TC, tidak diasersi; seed disediakan tim FE/BE.
- Pemulihan Setup Column: perubahan kolom spec ini dipulihkan dengan langkah eksplisit di spec yang sama; hook `after` menghapus preferensi kolom di browser sebagai cadangan (butir "Pemulihan Setup Column Changelog" di `suite.md`; kemampuan disediakan tim FE).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-332: Screening panel Column Visibility pada header kolom Actions

1. Klik ikon View history di header tab Preferences
2. Klik header kolom Actions (⋯)
3. Verifikasi panel menampilkan tujuh kolom berurutan Date, Action, Section, Field, Old Value, New Value, Modified By
4. Verifikasi tiap kolom pada panel memiliki checkbox tercentang dan Enabled
5. Verifikasi tiap kolom pada panel memiliki pegangan drag
6. Verifikasi bagian bawah panel memuat item "Setup Column..."

### TC-FA-PREF-333: Hapus centang kolom di panel Column Visibility langsung diterapkan tanpa tombol Save

7. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
8. Klik header kolom Actions (⋯)
9. Hapus centang kolom Field
10. Verifikasi kolom Field langsung hilang dari tabel
11. Muat ulang halaman dengan F5, lalu klik ikon View history untuk membuka kembali modal Changelog
12. Verifikasi kolom Date tampil pada tabel
13. Verifikasi kolom Field tetap tidak tampil
14. Klik header kolom Actions (⋯), lalu centang kembali kolom Field

### TC-FA-PREF-334: Screening modal Setup Column

15. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
16. Klik header kolom Actions (⋯), lalu klik item Setup Column...
17. Verifikasi modal Setup Column berjudul "Setup Column" dengan deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns." dan ikon `✕`
18. Verifikasi daftar kolom memuat tujuh kolom: Date, Action, Section, Field, Old Value, New Value, Modified By
19. Verifikasi tiap kolom pada daftar tercentang dan Enabled
20. Verifikasi tiap kolom pada daftar memiliki pegangan drag
21. Verifikasi tiap kolom pada daftar memiliki ikon Pin
22. Verifikasi tidak ada baris kolom tambahan yang tidak tercentang
23. Verifikasi bagian Live Preview menampilkan header kolom sesuai urutan daftar
24. Verifikasi footer memuat `[Reset to Default]` dan `[Save]` tanpa tombol `[Cancel]`
25. Klik ikon `✕` pada modal Setup Column

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC.
- Pemulihan Setup Column (8b.13, R-24): langkah "centang kembali kolom Field" memulihkan perubahan Column Visibility TC-FA-PREF-333; "Klik ikon `✕` pada modal Setup Column" di akhir TC-FA-PREF-334 menutup modal tanpa menyimpan.
- Asersi tambahan (S-03): "Verifikasi kolom Date tampil pada tabel" pada TC-FA-PREF-333 adalah anchor positif untuk asersi absence kolom Field sesudah muat ulang (8b.2); TC tidak memuatnya.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-332 sampai 334; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
