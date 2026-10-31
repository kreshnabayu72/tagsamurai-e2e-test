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
13. Verifikasi total Changelog Import sama dengan baseline langkah 2
14. Tutup modal Changelog Import
15. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total pada teks Pagination
16. Verifikasi total System Log sama dengan baseline langkah 4
17. Buka Activity Log pada tab User Action dan baca angka total pada teks Pagination
18. Verifikasi total Activity Log sama dengan baseline langkah 5

### TC-GS-IMPORT-429: Duplikasi baris

19. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
20. Buka halaman Import > Brand
21. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
22. Tutup modal Changelog Import
23. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total sebagai baseline System Log
24. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
25. Buka halaman Import > Brand
26. Buka row action Duplicate pada baris #2
27. Ubah Brand Name baris salinan menjadi `Lenovo 2`
28. Klik `[Save]`
29. Verifikasi toast sukses "Success, row has been added." tampil
30. Verifikasi kartu Total Rows menampilkan 13
31. Buka Changelog Import dan baca angka total pada teks Pagination
32. Verifikasi total Changelog Import sama dengan baseline langkah 21
33. Tutup modal Changelog Import
34. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total
35. Verifikasi total System Log sama dengan baseline langkah 23
36. Buka Activity Log pada tab User Action dan baca angka total
37. Verifikasi total Activity Log sama dengan baseline langkah 24

### TC-GS-IMPORT-430: Penghapusan baris

38. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
39. Buka halaman Import > Brand
40. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
41. Tutup modal Changelog Import
42. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total sebagai baseline System Log
43. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
44. Buka halaman Import > Brand
45. Buka row action Remove pada baris #3
46. Klik `[Delete]` pada dialog Delete Row
47. Verifikasi toast sukses "Success, row has been deleted." tampil
48. Verifikasi kartu Total Rows menampilkan 11
49. Buka Changelog Import dan baca angka total pada teks Pagination
50. Verifikasi total Changelog Import sama dengan baseline langkah 40
51. Tutup modal Changelog Import
52. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total
53. Verifikasi total System Log sama dengan baseline langkah 42
54. Buka Activity Log pada tab User Action dan baca angka total
55. Verifikasi total Activity Log sama dengan baseline langkah 43

### TC-GS-IMPORT-431: Discard Draft

56. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
57. Buka halaman Import > Brand
58. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
59. Tutup modal Changelog Import
60. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan catat angka total sebagai baseline System Log
61. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
62. Buka halaman Import > Brand
63. Klik `[Discard]` pada Unsaved Banner
64. Klik `[Discard Draft]` pada dialog Discard Draft
65. Verifikasi toast sukses "Success, draft has been discarded." tampil
66. Verifikasi Dropzone menggantikan Staging Table
67. Buka Changelog Import dan baca angka total pada teks Pagination
68. Verifikasi total Changelog Import sama dengan baseline langkah 58
69. Tutup modal Changelog Import
70. Buka System Log pada Detail User Sari Dewi (Tab System Log) dan baca angka total
71. Verifikasi total System Log sama dengan baseline langkah 60
72. Buka Activity Log pada tab User Action dan baca angka total
73. Verifikasi total Activity Log sama dengan baseline langkah 61

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (g); setiap TC memuat aksi nyata (Edit, Duplicate, Remove, Discard Draft) dengan baseline tiga surface sendiri, sehingga memenuhi S-05. Hook umur draft D-76 hanya pemicu (P-5a).
- Alasan melewati sekitar 35 langkah (73 langkah nominal): empat blok homogen satu kelas (absence log) yang berdiri sendiri dengan pemulihan draft di awal tiap blok. Sebagian besar langkah adalah blok baca-log berpola (buka surface, catat atau baca total, `Verifikasi` sama dengan baseline; enam langkah baca per TC) yang tidak dihitung sebagai smell (bagian 3 konvensi). Urutan TC-428, 429, 430, 431: Discard Draft paling akhir karena menghapus draft.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): pemulihan draft (langkah 1, 19, 38, 56), pembukaan surface dan pencatatan baseline (langkah 2 sampai 5, 21 sampai 24, 40 sampai 43, 58 sampai 61), penutupan modal Changelog Import sebelum surface berikutnya (langkah 3, 14, 22, 33, 41, 51, 59, 69), pembukaan halaman Import > Brand sebelum Changelog Import yang datang sesudah Activity Log (langkah 20, 39, 57), pembacaan total (langkah 12, 15, 17 dan padanannya), serta pembukaan Import > Brand dan row action. Asersi absence (kesamaan total) didahului toast sukses atas aksi (langkah 11, 30, 47, 65) sebagai anchor positif yang terhubung ke pemicu (butir 2 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-428 sampai 431 mengasersi absence pada tiga surface tanpa menyebut cara memuat ulang total Pagination (muat ulang halaman atau buka ulang modal); spec membuka ulang tiap surface.
  - TC-GS-IMPORT-428 sampai 431 tidak menyebut apakah baseline System Log dan Activity Log dapat berubah oleh aksi lain di run yang sama; asersi kesamaan total hanya lolos bila tidak ada aksi lain pada akun Sari Dewi di antara baseline dan pembacaan akhir (suite serial).
  - Post Condition semua TC di spec ini "-" dan tidak ada keadaan lain yang perlu dipulihkan selain yang dikerjakan hook `after`.
