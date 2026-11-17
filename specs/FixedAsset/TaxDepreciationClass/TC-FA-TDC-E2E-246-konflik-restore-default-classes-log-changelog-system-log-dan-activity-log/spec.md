---
id: TC-FA-TDC-E2E-246-konflik-restore-default-classes-log-changelog-system-log-dan-activity-log
title: "Konflik Restore Default Classes: Log Create per Class Dibuat dan Edit per Class Diaktifkan Kembali di Tiga Surface Log"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-674
sourceRules: ["ST-23", "§8.4#r5", "L-01", "§4.1.1#r31", "L-04", "§8.2#p1", "§8.2#r1", "§8.3#p1"]
smoke: []
dependsOn: []
trace:
  "ST-23": 1
  "§8.4#r5": [8, 11, 16, 20]
  "L-01": 9
  "§4.1.1#r31": 9
  "L-04": 10
  "§8.2#p1": 14
  "§8.2#r1": 15
  "§8.3#p1": [18, 19]
coverage:
  web: automated
---

# Konflik Restore Default Classes: Log Create per Class Dibuat dan Edit per Class Diaktifkan Kembali di Tiga Surface Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control Rina Puspita (tampil sebagai "Rina P" pada Modified By), company uji Fixed Asset. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi lain): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi lain hanya menyiapkan `NB-1` Active dan `NB-2` Inactive setelah halaman dibuka dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk tabel tanpa class sama sekali pada company/state yang disediakan tim FE khusus automation), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah entri Changelog, System Log Detail User Rina Puspita, dan Activity Log lewat fixture BE (disediakan tim FE/BE) untuk baseline (S-12).
- Sumber baca (8b.10, S-14): baseline (langkah 3) dan jumlah entri sesudah pemicu (langkah 8, 14, dan 18) dibaca lewat kemampuan baca fixture BE yang sama. Isi baris log (langkah 9 sampai 11, 15 sampai 16, dan 19 sampai 20) dibaca di UI tiap surface (modal Changelog, Tab System Log Detail User Rina Puspita, tab `User Action` Activity Log) sesudah selisih jumlah dibuktikan.
- Data milik spec (dikondisikan di hook `before` lewat API; class buatan spec dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `tabelKosong` | seluruh class | tabel tanpa class sama sekali (ketujuh seed sudah dihapus), Empty State tampil |
| `seedNb1` | `NB-1` | Active, dibuat sesi lain setelah halaman dibuka (dilewati oleh Restore) |
| `seedNb2` | `NB-2` | Inactive, dibuat sesi lain setelah halaman dibuka (diaktifkan kembali oleh Restore) |
| `seedBaru` | `NB-3`, `NB-4`, `BLD-P`, `BLD-NP`, `LAND` | dibuat oleh `Restore default classes` dengan nilai seed; Asset Type `NB-3` dan `NB-4` Non-building, `BLD-P` dan `BLD-NP` Building, `LAND` Land |

- Suite berjalan serial (`parallel: false`) karena tabel tanpa class adalah state company dan Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-674: Log Restore default classes, satu L-01 per class dibuat dan satu L-04 per class diaktifkan kembali

1. Verifikasi Empty State tabel tampil
2. Sesi lain (sesi API): buat `NB-1` (Active) dan `NB-2` (Active lalu nonaktifkan sehingga Inactive) hingga keduanya tersimpan
3. Catat baseline jumlah entri Changelog, System Log Detail User Rina Puspita, dan Activity Log lewat fixture BE
4. Klik `Restore default classes`
5. Klik `[Restore]`
6. Tunggu aksi selesai
7. Klik ikon Changelog di toolbar
8. Verifikasi lewat fixture BE jumlah entri Changelog bertambah tepat 11 dari baseline langkah 3
9. Verifikasi Changelog memuat 10 baris Create untuk `NB-3`, `NB-4`, `BLD-P`, `BLD-NP`, dan `LAND`: masing-masing satu baris Field "Class Code" dengan Old Value "—" dan New Value "[kode]" dan satu baris Field "Asset Type" dengan Old Value "—" dan New Value "[Asset Type]", Modified By "Rina P"
10. Verifikasi Changelog memuat satu baris Edit untuk `NB-2` dengan Field "Status", Old Value "Inactive", New Value "Active", Modified By "Rina P"
11. Verifikasi Changelog tidak memuat baris untuk `NB-1`
12. Tutup modal Changelog
13. Buka Detail User Rina Puspita > Tab System Log
14. Verifikasi lewat fixture BE jumlah entri System Log bertambah tepat 11 dari baseline langkah 3
15. Verifikasi System Log memuat 10 baris Create dan satu baris Edit dengan pola yang sama (Object "Tax Depreciation Class", Name "[kode]")
16. Verifikasi System Log tidak memuat baris untuk `NB-1`
17. Buka `Reports & Logs > Activity Log`, tab `User Action`
18. Verifikasi lewat fixture BE jumlah entri Activity Log bertambah tepat 11 dari baseline langkah 3
19. Verifikasi Activity Log memuat 10 baris Create dan satu baris Edit dengan pola yang sama (Modified By "Rina P")
20. Verifikasi Activity Log tidak memuat baris untuk `NB-1`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 3 (baseline, S-12, 8b.10), langkah 6 ("Tunggu aksi selesai" tanpa `Verifikasi`; menunggu `[Restore]` selesai sebelum membuka Changelog, 8b.8), langkah 12 (menutup modal Changelog), langkah 13 dan 17 (membuka surface log lain). Langkah 1 mengamati keadaan awal "Empty State tampil" yang dinyatakan langkah TC.
- Langkah 2 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ... tersimpan" (R-20); halaman sesi A sudah dibuka sebelum sesi lain menyiapkan `NB-1` dan `NB-2`.
- Langkah 9, 15, dan 19 (isi baris log): entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih jumlah dari baseline dibuktikan (langkah 8, 14, 18); karena banyak entri jatuh dalam menit yang sama, spec mengasersi himpunan 11 baris teratas tanpa mengandalkan urutan di antaranya (S-14).
- Langkah 11, 16, dan 20 (Expected d, tidak dicatat untuk `NB-1`): asersi absence ditulis dengan anchor positif, yaitu baris `NB-2` atau `NB-3` pada surface yang sama (langkah 10, 15, dan 19), dan selisih 11 terhadap baseline (8b.2). Asersi ini ditulis di spec ini karena TC-FA-TDC-674 tidak dimuat spec absence dan state tabel kosong dengan dua sesi baru dibentuk pada langkah 2 (P-1, S-05).
- Temuan untuk QA:
  - Email akun Total Control Rina Puspita dan akun sesi lain tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `NB-1` sampai `NB-4`, `BLD-P`, `BLD-NP`, `LAND` ditulis literal tanpa suffix `{runId}-<NNN>`; kode seed bawaan dipakai TC apa adanya (S-12), dan Lampiran A konvensi belum memuat pengecualian untuk modul ini. Tabel tanpa class sama sekali disediakan tim FE pada company/state khusus automation.
  - TC-FA-TDC-674 Expected a, b, c menyebut "Dicatat: 10 baris Create ..." dalam bentuk total absolut; spec membuktikan selisih 11 terhadap baseline karena audit trail permanen (S-12).
  - TC-FA-TDC-674 Expected a menulis New Value "[Asset Type]" tanpa menyebut nilainya per class; spec mengambil Asset Type seed dari fixture.
  - Kolom Automation TC-FA-TDC-674 memuat `Automatable`; TC ini memuat dua konteks sehingga masuk spec kelas c.
