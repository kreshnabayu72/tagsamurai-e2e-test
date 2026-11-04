---
id: TC-FA-TDC-E2E-057-drawer-edit-field-disabled-class-code-terkunci-class-land-building-dan-inactive
title: "Drawer Edit: Last Posted Tax Year, Class Code Terkunci, Class Inactive, dan Asset Type Disabled"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-180
  - TC-FA-TDC-181
  - TC-FA-TDC-182
  - TC-FA-TDC-183
  - TC-FA-TDC-185
  - TC-FA-TDC-186
coverage:
  web: automated
---

# Drawer Edit: Last Posted Tax Year, Class Code Terkunci, Class Inactive, dan Asset Type Disabled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk class berkunci dengan Last Posted Tax Year terisi), flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data (seed idempotent di hook `before` lewat API, dihapus di hook `after` untuk class `KHS-*`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |
| `khsLck` | `KHS-LCK` | Non-building, Useful Life `10`, Straight Line dan Declining Balance, Active, Used By 0, Last Posted Tax Year `2026` (Class Code terkunci) |
| `nbOld` | `NB-OLD` | Pre-setup Example Data: Inactive, Used By 0; hanya dibuka dan ditutup tanpa Save, tidak diubah |
| `lhnE1` | `LHN-E1` | Asset Type Land, Active, Used By 0 |
| `bgnE1` | `BGN-E1` | Asset Type Building, Useful Life `20`, Straight Line, Active, Used By 0 |

- Seluruh blok menutup Drawer tanpa Save; tidak ada data yang diubah.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-180: Last Posted Tax Year read-only

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`
3. Verifikasi Last Posted Tax Year bernilai `—`
4. Klik ikon ✕
5. Ganti isi kotak search dengan `KHS-LCK`, tekan Enter
6. Klik link Class Code `KHS-LCK`
7. Verifikasi Last Posted Tax Year bernilai `2026`
8. Klik field Last Posted Tax Year dan coba ketik `2030`
9. Verifikasi field Last Posted Tax Year tidak menerima input: nilai tetap `2026`

### TC-FA-TDC-183: Class Code Disabled dengan ikon gembok dan tooltip

10. Arahkan kursor ke field Class Code
11. Verifikasi tooltip `Code can't be changed after fiscal depreciation has been posted.` muncul
12. Verifikasi Class Code tampil Disabled dengan ikon gembok
13. Coba ketik `ABC` pada field Class Code
14. Verifikasi nilai Class Code tetap `KHS-LCK`
15. Verifikasi field Class Name dan Regulation Reference tetap enabled
16. Klik ikon ✕

### TC-FA-TDC-181: Badge Status dan edit untuk class Inactive

17. Ganti isi kotak search dengan `NB-OLD`, tekan Enter
18. Klik link Class Code `NB-OLD`
19. Verifikasi badge Status `Inactive` (severity danger) tampil di header
20. Verifikasi field Drawer enabled
21. Verifikasi tombol `[Save]` tampil
22. Klik ikon ✕

### TC-FA-TDC-182: Asset Type Disabled

23. Ganti isi kotak search dengan `KHS-E1`, tekan Enter
24. Klik link Class Code `KHS-E1`
25. Klik Select Asset Type
26. Verifikasi Select Asset Type Disabled tetap tampil dengan nilai `Non-building` dan tidak membuka daftar opsi
27. Verifikasi nilai Asset Type tidak berubah: `Non-building`
28. Klik ikon ✕

### TC-FA-TDC-185: Drawer Edit class Land

29. Ganti isi kotak search dengan `LHN-E1`, tekan Enter
30. Klik link Class Code `LHN-E1`
31. Verifikasi Useful Life, Allowed Methods, Straight Line Rate, dan Declining Balance Rate tampil Disabled dengan helper `Land is not depreciated.`
32. Verifikasi nilai keempat field kosong
33. Verifikasi Asset Type Disabled dengan nilai `Land`
34. Klik ikon ✕

### TC-FA-TDC-186: Drawer Edit class Building

35. Ganti isi kotak search dengan `BGN-E1`, tekan Enter
36. Klik link Class Code `BGN-E1`
37. Buka dropdown Allowed Methods
38. Arahkan kursor ke opsi `Declining Balance`
39. Verifikasi opsi `Declining Balance` tampil Disabled dengan tooltip `Declining balance does not apply to buildings.`
40. Verifikasi opsi `Straight Line` terpilih
41. Verifikasi opsi `Straight Line` enabled
42. Tutup dropdown Allowed Methods
43. Klik ikon ✕

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 17, 23, 29, dan 35 Search kode class agar baris target ada di halaman teramati (R-16, 8b.13); langkah 4, 16, 22, 28, 34, dan 43 menutup Drawer yang bersih (tanpa dialog Unsaved Changes); langkah 42 menutup dropdown.
- Urutan TC: TC-FA-TDC-180, TC-FA-TDC-183, TC-FA-TDC-181, TC-FA-TDC-182, TC-FA-TDC-185, TC-FA-TDC-186 (S-10).
- Alasan spec melewati sekitar 35 langkah: seluruh blok memeriksa keadaan field Drawer Edit per jenis class (berkunci, Inactive, Land, Building) tanpa Save dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah pembuka berulang per blok (Search, klik link, tutup) dan `Verifikasi` per klausa (S-01) membentuk jumlah langkah. TC-FA-TDC-183 dilanjutkan pada Drawer `KHS-LCK` yang sama dengan langkah 6 sampai 9 TC-FA-TDC-180; langkah buka Drawer TC-FA-TDC-183 (klik link Class Code `KHS-LCK`) sudah dilakukan pada langkah 6 (S-04). Langkah 13 mengetik `ABC`: TC tidak menyebut nilai yang diketik.
- Hover pada langkah 10 dan tooltip langkah 11 diasersi sebelum langkah berikutnya mengubah state (8b.5).
- Hover langkah 38 dan tooltip langkah 39 diasersi sebelum langkah berikutnya mengubah state (8b.5).
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-*` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini. Usulan butir Lampiran A: seed idempotent, cleanup hanya yang dibuat spec, suite serial.
  - TC-FA-TDC-183 langkah 3 ("Coba ketik pada field Class Code") tidak menyebut nilai yang diketik; spec memakai `ABC`.
  - TC-FA-TDC-181 memakai `NB-OLD` (Pre-setup) sebagai objek buka saja; tidak diubah.
