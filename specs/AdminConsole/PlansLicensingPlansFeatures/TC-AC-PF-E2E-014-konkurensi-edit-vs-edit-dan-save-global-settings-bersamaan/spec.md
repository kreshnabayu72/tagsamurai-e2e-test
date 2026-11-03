---
id: TC-AC-PF-E2E-014-konkurensi-edit-vs-edit-dan-save-global-settings-bersamaan
title: "Konkurensi Edit vs Edit Custom dan Default Plan serta Save Global Settings Bersamaan (Last-Write-Wins)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-590
  - TC-AC-PF-591
  - TC-AC-PF-592
coverage:
  web: automated
---

# Konkurensi Edit vs Edit Custom dan Default Plan serta Save Global Settings Bersamaan (Last-Write-Wins)

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor pertama): Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Akun sesi B (konteks browser kedua): Total Control Principal kedua `secondAdminPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`, Pre-setup #9), password dari `Spectra.env.AC_PF_SA_PASSWORD`. Kelas harness: c multi-konteks (dua sesi UI; sesi B menjadi objek asersi).
- Login sesi A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Sesi B login pada langkah 1 di konteks browser kedua; hook `after` menutup konteks kedua dan mengembalikan sesi ke akun default suite.
- Data Pre-setup yang diubah (hook `before`): custom plan `Growth Tier` v20 (Pre-setup Dataset Plan A/C; nilai awal Group count `25`, Borrowing `Full`), default plan `Growth` v5 (Dataset Plan A; nilai awal Group count `3`, Borrowing `Basic`), dan Global FAMS Settings dengan nilai awal Max custom fields per asset name `5` dan Max depreciation methods (Multi Depreciation tier) `2`. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20, `Growth` v5, dan Global FAMS Settings (singleton) menjadi target aksi tulis karena berupa data Pre-setup yang tidak dapat dimiliki spec (slot default plan terbatas). Pemulihan ke keadaan awal dijamin fixture BE yang idempoten (disediakan tim FE/BE): dijalankan di hook `before` dan `after` serta pada langkah 17, 30, dan 44. Efek yang tersisa dan tidak dapat dipulihkan lewat UI: Last Updated plan dan entri Changelog baru pada ketiga surface (Changelog permanen). Suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`) untuk kedua akun; spec ini tidak mengubahnya.
- Kemampuan teknis: konteks browser kedua dengan login akun #9; fixture BE (pemulihan plan, versi, dan Global FAMS Settings) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Kemampuan baca jumlah entri Changelog tiap surface (Custom, Default, Global Settings) sebelum Save pertama blok (langkah 4, 20, dan 33) disediakan tim FE/BE; asersi memakai selisih terhadap baseline dan entri dicari lewat teks atau field, bukan posisi teratas (S-12, bagian 8b butir 10).
- Env var: `Spectra.env.AC_TC_PASSWORD` (sesi A) dan `Spectra.env.AC_PF_SA_PASSWORD` (sesi B); nama `AC_PF_SA_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-590: Edit-vs-Edit pada custom plan yang sama: last-write-wins tanpa dialog konflik

1. Sesi B: buka konteks browser kedua, login sebagai Total Control kedua (Principal), lalu buka Plans & Licensing > Plans & Features
2. Sesi A: klik tab Custom, buka Overlay Row Action `Growth Tier`, klik `Edit`
3. Sesi B: klik tab Custom, buka Overlay Row Action `Growth Tier`, klik `Edit`
4. Catat jumlah entri Changelog tab Custom (baseline C0) lewat kemampuan baca yang disediakan tim FE/BE
5. Sesi A: ubah Group count `25` menjadi `3`, klik `[Save]`
6. Verifikasi sesi A menampilkan toast sukses: "Success, plan has been updated."
7. Sesi B (form lama): ubah Borrowing `Full` menjadi `Basic`, klik `[Save]`
8. Verifikasi sesi B menampilkan toast sukses: "Success, plan has been updated."
9. Verifikasi kedua Save berhasil berurutan tanpa dialog konflik versi
10. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar lalu klik tab Custom
11. Verifikasi kolom Version `Growth Tier` bernilai `v22`
12. Sesi A: klik ikon Changelog pada toolbar tab Custom
13. Verifikasi jumlah entri Changelog tab Custom bertambah tepat dua dari C0
14. Verifikasi Changelog memuat entri field Group count dan entri field Borrowing yang terpisah
15. Verifikasi nilai akhir mengikuti Save terakhir
16. Tutup modal Changelog lewat `✕`
17. Pulihkan `Growth Tier` ke v20 lewat fixture BE hingga tersimpan

### TC-AC-PF-591: Edit-vs-Edit pada default plan yang sama: last-write-wins tanpa dialog konflik

18. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar, buka Overlay Row Action `Growth`, klik `Edit`
19. Sesi B: klik menu Plans & Licensing > Plans & Features di sidebar, buka Overlay Row Action `Growth`, klik `Edit`
20. Catat jumlah entri Changelog tab Default (baseline D0) lewat kemampuan baca yang disediakan tim FE/BE
21. Sesi A: ubah Group count `3` menjadi `25`, klik `[Save]`
22. Sesi B (form lama): ubah Borrowing `Basic` menjadi `Full`, klik `[Save]`
23. Verifikasi kedua Save berhasil berurutan tanpa dialog konflik versi
24. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar
25. Verifikasi kolom Version `Growth` bernilai `v7`
26. Sesi A: klik ikon Changelog pada toolbar tab Default
27. Verifikasi jumlah entri Changelog tab Default bertambah tepat dua dari D0
28. Verifikasi Changelog memuat entri field Group count dan entri field Borrowing yang terpisah
29. Tutup modal Changelog lewat `✕`
30. Pulihkan `Growth` ke v5 lewat fixture BE hingga tersimpan

### TC-AC-PF-592: Save Global Settings dari dua sesi bersamaan: last-write-wins tanpa pengecekan baseline

31. Sesi A: klik tab Global Settings
32. Sesi B: klik menu Plans & Licensing > Plans & Features di sidebar, lalu klik tab Global Settings
33. Catat jumlah entri Changelog Max custom fields per asset name di tab Global Settings (baseline G0) lewat kemampuan baca yang disediakan tim FE/BE
34. Sesi A: ubah Max custom fields per asset name menjadi `8`, klik `[Save]`
35. Sesi B: ubah Max custom fields per asset name menjadi `9`, klik `[Save]`
36. Verifikasi kedua Save berhasil tanpa dialog konflik
37. Sesi A: muat ulang halaman dengan F5
38. Verifikasi nilai akhir Max custom fields per asset name `9`
39. Sesi A: klik ikon Changelog di Card tab Global Settings
40. Verifikasi jumlah entri Changelog Max custom fields per asset name bertambah tepat dua dari G0
41. Verifikasi Changelog memuat entri `5` ke `8`
42. Verifikasi Changelog memuat entri `8` ke `9`
43. Tutup modal Changelog lewat `✕`
44. Pulihkan Global FAMS Settings ke nilai awal `5` dan `2` lewat fixture BE hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 10, 24, dan 37 memuat ulang list atau halaman untuk mengamati hasil di sesi A ("muat ulang" pada langkah TC); klik tab pada langkah 2, 3, 31, dan 32 serta klik menu sidebar pada langkah 18, 19, dan 32 (sesi B berada di Plan Detail sesudah `[Save]` langkah 22) mengarahkan layar ke tab yang disyaratkan precondition TC; penutupan modal pada langkah 16, 29, dan 43 membuka jalan bagi langkah berikutnya; langkah 17, 30, dan 44 memulihkan data Pre-setup (S-06, A-6); langkah 4, 20, dan 33 mencatat baseline jumlah entri Changelog (S-12).
- Nilai Group count dan Borrowing pada TC-AC-PF-591 diambil dari nilai awal Dataset Plan A (Group count `3`, Borrowing `Basic`) dan diubah ke nilai lain (`25`, `Full`).
- Alasan di atas sekitar 35 langkah (44 langkah): ketiga blok satu kelas harness (c multi-konteks, dua sesi menyimpan bersamaan) dan satu topik (last-write-wins), tiap blok pada surface sendiri (Custom, Default, Global Settings) dan dipulihkan fixture BE sebelum blok berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; kelebihan langkah berasal dari baseline Changelog tiap surface dan pemisahan Verifikasi per entri.
- Temuan untuk QA:
  - TC-AC-PF-591: langkah TC menyebut "ubah Group count" dan "ubah Borrowing" tanpa nilai; spec memilih nilai dari data awal Dataset Plan A. Expected "versi akhir `v7`" mengandaikan `Growth` v5 dan dua Save (v5 ke v7).
  - TC-AC-PF-590: Expected b "nilai akhir mengikuti Save terakhir" tidak menyebut nilai atau tempat pengamatannya; spec menulis `Verifikasi` dengan kalimat TC setelah Changelog dibuka, tanpa nilai tambahan.
  - TC-AC-PF-590 dan TC-AC-PF-591: Save sesi B memakai form lama yang masih memuat nilai awal Group count, sehingga Group count akhir kembali ke nilai awal menurut semantik last-write-wins; TC tidak menyebut apakah Group count hasil Save sesi A ikut tertimpa.
