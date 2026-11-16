---
id: TC-FA-PREF-E2E-112-changelog-setup-column-tutup-lewat-esc-dan-kolom-terakhir-tidak-dapat-dihapus-centangnya
title: "Changelog Setup Column: tutup lewat Esc membuang perubahan, kolom terakhir tidak dapat dihapus centangnya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-340
  - TC-FA-PREF-341
sourceRules: ["§4.5#b1"]
smoke: []
dependsOn: []
trace:
  "§4.5#b1": 5
anchor: [6, 11, 12, 14]
coverage:
  web: automated
---

# Changelog Setup Column: tutup lewat Esc membuang perubahan, kolom terakhir tidak dapat dihapus centangnya

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

### TC-FA-PREF-340: Tutup Setup Column lewat Esc membuang perubahan yang belum disimpan

1. Klik ikon View history di header tab Preferences
2. Klik header kolom Actions (⋯), lalu klik item Setup Column...
3. Hapus centang kolom Field
4. Tekan tombol Esc pada keyboard
5. Verifikasi modal Setup Column tertutup
6. Verifikasi kolom Field tampil kembali pada tabel

### TC-FA-PREF-341: Kolom terakhir yang tersisa tidak dapat dihapus centangnya

7. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
8. Klik header kolom Actions (⋯), lalu klik item Setup Column...
9. Hapus centang enam kolom: Date, Action, Section, Field, Old Value, New Value
10. Arahkan kursor ke checkbox kolom Modified By
11. Verifikasi tooltip "At least one column must remain visible." tampil pada checkbox kolom Modified By
12. Verifikasi checkbox kolom Modified By berstatus Disabled
13. Coba hapus centang kolom Modified By
14. Verifikasi kolom Modified By tetap tercentang (tidak dapat dihapus centangnya)
15. Klik ikon `✕` pada modal Setup Column

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC.
- Pemulihan Setup Column (8b.14, R-24): perubahan kolom kedua TC tidak pernah disimpan; langkah "Klik ikon `✕` pada modal Setup Column" di akhir TC-FA-PREF-341 membuang perubahan yang belum disimpan. Tidak ada `[Save]` di spec ini.
- Urutan Verifikasi TC-FA-PREF-341: tooltip diasersi sebelum klik berikutnya karena state hover bersifat sementara (8b.5); karena itu butir Expected b ditulis sebelum butir a.
- Pembagian TC lintas spec: TC-FA-PREF-337 (Pin dan unpin) ada di spec 169.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-340 dan 341; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
