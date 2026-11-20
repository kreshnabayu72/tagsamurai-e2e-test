---
id: TC-FA-FAAC-E2E-086-duplicate-nilai-sumber-tidak-valid-dan-versi-scheduled
title: "Duplicate Asset Class: Nilai Sumber Tidak Valid Dikosongkan dan Pre-fill dari Versi Terakhir"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-265
  - TC-FA-FAAC-674
sourceRules: ["§4.2b#p1", "R-07", "§3.8#p1", "ST-34", "§4.2f#b2", "V-19"]
smoke: []
dependsOn: []
trace:
  "§4.2b#p1": 3
  "R-07": 4
  "§3.8#p1": [6, 13, 14, 16]
  "ST-34": 7
  "§4.2f#b2": [9, 21]
  "V-19": 19
coverage:
  web: automated
---

# Duplicate Asset Class: Nilai Sumber Tidak Valid Dikosongkan dan Pre-fill dari Versi Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Class `B-DUPSRC` (memakai Asset Cost "19999 – Inactive Cost" yang kini Inactive, akun lain Active, dan Tax Depreciation Class "Bukan bangunan – Kelompok 4" yang kini Inactive); Asset Class `B-DUPSCHED` (dipakai aset; versi berlaku Straight Line, Useful Life 60; satu versi Scheduled sejak M+2 dengan Useful Life 96). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Data uji: Class Code `B-DSRC2` untuk Submit yang ditolak (literal maks 15 karakter, tidak pernah tersimpan sehingga tanpa cleanup); jam: M = bulan berjalan pada zona waktu General Settings client (NC-11).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; kemampuan baca BE untuk jumlah Asset Class.
- State global: tidak ada yang diubah (setiap form Duplicate dibuang lewat [Leave]).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Baca jumlah Asset Class sebagai baseline

### TC-FA-FAAC-674: Duplicate dari Asset Class ber-versi Scheduled mengisi tab Depreciation dari versi terakhir

2. Klik ikon "⋯" pada baris B-DUPSCHED lalu pilih "Duplicate"
3. Verifikasi halaman Detail mode Create terbuka dengan judul "Add Asset Class"
4. Verifikasi jumlah Asset Class sama dengan baseline langkah 1 (tanpa mutasi data)
5. Klik tab "Depreciation" lalu periksa Method dan Useful Life
6. Verifikasi tab Depreciation: Method "Straight Line" dan Useful Life 96 (versi terakhir, termasuk versi Scheduled), bukan 60
7. Verifikasi Alert versi Scheduled tidak tampil di area di atas bar tab karena mode Create
8. Klik breadcrumb "Asset Class"
9. Verifikasi dialog Unsaved Changes tampil
10. Klik [Leave]

### TC-FA-FAAC-265: Duplicate mengosongkan akun Inactive dan Tax Depreciation Class yang tidak Active

11. Klik ikon "⋯" pada baris B-DUPSRC lalu pilih "Duplicate"
12. Klik tab "Accounts"
13. Verifikasi akun yang Inactive (Asset Cost "19999 – Inactive Cost") dikosongkan pada field aslinya
14. Verifikasi akun yang Active tetap terisi
15. Klik tab "Depreciation"
16. Verifikasi Tax Depreciation Class yang Inactive dan Tax Method-nya dikosongkan
17. Isi Class Code `B-DSRC2`
18. Klik "Submit" tanpa memilih ulang Tax Depreciation Class
19. Verifikasi caption "Tax depreciation class must not be empty"
20. Klik breadcrumb "Asset Class"
21. Verifikasi dialog Unsaved Changes tampil
22. Klik [Leave]

## Notes

- Class Code `B-DSRC2` ditulis literal tanpa `{runId}` karena Class Code dibatasi 15 karakter (TC-98); tidak pernah tersimpan (Submit ditolak) sehingga tidak perlu cleanup.
- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 674, 265.
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-DUPSRC`, `B-DUPSCHED` adalah seed bertanda `B-*` per TC, dipakai apa adanya dan tidak diubah (hanya disalin ke form Create yang dibuang).
- Langkah penghubung (S-03): langkah 1 (baseline); langkah 8 sampai 10 dan 20 sampai 22 (menutup form dirty sesuai S-08).
- Langkah 17 menambah pengisian Class Code agar Submit dievaluasi pada Tax Depreciation Class; TC-265 tidak menyebut Class Code (Temuan untuk QA). Langkah 18 pada TC-265 memakai klik Submit yang tidak tertulis di langkah TC tetapi tersirat dari Expected.
- Temuan untuk QA: TC-265 tidak punya langkah Submit atau Class Code walau Expected menyebut Submit ditolak; TC-265 mengharapkan hanya caption Tax Depreciation Class walau Asset Cost Inactive ikut dikosongkan (apakah Asset Cost wajib tidak disebut).
