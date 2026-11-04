---
id: TC-FA-PREF-E2E-169-changelog-setup-column-pin-dan-unpin-tujuh-kolom
title: "Changelog Setup Column: Pin dan unpin tujuh kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-337
coverage:
  web: automated
---

# Changelog Setup Column: Pin dan unpin tujuh kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 9 entri contoh (PB-C1); dipakai sebagai precondition TC, tidak diasersi; seed disediakan tim FE/BE.
- Kolom yang diuji (urutan default Changelog): Date, Action, Section, Field, Old Value, New Value, Modified By.
- Lebar viewport uji membuat tabel Changelog dapat digeser secara horizontal; TC tidak menyebut lebar viewport (lihat Temuan untuk QA), nilainya disediakan tim FE.
- Pemulihan Setup Column: perubahan kolom spec ini dipulihkan dengan langkah eksplisit di spec yang sama; hook `after` menghapus preferensi kolom di browser sebagai cadangan (butir "Pemulihan Setup Column Changelog" di `suite.md`; kemampuan disediakan tim FE).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-337: Pin dan unpin tujuh kolom pada Setup Column

1. Klik ikon View history di header tab Preferences
2. Untuk setiap kolom pada tabel "Kolom yang diuji" di Prerequisites (kolom uji), lakukan langkah 3 sampai 12
3. Klik header kolom Actions (⋯), lalu klik item Setup Column...
4. Klik ikon Pin kolom uji
5. Klik `[Save]`
6. Geser tabel secara horizontal
7. Verifikasi kolom uji tetap pada posisinya saat tabel digeser horizontal
8. Klik header kolom Actions (⋯), lalu klik item Setup Column...
9. Klik ikon Pin kolom uji sekali lagi (unpin)
10. Klik `[Save]`
11. Geser tabel secara horizontal
12. Verifikasi kolom uji ikut bergeser saat tabel digeser horizontal

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 3 sampai 12 diulang untuk setiap kolom pada tabel "Kolom yang diuji" (tujuh iterasi; 8b.7); tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa (S-01).
- Alasan melewati sekitar 35 langkah (dihitung dengan ekspansi, sekitar 71): spec ini memuat satu TC (TC-FA-PREF-337) dengan tujuh iterasi identik; satu TC tepat satu spec sehingga tidak dapat dipecah. TC-FA-PREF-340 dan 341 ada di spec 112.
- Pemulihan Setup Column (8b.14, R-24): tiap iterasi di-unpin dan disimpan sebelum iterasi berikutnya, sehingga tidak ada kolom yang tetap ter-Pin.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-337; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - TC-FA-PREF-337 mensyaratkan tabel yang dapat digeser horizontal tetapi tidak menyebut lebar viewport atau jumlah kolom yang melebihi lebar modal; kemampuan itu dicatat sebagai kebutuhan tim FE.
