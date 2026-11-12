---
id: TC-AC-LA-E2E-115-changelog-search-dan-filter
title: "Modal Changelog: Search dan Filter Panel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-360
  - TC-AC-LA-361
  - TC-AC-LA-362
  - TC-AC-LA-363
  - TC-AC-LA-364
  - TC-AC-LA-365
  - TC-AC-LA-366
  - TC-AC-LA-367
coverage:
  web: automated
---

# Modal Changelog: Search dan Filter Panel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status dan 25 entri Changelog termasuk Modified By `System`, aksi job `Auto-Expire`, `Auto-Activate`, `Timeout Auto-Cancel`, Action `Create` dan `Edit`, Field `Status`, Old Value `Pending`, New Value `Active`, Allocation ID `LALC-20260105-00001`, dan entri pada sedikitnya dua hari berbeda) bersifat baca-saja untuk spec ini. Changelog adalah audit trail permanen yang tumbuh; asersi isi hanya atas baris yang dijamin berada pada halaman teramati, dan jumlah total tidak diasersi sebagai angka absolut (S-12, S-14).
- Data Dinamis TC-AC-LA-367: satu aksi yang mencatat Action baru di Changelog, dilakukan lewat sesi API aktor yang sama (token tidak dihitung sebagai sesi web; lihat `suite.md`); aksi dan akun pelakunya "disediakan tim FE" (S-13). Pemulihan dilakukan baseline automation sebelum tiap spec (Catatan TC).
- Kemampuan teknis: spec menyembunyikan kolom `Field` lewat overlay Column Visibility Changelog (langkah 13 menyembunyikan, langkah 18 memulihkan); hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`), disediakan tim FE.
- Parameter langkah 2 sampai 4 (TC-AC-LA-360), satu baris per kolom:

| Kolom | Kata kunci | Nilai yang cocok |
|---|---|---|
| Action | `create` | Action `Create` (tanpa membedakan huruf besar dan kecil) |
| Allocation ID | `LALC-2026` | Allocation ID berawalan `LALC-2026` |
| Field | `Status` | Field `Status` |
| Old Value | `Pending` | Old Value `Pending` |
| New Value | `Active` | New Value `Active` |

- Parameter langkah 45 sampai 52 (TC-AC-LA-365), satu baris per field:

| Field | Opsi yang dipilih |
|---|---|
| Action | `Create` |
| Allocation ID | `LALC-20260105-00001` |
| Field | `Status` |
| Modified By | `System` |

- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-360: Search Changelog kelas teks

1. Klik ikon Changelog
2. Untuk setiap baris tabel parameter TC-AC-LA-360 (langkah 2 sampai 4): ketik Search Kata kunci, tekan Enter
3. Verifikasi sedikitnya satu baris dengan Kolom bernilai Nilai yang cocok tampil
4. Klik `(←)` pada kotak Search
5. Ketik Search `zzzzqqqq`, tekan Enter
6. Verifikasi `No results found` tampil

### TC-AC-LA-361: Search Modified By dan guard kolom Date

7. Ganti isi kotak search dengan `system`, tekan Enter
8. Verifikasi baris dengan Modified By `System` tampil
9. Catat teks tanggal pada kolom Date baris pertama
10. Ganti isi kotak search dengan teks tanggal yang dicatat pada langkah 9, tekan Enter
11. Verifikasi `No results found` tampil

### TC-AC-LA-362: Search terikat visibilitas kolom

12. Klik `⋯` pada header kolom Actions Changelog
13. Hapus centang `Field` pada overlay
14. Tekan `Esc` untuk menutup overlay
15. Ganti isi kotak search dengan `Status`, tekan Enter
16. Verifikasi `No results found` tampil
17. Klik `⋯` pada header kolom Actions Changelog
18. Centang `Field` pada overlay
19. Tekan `Esc` untuk menutup overlay
20. Ganti isi kotak search dengan `Status`, tekan Enter
21. Verifikasi baris dengan Field `Status` tampil

### TC-AC-LA-363: Siklus interaksi Search Changelog

22. Klik ikon panah `(←)`
23. Klik ikon Search pada Modal Changelog
24. Verifikasi search bar melebar
25. Verifikasi kursor otomatis fokus di input
26. Catat isi halaman pertama tabel sebagai baseline
27. Ketik `Create` di input Search tanpa menekan Enter
28. Verifikasi tabel belum tersaring (isi halaman pertama sama dengan baseline langkah 26)
29. Tekan Enter
30. Verifikasi tabel menampilkan hasil `Create`
31. Klik ikon `(✕)`
32. Verifikasi tabel tetap menampilkan hasil `Create`
33. Tekan Enter pada input kosong
34. Verifikasi tabel mereset (isi halaman pertama sama dengan baseline langkah 26)
35. Ketik `Create` di input Search, tekan Enter
36. Klik ikon panah `(←)`
37. Verifikasi search bar tertutup
38. Verifikasi kata kunci dikosongkan
39. Verifikasi tabel langsung reset (isi halaman pertama sama dengan baseline langkah 26)

### TC-AC-LA-364: Screening Filter Panel Changelog

40. Klik ikon Filter pada Modal Changelog
41. Verifikasi field berurutan: `Date` (date range picker, `Select date`), `Action` (`All actions`), `Allocation ID` (`All allocation IDs`), `Field` (`All fields`), `Modified By` (`All users`)
42. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
43. Verifikasi tidak ada field Old Value dan New Value
44. Klik ikon Filter

### TC-AC-LA-365: Eksekusi filter multi-select

45. Untuk setiap baris tabel parameter TC-AC-LA-365 (langkah 45 sampai 52): klik ikon Filter
46. Buka dropdown Field
47. Pilih Opsi yang dipilih
48. Klik `[Apply]`
49. Verifikasi sedikitnya satu baris tampil
50. Verifikasi hanya baris dengan Field Opsi yang dipilih yang tampil
51. Klik ikon Filter
52. Klik `[Clear Field]` lalu `[Apply]`
53. Klik ikon Filter
54. Buka dropdown Action
55. Verifikasi opsi Action memuat aksi job `Auto-Expire`, `Auto-Activate`, dan `Timeout Auto-Cancel`
56. Verifikasi opsi Action hanya nilai yang tercatat di Changelog tanpa duplikat
57. Buka dropdown Allocation ID
58. Verifikasi opsi Allocation ID hanya nilai yang tercatat di Changelog tanpa duplikat
59. Buka dropdown Field
60. Verifikasi opsi Field hanya nilai yang tercatat di Changelog tanpa duplikat
61. Buka dropdown Modified By
62. Verifikasi opsi Modified By memuat `System`
63. Verifikasi opsi Modified By hanya nilai yang tercatat di Changelog tanpa duplikat
64. Klik ikon Filter

### TC-AC-LA-366: Filter tanggal Date dan kombinasi AND

65. Klik ikon Filter
66. Pilih rentang tanggal pada Date dari tanggal dua entri seed pada hari berbeda
67. Verifikasi teks tanggal pada input mengikuti Date Format General Settings
68. Klik `[Apply]`
69. Verifikasi sedikitnya satu baris tampil
70. Verifikasi hasil dalam rentang tanggal inklusif
71. Klik ikon Filter
72. Buka dropdown Action
73. Centang `Edit`
74. Klik `[Apply]`
75. Verifikasi sedikitnya satu baris tampil
76. Verifikasi hasil memenuhi kedua kriteria (Date dalam rentang dan Action `Edit`)
77. Klik ikon Filter
78. Klik `[Clear Field]` lalu `[Apply]`

### TC-AC-LA-367: Opsi filter Action dan Field dari nilai yang tercatat

79. Klik ikon Filter
80. Buka dropdown Action
81. Verifikasi opsi Action hanya nilai yang ada di Changelog
82. Buka dropdown Field
83. Verifikasi opsi Field hanya nilai yang ada di Changelog
84. Buka dropdown Action
85. Centang `Create`
86. Klik `[Apply]`
87. Lakukan aksi yang mencatat Action baru di Changelog lewat sesi API hingga entri tersimpan
88. Klik ikon Filter
89. Buka dropdown Action
90. Verifikasi Action baru muncul sebagai opsi

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-358 (empty filtered, loading, dan error load Modal Changelog) tidak ada di spec ini.
- Langkah 2 sampai 4 diulang untuk lima baris tabel parameter (15 langkah terekspansi) dan langkah 45 sampai 52 untuk empat baris (32 langkah terekspansi); total sekitar 120 langkah terekspansi. Verifikasi tetap satu per klausa per iterasi.
- Alasan spec melewati sekitar 35 langkah: semua blok satu topik (Search dan Filter Modal Changelog) pada satu dataset baca-saja, dengan langkah berulang berparameter tabel Prerequisites tanpa langkah bersyarat (konvensi bagian 8b butir 7); tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 4 (menutup dan mengosongkan Search antar iterasi), langkah 9 (mencatat teks tanggal), langkah 14 dan 19 (menutup overlay), langkah 26 (baseline), langkah 44, 51, 53, 64, 71, 77, 88 (membuka dan menutup panel), langkah 52 dan 78 (membersihkan filter), langkah 54, 57, 59, 61 (membuka dropdown filter; `Verifikasi` opsi mengikuti pada langkah berikutnya).
- Temuan untuk QA:
  - TC-AC-LA-367 langkah 2 ("buat alokasi baru dengan Action berbeda") tidak menyebut Action yang dimaksud, cara, dan akun; spec memakai aksi "disediakan tim FE" lewat sesi API tanpa endpoint karangan (S-13). Butuh keputusan QA.
  - TC-AC-LA-365 butir e menyebut opsi `System` dan aksi job pada dropdown, yang bergantung pada seed #54 yang memuat entri job; spec mengasumsikannya ada.
  - TC-AC-LA-366 tidak menyebut rentang tanggal konkret dan nilai Date Format General Settings akun uji; spec memakai tanggal dua entri seed dan mengasersi bahwa input mengikuti format yang berlaku.
  - TC-AC-LA-360 Expected a sampai e memakai "termasuk dalam hasil" pada Changelog yang tumbuh; spec mengasersi sedikitnya satu baris cocok pada halaman teramati dan Search diperkuat dengan nilai seed.
  - TC-AC-LA-361 butir b ("Teks tanggal tidak mencocokkan baris") tidak menyebut teks tanggal konkret; spec memakai teks sel Date baris pertama yang dibaca saat uji.
