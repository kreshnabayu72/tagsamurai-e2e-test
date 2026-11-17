---
id: TC-FA-TDC-E2E-124-konflik-dua-admin-edit-class-name-dan-class-dihapus-saat-save
title: "Konflik Dua Admin: Edit Class Name Bersamaan dan Class Dihapus Saat Save"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-201
  - TC-FA-TDC-202
sourceRules: ["T-02a", "F-FATDC-02.k4a", "T-13", "F-FATDC-02.k12b"]
smoke: []
dependsOn: []
trace:
  "T-02a": [8, 11]
  "F-FATDC-02.k4a": [12, 13]
  "T-13": [20, 22]
  "F-FATDC-02.k12b": 21
coverage:
  web: automated
---

# Konflik Dua Admin: Edit Class Name Bersamaan dan Class Dihapus Saat Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Akun sesi B: Total Control kedua (akun berbeda). Email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). TC-FA-TDC-201 memakai sesi B sebagai konteks browser kedua yang hasilnya diasersi (login di langkah 1); TC-FA-TDC-202 memakai sesi API aktor sesi B hanya untuk menghapus class.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |

- `KHS-E1` diseed ulang lewat API di antara dua blok (langkah 15) karena TC-FA-TDC-201 mengubah Class Name dan TC-FA-TDC-202 menghapus class.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-201: Dua admin menyimpan Edit Class Name yang sama hampir bersamaan, last-write-wins

1. Buka konteks browser kedua (sesi B), login sebagai Total Control kedua dengan `Spectra.env.FA_TC_B_PASSWORD`, lalu buka Settings > Accounting > Tax Depreciation Class
2. Sesi A: ketik Search `KHS-E1`, tekan Enter
3. Sesi B: ketik Search `KHS-E1`, tekan Enter
4. Sesi A: klik link Class Code `KHS-E1`
5. Sesi B: klik link Class Code `KHS-E1`
6. Sesi A: ganti Class Name menjadi `Kelompok A`
7. Sesi A: klik `[Save]`
8. Verifikasi sesi A muncul toast sukses: `Success, tax depreciation class has been updated.`
9. Sesi B: ganti Class Name menjadi `Kelompok B`
10. Sesi B: klik `[Save]`
11. Verifikasi sesi B muncul toast sukses: `Success, tax depreciation class has been updated.`
12. Verifikasi sesi B tidak ada dialog konflik
13. Verifikasi baris `KHS-E1` di tabel sesi B menampilkan Class Name `Kelompok B`
14. Tutup konteks browser sesi B

### TC-FA-TDC-202: Save Edit pada class yang sudah dihapus admin lain

15. Pulihkan class `KHS-E1` lewat seeding API ke nilai awal (Class Name `Kelompok edit uji`)
16. Sesi A: klik link Class Code `KHS-E1`
17. Sesi A: ganti Class Name menjadi `Kelompok X`
18. Sesi B (sesi API): hapus class `KHS-E1` hingga class terhapus di server
19. Sesi A: klik `[Save]`
20. Verifikasi muncul toast info: `This tax depreciation class is no longer available.`
21. Verifikasi Drawer tertutup
22. Verifikasi tabel disegarkan dan tidak memuat baris `KHS-E1`
23. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2, 3, dan 16 (Search atau membuka baris target; R-16, 8b.13; langkah 16 memakai Search langkah 2 yang masih aktif di sesi A), langkah 14 (menutup konteks sesi B; S-09), langkah 15 (membentuk precondition TC-FA-TDC-202), langkah 23 (mengosongkan Search).
- Langkah 18 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ... " (R-20); sesi B pada TC-FA-TDC-201 memakai UI karena Expected a mengasersi toast dan dialog di sesi B.
- Langkah 22 (absence): toast info langkah 20 adalah respons server yang sudah diasersi dan menjadi anchor positif untuk hilangnya baris (8b.2).
- Langkah 12 (tidak ada dialog konflik): toast sukses langkah 11 menjadi anchor bahwa respons server sudah diproses (8b.2).
- Langkah 13 mengamati nilai akhir Class Name di tabel sesi B setelah Drawer tertutup dan tabel disegarkan.
- Urutan TC: TC-FA-TDC-201 lalu TC-FA-TDC-202 (S-10, aksi menghapus data di akhir).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-201 Post Condition (dua entri L-02 terpisah untuk Class Name, A lalu B) dan TC-FA-TDC-202 Post Condition (tidak ada entri log untuk Save sesi A, tidak ada data berubah) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini (S-01, S-05).
  - TC-FA-TDC-201 menyebut "hampir bersamaan" tanpa menjamin timing race; spec menyimpan sesi A lebih dulu lalu sesi B.
  - Kolom Automation TC-FA-TDC-201 dan TC-FA-TDC-202 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
