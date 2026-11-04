---
id: TC-FA-LIC-E2E-008-license-summary-setup-column-baris-unmanaged-dan-used
title: "License Summary: Setup Column, Baris Unmanaged, dan Used Hanya Aset Active"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-17
  - TC-FA-LIC-23
  - TC-FA-LIC-595
coverage:
  web: automated
---

# License Summary: Setup Column, Baris Unmanaged, dan Used Hanya Aset Active

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #12: Total Asset License 5.000, Used 4.320, Reserved 15, Unmanaged 27; hierarki Kantor Pusat (Group Quota Summary Total 1500). Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan: (1) konfigurasi kolom License Summary dan Group Quota Summary yang disimpan dengan `[Save]` (TC-FA-LIC-595); License Summary dipulihkan eksplisit pada langkah 28 sampai 33 (centang kembali `+ Maps` dan `+ IT Inventory`, `[Save]`) dan Group Quota Summary pada langkah 23 sampai 26 (`[Reset to Default]`, `[Save]`); hook `after` hanya cadangan dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`; kemampuan disediakan tim FE). (2) Aset Unmanaged +3 (TC-FA-LIC-17), aset Draft +1 dan aset Active +1 di grup Produksi (TC-FA-LIC-23) lewat fixture BE; langkah 44 dan hook `after` memulihkan Pre-setup #12 (fixture BE pemulih disediakan tim FE/BE).
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE, pemulihan konfigurasi kolom): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-595: Setup Column License Summary dan Group Quota Summary

1. Klik header kolom Actions `⋯` pada tabel License Summary
2. Klik `Setup Column...`
3. Verifikasi popup Setup Column License Summary memiliki Title `Setup Column`
4. Verifikasi popup Setup Column License Summary memiliki deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
5. Verifikasi footer popup memuat `[Reset to Default]`
6. Verifikasi footer popup memuat `[Save]`
7. Verifikasi popup tidak memiliki `[Cancel]`
8. Verifikasi daftar kolom License Summary: `License`, `Asset`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`, semuanya Hideable dan tercentang secara default
9. Hilangkan centang `+ Maps`
10. Hilangkan centang `+ IT Inventory`
11. Klik `[Save]`
12. Verifikasi kolom lain pada License Summary tetap tampil
13. Verifikasi tabel License Summary tidak memuat kolom `+ Maps` dan `+ IT Inventory`
14. Klik Tab `Allocation Quota`
15. Klik node `Kantor Pusat`
16. Klik header kolom Actions `⋯` pada tabel Group Quota Summary
17. Klik `Setup Column...`
18. Verifikasi daftar kolom Group Quota Summary memuat kedelapan kolom yang sama dengan status default yang sama
19. Hilangkan centang `+ Audit`
20. Klik `[Save]`
21. Verifikasi kolom `+ Tracking` tampil pada Group Quota Summary
22. Verifikasi kolom `+ Audit` hilang dari Group Quota Summary
23. Klik header kolom Actions `⋯` pada tabel Group Quota Summary
24. Klik `Setup Column...`
25. Klik `[Reset to Default]`
26. Klik `[Save]`
27. Verifikasi kolom `+ Audit` tampil kembali pada Group Quota Summary
28. Klik Tab `All License`
29. Klik header kolom Actions `⋯` pada tabel License Summary
30. Klik `Setup Column...`
31. Centang kembali `+ Maps`
32. Centang kembali `+ IT Inventory`
33. Klik `[Save]`

### TC-FA-LIC-17: Baris Unmanaged tidak mengubah Used dan Remaining

34. Catat `Used`, `Remaining`, dan `Unmanaged` kolom `Asset`
35. Tambah 3 aset Unmanaged lewat fixture BE, lalu muat ulang halaman License
36. Verifikasi `Unmanaged` naik 3 (dari 27 menjadi 30)
37. Verifikasi `Used` dan `Remaining` tidak berubah

### TC-FA-LIC-23: Used hanya menghitung aset berstatus Active

38. Catat `Used` dan `Reserved`
39. Tambah 1 aset Draft di group Produksi lewat fixture BE, lalu muat ulang halaman License
40. Verifikasi aset Draft tidak mengubah `Used`, `Reserved`, maupun `Remaining`
41. Tambah 1 aset Active baru di group Produksi lewat fixture BE, lalu muat ulang halaman License
42. Verifikasi `Used` bertambah 1
43. Verifikasi `Reserved` tidak berubah
44. Pulihkan aset yang ditambahkan lewat fixture BE

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-17, 23, 595). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-595 (tanpa mengubah data) di awal; TC-17 dan TC-23 (menambah aset) di akhir (S-10).
- Spec di atas 35 langkah (44 langkah): seluruh blok satu topik (tabel License Summary dan Group Quota Summary pada dataset #12 yang sama) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 28 sampai 33 (kembali ke Tab `All License` dan memulihkan kolom License Summary, 8b.14), langkah 44 (pemulihan aset). Langkah 21 (anchor `+ Tracking` tampil) mendahului asersi kolom `+ Audit` hilang pada langkah 22, dan langkah 12 (kolom lain tetap tampil) mendahului asersi kolom `+ Maps` dan `+ IT Inventory` hilang pada langkah 13 (S-03, 8b.2); urutan Verifikasi butir TC-595 ditukar. Langkah 14 dan 15 adalah langkah TC-595 (membuka Allocation Quota dan node `Kantor Pusat`).
- TC-23 langkah 2 menambah aset Active dan Draft sekaligus; spec menambahkannya berurutan (Draft lebih dulu, langkah 39 sampai 40) supaya klausa "Aset Draft tidak mengubah `Used`, `Reserved`, maupun `Remaining`" dapat diasersi terpisah dari kenaikan `Used` oleh aset Active (yang juga mengurangi `Remaining`).
- Temuan untuk QA:
  - TC-23 Expected c menyatakan aset Draft tidak mengubah `Remaining`, sedangkan `Remaining` = Total − Used − Reserved turun 1 oleh aset Active yang ditambahkan pada langkah TC yang sama; klausa c hanya dapat diasersi bila Draft ditambah terpisah (langkah 39 dan 40).
  - TC-595 langkah 2 meminta menghilangkan centang pada popup License Summary dan memeriksa tabel sesudah `[Save]`; TC tidak menyebut pemulihan konfigurasi kolom; spec memulihkannya dengan langkah eksplisit (langkah 23 sampai 26 dan 28 sampai 33), hook `after` hanya cadangan.
