---
id: TC-FA-TDC-E2E-063-edit-menutup-drawer-tanpa-perubahan-ikon-esc-backdrop-leave-dan-cancel
title: "Edit: Menutup Drawer dengan Ikon Tutup, Esc, Backdrop, Leave, dan Cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-203
  - TC-FA-TDC-204
  - TC-FA-TDC-205
  - TC-FA-TDC-206
  - TC-FA-TDC-207
coverage:
  web: automated
---

# Edit: Menutup Drawer dengan Ikon Tutup, Esc, Backdrop, Leave, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |

- Tidak ada Save di spec ini: Class Name tidak pernah berubah di server.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-203: Tutup lewat ikon ✕ tanpa perubahan

1. Ketik Search `KHS-E1`, tekan Enter
2. Klik link Class Code `KHS-E1`
3. Klik ikon ✕
4. Verifikasi Drawer langsung tertutup
5. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-FA-TDC-204: Tutup lewat Esc tanpa perubahan

6. Klik link Class Code `KHS-E1`
7. Tekan `Esc`
8. Verifikasi Drawer langsung tertutup
9. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-FA-TDC-205: Klik backdrop tidak menutup Drawer

10. Klik link Class Code `KHS-E1`
11. Klik area gelap di luar Drawer (backdrop)
12. Verifikasi Drawer tetap terbuka
13. Verifikasi dialog `Unsaved Changes` tidak muncul
14. Tekan `Esc`
15. Verifikasi Drawer tertutup

### TC-FA-TDC-206: Tutup Drawer yang berubah lewat ikon ✕, pilih Leave

16. Klik link Class Code `KHS-E1`
17. Ganti Class Name menjadi `Kelompok edit uji U`
18. Klik ikon ✕
19. Verifikasi dialog dengan teks `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Cancel]` dan `[Leave]`
20. Klik `[Leave]`
21. Verifikasi Drawer tertutup
22. Verifikasi baris `KHS-E1` menampilkan Class Name `Kelompok edit uji`
23. Verifikasi tidak ada toast

### TC-FA-TDC-207: Tutup Drawer yang berubah lewat Esc, pilih Cancel

24. Klik link Class Code `KHS-E1`
25. Ganti Class Name menjadi `Kelompok edit uji U`
26. Tekan `Esc`
27. Verifikasi dialog dengan teks `You have unsaved changes. Are you sure you want to leave?`
28. Klik `[Cancel]`
29. Verifikasi dialog tertutup
30. Verifikasi Drawer tetap terbuka dengan Class Name `Kelompok edit uji U` dipertahankan
31. Klik ikon ✕
32. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Cancel]` dan `[Leave]`
33. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 Search `KHS-E1` agar baris target ada di halaman teramati (R-16, 8b.13), Search dipertahankan sampai langkah 33; langkah 31 sampai 33 menutup form dirty secara deterministik di akhir spec (S-08, S-09).
- Langkah 5, 9, dan 13 (dialog tidak muncul): Drawer yang sudah tertutup atau tetap terbuka pada langkah 4, 8, dan 12 menjadi anchor positif pada surface yang sama (8b.2, 8b.11). Langkah 23 (tidak ada toast): Drawer tertutup pada langkah 21 dan baris tabel langkah 22 menjadi anchor.
- Langkah 22 mengamati Post Condition "Class Name tersimpan tetap" yang disebut Expected b TC-FA-TDC-206 ("Class Name tersimpan tetap 'Kelompok edit uji'").
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-E1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-206 Post Condition ("Tidak ada entri log") tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini (S-01).
  - TC-FA-TDC-205 Expected a: "dialog Unsaved Changes tidak muncul" ditulis pada form tanpa perubahan; TC tidak menguji backdrop pada form yang berubah.
