---
id: TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir
title: "Empty State Tabel Asset Class dan Dialog Use Recommended Classes: Screening, Create Tanpa Baris, Cancel, Baris Disabled, dan Blokir Batas Jumlah"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-9
  - TC-FA-FAAC-282
  - TC-FA-FAAC-285
  - TC-FA-FAAC-293
  - TC-FA-FAAC-286
  - TC-FA-FAAC-290
  - TC-FA-FAAC-291
coverage:
  web: automated
---

# Empty State Tabel Asset Class dan Dialog Use Recommended Classes: Screening, Create Tanpa Baris, Cancel, Baris Disabled, dan Blokir Batas Jumlah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state client): client belum memiliki Asset Class sama sekali (tabel kosong) dan Tax Depreciation Class rekomendasi Active, disiapkan di hook `before` lewat fixture BE; hook `after` memulihkan state client ke nilai awal. Seed disediakan tim FE/BE (lihat `suite.md`).
- Data per blok: TC-FA-FAAC-286 membutuhkan Tax Depreciation Class `Bukan bangunan – Kelompok 1` Inactive atau tidak ada; TC-FA-FAAC-290 membutuhkan Master Data Count Limit 0; TC-FA-FAAC-291 membutuhkan Master Data Count Limit 2 (sisa kapasitas 2). Ketiganya diatur lewat fixture BE dan dipulihkan di hook `after`.
- Kemampuan teknis: fixture BE untuk mengatur Tax Depreciation Class dan Master Data Count Limit (Lifecycle Settings) dan untuk membaca jumlah Asset Class serta jumlah entri Changelog Asset Class, System Log aktor, dan Activity Log FAMS; disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah state global.

## Test Steps

### TC-FA-FAAC-9: Empty state tabel Asset Class belum ada data

1. Verifikasi EmptyState menampilkan illustration, title `No asset class yet`, dan description `Get started by creating your first asset class.`
2. Verifikasi link `Use recommended classes` tampil di dalam EmptyState

### TC-FA-FAAC-282: Screening dialog Use Recommended Classes

3. Klik link `Use recommended classes` pada EmptyState tabel
4. Verifikasi dialog `Use Recommended Classes` (ukuran LG) terbuka
5. Verifikasi Alert info `Recommended values are a starting point. Review them with your accountant and tax consultant.`
6. Verifikasi tabel berisi delapan baris tetap: `BLDG` `Buildings` `Straight Line · 20 yrs` `Bangunan permanen` `Straight Line`; `HEAVY-EQ` `Heavy Equipment` `Straight Line · 10 yrs` `Bukan bangunan – Kelompok 3` `Declining Balance`; `MACH` `Machinery` `Straight Line · 8 yrs` `Bukan bangunan – Kelompok 2` `Declining Balance`; `VEH` `Vehicles` `Straight Line · 8 yrs` `Bukan bangunan – Kelompok 2` `Declining Balance`; `LT-VEH` `Light Vehicles` `Straight Line · 4 yrs` `Bukan bangunan – Kelompok 1` `Declining Balance`; `IT-EQ` `IT Equipment` `Straight Line · 4 yrs` `Bukan bangunan – Kelompok 1` `Declining Balance`; `OFC-EQ` `Office Equipment & Furniture` `Straight Line · 4 yrs` `Bukan bangunan – Kelompok 1` `Straight Line`; `LAND` `Land` `Not Depreciated` `Tanah` `—`
7. Verifikasi kolom Class Code dan Class Name berupa input dengan placeholder `Enter class code` dan `Enter class name`
8. Verifikasi kolom Commercial, Tax Depreciation Class, dan Tax Method read-only
9. Verifikasi tabel tanpa sort, filter, dan paginasi
10. Verifikasi footer memuat tombol `Cancel` dan `Create` dengan `Create` selalu Enabled

### TC-FA-FAAC-285: Klik Create tanpa baris terpilih

11. Klik `Create` tanpa mencentang baris
12. Verifikasi tombol `Create` tetap Enabled
13. Verifikasi submit dicegah dan error inline baku tampil
14. Verifikasi dialog `Use Recommended Classes` tetap terbuka
15. Verifikasi jumlah Asset Class pada client tetap 0 lewat fixture BE

### TC-FA-FAAC-293: Cancel pada dialog rekomendasi tidak membuat apa pun

16. Centang baris BLDG
17. Catat jumlah entri Changelog Asset Class (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) lewat kemampuan baca BE sebagai baseline
18. Klik `Cancel`
19. Verifikasi dialog menutup
20. Verifikasi tabel tetap kosong dengan EmptyState `No asset class yet`
21. Verifikasi tidak ada toast
22. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
23. Verifikasi jumlah entri System Log aktor sama dengan Ns (tidak ada entri baru)
24. Verifikasi jumlah entri Activity Log FAMS sama dengan Na (tidak ada entri baru)

### TC-FA-FAAC-286: Baris dengan Tax Depreciation Class tidak tersedia Disabled dengan tooltip

25. Atur Tax Depreciation Class `Bukan bangunan – Kelompok 1` menjadi Inactive lewat fixture BE hingga tersimpan
26. Klik link `Use recommended classes` pada EmptyState tabel
27. Arahkan kursor ke checkbox baris OFC-EQ
28. Verifikasi checkbox baris OFC-EQ Disabled
29. Verifikasi tooltip `Tax depreciation class Bukan bangunan – Kelompok 1 is not available.`
30. Coba centang checkbox baris OFC-EQ
31. Verifikasi checkbox baris OFC-EQ tetap tidak tercentang
32. Klik `Cancel`
33. Pulihkan Tax Depreciation Class `Bukan bangunan – Kelompok 1` menjadi Active lewat fixture BE hingga tersimpan

### TC-FA-FAAC-290: Klik Use recommended classes saat batas jumlah tercapai

34. Atur Master Data Count Limit ke 0 lewat fixture BE hingga tersimpan
35. Klik link `Use recommended classes`
36. Verifikasi dialog Blok `Asset Class Limit Reached` dengan isi `You've reached the platform limit of 0 asset classes. Contact support if you need a higher limit.` dan tombol `OK`
37. Verifikasi dialog `Use Recommended Classes` tidak dibuka
38. Klik `OK`

### TC-FA-FAAC-291: Sisa kapasitas lebih kecil dari jumlah baris terpilih

39. Atur Master Data Count Limit ke 2 lewat fixture BE hingga tersimpan
40. Klik link `Use recommended classes` pada EmptyState tabel
41. Centang tiga baris (BLDG, MACH, VEH)
42. Klik `Create`
43. Verifikasi dialog Blok `Asset Class Limit Reached` muncul
44. Verifikasi jumlah Asset Class pada client tetap 0 lewat fixture BE
45. Klik `OK`

## Notes

- Spec melewati sekitar 35 langkah (45 langkah): semua blok adalah satu topik (EmptyState tabel dan dialog Use Recommended Classes) pada satu dataset awal (client tanpa Asset Class), tiap blok berdiri sendiri, dan memisahnya hanya menggandakan login, hook, dan pemulihan state. Tambahan langkah berasal dari pengaturan state per blok lewat fixture BE.
- Langkah penghubung (S-03): langkah 16 dan 41 (mencentang baris sebagai precondition aksi TC), langkah 32 (menutup dialog sebelum state berubah), langkah 33 (memulihkan Tax Depreciation Class), langkah 25, 34, dan 39 (mengatur state lewat fixture BE sebagai pemicu), langkah 38 dan 45 (menutup dialog Blok).
- Urutan TC dalam spec: 9, 282, 285, 293, 286, 290, 291. Blok yang tidak mengubah state client lebih dulu (S-10); TC-FA-FAAC-293 menutup dialog sehingga diletakkan sebelum blok berikutnya yang membuka dialog lagi.
- Klausa "tidak ada log" pada TC-FA-FAAC-293 menyebut tiga surface (Changelog Asset Class, System Log, Activity Log); tiap surface diasersi dengan baseline jumlah entri yang dicatat pada langkah 17 dan selisih 0 pada langkah 22 sampai 24 (S-12), karena TC-FA-FAAC-293 tidak termasuk spec absence (kelas g) di suite ini.
- Nama literal baris rekomendasi (BLDG, HEAVY-EQ, MACH, VEH, OFC-EQ, dan lainnya) berasal dari isi tetap dialog dan tidak dibuat spec; dialog tidak dikirim (Create tidak diklik sampai sukses), sehingga tidak ada data yang dibuat.
- Temuan untuk QA:
  - TC-FA-FAAC-285 menyebut "error inline baku tampil" tanpa teks error; spec mengasersi keberadaannya (langkah 13) tanpa teks.
  - TC-FA-FAAC-290 menulis `[Limit]` sebagai placeholder pada teks dialog; spec memakai nilai tersubstitusi `0` sesuai Master Data Count Limit yang diatur.
  - TC-FA-FAAC-290 dan TC-FA-FAAC-291 tidak menyatakan apakah dialog Use Recommended Classes tetap terbuka setelah `OK` pada dialog Blok; spec berhenti sesudah `OK` dan menyerahkan penutupan dialog yang tersisa kepada hook `beforeEach` suite.
