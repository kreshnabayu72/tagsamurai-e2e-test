---
id: TC-GS-IMPORT-E2E-181-absence-log-edit-sel-duplikasi-hapus-baris-discard-draft-tidak-mencatat
title: "Absence log: edit sel, duplikasi, hapus baris, Discard Draft tidak mencatat Changelog Import, System Log, Activity Log (Client A)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-428
  - TC-GS-IMPORT-429
  - TC-GS-IMPORT-430
  - TC-GS-IMPORT-431
coverage:
  web: automated
---

# Absence log: edit sel, duplikasi, hapus baris, Discard Draft tidak mencatat Changelog Import, System Log, Activity Log (Client A)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Client A dibagikan ke seluruh admin dan Changelog Import, System Log, serta Activity Log bersifat permanen sehingga asersi memakai baseline jumlah; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam, bukan menggeser jam server) agar Unsaved Banner dan `[Discard]` tampil pada TC-431 (pemicu aksi absence, P-5a); skrip fixture pemulihan draft dasar Client A (D-01, Kontrak Fixture R2).
- Baseline log (S-12): tiga surface log dicatat sebelum aksi pemicu pertama tiap TC dari teks Pagination "Showing [From] - [To] of [N] items" (0 bila yang tampil adalah empty state): Changelog Import (icon `[Changelog]` di header halaman Import), System Log pada Detail User Sari Dewi (Tab System Log), dan Activity Log (Global Settings > Activity Log, tab User Action). Asersi memakai kesamaan total terhadap baseline, bukan angka absolut atau posisi baris.
- Data Dinamis (milik spec ini; Population Client A, nama literal karena asersi urutan baris; seeding idempotent dan dipulihkan sebelum tiap TC): D-01 draft Brand 12 baris `pending`: `Acme Corp` (#1), `Lenovo` (#2), `Zebra Technologies` (#3), `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus`. Nama hasil perubahan: `Acme Corp 2`, `Lenovo 2`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan draft dasar Client A dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-428: Penyuntingan sel

1. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
2. Buka Changelog Import (icon `[Changelog]` di header halaman) dan catat angka total pada teks Pagination sebagai baseline Changelog
3. Tutup modal Changelog Import
4. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total pada teks Pagination sebagai baseline System Log
5. Buka Activity Log (Global Settings > Activity Log) pada tab User Action dan catat angka total pada teks Pagination sebagai baseline Activity Log
6. Buka halaman Import > Brand
7. Buka row action Edit pada baris #1
8. Ubah Brand Name menjadi `Acme Corp 2`
9. Klik `[Save]`
10. Verifikasi sel Brand Name baris #1 menampilkan `Acme Corp 2`
11. Verifikasi toast sukses "Success, row has been updated." tampil
12. Buka Changelog Import dan baca angka total pada teks Pagination
13. Verifikasi modal `Changelog: Import` terbuka
14. Verifikasi total Changelog Import sama dengan baseline langkah 2
15. Tutup modal Changelog Import
16. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total pada teks Pagination
17. Verifikasi tab System Log pada Detail User Sari Dewi tampil
18. Verifikasi total System Log sama dengan baseline langkah 4
19. Buka Activity Log pada tab User Action dan baca angka total pada teks Pagination
20. Verifikasi halaman Activity Log pada tab User Action tampil
21. Verifikasi total Activity Log sama dengan baseline langkah 5

### TC-GS-IMPORT-429: Duplikasi baris

22. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
23. Buka halaman Import > Brand
24. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
25. Tutup modal Changelog Import
26. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total sebagai baseline System Log
27. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
28. Buka halaman Import > Brand
29. Buka row action Duplicate pada baris #2
30. Ubah Brand Name baris salinan menjadi `Lenovo 2`
31. Klik `[Save]`
32. Verifikasi toast sukses "Success, row has been added." tampil
33. Verifikasi kartu Total Rows menampilkan 13
34. Buka Changelog Import dan baca angka total pada teks Pagination
35. Verifikasi modal `Changelog: Import` terbuka
36. Verifikasi total Changelog Import sama dengan baseline langkah 24
37. Tutup modal Changelog Import
38. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total
39. Verifikasi tab System Log pada Detail User Sari Dewi tampil
40. Verifikasi total System Log sama dengan baseline langkah 26
41. Buka Activity Log pada tab User Action dan baca angka total
42. Verifikasi halaman Activity Log pada tab User Action tampil
43. Verifikasi total Activity Log sama dengan baseline langkah 27

### TC-GS-IMPORT-430: Penghapusan baris

44. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
45. Buka halaman Import > Brand
46. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
47. Tutup modal Changelog Import
48. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total sebagai baseline System Log
49. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
50. Buka halaman Import > Brand
51. Buka row action Remove pada baris #3
52. Klik `[Delete]` pada dialog Delete Row
53. Verifikasi toast sukses "Success, row has been deleted." tampil
54. Verifikasi kartu Total Rows menampilkan 11
55. Buka Changelog Import dan baca angka total pada teks Pagination
56. Verifikasi modal `Changelog: Import` terbuka
57. Verifikasi total Changelog Import sama dengan baseline langkah 46
58. Tutup modal Changelog Import
59. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total
60. Verifikasi tab System Log pada Detail User Sari Dewi tampil
61. Verifikasi total System Log sama dengan baseline langkah 48
62. Buka Activity Log pada tab User Action dan baca angka total
63. Verifikasi halaman Activity Log pada tab User Action tampil
64. Verifikasi total Activity Log sama dengan baseline langkah 49

### TC-GS-IMPORT-431: Discard Draft

65. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
66. Buka halaman Import > Brand
67. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
68. Tutup modal Changelog Import
69. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total sebagai baseline System Log
70. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
71. Buka halaman Import > Brand
72. Klik `[Discard]` pada Unsaved Banner
73. Klik `[Discard Draft]` pada dialog Discard Draft
74. Verifikasi toast sukses "Success, draft has been discarded." tampil
75. Verifikasi Dropzone menggantikan Staging Table
76. Buka Changelog Import dan baca angka total pada teks Pagination
77. Verifikasi modal `Changelog: Import` terbuka
78. Verifikasi total Changelog Import sama dengan baseline langkah 67
79. Tutup modal Changelog Import
80. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total
81. Verifikasi tab System Log pada Detail User Sari Dewi tampil
82. Verifikasi total System Log sama dengan baseline langkah 69
83. Buka Activity Log pada tab User Action dan baca angka total
84. Verifikasi halaman Activity Log pada tab User Action tampil
85. Verifikasi total Activity Log sama dengan baseline langkah 70

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (g); setiap TC memuat aksi nyata (Edit, Duplicate, Remove, Discard Draft) dengan baseline tiga surface sendiri, sehingga memenuhi S-05. Hook umur draft D-76 hanya pemicu (P-5a).
- Alasan melewati sekitar 35 langkah (85 langkah nominal): empat blok homogen satu kelas (absence log) yang berdiri sendiri dengan pemulihan draft di awal tiap blok. Sebagian besar langkah adalah blok baca-log berpola (buka surface, catat atau baca total, `Verifikasi` sama dengan baseline; sembilan langkah baca per TC) yang tidak dihitung sebagai smell (bagian 3 konvensi). Urutan TC-428, 429, 430, 431: Discard Draft paling akhir karena menghapus draft.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): pemulihan draft (langkah 1, 22, 44, 65), pembukaan surface dan pencatatan baseline (langkah 2 sampai 5, 24 sampai 27, 46 sampai 49, 67 sampai 70), penutupan modal Changelog Import sebelum surface berikutnya (langkah 3, 15, 25, 37, 47, 58, 68, 79), pembukaan halaman Import > Brand sebelum Changelog Import yang datang sesudah Activity Log (langkah 23, 45, 66), pembacaan total (langkah 12, 16, 19 dan padanannya), serta pembukaan Import > Brand dan row action. Pembacaan akhir tiap Changelog Import, System Log, dan Activity Log didahului satu `Verifikasi` (modal Changelog: Import terbuka; tab System Log tampil; halaman Activity Log tampil) sebagai anchor positif sebelum asersi kesamaan total. Asersi absence (kesamaan total) didahului toast sukses atas aksi (langkah 11, 32, 53, 74) sebagai anchor positif yang terhubung ke pemicu (butir 2 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-428 sampai 431 mengasersi absence pada tiga surface tanpa menyebut cara memuat ulang total Pagination (muat ulang halaman atau buka ulang modal); spec membuka ulang tiap surface.
  - TC-GS-IMPORT-428 sampai 431 tidak menyebut apakah baseline System Log dan Activity Log dapat berubah oleh aksi lain di run yang sama; asersi kesamaan total hanya lolos bila tidak ada aksi lain pada akun Sari Dewi di antara baseline dan pembacaan akhir (suite serial).
  - Post Condition semua TC di spec ini "-" dan tidak ada keadaan lain yang perlu dipulihkan selain yang dikerjakan hook `after`.
