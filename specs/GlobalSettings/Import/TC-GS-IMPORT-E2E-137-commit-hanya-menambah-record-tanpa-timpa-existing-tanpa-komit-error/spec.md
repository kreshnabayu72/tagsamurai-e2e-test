---
id: TC-GS-IMPORT-E2E-137-commit-hanya-menambah-record-tanpa-timpa-existing-tanpa-komit-error
title: "Commit hanya menambah record: tanpa timpa existing, tanpa komit error/duplicate, tanpa saran AI atau master data otomatis"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-301
  - TC-GS-IMPORT-343
  - TC-GS-IMPORT-369
  - TC-GS-IMPORT-370
  - TC-GS-IMPORT-371
  - TC-GS-IMPORT-930
coverage:
  web: automated
---

# Commit hanya menambah record: tanpa timpa existing, tanpa komit error/duplicate, tanpa saran AI atau master data otomatis

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand (Client E); perpindahan ke Sub-Tab atau halaman lain ditulis sebagai langkah.
- Data Pre-setup Client E (tidak diubah spec): Brand `Samsung`; Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (5 item), `Logistik` belum ada; Custom Field Active `Shift` (Dropdown: `Pagi`, `Siang`, `Malam`), `Lembur` belum menjadi opsi.
- Data Dinamis (berkas dan draft lewat fixture `Fixture.import.commitOnly137`, fixture baru; nama literal dari Data Dinamis karena asersi bergantung pada nama dan jumlah): brand-ai-commit.csv (D-44: `Lenovo`, `Dell`, dan Brand Name 121 karakter sumber D-41); user-login-commit-logistik.csv (D-45: Bambang Hartono Division `Engineering`, Citra Wulandari dan Doni Kurniawan Division `Logistik`, Position kosong); brand-12.csv (D-50, draft 12 baris); brand-nikon-samsung.csv (`Nikon` `pending`, `Samsung` `duplicate`); brand-mixed-3.csv (`Nikon` `pending`, Brand Name 121 karakter huruf `A` `error`, `Samsung` `duplicate`); user-login-commit-shift.csv (D-86).
- Kemampuan teknis (disediakan tim FE/BE): mock layanan AI mode normal (D-40, D-41, D-42) dipulihkan ke normal di hook `after`; skrip reset Client E sesuai D-47 (hapus Brand, User, Division, Position hasil commit, draft, hasil commit terakhir, dan penanda Banner Hasil Commit); penyiapan draft lewat fixture.
- State global: mock AI (normal, tidak diubah selama spec); Client E dimutasi lalu direset. Suite Import berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 dan mock AI dikembalikan ke normal.

## Test Steps

### TC-GS-IMPORT-301: Saran tidak pernah diterapkan otomatis termasuk saat commit berjalan

1. Reset Client E ke tanpa draft Tab Brand (D-47) dan pastikan mock AI mode normal (D-40), lalu muat ulang halaman Import > Brand
2. Klik [Upload File] di toolbar dan pilih berkas brand-ai-commit.csv
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi Footer menampilkan `[Import (2)]`
5. Verifikasi baris #3 berstatus `error`
6. Verifikasi baris #3 menampilkan badge saran
7. Klik [Import (2)]
8. Muat ulang halaman Import berkala sampai Footer menampilkan `[Import (0)]` Disabled dengan tooltip "No rows are ready to import."
9. Verifikasi Staging Table berisi 1 baris `error`
10. Verifikasi nilai sel Brand Name baris itu tetap 121 karakter semula
11. Verifikasi badge "AI suggestion: 'Samsung Electronics Indonesia'?" masih tampil
12. Verifikasi Staging Metric Cards Total Rows 1
13. Verifikasi Staging Metric Cards Errors 1
14. Buka Master Reference > Brand
15. Verifikasi daftar Brand Client E memuat `Samsung`, `Lenovo`, dan `Dell` (3 item)
16. Verifikasi daftar Brand Client E tidak memuat `Samsung Electronics Indonesia` maupun nilai 121 karakter
17. Hapus Brand `Lenovo` dan `Dell` serta draft Brand Client E lewat fixture pembersihan (D-47)

### TC-GS-IMPORT-343: Tidak ada Division atau Position dibuat otomatis saat commit

18. Reset Client E ke tanpa draft Tab User Login (D-47), lalu buka Import > User Login
19. Klik [Upload File] di toolbar dan pilih berkas user-login-commit-logistik.csv
20. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
21. Verifikasi Footer menampilkan `[Import (1)]`
22. Verifikasi Error Summary Callout memuat "Division not found"
23. Verifikasi Error Summary Callout menampilkan badge "2 rows"
24. Klik [Import (1)]
25. Muat ulang halaman Import berkala sampai Footer menampilkan `[Import (0)]` Disabled dengan tooltip "No rows are ready to import."
26. Verifikasi Staging Table berisi 2 baris `error` dengan Division `Logistik`
27. Verifikasi Staging Metric Cards Total Rows 2
28. Verifikasi Staging Metric Cards Errors 2
29. Buka Global Settings > User > Division
30. Verifikasi tabel Division menampilkan 5 baris
31. Verifikasi daftar Division tidak memuat `Logistik`
32. Hapus User Login `bambang.hartono@example.com` dan draft User Login Client E lewat fixture pembersihan (D-47)

### TC-GS-IMPORT-369: Commit tidak menulis Changelog modul target, hanya satu entri ringkasan job

33. Reset Client E ke tanpa draft (D-47), siapkan draft Brand D-50 lewat fixture
34. Buka halaman Master Reference > Brand
35. Buka Changelog modul Brand (icon [Changelog])
36. Catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state) sebagai baseline Changelog Brand
37. Tutup modal Changelog modul Brand dan buka halaman Import > Brand
38. Buka Changelog Import (icon [Changelog] di header halaman)
39. Klik icon Filter
40. Pilih Action `Import Brand` pada dropdown Action
41. Klik `[Apply]`
42. Catat angka total pada teks Pagination sebagai baseline Changelog Import
43. Tutup modal Changelog Import
44. Klik [Import (12)]
45. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
46. Buka halaman Master Reference > Brand
47. Verifikasi tabel Brand Client E menampilkan Pagination "Showing 1 - 10 of 13 items"
48. Buka Changelog modul Brand (icon [Changelog])
49. Verifikasi total pada Pagination Changelog modul Brand sama dengan baseline langkah 36
50. Tutup modal Changelog modul Brand dan buka halaman Import > Brand
51. Buka Changelog Import (icon [Changelog] di header halaman)
52. Klik icon Filter
53. Pilih Action `Import Brand` pada dropdown Action
54. Klik `[Apply]`
55. Verifikasi total pada Pagination Changelog Import dengan Filter Action `Import Brand` bertambah tepat satu dibanding baseline langkah 42
56. Verifikasi baris pertama tabel (sort default Date descending) memiliki Action `Import Brand`

### TC-GS-IMPORT-370: Impor hanya menambah record, Brand existing pada baris duplicate tidak ditimpa

57. Reset Client E ke tanpa draft (D-47), siapkan draft Brand 2 baris dari brand-nikon-samsung.csv (`Nikon` `pending`, `Samsung` `duplicate`) lewat fixture
58. Buka halaman Master Reference > Brand
59. Catat nilai kolom Last Updated Brand `Samsung`
60. Buka halaman Import > Brand
61. Klik [Import (1)]
62. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
63. Verifikasi Dropzone tampil (baris `Samsung` sudah dihapus dari Staging Table tanpa disisipkan)
64. Buka halaman Master Reference > Brand
65. Verifikasi Brand `Nikon` ada di halaman Master Reference > Brand Client E
66. Verifikasi Brand `Samsung` tampil satu kali dengan nama `Samsung`
67. Verifikasi Last Updated Brand `Samsung` sama dengan nilai langkah 59

### TC-GS-IMPORT-371: Baris error dan duplicate tidak pernah dikomit

68. Reset Client E ke tanpa draft (D-47), siapkan draft Brand 3 baris dari brand-mixed-3.csv (`Nikon` `pending`, Brand Name 121 karakter huruf `A` `error`, `Samsung` `duplicate`) lewat fixture, lalu muat ulang halaman Import > Brand
69. Klik [Import (1)]
70. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
71. Verifikasi Staging Table masih menampilkan 1 baris `error` (Brand Name 121 karakter)
72. Verifikasi Staging Table tidak menampilkan baris `duplicate`
73. Verifikasi kartu Errors 1
74. Verifikasi kartu Duplicates 0
75. Buka halaman Master Reference > Brand
76. Verifikasi halaman Master Reference > Brand Client E memuat Brand `Nikon`
77. Verifikasi tidak ada Brand dengan nama 121 karakter huruf `A`
78. Verifikasi `Samsung` tetap satu

### TC-GS-IMPORT-930: Tidak ada opsi Custom Field dibuat otomatis saat commit

79. Reset Client E ke tanpa draft Tab User Login (D-47), lalu buka Import > User Login
80. Klik [Upload File] di toolbar dan pilih berkas user-login-commit-shift.csv
81. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
82. Verifikasi Footer menampilkan `[Import (1)]`
83. Verifikasi Error Summary Callout memuat "Shift: Invalid option"
84. Verifikasi Error Summary Callout menampilkan badge "2 rows"
85. Klik [Import (1)]
86. Muat ulang halaman Import berkala sampai Footer menampilkan `[Import (0)]` Disabled dengan tooltip "No rows are ready to import."
87. Verifikasi Staging Table berisi 2 baris `error` dengan Shift `Lembur`
88. Verifikasi Staging Metric Cards Total Rows 2
89. Verifikasi Staging Metric Cards Errors 2
90. Buka Global Settings > User > Custom Field dan buka Value Setting Shift
91. Verifikasi Value Setting Shift Client E tetap `Pagi, Siang, Malam`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan (301, 343, 369, 370, 371, 930); semuanya commit di Client E sehingga tidak ada aksi yang menghabisi data pada spec ini selain reset antar blok.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 18, 33, 57, 68, dan 79 (reset Client E dan penyiapan draft karena tiap TC mensyaratkan Client E direset sebelum TC); langkah 17 dan 32 (pemulihan sesuai Post Condition TC-301 dan TC-343, Data Dinamis D-47); langkah 8, 25, 45, 62, 70, dan 86 (menunggu commit selesai); langkah 36 dan 42 (mencatat baseline Changelog sebelum aksi pemicu); langkah 37, 43, dan 50 (menutup modal dan pindah halaman); langkah 59 (baseline Last Updated).
- Baseline Changelog (S-12): jumlah total Changelog modul Brand dan Changelog Import difilter `Import Brand` dicatat sebelum aksi commit (langkah 36 dan 42) dan dibandingkan sesudah commit (langkah 49 dan 55); asersi jumlah, bukan absence, sehingga tidak butuh spec kelas g. Anchor positif commit membuat record: langkah 47.
- Anchor positif untuk asersi absence: langkah 15 sebelum langkah 16, langkah 30 sebelum langkah 31, langkah 76 sebelum langkah 77, dan langkah 90 sebelum langkah 91 (Value Setting terbuka).
- Spec melewati sekitar 35 langkah (91 langkah). Alasan: enam blok TC homogen (satu objek uji "commit hanya menambah record") yang berdiri sendiri dan masing-masing mereset Client E; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah prefix berulang (upload, auto-match, Confirm Mapping, tunggu commit) mendominasi jumlah langkah.
- Pembagian TC lintas spec: kontrol worker commit tidak dipakai; mock AI mode normal hanya prasyarat TC-301, bukan objek uji kelas lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-301 dan TC-GS-IMPORT-343: Post Condition a (Brand `Lenovo` dan `Dell` tersimpan dan draft berisi 1 baris `error`; User Login `bambang.hartono@example.com` tersimpan) sebagian sudah teramati lewat Expected c TC-301 dan tidak diulang; User Login `bambang.hartono@example.com` tersimpan tidak punya langkah observasi di TC-343 sehingga tidak diasersi.
  - TC-GS-IMPORT-369: Expected a mengasumsikan Brand Client E sebelum commit hanya `Samsung` ("13 items"); TC tidak menyatakan bahwa Client E tidak memuat Brand lain selain Pre-setup dan hasil reset D-47.
  - TC-GS-IMPORT-370, TC-GS-IMPORT-371: berkas brand-nikon-samsung.csv dan brand-mixed-3.csv tidak punya entri Data Dinamis; isinya diambil dari kolom Data Uji TC masing-masing.
  - TC-GS-IMPORT-930: Post Condition (draft berisi 2 baris `error`, User Login `bambang.hartono@example.com` tersimpan) tanpa langkah observasi di TC; tidak diasersi.
  - Data Dinamis commit (Brand `Nikon`, `Lenovo`, `Dell`, nama user D-45) literal tanpa suffix per run karena asersi bergantung pada nama; pengecualian S-12 untuk data ini belum dinyatakan di konvensi, dipertahankan dengan reset D-47 dan suite serial.
