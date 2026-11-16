---
id: TC-FA-TDC-E2E-125-konflik-d-13-class-code-terkunci-saat-drawer-terbuka
title: "Konflik D-13: Class Code Terkunci Saat Drawer Edit Terbuka, Penolakan Save, Screening Dialog, dan Tombol OK"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-210
  - TC-FA-TDC-211
  - TC-FA-TDC-212
sourceRules: ["F-FATDC-02.k3c", "D-13", "F-FATDC-02.k3d", "ST-06", "FATDC-LOGIC-07a", "F-FATDC-02.k3b"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-02.k3c": 7
  "D-13": [8, 9, 10, 11, 12]
  "F-FATDC-02.k3d": 15
  "ST-06": 15
  "FATDC-LOGIC-07a": 16
  "F-FATDC-02.k3b": [19, 20, 21]
anchor: [14, 17]
coverage:
  web: automated
---

# Konflik D-13: Class Code Terkunci Saat Drawer Edit Terbuka, Penolakan Save, Screening Dialog, dan Tombol OK

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): fixture BE yang memajukan Last Posted Tax Year `KHS-D13` ke 2026 (menyerupai posting penyusutan fiskal J-03; kemampuan disediakan tim FE/BE). Sesi B tidak membuka UI dan hasilnya tidak diasersi.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk class berkunci), flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsD13` | `KHS-D13` | Non-building, Used By 0, Last Posted Tax Year kosong (Class Code belum terkunci), Class Name `Kelompok D13`, Active |

- Ketiga TC memiliki precondition dan langkah 1 sampai 4 yang identik, sehingga dijalankan sebagai satu alur dengan satu pembukaan Drawer (lihat Notes). Last Posted Tax Year `KHS-D13` dipulihkan ke kosong di hook `after`.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-210, TC-FA-TDC-211, dan TC-FA-TDC-212: Save mengubah Class Code setelah kunci berubah, screening dialog D-13, dan tombol OK

1. Ketik Search `KHS-D13`, tekan Enter
2. Catat baseline jumlah entri Changelog class `KHS-D13` lewat fixture BE
3. Klik link Class Code `KHS-D13` (Drawer Edit; Class Code enabled)
4. Fixture BE (sesi B): majukan Last Posted Tax Year `KHS-D13` ke 2026 hingga tersimpan
5. Ganti Class Code menjadi `KHS-D13B`
6. Klik `[Save]`
7. Verifikasi dialog D-13 muncul
8. Verifikasi header dialog berjudul `Cannot Save Tax Depreciation Class`
9. Verifikasi body memuat bullet `• KHS-D13 – Kelompok D13`
10. Verifikasi body memuat teks `The class code has been locked by another action. The page has been reloaded with the latest lock status.`
11. Verifikasi footer memuat satu tombol `[OK]`
12. Verifikasi tidak ada tombol `[Cancel]` pada footer
13. Klik `[OK]` pada dialog D-13
14. Verifikasi dialog D-13 tertutup
15. Verifikasi Drawer memuat ulang status kunci: Class Code Disabled dengan ikon gembok bernilai `KHS-D13`
16. Verifikasi Last Posted Tax Year `2026`
17. Verifikasi tidak ada toast
18. Klik ikon ✕ pada Drawer
19. Verifikasi baris `KHS-D13` di tabel menampilkan Class Code `KHS-D13`
20. Verifikasi tidak ada baris `KHS-D13B` di tabel
21. Verifikasi jumlah entri Changelog class `KHS-D13` sama dengan baseline langkah 2
22. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC dalam satu alur: TC-FA-TDC-210 (langkah 1 sampai 6 dan Expected a, b, c pada langkah 7, 20, dan 21), TC-FA-TDC-211 (Expected a, b, c pada langkah 8 sampai 12), TC-FA-TDC-212 (langkah 13 dan Expected a, b, c pada langkah 14 sampai 17). Ketiga TC berbagi precondition dan langkah 1 sampai 4 yang identik; Expected tiap TC tetap punya `Verifikasi` sendiri (S-01) dan urutan langkah mengikuti urutan state dialog (8b.5). Expected b TC-FA-TDC-210 (Class Code tersimpan tetap `KHS-D13`; tidak ada yang tersimpan) diasersi di tabel pada langkah 19 dan 20 setelah Drawer ditutup.
- Langkah penghubung (S-03): langkah 1 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 2 (baseline Changelog, S-12), langkah 18 (menutup Drawer yang bersih sesudah dimuat ulang), langkah 22 (mengosongkan Search).
- Langkah 17 (tidak ada toast): dialog D-13 tertutup pada langkah 14 dan Drawer sudah dimuat ulang pada langkah 15 sebagai anchor positif (8b.2, 8b.11).
- Langkah 20 (absence): baris `KHS-D13` tampil pada Search yang sama pada langkah 19 sebagai anchor positif (8b.2).
- Langkah 21 (Expected c TC-FA-TDC-210, tidak ada entri log dari Save ini): asersi absence log ditulis di spec ini dengan baseline karena TC ini tidak dimuat spec absence dan keadaan dua sesi baru dibentuk pada langkah 4 (P-1, S-05); dialog D-13 pada langkah 7 menjadi anchor bahwa Save sudah diproses server.
- Temuan untuk QA:
  - Email akun Total Control sesi A tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-D13` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-211 dan TC-FA-TDC-212 tidak menyebut Class Name di bagian kolom Data Uji untuk TC-FA-TDC-212 (precondition hanya "Class Code belum terkunci"); spec memakai class `KHS-D13` dengan Class Name `Kelompok D13` seperti TC-FA-TDC-211.
  - TC-FA-TDC-210 menulis "Tidak ada yang tersimpan" pada Expected b tanpa menyebut cara mengamatinya; spec mengamati lewat baris tabel (langkah 19 dan 20).
  - Kolom Automation TC-FA-TDC-210, TC-FA-TDC-211, dan TC-FA-TDC-212 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
