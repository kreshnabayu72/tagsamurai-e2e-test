---
id: TC-FA-TDC-E2E-130-konflik-restore-kapitalisasi-all-exist-dan-seed-dibuat-admin-lain
title: "Konflik Restore Default Classes: Kapitalisasi Class Code, Semua Seed Sudah Ada, dan Seed Dibuat Admin Lain Antara Pratinjau dan Restore"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-327
  - TC-FA-TDC-328
  - TC-FA-TDC-332
sourceRules: ["ST-23", "FATDC-LOGIC-02h", "T-10", "FATDC-LOGIC-02g", "F-FATDC-08.k2", "F-FATDC-08.k5"]
smoke: []
dependsOn: []
trace:
  "ST-23": [1, 14]
  "FATDC-LOGIC-02h": [4, 5]
  "T-10": [7, 26]
  "FATDC-LOGIC-02g": [9, 10]
  "F-FATDC-08.k2": [17, 18, 19]
  "F-FATDC-08.k5": [27, 28]
coverage:
  web: automated
---

# Konflik Restore Default Classes: Kapitalisasi Class Code, Semua Seed Sudah Ada, dan Seed Dibuat Admin Lain Antara Pratinjau dan Restore

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu perubahan state dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk tabel tanpa class sama sekali pada company/state yang disediakan tim FE khusus automation), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (dikondisikan di hook `before` lewat API; class buatan spec dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `tabelKosong` | seluruh class | tabel tanpa class sama sekali (ketujuh seed sudah dihapus), Empty State tampil |
| `nb1Kecil` | `nb-1` | Active, dibuat sesi B pada TC-FA-TDC-327 (huruf kecil) |
| `seedTujuh` | tujuh seed | `NB-1`, `NB-2`, `NB-3`, `NB-4`, `BLD-P`, `BLD-NP`, `LAND` dengan nilai seed, dibuat oleh `Restore default classes` |

- Tabel dikembalikan ke keadaan tanpa class di antara blok (langkah 12 dan 22) karena tiap blok menghasilkan class.
- Suite berjalan serial (`parallel: false`) karena tabel tanpa class adalah state company dan Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-327: Class yang Class Code-nya hanya berbeda kapitalisasi dari seed dianggap sudah ada

1. Verifikasi Empty State tabel tampil
2. Sesi B (sesi API): buat class `nb-1` (huruf kecil) Active hingga class tersimpan
3. Sesi A: klik `Restore default classes`
4. Verifikasi kode `NB-1` ada pada bagian "Skipped, already exists"
5. Verifikasi kode `NB-1` tidak ada pada bagian "To be created"
6. Klik `[Restore]`
7. Verifikasi muncul toast sukses: `Success, default classes have been restored.`
8. Ketik Search `nb-1`, tekan Enter
9. Verifikasi tabel memuat tepat satu baris dengan Class Code `nb-1`
10. Verifikasi tidak ada baris dengan Class Code `NB-1` (huruf kapital) pada hasil Search
11. Klik `(←)` pada kotak Search

### TC-FA-TDC-328: D-12 menampilkan All default classes already exist. dan Restore Disabled bila seluruh seed sudah ada dan Active

12. Pulihkan tabel ke keadaan tanpa class lewat seeding API
13. Muat ulang halaman (F5)
14. Verifikasi Empty State tabel tampil
15. Sesi B (sesi API): jalankan Restore default classes hingga ketujuh seed Active tersimpan
16. Sesi A: klik `Restore default classes`
17. Verifikasi dialog D-12 menampilkan teks `All default classes already exist.`
18. Verifikasi bagian "To be created" dan "To be reactivated" tidak tampil
19. Verifikasi tombol `[Restore]` tampil tetapi Disabled dan tombol `[Cancel]` enabled
20. Klik `[Cancel]`

### TC-FA-TDC-332: Seed dibuat admin lain antara pratinjau dan Restore, server melewati yang sudah ada

21. Pulihkan tabel ke keadaan tanpa class lewat seeding API
22. Muat ulang halaman (F5)
23. Klik `Restore default classes` (dialog D-12 tampil dengan tujuh class akan dibuat)
24. Sesi B (sesi API): buat `NB-1` dengan nilai seed hingga class tersimpan
25. Sesi A: klik `[Restore]`
26. Verifikasi muncul toast sukses: `Success, default classes have been restored.`
27. Verifikasi tabel memuat tujuh class
28. Verifikasi tabel memuat tepat satu baris Class Code `NB-1` (tidak ada duplikat)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 8 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 11 (mengosongkan Search), langkah 12 dan 21 (membentuk precondition tabel tanpa class), langkah 13 dan 22 (memuat ulang halaman agar Empty State tampil), langkah 20 (menutup dialog D-12 dengan `[Cancel]`). Langkah 1 dan 14 mengamati keadaan awal "Empty State tampil" yang dinyatakan langkah TC.
- Langkah 2, 15, dan 24 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20); sesi A tidak memuat ulang tabel antara pembukaan halaman dan pembukaan dialog D-12.
- Langkah 5 dan 18 (absence): bagian "Skipped, already exists" langkah 4 dan teks langkah 17 menjadi anchor positif pada dialog yang sama (8b.2). Langkah 10: baris `nb-1` langkah 9 menjadi anchor positif pada hasil Search yang sama; Search tidak peka kapitalisasi sehingga asersi memeriksa Class Code persis.
- Langkah 23 menulis "dialog D-12 tampil dengan tujuh class akan dibuat" sebagai keterangan keadaan dari langkah TC, bukan Expected; tidak diasersi.
- Urutan TC: TC-FA-TDC-327, TC-FA-TDC-328, TC-FA-TDC-332 (S-10).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `NB-1`, `nb-1`, dan seed lain ditulis literal tanpa suffix `{runId}-<NNN>`; kode seed bawaan dipakai TC apa adanya (S-12), dan Lampiran A konvensi belum memuat pengecualian untuk modul ini. Tabel tanpa class sama sekali disediakan tim FE pada company/state khusus automation.
  - TC-FA-TDC-332 Post Condition (entri L-01 hanya untuk enam class yang dibuat sesi A) dan Post Condition lain tanpa langkah observasi tidak diasersi (S-01, S-05).
  - TC-FA-TDC-328 langkah 2 ("Sesi B menjalankan Restore default classes hingga ketujuh seed Active") tidak menyebut mekanisme sesi B; spec memakai sesi API aktor.
  - Kolom Automation TC-FA-TDC-332 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
