---
id: TC-GS-UOM-E2E-056-detail-setup-column-item-type-list
title: "Unit Detail: Setup Column Item Type List (Screening, Hide, Reorder, Pin, Reset, Tutup, Guard)"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-212
  - TC-GS-UOM-313
  - TC-GS-UOM-314
  - TC-GS-UOM-315
  - TC-GS-UOM-316
  - TC-GS-UOM-317
  - TC-GS-UOM-318
  - TC-GS-UOM-319
  - TC-GS-UOM-351
coverage:
  web: automated
---

# Unit Detail: Setup Column Item Type List (Screening, Hide, Reorder, Pin, Reset, Tutup, Guard)

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Flag Guided Tooltip halaman Measurement: disetel true (flag `seen`) oleh kemampuan yang disediakan tim FE untuk integration test; rujukan pernyataan hook suite di `suite.md` (bagian "Hook suite").
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).
- Kebutuhan mock (endpoint dan respons yang dipaksa):
  - Daftar Measurement (tabel utama) mengembalikan unit `Pieces` (Symbol `pc`) beserta Used By (Items) `3` dan Last Updated, supaya baris `Pieces` dapat dibuka lewat `⋯` > Detail.
  - Detail Measurement `Pieces` mengembalikan Item Type `Laptop` (Product Fixed Asset), `Monitor` (Product Fixed Asset), dan `Printer Ink` (Product Supply), tanpa Device Name (instance Client). Detail diambil lewat request terpisah dari List (NC-18).
  - API pendukung di luar modul (identitas pengguna Total Control Client A, menu, flag Guided Tooltip): disediakan tim FE.
  - Path daftar Measurement: `POST /v2/enterprise-management/measurements/list`; path Detail Measurement: `GET /v2/enterprise-management/measurements/{measurement_id}` (`tc-measurement-backend.md`). Rujukan `openapi.yaml` dan `low-level-design.md`: disediakan tim FE.
- Preferensi kolom tabel (visibilitas, urutan, pin) disimpan di `localStorage` browser dengan key unik per tabel (PRD measurement.md §4.2i; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya. Tutup lalu buka kembali Modal Unit Detail dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada.
- Tabel "Kolom Item Type List" (dipakai TC-GS-UOM-314 langkah 32 sampai 35 dan TC-GS-UOM-316 langkah 66 sampai 75): `Item Type`, `Product`.
- Data: tidak ada data dinamis; tidak ada seeding backend.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Item Type List dikembalikan ke default (urutan `Item Type`, `Product`, kedua kolom tampil, tanpa pin) lewat penghapusan preferensi kolom tabel Item Type List di browser (key `localStorage` tabel Item Type List; kemampuan disediakan tim FE, lihat Kemampuan teknis); viewport dikembalikan ke ukuran awal.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Measurement.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar dan Detail Measurement; drag and drop elemen (baris kolom pada modal dan panel); mengatur dan mengembalikan ukuran viewport; scroll horizontal tabel; hover (tooltip); membaca dan menghapus key `localStorage` browser (disediakan tim FE).
- Precondition TC-GS-UOM-212, 313, 314, 315, 316 (viewport diperkecil hingga tabel Item Type List dapat di-scroll horizontal), 317, 318, 319, 351: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

1. Klik `⋯` pada baris Pieces
2. Klik Detail

### TC-GS-UOM-212: Panel Column Visibility pada tabel Item Type List

3. Klik header Actions (⋯) tabel Item Type List
4. Verifikasi Panel Column Visibility berisi `Item Type` dan `Product`
5. Verifikasi Panel Column Visibility berisi item `Setup Column...`

### TC-GS-UOM-313: Screening Popup Setup Column dari tabel Item Type List

6. Klik `Setup Column...`
7. Verifikasi Header: Title `Setup Column`
8. Verifikasi Header: subtitle `Manage column visibility, reorder, and freeze columns.`
9. Verifikasi Header: icon close `[✕]`
10. Verifikasi Body: kolom search `Search column name...`
11. Verifikasi Body: daftar kolom `Item Type` dan `Product` masing-masing dengan checkbox tercentang dan enabled (Hideable)
12. Verifikasi Body: drag handle pada setiap baris kolom
13. Verifikasi Body: icon Pin pada setiap baris kolom
14. Verifikasi Footer rata kanan: `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)
15. Verifikasi Footer tidak memuat tombol `[Cancel]`

### TC-GS-UOM-318: Menutup modal Setup Column tabel Item Type List lewat [✕] dan Esc membuang perubahan preview

16. Uncheck `Product` (tabel ter-preview tanpa Product)
17. Klik `[✕]`
18. Verifikasi kolom `Product` kembali tampil
19. Klik header Actions (⋯) pada tabel Item Type List, lalu klik `Setup Column...`
20. Uncheck `Product`
21. Tekan Esc
22. Verifikasi kolom `Product` kembali tampil dengan hasil yang sama seperti `[✕]`

### TC-GS-UOM-319: Kolom tabel Item Type List terakhir yang tampil tidak dapat di-uncheck

23. Klik header Actions (⋯) pada tabel Item Type List, lalu klik `Setup Column...`
24. Uncheck `Product` sehingga hanya `Item Type` visible
25. Coba uncheck `Item Type`
26. Hover checkbox `Item Type`
27. Verifikasi checkbox `Item Type` disabled (tetap tampil)
28. Verifikasi tooltip `At least one column must remain visible.`
29. Klik `[✕]`
30. Verifikasi kolom `Item Type` dan `Product` kembali tampil

### TC-GS-UOM-314: Hide dan unhide tiap kolom tabel Item Type List

31. Klik header Actions (⋯) pada tabel Item Type List, lalu klik `Setup Column...`

Untuk setiap kolom pada tabel "Kolom Item Type List" di Prerequisites (langkah 32 sampai 35):

32. Uncheck kolom, amati preview tabel
33. Verifikasi kolom hilang dari preview
34. Check kembali kolom
35. Verifikasi kolom kembali tampil pada preview

36. Uncheck `Product`
37. Klik [Save]
38. Verifikasi kolom `Product` tidak tampil pada tabel Item Type List
39. Verifikasi modal Setup Column tertutup
40. Tutup Modal Unit Detail lewat `[✕]`
41. Klik `⋯` pada baris Pieces, lalu klik Detail
42. Verifikasi kolom `Product` tetap tidak tampil
43. Klik header Actions (⋯) > `Setup Column...`
44. Check `Product`
45. Klik [Save]
46. Verifikasi kolom `Product` tampil kembali

### TC-GS-UOM-315: Reorder kolom tabel Item Type List lewat drag

47. Klik header Actions (⋯) pada tabel Item Type List, lalu klik `Setup Column...`
48. Geser `Product` ke atas `Item Type`
49. Verifikasi preview mengurutkan `Product`, `Item Type`
50. Klik [Save]
51. Verifikasi header tabel Item Type List mengurutkan `Product`, `Item Type`
52. Tutup Modal Unit Detail lewat `[✕]`
53. Klik `⋯` pada baris Pieces, lalu klik Detail
54. Verifikasi header tabel Item Type List tetap mengurutkan `Product`, `Item Type`
55. Klik header Actions (⋯) > `Setup Column...`, klik [Reset to Default], klik [Save]
56. Verifikasi urutan header kembali `Item Type`, `Product`

### TC-GS-UOM-351: Reorder kolom tabel Item Type List lewat drag di panel Column Visibility ter-apply langsung dan tersimpan

57. Klik header Actions (⋯) pada tabel Item Type List
58. Geser `Product` ke atas `Item Type` di panel
59. Verifikasi urutan header langsung `Product`, `Item Type` tanpa tombol Save
60. Tutup Modal Unit Detail lewat `[✕]`
61. Klik `⋯` pada baris Pieces, lalu klik Detail
62. Verifikasi urutan header tetap `Product`, `Item Type`
63. Klik header Actions (⋯) > `Setup Column...`, klik [Reset to Default], klik [Save]
64. Verifikasi urutan header kembali `Item Type`, `Product`

### TC-GS-UOM-316: Pin dan unpin tiap kolom tabel Item Type List

65. Perkecil viewport hingga tabel Item Type List dapat di-scroll horizontal

Untuk setiap kolom pada tabel "Kolom Item Type List" di Prerequisites (langkah 66 sampai 75):

66. Klik header Actions (⋯) pada tabel Item Type List, lalu klik `Setup Column...`
67. Klik icon Pin kolom
68. Klik [Save]
69. Scroll tabel Item Type List secara horizontal
70. Verifikasi kolom tetap di posisinya saat tabel di-scroll horizontal
71. Klik header Actions (⋯) > `Setup Column...`
72. Klik icon Pin kolom untuk unpin
73. Klik [Save]
74. Scroll tabel Item Type List secara horizontal
75. Verifikasi kolom kembali ikut bergeser saat di-scroll

76. Kembalikan viewport ke ukuran awal

### TC-GS-UOM-317: Reset to Default modal Setup Column tabel Item Type List

77. Klik header Actions (⋯) pada tabel Item Type List, lalu klik `Setup Column...`
78. Uncheck `Product` dan geser `Product` ke atas `Item Type`
79. Klik [Save]
80. Klik header Actions (⋯) > `Setup Column...`
81. Klik [Reset to Default]
82. Verifikasi preview menampilkan `Item Type` lalu `Product`, keduanya visible
83. Klik [Save]
84. Verifikasi tabel Item Type List memakai susunan default

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-212, 313, 318, 319, 314, 315, 351, 316, 317. Alasan: screening lebih dulu (212, 313); tutup tanpa Save (318) dan guard kolom terakhir (319) sebelum TC yang menyimpan konfigurasi; TC yang menyimpan berakhir dengan reset ke default (315, 351) atau unhide (314) sehingga TC berikutnya mulai dari state bersih; TC-GS-UOM-316 membutuhkan viewport diperkecil dan dipulihkan sebelum TC-GS-UOM-317; TC-GS-UOM-317 di akhir karena reset mengembalikan konfigurasi sekaligus menjadi pemulihan state (prinsip 3 dan 5 konvensi 3).
- Langkah 32 sampai 35 diulang untuk 2 kolom dan langkah 66 sampai 75 untuk 2 kolom (ekspansi: 8 dan 20 langkah); parameter ada di Prerequisites.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 19, 23, 31, 43, 47, 66, 71, 77, 80 (membuka ulang popup Setup Column), langkah 40, 41, 52, 53, 60, 61 (tutup dan buka kembali Detail untuk mengamati persistensi sesuai Expected TC), langkah 65 dan 76 (memperkecil dan mengembalikan viewport).
- Langkah 55 dan 63 adalah langkah akhir TC sumber (Reset to Default sebagai pemulihan) yang ekspektasinya diasersi di langkah 56 dan 64.
- Spec ini melewati sekitar 35 langkah (84 langkah nominal, sekitar 100 dengan ekspansi). Alasan: kesembilan TC menguji satu tabel Item Type List pada satu Modal Unit Detail dengan satu dataset mock dan satu kelas harness (mock UI); semua langkah mengikuti state Setup Column yang sama dan tiap TC berakhir dengan pemulihan ke default. Gagalnya membuka Detail di langkah 2 membuat seluruh blok kehilangan makna, sehingga pemisahan hanya menambah pembukaan Detail tanpa mengurangi risiko.
- Temuan untuk QA:
  - TC-GS-UOM-316 langkah 2 mensyaratkan "klik [Save], scroll tabel horizontal dan amati" untuk dua kolom dengan hanya dua kolom di tabel; lebar tabel melebihi viewport bergantung pada ukuran viewport diperkecil, yang tidak ditentukan TC. Spec menuliskannya sebagai kebutuhan lingkungan.
