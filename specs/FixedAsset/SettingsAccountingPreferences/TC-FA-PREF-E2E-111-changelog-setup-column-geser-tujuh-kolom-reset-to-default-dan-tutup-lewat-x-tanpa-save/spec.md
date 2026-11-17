---
id: TC-FA-PREF-E2E-111-changelog-setup-column-geser-tujuh-kolom-reset-to-default-dan-tutup-lewat-x-tanpa-save
title: "Changelog Setup Column: geser tujuh kolom, Reset to Default, tutup lewat ✕ tanpa Save"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-336
  - TC-FA-PREF-338
  - TC-FA-PREF-339
sourceRules: ["§4.1.4#r1", "§4.1.4#r2", "§4.1.4#r3", "§4.1.4#r4", "§4.1.4#r5", "§4.1.4#r6", "§4.1.4#r7"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#r1": [20, 22]
  "§4.1.4#r2": [20, 22]
  "§4.1.4#r3": [20, 22]
  "§4.1.4#r4": [20, 22, 26]
  "§4.1.4#r5": [20, 22]
  "§4.1.4#r6": [20, 22]
  "§4.1.4#r7": [20, 22]
anchor: [5, 6, 9, 28, 29]
coverage:
  web: automated
---

# Changelog Setup Column: geser tujuh kolom, Reset to Default, tutup lewat ✕ tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 9 entri contoh (PB-C1); dipakai sebagai precondition TC, tidak diasersi; seed disediakan tim FE/BE.
- Kolom yang digeser (tabel "Urutan geser", dikerjakan berurutan): Date, Action, Section, Field, Old Value, New Value, Modified By; tiap kolom digeser ke posisi paling atas daftar.
- Pemulihan Setup Column: perubahan kolom spec ini dipulihkan dengan langkah eksplisit di spec yang sama; hook `after` menghapus preferensi kolom di browser sebagai cadangan (butir "Pemulihan Setup Column Changelog" di `suite.md`; kemampuan disediakan tim FE).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-336: Geser tujuh kolom pada Setup Column mengubah urutan kolom tabel setelah Save

1. Klik ikon View history di header tab Preferences
2. Klik header kolom Actions (⋯), lalu klik item Setup Column...
3. Untuk setiap kolom pada tabel "Urutan geser" di Prerequisites (kolom uji), secara berurutan, lakukan langkah 4
4. Geser kolom uji ke posisi paling atas daftar
5. Verifikasi Live Preview menampilkan urutan Modified By, New Value, Old Value, Field, Section, Action, Date
6. Verifikasi header tabel menampilkan urutan Modified By, New Value, Old Value, Field, Section, Action, Date
7. Klik `[Save]`
8. Muat ulang halaman dengan F5, lalu klik ikon View history untuk membuka kembali modal Changelog
9. Verifikasi urutan kolom tabel tetap Modified By, New Value, Old Value, Field, Section, Action, Date
10. Klik header kolom Actions (⋯), lalu klik item Setup Column...
11. Klik `[Reset to Default]`
12. Klik `[Save]`

### TC-FA-PREF-338: Reset to Default mengembalikan konfigurasi kolom ke bawaan setelah Save

13. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
14. Klik header kolom Actions (⋯), lalu klik item Setup Column...
15. Hapus centang kolom Field
16. Geser kolom Date ke posisi terakhir daftar
17. Klik `[Save]`
18. Klik header kolom Actions (⋯), lalu klik item Setup Column...
19. Klik `[Reset to Default]`
20. Verifikasi Live Preview menampilkan tujuh kolom dengan urutan Date, Action, Section, Field, Old Value, New Value, Modified By
21. Klik `[Save]`
22. Verifikasi tabel menampilkan tujuh kolom dengan urutan bawaan Date, Action, Section, Field, Old Value, New Value, Modified By

### TC-FA-PREF-339: Tutup Setup Column lewat [✕] membuang perubahan yang belum disimpan

23. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
24. Klik header kolom Actions (⋯), lalu klik item Setup Column...
25. Hapus centang kolom Field
26. Verifikasi tabel di balik modal langsung tidak menampilkan kolom Field (preview)
27. Klik ikon `✕` pada modal Setup Column
28. Verifikasi modal Setup Column tertutup
29. Verifikasi kolom Field tampil kembali pada tabel

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC.
- Langkah 4 diulang untuk setiap kolom pada tabel "Urutan geser" (tujuh iterasi; 8b.7); tanpa langkah bersyarat. Jumlah langkah dengan ekspansi sekitar 34.
- Pemulihan Setup Column (8b.14, R-24): tiga langkah di akhir TC-FA-PREF-336 ("Klik header kolom Actions (⋯), lalu klik item Setup Column...", "Klik `[Reset to Default]`", "Klik `[Save]`") memulihkan urutan kolom ke default sebelum TC-FA-PREF-338; TC-FA-PREF-338 berakhir pada urutan bawaan; TC-FA-PREF-339 tidak menyimpan perubahan.
- Langkah TC-FA-PREF-338 "geser kolom Date ke posisi terakhir" disalin apa adanya (8b.13).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-336, 338, dan 339; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - TC-FA-PREF-336 langkah 3 sampai 9 menyebut tujuh pergeseran berurutan tanpa menyebut posisi akhir tiap langkah; spec hanya mengasersi urutan akhir (Expected a dan b).
