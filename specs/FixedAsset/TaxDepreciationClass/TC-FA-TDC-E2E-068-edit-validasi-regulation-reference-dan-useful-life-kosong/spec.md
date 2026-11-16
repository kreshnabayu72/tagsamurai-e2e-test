---
id: TC-FA-TDC-E2E-068-edit-validasi-regulation-reference-dan-useful-life-kosong
title: "Edit: Validasi Regulation Reference (Kosong, 255 Karakter, Trim) dan Useful Life Kosong"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-236
  - TC-FA-TDC-237
  - TC-FA-TDC-238
  - TC-FA-TDC-239
  - TC-FA-TDC-240
sourceRules: ["V-08", "F-FATDC-01.k4c", "V-09", "F-FATDC-01.k3c", "§4.1.2#r1", "V-11", "F-FATDC-01.k4f", "DO-01", "T-02a"]
smoke: []
dependsOn: []
trace:
  "V-08": [5, 9]
  "F-FATDC-01.k4c": [5, 9, 11]
  "V-09": 13
  "F-FATDC-01.k3c": 13
  "§4.1.2#r1": [15, 16, 29]
  "V-11": 20
  "F-FATDC-01.k4f": [20, 23]
  "DO-01": 22
  "T-02a": 27
anchor: [10, 21]
coverage:
  web: automated
---

# Edit: Validasi Regulation Reference (Kosong, 255 Karakter, Trim) dan Useful Life Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |

- Kemampuan teknis: pembacaan nilai class lewat fixture BE untuk `Verifikasi` "tidak ada data tersimpan" pada langkah 11 dan 23; disediakan tim FE/BE tanpa endpoint karangan (S-11).
- Satu-satunya Save yang berhasil adalah langkah 26 (TC-FA-TDC-239); semua Save lain diblokir validasi.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`

### TC-FA-TDC-236: Regulation Reference kosong atau hanya spasi ditolak

3. Hapus seluruh isi Regulation Reference
4. Klik `[Save]`
5. Verifikasi caption `Regulation reference must not be empty` muncul pada Regulation Reference
6. Ganti isi Regulation Reference dengan `UU HPP 7/2021; PMK 72/2023`
7. Isi Regulation Reference dengan tiga spasi (`   `)
8. Klik `[Save]`
9. Verifikasi caption `Regulation reference must not be empty` muncul pada Regulation Reference
10. Verifikasi Drawer tetap terbuka
11. Verifikasi tidak ada data tersimpan: Regulation Reference class `KHS-E1` tetap `UU HPP 7/2021; PMK 72/2023` (dibaca lewat fixture BE)

### TC-FA-TDC-237: Regulation Reference 256 karakter ditolak saat mengetik

12. Ganti isi Regulation Reference dengan 256 karakter `A`
13. Verifikasi segera setelah input caption `Max. 255 characters` muncul pada Regulation Reference

### TC-FA-TDC-238: Regulation Reference tepat 255 karakter diterima

14. Ganti isi Regulation Reference dengan 255 karakter `A`
15. Verifikasi field Regulation Reference berisi 255 karakter `A`
16. Verifikasi tidak ada caption error pada Regulation Reference

### TC-FA-TDC-240: Useful Life kosong pada Asset Type Non-building ditolak

17. Ganti isi Regulation Reference dengan `UU HPP 7/2021; PMK 72/2023`
18. Hapus seluruh isi Useful Life
19. Klik `[Save]`
20. Verifikasi caption `Useful life must not be empty` muncul pada Useful Life
21. Verifikasi Drawer tetap terbuka
22. Verifikasi dialog Save Changes tidak muncul
23. Verifikasi tidak ada data tersimpan: Useful Life class `KHS-E1` tetap `8` (dibaca lewat fixture BE)
24. Ganti isi Useful Life dengan `8`

### TC-FA-TDC-239: Regulation Reference dengan spasi tepi disimpan ter-trim

25. Ganti isi Regulation Reference dengan `  PMK 72/2023  ` (dua spasi di awal dan akhir)
26. Klik `[Save]`
27. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
28. Klik link Class Code `KHS-E1`
29. Verifikasi Regulation Reference tampil `PMK 72/2023` tanpa spasi tepi
30. Klik ikon ✕

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 Search `KHS-E1` agar baris target ada di halaman teramati (R-16, 8b.13), Search dipertahankan sampai langkah 28; langkah 6 dan 17 mengembalikan Regulation Reference ke nilai tersimpan agar caption sebelumnya hilang sebelum nilai berikutnya diasersi (R-12); langkah 24 mengembalikan Useful Life ke `8`; langkah 30 menutup Drawer yang bersih (tanpa dialog Unsaved Changes).
- Urutan TC: validasi diblokir lebih dulu (TC-FA-TDC-236, TC-FA-TDC-237, TC-FA-TDC-238, TC-FA-TDC-240), aksi sukses terakhir (TC-FA-TDC-239) (S-10). Drawer `KHS-E1` yang sama dipakai berturut-turut sampai Save sukses pada langkah 26.
- Langkah 11 dan 23 (tidak ada data tersimpan, dibaca lewat fixture BE) dan langkah 22 (dialog tidak muncul): caption error pada langkah 9 dan 20 menjadi anchor positif pada surface yang sama (8b.2). Langkah 16: langkah 15 (nilai field) menjadi anchor.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - Kolom Data Uji TC-FA-TDC-236, TC-FA-TDC-239, dan TC-FA-TDC-240 memuat nilai field lain (Class Code `KHS-R1`, `KHS-R2`, `KHS-U1`, Class Name `Kelompok uji validasi`, Asset Type, Useful Life, Allowed Methods) seperti form Create; langkah TC hanya mengubah satu field pada class `KHS-E1` yang sudah terisi, sehingga nilai itu tidak dipakai (S-15).
  - TC-FA-TDC-239 Expected b mengamati Regulation Reference di Drawer Edit `KHS-E1` setelah Save; Drawer ditutup oleh Save sukses, sehingga spec membukanya ulang pada langkah 28.
  - Post Condition "Tidak ada data berubah dan tidak ada entri log" TC-FA-TDC-236 sampai TC-FA-TDC-238 dan TC-FA-TDC-240, serta "Regulation Reference tersimpan ter-trim" pada TC-FA-TDC-239 (teramati lewat Expected b), tidak punya langkah observasi tambahan; entri log tidak diasersi (S-01).
