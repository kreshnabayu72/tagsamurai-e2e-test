---
id: TC-FA-LIC-E2E-007-license-summary-plan-paid-screening-kolom-asset-addon-not
title: "License Summary Plan Paid: Screening Kolom Asset, Addon, Not Available, Loading, dan Kolom Identik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-12
  - TC-FA-LIC-13
  - TC-FA-LIC-14
  - TC-FA-LIC-15
  - TC-FA-LIC-16
  - TC-FA-LIC-21
coverage:
  web: automated
---

# License Summary Plan Paid: Screening Kolom Asset, Addon, Not Available, Loading, dan Kolom Identik

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License (Tab All License) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #12: Total Asset License 5.000, Used 4.320, Reserved 15, Unmanaged 27; ledger Add-on Audit 100/60, Tracking 50/48, Maintenance 30/12, IT Inventory 200/120, Maps belum dialokasikan. Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan: ledger Add-on Maintenance diubah ke Total 40, Used 15 lewat fixture BE (TC-FA-LIC-15, langkah 25); langkah 29 dan hook `after` memulihkannya ke Total 30, Used 12. Fixture BE penyetel dan pemulih disediakan tim FE/BE.
- Kemampuan teknis: intercept jaringan yang menunda respons data ledger selama 3 detik (TC-FA-LIC-21), dilepas segera sesudah pengamatan (langkah 22).
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-12: Screening License Summary plan Paid

1. Verifikasi judul SectionCard teratas `License Summary`
2. Verifikasi header kanan memuat ikon Download (ExportButton)
3. Verifikasi kolom: `License | Asset | + Audit | + Tracking | + Maintenance Routine | + Repair Ticketing | + Maps | + IT Inventory`
4. Verifikasi baris berurutan: `Total`, `Used`, `Reserved`, `Remaining`, `Unmanaged`
5. Verifikasi tidak ada Search, Filter, Paginator, row action, dan checkbox pada tabel License Summary
6. Verifikasi header kolom Actions `⋯` ada sebagai pemicu Column Visibility

### TC-FA-LIC-13: Kolom Asset plan Paid

7. Verifikasi kolom `Asset`: `Total` = 5000
8. Verifikasi kolom `Asset`: `Used` = 4320 (angka biasa tanpa progress bar)
9. Verifikasi kolom `Asset`: `Reserved` = 15
10. Verifikasi kolom `Asset`: `Remaining` = 665 (5000 − 4320 − 15)
11. Verifikasi kolom `Asset`: `Unmanaged` = 27

### TC-FA-LIC-14: Kolom addon dengan data

12. Verifikasi kolom `+ Audit`: Total 100, Used 60, Reserved `—`, Remaining 40, Unmanaged `—`
13. Verifikasi kolom `+ Tracking`: Total 50, Used 48, Reserved `—`, Remaining 2, Unmanaged `—`
14. Verifikasi kolom `+ IT Inventory`: Total 200, Used 120, Reserved `—`, Remaining 80, Unmanaged `—`

### TC-FA-LIC-16: Addon belum dialokasikan tampil Not Available

15. Verifikasi kolom `+ Maps`: `Total` = `Not Available`
16. Verifikasi kolom `+ Maps`: `Used`, `Reserved`, `Remaining`, `Unmanaged` = `—`
17. Verifikasi tidak ada nilai `0` pada kolom `+ Maps`

### TC-FA-LIC-21: Skeleton shimmer saat memuat

18. Tunda respons data ledger selama 3 detik lewat intercept jaringan
19. Muat ulang halaman License (F5)
20. Verifikasi sel angka License Summary menampilkan skeleton shimmer selama memuat
21. Verifikasi setelah respons diterima skeleton diganti nilai (`Total` kolom `Asset` = 5000)
22. Lepas intercept jaringan

### TC-FA-LIC-15: Kolom Maintenance Routine dan Repair Ticketing selalu identik

23. Verifikasi kolom `+ Maintenance Routine`: Total 30, Used 12, Remaining 18, Reserved `—`, Unmanaged `—`
24. Verifikasi kolom `+ Repair Ticketing`: Total 30, Used 12, Remaining 18, Reserved `—`, Unmanaged `—`
25. Ubah ledger Maintenance menjadi Total 40, Used 15 lewat fixture BE
26. Muat ulang halaman License
27. Verifikasi kolom `+ Maintenance Routine`: Total 40, Used 15, Remaining 25
28. Verifikasi kolom `+ Repair Ticketing` identik: Total 40, Used 15, Remaining 25
29. Pulihkan ledger Maintenance ke Total 30, Used 12 lewat fixture BE

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-12, 13, 14, 15, 16, 21). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-21 (muat ulang dengan intercept) sebelum TC-15 dan TC-15 (mengubah state) di akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 22 (melepas intercept), langkah 29 (memulihkan ledger). Langkah TC-12 sampai TC-16 "Amati" dipenuhi dengan `Verifikasi` pada halaman yang dibuka hook `beforeEach` suite.
- Langkah 17 (absence `0` pada kolom `+ Maps`) berposisi sesudah langkah 15 dan 16 yang memverifikasi nilai pada kolom yang sama (anchor positif).
- Temuan untuk QA:
  - TC-21 tidak menyebut nilai yang diharapkan sesudah skeleton hilang ("diganti nilai"); spec memakai `Total` kolom `Asset` = 5000 dari Pre-setup #12.
  - TC-21 mensyaratkan muat ulang untuk mengamati skeleton; spec memuat ulang halaman (F5) setelah intercept terpasang.
