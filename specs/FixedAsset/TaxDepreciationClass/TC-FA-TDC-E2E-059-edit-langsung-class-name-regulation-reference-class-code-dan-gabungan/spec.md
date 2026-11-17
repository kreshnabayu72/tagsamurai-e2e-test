---
id: TC-FA-TDC-E2E-059-edit-langsung-class-name-regulation-reference-class-code-dan-gabungan
title: "Edit Langsung Tanpa Versi Baru: Class Name dan Regulation Reference"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-189
  - TC-FA-TDC-190
sourceRules: ["T-02a", "F-FATDC-02.k11a", "§4.1.2#p4", "§4.1.1#r3", "FATDC-LOGIC-04ad", "FATDC-LOGIC-04c", "FATDC-LOGIC-04p.2", "FATDC-LOGIC-04m"]
smoke: []
dependsOn: []
trace:
  "T-02a": [5, 18]
  "F-FATDC-02.k11a": [6, 19]
  "§4.1.2#p4": [6, 19]
  "§4.1.1#r3": 8
  "FATDC-LOGIC-04ad": [11, 22]
  "FATDC-LOGIC-04c": [11, 22, 23]
  "FATDC-LOGIC-04p.2": 12
  "FATDC-LOGIC-04m": 23
anchor: [7]
coverage:
  web: automated
---

# Edit Langsung Tanpa Versi Baru: Class Name dan Regulation Reference

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |

- Dua blok memakai class yang sama berurutan: blok kedua (TC-FA-TDC-190) berjalan pada class hasil blok pertama (Class Name `Kelompok edit uji A`); nilai yang diasersi blok kedua (Regulation Reference) tidak bergantung pada Class Name.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-189: Edit hanya Class Name tersimpan langsung (T-02a)

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`
3. Ganti Class Name menjadi `Kelompok edit uji A`
4. Klik `[Save]`
5. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
6. Verifikasi dialog Save Changes (D-09) tidak muncul
7. Verifikasi Drawer Edit tertutup
8. Verifikasi baris `KHS-E1` menampilkan Class Name `Kelompok edit uji A` (tabel menampilkan data terbaru)
9. Klik link Class Code `KHS-E1`
10. Klik tautan `View versions`
11. Verifikasi modal Versions memuat tepat satu versi
12. Verifikasi versi tersebut berstatus `Current`
13. Tutup modal Versions
14. Klik ikon ✕

### TC-FA-TDC-190: Edit hanya Regulation Reference menimpa dasar hukum versi terakhir

15. Klik link Class Code `KHS-E1`
16. Ganti Regulation Reference menjadi `PMK 72/2023`
17. Klik `[Save]`
18. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
19. Verifikasi dialog Save Changes (D-09) tidak muncul
20. Klik link Class Code `KHS-E1`
21. Klik tautan `View versions`
22. Verifikasi modal Versions memuat tepat satu versi
23. Verifikasi versi tersebut memiliki Regulation Reference `PMK 72/2023`
24. Tutup modal Versions
25. Klik ikon ✕

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 Search `KHS-E1` agar baris target ada di halaman teramati (R-16, 8b.13), Search dipertahankan sampai langkah 25; langkah 13, 14, 24, dan 25 menutup modal Versions dan Drawer yang bersih (tanpa dialog Unsaved Changes). Langkah 15 dan 20 tidak mengulang Search karena kotak Search masih berisi `KHS-E1` dan baris itu masih tampil.
- Langkah 6 dan 19 (dialog D-09 tidak muncul): toast sukses pada langkah 5 dan 18 menjadi anchor positif bahwa respons server sudah diproses (8b.2, 8b.11).
- Pembagian TC lintas spec: TC-FA-TDC-191 dan TC-FA-TDC-192 (edit langsung Class Code dan gabungan tiga field) ada di spec 236.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-189 Post Condition b dan c (entri log L-02 untuk Class Name; Class Name baru tercermin di dropdown Asset Class dan modal Used By) dan TC-FA-TDC-190 Post Condition b (entri log L-02 untuk Regulation Reference) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini (S-01). Post Condition a pada kedua TC ("tidak ada versi baru") sudah teramati lewat Expected modal Versions.
  - TC-FA-TDC-190 memakai precondition class `KHS-E1` dengan Class Name `Kelompok edit uji`, sedangkan spec menjalankannya berurutan sesudah TC-FA-TDC-189 (Class Name `Kelompok edit uji A`); hasil asersi TC-FA-TDC-190 tidak terpengaruh.
