---
id: TC-FA-TDC-E2E-056-drawer-edit-screening-header-dan-buka-lewat-row-action
title: "Drawer Edit: Screening Tiga Zona dan Buka Lewat Row Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-177
  - TC-FA-TDC-178
coverage:
  web: automated
---

# Drawer Edit: Screening Tiga Zona dan Buka Lewat Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |

- Spec tidak mengubah data: semua blok menutup Drawer tanpa Save.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-177: Screening Drawer Edit tiga zona

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1` pada tabel
3. Verifikasi Header Drawer memuat judul `Edit Tax Depreciation Class`
4. Verifikasi Header Drawer memuat badge Status `Active` (severity success)
5. Verifikasi Header Drawer memuat ikon ✕
6. Verifikasi Header Drawer memuat satu baris teks polos di bawah judul `Class Name: Kelompok edit uji`
7. Verifikasi Body tidak memuat Alert versi Scheduled
8. Verifikasi Body: Regulation Reference * terisi `UU HPP 7/2021; PMK 72/2023`
9. Verifikasi Body: Class Code * terisi `KHS-E1`
10. Verifikasi Body: Class Code * enabled
11. Verifikasi Body: Class Name * terisi `Kelompok edit uji`
12. Verifikasi Body: Asset Type * Disabled dengan nilai `Non-building`
13. Verifikasi Body: Useful Life (years) * terisi `8`
14. Verifikasi Body: Allowed Methods * terisi `Straight Line` dan `Declining Balance`
15. Verifikasi Body: Straight Line Rate (%) berupa teks read-only `12.5`
16. Verifikasi Body: Declining Balance Rate (%) berupa teks read-only `25`
17. Verifikasi Body: Effective From berupa teks read-only `—`
18. Verifikasi Body: tautan `View versions` tampil di bawah nilai Effective From
19. Verifikasi Body: Last Posted Tax Year berupa teks read-only `—`
20. Verifikasi label Straight Line Rate (%) dan Declining Balance Rate (%) tanpa tanda `*`
21. Verifikasi Footer memuat tombol `[Clear Field]` dan `[Save]`
22. Verifikasi Footer tidak memuat checkbox `Stay on this form after submitting`, tombol `[Submit]`, dan tombol `[Cancel]`

### TC-FA-TDC-178: Buka Drawer Edit lewat row action Edit

23. Klik ikon ✕
24. Klik ikon ⋯ pada baris `KHS-E1`
25. Klik `Edit` pada overlay row action
26. Verifikasi Drawer Edit Tax Depreciation Class terbuka dengan judul `Edit Tax Depreciation Class` dan baris `Class Name: Kelompok edit uji`
27. Verifikasi isi form identik dengan pembukaan lewat link Class Code: Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `KHS-E1`, Class Name `Kelompok edit uji`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line` dan `Declining Balance`, Straight Line Rate `12.5`, Declining Balance Rate `25`
28. Klik ikon ✕

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 Search `KHS-E1` (R-16, 8b.13) agar baris target ada di halaman teramati; langkah 23 dan 28 menutup Drawer yang bersih (tanpa dialog Unsaved Changes) sebelum blok berikutnya.
- Langkah 26 dan 27 membandingkan isi form dengan nilai langkah 8 sampai 16 (R-04: nomor langkah spec kontinu).
- Urutan langkah 7 mengikuti urutan TC (Header, Body atas ke bawah, Footer); Header yang sudah tampil pada langkah 3 sampai 6 menjadi anchor permukaan untuk asersi absence langkah 7 dan 22 (8b.2).
- Pembagian TC lintas spec: TC-FA-TDC-179 dan TC-FA-TDC-32 (Header dan Effective From class dengan versi) ada di spec 235.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini. Usulan butir Lampiran A: seed idempotent, cleanup hanya yang dibuat spec, suite serial.
  - TC-FA-TDC-177 Expected b.x: "Effective From — teks read-only '—'" dan b.xi Last Posted Tax Year "—" memakai tanda pisah em-dash; spec menyalin apa adanya.
