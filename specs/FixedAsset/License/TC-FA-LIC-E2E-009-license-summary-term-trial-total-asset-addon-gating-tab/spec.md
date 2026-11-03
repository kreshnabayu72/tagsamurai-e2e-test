---
id: TC-FA-LIC-E2E-009-license-summary-term-trial-total-asset-addon-gating-tab
title: "License Summary Term Trial: Total Asset, Addon, Concurrent User, dan Gating Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-589
  - TC-FA-LIC-590
  - TC-FA-LIC-591
coverage:
  web: automated
---

# License Summary Term Trial: Total Asset, Addon, Concurrent User, dan Gating Tab

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control client Trial plan Free Pre-setup #32 `totalControlTrialFree_automated_{namaCompany}@qwertysystem.net` (hanya term Trial Active, plan term `rank=0`; Trial Asset Quota 200 dengan cap plan Free 500, Trial Concurrent User Quota 3 dengan 2 sesi aktif (aktor dan satu sesi lain), Used 40, Reserved 2, Unmanaged 1; ledger Add-on term Trial berisi lima addon dengan Total 200: Audit Used 5, Tracking Used 0, Maintenance Used 3, Maps Used 0, IT Inventory Used 0; approval OFF; kredensial `Spectra.env.FA_TRIALFREE_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit di langkah 16 sampai 18): Total Control client Trial plan Enterprise Pre-setup #33 `totalControlTrialPaid_automated_{namaCompany}@qwertysystem.net` (hanya term Trial Active, plan term Enterprise `rank≥1` Paid, `License allocation per group` ON; Trial Asset Quota 300, Used 10, Reserved 0, Unmanaged 0; kredensial `Spectra.env.FA_TRIALPAID_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1).
- Data: hanya dibaca, tidak ada state yang diubah. Sesi aktif kedua pada client #32 (selain sesi UI aktor) disediakan tim FE/BE. Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Client Trial plan Free: License Summary dan gating (TC-FA-LIC-589)

1. Verifikasi kolom `Asset`: `Total` = 200 (Trial Asset Quota), bukan 500 (cap konfigurasi plan tidak dipakai untuk term Trial walau plan `rank=0` (Free))
2. Verifikasi kolom `Asset`: `Used` = 40, `Reserved` = 2, `Remaining` = 158 (200 − 40 − 2), `Unmanaged` = 1
3. Verifikasi kolom `+ Audit`: `Total` 200, `Used` 5, `Remaining` 195
4. Verifikasi kolom `+ Tracking`: `Total` 200, `Used` 0, `Remaining` 200
5. Verifikasi kolom `+ Maintenance Routine`: `Total` 200, `Used` 3, `Remaining` 197
6. Verifikasi kolom `+ Maps`: `Total` 200, `Used` 0, `Remaining` 200
7. Verifikasi kolom `+ IT Inventory`: `Total` 200, `Used` 0, `Remaining` 200
8. Verifikasi `Reserved` dan `Unmanaged` kolom addon `—`
9. Verifikasi kolom `+ Repair Ticketing` identik dengan `+ Maintenance Routine` (`Total` 200, `Used` 3, `Remaining` 197; satu ledger)
10. Verifikasi tidak ada kolom addon yang menampilkan `Not Available`
11. Verifikasi Tabs: `All License | Concurrent User` (Tab `Allocation Quota` tidak dirender)
12. Verifikasi Sub-Tab `Subscription History` dan `Allocation History` tidak dirender

### Client Trial plan Free: Concurrent User (TC-FA-LIC-591)

13. Klik Tab `Concurrent User`
14. Verifikasi Metric Summary Bar `Online Users: 2/3` (Total = Trial Concurrent User Quota)
15. Verifikasi Tab `Concurrent User` tersedia dan daftar memuat dua baris sesi

### Client Trial plan Enterprise: License Summary dan gating (TC-FA-LIC-590)

16. Ganti akun: Logout
17. Login sebagai Total Control client Trial plan Enterprise Pre-setup #33 (`Spectra.env.FA_TRIALPAID_TC_PASSWORD`)
18. Klik menu License pada sidebar
19. Verifikasi kolom `Asset`: `Total` = 300 (Trial Asset Quota), `Used` = 10, `Reserved` = 0, `Remaining` = 290, `Unmanaged` = 0
20. Verifikasi Tabs: `All License | Allocation Quota | Concurrent User`
21. Klik sub-tab `Subscription History`
22. Verifikasi Sub-Tab `Subscription History` dan `Allocation History` dirender
23. Verifikasi `Subscription History` memuat satu baris term Trial dengan Type `Trial` (badge) dan Status `Active`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-589, 590, 591). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-591 (akun #32) sebelum TC-590 (akun #33) agar hanya satu kali ganti akun (S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 16 sampai 18 (ganti akun dan membuka License). Langkah 13 dan 21 adalah langkah TC (klik Tab dan klik sub-tab).
- Langkah 2 mengelompokkan `Used`, `Reserved`, `Remaining`, dan `Unmanaged` kolom `Asset` karena Expected TC menyebutnya dalam satu butir baris yang sama.
- Temuan untuk QA:
  - TC-590 langkah 3 menyebut "Buka Sub-Tab `Subscription History`" sedangkan Expected butir c juga memverifikasi `Allocation History` dirender; spec hanya mengasersi bahwa kedua sub-tab dirender (langkah 22) dan tidak membuka `Allocation History`.
