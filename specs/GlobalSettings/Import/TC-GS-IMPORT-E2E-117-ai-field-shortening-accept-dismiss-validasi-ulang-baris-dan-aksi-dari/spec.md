---
id: TC-GS-IMPORT-E2E-117-ai-field-shortening-accept-dismiss-validasi-ulang-baris-dan-aksi-dari
title: "AI Field Shortening: Accept, Dismiss, validasi ulang baris, dan aksi dari halaman basi setelah nilai sel diubah admin lain"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-293
  - TC-GS-IMPORT-294
  - TC-GS-IMPORT-295
  - TC-GS-IMPORT-296
  - TC-GS-IMPORT-302
  - TC-GS-IMPORT-700
  - TC-GS-IMPORT-851
  - TC-GS-IMPORT-852
coverage:
  web: automated
---

# AI Field Shortening: Accept, Dismiss, validasi ulang baris, dan aksi dari halaman basi setelah nilai sel diubah admin lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua (TC-GS-IMPORT-851 dan 852): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net`, hanya memicu perubahan nilai sel lewat sesi API (P-2) dengan `Spectra.env.GS_CLIENTC_TC2_PASSWORD`; klien HTTP disediakan tim FE/BE dan endpoint tidak dikarang.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Tab Brand); perpindahan Tab ke Division dan User Login ditulis sebagai langkah penghubung.
- Kondisi awal tiap TC (Kontrak Fixture R1): Client C tanpa draft pada Sub-Tab yang diuji. Skrip reset draft Client C disediakan tim FE/BE; dijalankan di hook `before` dan sebagai langkah penghubung di antara TC.
- Layanan AI: mock deterministik mode normal (Data Dinamis D-40, tabel D-41 dan D-42); hook `before` memastikan mode normal, hook `after` mengembalikannya ke normal.
- Data Pre-setup yang dibaca (tidak diubah): Division `Engineering` dengan Code `ENG` di Client C (TC-GS-IMPORT-294 dan 302).
- Data Dinamis (berkas upload disediakan tim QA; fixture baru `Fixture.import.aiAcceptDismiss117`):
  - `ai-brand-long.csv` (D-44): kolom `Brand Name`, 1 baris, Brand Name = nilai sumber Brand pertama D-41 (121 karakter); dipakai TC 293, 295, 296, 851, 852. Nilai sumber kedua Brand pada D-41 (125 karakter) dipakai sebagai nilai sunting TC 296.
  - `ai-division-long-code-eng.csv` (D-44): `Division Name,Code`, Division Name = nilai sumber Division pertama D-41 (121 karakter), Code `ENG` (TC 294).
  - `ai-division-dup.csv` (D-44): `Division Name`, Division Name = nilai sumber Division kedua D-41 (121 karakter; saran mock `Engineering`) (TC 302).
  - `ai-ul-first-long-div-typo.csv` (berkas User Login standar D-45): First Name = nilai sumber First Name D-41 (121 karakter), Last Name `Rahmawati`, Email `siti.rahmawati@example.com`, Division `Enginering`, Position kosong (TC 700).
  - Nilai ubahan Admin kedua: `Brand Revisi Satu` (TC 851), `Brand Revisi Dua` (TC 852).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft Client C pada Sub-Tab Brand, Division, dan User Login; kembalikan mock AI ke mode normal.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: input upload berkas; mock AI (D-40); skrip reset draft; sesi API Admin kedua; fixture inspeksi data tersimpan (membaca status dan nilai baris draft di server) disediakan tim FE/BE.
- State global: mock layanan AI (dipulihkan di hook `after`); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-IMPORT-293: Accept memperbarui sel dan memvalidasi ulang baris tanpa sesi edit

1. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long.csv`
2. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
3. Tunggu sampai toast `Success, row has been added.` tidak tampil lagi
4. Klik `[Accept]` pada badge saran sel Brand Name baris #1
5. Verifikasi tidak ada toast baru sesudah klik `[Accept]`
6. Verifikasi sel Brand Name baris #1 berisi `Samsung Electronics Indonesia`
7. Verifikasi baris #1 berstatus `pending`
8. Verifikasi Staging Metric Cards: Total Rows 1
9. Verifikasi Staging Metric Cards: Ready to Import 1
10. Verifikasi Staging Metric Cards: Errors 0
11. Verifikasi footer menampilkan `[Import (1)]`
12. Verifikasi footer tidak menampilkan `[Cancel]` maupun `[Save]` (tidak ada sesi edit)
13. Verifikasi Error Summary Callout tidak tampil

### TC-GS-IMPORT-295: Dismiss menghilangkan badge dan baris tetap error

14. Reset draft Client C Tab Brand lewat skrip reset, lalu muat ulang halaman Import > Brand
15. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long.csv`
16. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
17. Tunggu sampai toast `Success, row has been added.` tidak tampil lagi
18. Klik `[Dismiss]` pada badge saran sel Brand Name baris #1
19. Verifikasi tidak ada toast baru
20. Verifikasi badge hilang dari sel Brand Name baris #1
21. Verifikasi baris #1 tetap berstatus `error`
22. Muat ulang halaman Import > Brand
23. Verifikasi Staging Table menampilkan baris #1 (halaman termuat)
24. Verifikasi badge saran tidak muncul lagi pada nilai sel yang sama
25. Verifikasi baris #1 tetap berstatus `error`
26. Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters" dengan badge "1 row"

### TC-GS-IMPORT-296: Save diblokir saat sel yang di-Dismiss diedit ke nilai lain yang masih melebihi batas

27. Reset draft Client C Tab Brand lewat skrip reset, lalu muat ulang halaman Import > Brand
28. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long.csv`
29. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
30. Klik `[Dismiss]` pada badge saran sel Brand Name baris #1
31. Verifikasi badge saran hilang dari sel Brand Name baris #1
32. Klik `⋯` pada baris #1 lalu pilih Edit
33. Ganti isi sel dengan nilai sumber kedua Brand pada D-41 (125 karakter)
34. Klik `[Save]`
35. Verifikasi `[Save]` diblokir tanpa toast sukses: sel Brand Name baris #1 berborder `danger` dengan pesan "Max. 120 characters"
36. Verifikasi footer tetap menampilkan `[Cancel]` dan `[Save]`
37. Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters" dengan badge "1 row"
38. Klik `[Cancel]`
39. Klik `[Discard]` pada dialog
40. Verifikasi sel Brand Name baris #1 bernilai 121 karakter semula
41. Verifikasi baris #1 berstatus `error`
42. Verifikasi footer tidak menampilkan `[Cancel]` maupun `[Save]`

### TC-GS-IMPORT-851: Accept dari halaman basi ditolak bila nilai sel sudah diubah admin lain

43. Reset draft Client C Tab Brand lewat skrip reset, lalu muat ulang halaman Import > Brand
44. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long.csv`
45. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
46. Verifikasi badge saran tampil pada sel Brand Name baris #1
47. Admin kedua Client C (sesi API): ubah Brand Name baris #1 menjadi `Brand Revisi Satu` hingga tersimpan
48. Verifikasi (fixture inspeksi data tersimpan) baris #1 berstatus `pending` dengan nilai `Brand Revisi Satu`
49. Total Control Client C: klik `[Accept]` pada badge saran yang masih tampil
50. Verifikasi tidak ada dialog
51. Verifikasi tidak ada toast
52. Verifikasi sel Brand Name baris #1 tetap `Brand Revisi Satu` (tidak ditimpa saran lama)
53. Verifikasi badge saran tidak tampil lagi

### TC-GS-IMPORT-852: Dismiss dari halaman basi tidak berefek bila nilai sel sudah diubah admin lain

54. Reset draft Client C Tab Brand lewat skrip reset, lalu muat ulang halaman Import > Brand
55. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long.csv`
56. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
57. Verifikasi badge saran tampil pada sel Brand Name baris #1
58. Admin kedua Client C (sesi API): ubah Brand Name baris #1 menjadi `Brand Revisi Dua` hingga tersimpan
59. Total Control Client C: klik `[Dismiss]` pada badge saran yang masih tampil
60. Verifikasi tidak ada dialog
61. Verifikasi tidak ada toast
62. Muat ulang halaman Import > Brand
63. Verifikasi Staging Table menampilkan baris #1 (halaman termuat)
64. Verifikasi baris #1 berstatus `pending` dengan nilai `Brand Revisi Dua`
65. Verifikasi tidak ada badge saran
66. Verifikasi Staging Metric Cards: Total Rows 1
67. Verifikasi Staging Metric Cards: Ready to Import 1
68. Verifikasi Staging Metric Cards: Errors 0 (Disabled)

### TC-GS-IMPORT-294: Accept pada baris dengan pelanggaran lain, baris tetap error

69. Reset draft Client C Tab Brand lewat skrip reset, lalu muat ulang halaman Import > Division
70. Klik [Upload File] di toolbar dan pilih berkas `ai-division-long-code-eng.csv`
71. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
72. Verifikasi baris #1 berstatus `error`
73. Verifikasi Error Summary Callout memuat "Division Name: Max. 120 characters" dengan badge "1 row"
74. Verifikasi Error Summary Callout memuat "Code already exists" dengan badge "1 row"
75. Klik `[Accept]` pada badge saran sel Division Name baris #1
76. Verifikasi sel Division Name baris #1 berisi `Corporate Strategy and Business Development`
77. Verifikasi baris #1 tetap `error`
78. Verifikasi Error Summary Callout memuat "Code already exists" dengan badge "1 row"
79. Verifikasi Error Summary Callout tidak lagi memuat "Division Name: Max. 120 characters"

### TC-GS-IMPORT-302: Saran Division Name dicek ulang terhadap keunikan

80. Reset draft Client C Tab Division lewat skrip reset, lalu muat ulang halaman Import > Division
81. Klik [Upload File] di toolbar dan pilih berkas `ai-division-dup.csv`
82. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
83. Klik `[Accept]` pada badge saran sel Division Name baris #1
84. Verifikasi sel Division Name baris #1 berisi `Engineering`
85. Verifikasi baris #1 berstatus `duplicate`
86. Verifikasi Staging Metric Cards: Duplicates 1
87. Arahkan kursor ke badge Status baris #1
88. Verifikasi tooltip badge Status: "Division name already exists. This row will be skipped automatically."

### TC-GS-IMPORT-700: Dua badge AI pada baris yang sama dievaluasi terpisah per field

89. Reset draft Client C Tab Division lewat skrip reset, lalu muat ulang halaman Import > User Login
90. Klik [Upload File] di toolbar dan pilih berkas `ai-ul-first-long-div-typo.csv`
91. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
92. Verifikasi sel First Name menampilkan badge "AI suggestion: 'Muhammad Abdurrahman Nurrahman'?" disertai `[Accept]` dan `[Dismiss]`
93. Verifikasi sel Division menampilkan badge "Did you mean 'Engineering'?" disertai `[Accept]` dan `[Dismiss]`
94. Klik `[Accept]` pada badge saran sel First Name
95. Verifikasi sel First Name berisi `Muhammad Abdurrahman Nurrahman` tanpa badge
96. Verifikasi sel Division tetap `Enginering` dengan badge "Did you mean 'Engineering'?"
97. Verifikasi baris #1 tetap `error`
98. Klik `[Accept]` pada badge saran sel Division
99. Verifikasi sel Division berisi `Engineering`
100. Verifikasi baris #1 berstatus `pending`
101. Verifikasi Staging Metric Cards: Total Rows 1
102. Verifikasi Staging Metric Cards: Ready to Import 1
103. Verifikasi Staging Metric Cards: Errors 0

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`, TC-GS-IMPORT-293 sampai 296, 302, 700, 851, 852.
- Urutan TC sumber: Brand (293, 295, 296, 851, 852) lebih dulu, lalu Division (294, 302), lalu User Login (700), supaya perpindahan Tab minimal dan reset draft tiap Tab dilakukan seperlunya (S-10); tidak ada TC yang menghapus data milik TC lain.
- Spec berisi 103 langkah, jauh di atas sekitar 35 langkah. Alasan: delapan TC, tiap TC berdiri sendiri dengan draft barunya, seluruhnya satu kelas (AI Field Shortening, mock normal); kegagalan satu TC tidak membuat TC lain kehilangan makna.
- P-2 (pemicu bukan objek uji): Admin kedua Client C pada langkah 47 dan 58 hanya mengubah nilai sel lewat sesi API; hasilnya diasersi di sesi Total Control Client C. Halaman Total Control Client C tidak dimuat ulang sesudah langkah 46 dan 57, sehingga langkah 49 dan 59 beraksi dari halaman basi.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 dan 17 (menunggu toast lama hilang), 14, 27, 43, 54, 69, 80, 89 (reset draft; pada 14, 27, 43, 54, 80 disertai muat ulang halaman Import pada Tab yang sama, pada 69 dan 89 disertai muat ulang halaman Import pada Tab tujuan), 22 dan 62 (muat ulang), 38 dan 39 (Cancel lalu Discard sesuai Langkah Uji TC 296), 47 dan 58 (pemicu Admin kedua). Langkah 5 dan 19 (`Verifikasi` tidak ada toast) ditulis tepat sesudah pemicu `[Accept]` dan `[Dismiss]`, sebelum `Verifikasi` artefak (8b butir 11). Langkah 23 dan 63 adalah anchor positif halaman termuat sebelum asersi absence badge (8b butir 2).
- Pembagian TC lintas spec: TC-GS-IMPORT-286 sampai 292 dan 697 (badge tampil) ada di spec 115; kasus tanpa badge ada di spec 116; Accept dan Dismiss Reference Suggestion ada di spec 119; Read Only di spec 131; commit tanpa saran AI di spec 137.
- Temuan untuk QA:
  - TC-GS-IMPORT-851 dan 852: Langkah Uji "ubah Brand Name baris #1 ... dan simpan" lewat fixture permintaan tanpa menyebut mekanisme; spec memakai sesi API Admin kedua dan fixture inspeksi data tersimpan yang disediakan tim FE/BE (S-11, S-13).
  - TC-GS-IMPORT-851 Expected b menyatakan "UI hanya di-refresh" tanpa tanda yang bisa diamati; spec mengasersi tidak ada dialog dan tidak ada toast, lalu nilai sel dan badge.
  - TC-GS-IMPORT-296: nilai sumber kedua Brand hanya dirujuk "lihat Data Dinamis D-41" (125 karakter); spec memakai nilai itu apa adanya.
  - TC-GS-IMPORT-294 dan 302: Precondition e menyebut Division `Engineering` ada di Client C (Pre-setup), tetapi Tabel Pre-setup Client C hanya menulis "master data seperti Client A".
  - TC-GS-IMPORT-293 dan 295: Langkah Uji 3 "Tunggu sampai toast ... tidak tampil lagi" tanpa batas waktu tunggu.
