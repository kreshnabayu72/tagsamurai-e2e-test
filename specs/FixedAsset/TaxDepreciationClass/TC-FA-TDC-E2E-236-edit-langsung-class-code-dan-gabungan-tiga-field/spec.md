---
id: TC-FA-TDC-E2E-236-edit-langsung-class-code-dan-gabungan-tiga-field
title: "Edit Langsung Tanpa Versi Baru: Class Code dan Gabungan Class Code, Class Name, Regulation Reference"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-191
  - TC-FA-TDC-192
coverage:
  web: automated
---

# Edit Langsung Tanpa Versi Baru: Class Code dan Gabungan Class Code, Class Name, Regulation Reference

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after` termasuk class hasil ganti kode `KHS-E1B` dan `KHS-E1C`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |

- Class Code `KHS-E1B` dan `KHS-E1C` belum ada saat spec mulai (syarat TC-FA-TDC-191 dan TC-FA-TDC-192); hook `before` memastikannya dengan menghapus sisa run sebelumnya.
- Dua blok memakai class yang sama berurutan: blok kedua (TC-FA-TDC-192) berjalan pada class hasil blok pertama (Class Code `KHS-E1B`); semua field yang diubah blok kedua berbeda dari nilai saat itu.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-191: Edit hanya Class Code (tidak terkunci)

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`
3. Ganti Class Code menjadi `KHS-E1B`
4. Klik `[Save]`
5. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
6. Verifikasi dialog Save Changes (D-09) tidak muncul
7. Verifikasi baris tabel menampilkan Class Code `KHS-E1B`
8. Verifikasi tidak ada baris dengan Class Code `KHS-E1`
9. Klik link Class Code `KHS-E1B`
10. Klik tautan `View versions`
11. Verifikasi modal Versions memuat tepat satu versi
12. Tutup modal Versions
13. Klik ikon ✕

### TC-FA-TDC-192: Edit Class Code, Class Name, dan Regulation Reference sekaligus

14. Ganti isi kotak search dengan `KHS-E1B`, tekan Enter
15. Klik link Class Code `KHS-E1B`
16. Ganti Class Code menjadi `KHS-E1C`, Class Name menjadi `Kelompok edit uji C`, Regulation Reference menjadi `UU HPP 7/2021`
17. Klik `[Save]`
18. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
19. Verifikasi dialog Save Changes (D-09) tidak muncul
20. Ganti isi kotak search dengan `KHS-E1C`, tekan Enter
21. Verifikasi baris `KHS-E1C` menampilkan Class Name `Kelompok edit uji C`
22. Klik link Class Code `KHS-E1C`
23. Klik tautan `View versions`
24. Verifikasi modal Versions memuat tepat satu versi (tidak ada versi baru)
25. Tutup modal Versions
26. Klik ikon ✕

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 14, dan 20 Search kode class agar baris target ada di halaman teramati (R-16, 8b.13); langkah 12, 13, 25, dan 26 menutup modal Versions dan Drawer yang bersih (tanpa dialog Unsaved Changes).
- Langkah 8 (baris `KHS-E1` tidak ada lagi): Search `KHS-E1` masih aktif sehingga baris `KHS-E1B` pada langkah 7 menjadi anchor positif pada surface yang sama, dan toast sukses langkah 5 membuktikan respons server selesai (8b.2). Langkah 6 dan 19 (dialog D-09 tidak muncul) memakai toast sukses sebagai anchor (8b.11).
- Pembagian TC lintas spec: TC-FA-TDC-189 dan TC-FA-TDC-190 (edit langsung Class Name dan Regulation Reference) ada di spec 059.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-191 Post Condition a dan b (entri log L-02 Class Code `KHS-E1B`; Class Code baru tercermin di dropdown Asset Class dan modal Used By) dan TC-FA-TDC-192 Post Condition (tiga entri L-02) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini (S-01).
  - TC-FA-TDC-192 memakai precondition class `KHS-E1` asli, sedangkan spec menjalankannya sesudah TC-FA-TDC-191 pada class yang sama (Class Code `KHS-E1B`); asersi TC-FA-TDC-192 tidak terpengaruh.
