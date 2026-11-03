---
id: TC-AC-ACHA-E2E-040-kombinasi-kontrol-list
title: "Kombinasi Search, Filter, Sort, dan Pagination pada List Device Allocation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-342
  - TC-AC-ACHA-343
  - TC-AC-ACHA-344
  - TC-AC-ACHA-345
  - TC-AC-ACHA-346
  - TC-AC-ACHA-347
  - TC-AC-ACHA-348
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-11: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Data Dinamis: TC-AC-ACHA-347 membuat satu alokasi baru yang langsung Completed (pengirim PT ABC, jalur langsung, Client `PT Manufaktur Unggul`, Category NFC, Quantity `1`, Payment Free) lewat sesi API aktor; Allocation ID baru ditangkap dari respons pembuatan (Dynamic Reference) dan tidak di-hardcode. Alokasi ini tidak dapat dihapus lewat UI; seed dipulihkan ke Seed List 30 baris lewat fixture API Pre-setup #20 di hook `after` (disediakan tim FE/BE). TC-AC-ACHA-347 ditaruh paling akhir karena menambah baris ke tabel.
- Kemampuan teknis (disediakan tim FE): sesi API aktor (login API password akun aktor, bukan sesi web; dinyatakan di `suite.md`) untuk membuat alokasi.
- State yang diubah: Search, Filter, Sort, dan Page size dikembalikan ke default di akhir tiap TC.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHA-342: Kombinasi penuh Search, Filter, Sort, dan Pagination

1. Ketik Search `Budi`, tekan Enter
2. Klik ikon Filter
3. Pilih Status `Completed`, klik `[Apply]`
4. Tutup Filter Panel (klik ikon Filter)
5. Klik header kolom Quantity sekali (ascending)
6. Verifikasi hasil adalah irisan Search dan Filter: 3 baris urut Quantity ascending dengan baris teratas `HALC-20260906-00002`, `HALC-20260902-00001`, `HALC-20260901-00001`
7. Ubah Page size menjadi `25`
8. Verifikasi kotak Search masih berisi `Budi` (Search tidak direset oleh Page size)
9. Verifikasi ikon Filter masih menampilkan badge titik (Filter Status `Completed` tidak direset oleh Page size)
10. Verifikasi indikator sort Quantity ascending (`↑`) tetap (Sort tidak direset oleh Page size)
11. Klik `(←)` pada kotak Search
12. Klik ikon Filter
13. Klik `[Clear Field]`, klik `[Apply]`
14. Tutup Filter Panel (klik ikon Filter)
15. Klik header kolom aktif hingga netral (indikator sort hilang)
16. Ubah Page size menjadi `10`

### TC-AC-ACHA-343: Urutan Search dan Filter simetris

17. Klik ikon Filter
18. Pilih Status `Completed`, klik `[Apply]`
19. Tutup Filter Panel (klik ikon Filter)
20. Ketik Search `Budi`, tekan Enter
21. Verifikasi urutan Filter lalu Search menghasilkan 3 baris (`HALC-20260906-00002`, `HALC-20260902-00001`, `HALC-20260901-00001`)
22. Klik `(←)` pada kotak Search
23. Klik ikon Filter
24. Klik `[Clear Field]`, klik `[Apply]`
25. Tutup Filter Panel (klik ikon Filter)
26. Ketik Search `Budi`, tekan Enter
27. Klik ikon Filter
28. Pilih Status `Completed`, klik `[Apply]`
29. Tutup Filter Panel (klik ikon Filter)
30. Verifikasi urutan Search lalu Filter menghasilkan dataset identik: 3 baris (`HALC-20260906-00002`, `HALC-20260902-00001`, `HALC-20260901-00001`)
31. Klik `(←)` pada kotak Search
32. Klik ikon Filter
33. Klik `[Clear Field]`, klik `[Apply]`
34. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-344: Pelepasan Filter mempertahankan Search dan Sort

35. Ketik Search `Budi`, tekan Enter
36. Klik ikon Filter
37. Pilih Status `Completed`, klik `[Apply]`
38. Tutup Filter Panel (klik ikon Filter)
39. Klik header kolom Quantity sekali (ascending)
40. Klik ikon Filter
41. Klik `[Clear Field]`, klik `[Apply]`
42. Tutup Filter Panel (klik ikon Filter)
43. Verifikasi badge titik hilang dari ikon Filter (kriteria Filter dilepas)
44. Verifikasi kotak Search masih berisi `Budi`
45. Verifikasi indikator sort Quantity ascending (`↑`) tetap
46. Verifikasi hasil 6 baris milik `Budi S` dengan baris teratas `HALC-20260906-00002`, `HALC-20260903-00002`, `HALC-20260908-00002`
47. Klik `(←)` pada kotak Search
48. Klik ikon Filter
49. Klik `[Clear Field]`, klik `[Apply]`
50. Tutup Filter Panel (klik ikon Filter)
51. Klik header kolom aktif hingga netral (indikator sort hilang)

### TC-AC-ACHA-345: Pelepasan Search mempertahankan Filter dan Sort

52. Ketik Search `Budi`, tekan Enter
53. Klik ikon Filter
54. Pilih Status `Completed`, klik `[Apply]`
55. Tutup Filter Panel (klik ikon Filter)
56. Klik header kolom Quantity sekali (ascending)
57. Klik ikon `(✕)` pada Search
58. Tekan Enter pada input kosong
59. Verifikasi Search dilepas (kotak Search kosong)
60. Verifikasi badge titik pada ikon Filter masih tampil (Filter Status `Completed` tetap aktif)
61. Verifikasi indikator sort Quantity ascending (`↑`) tetap
62. Verifikasi hasil 16 baris Completed urut Quantity ascending dengan baris teratas `HALC-20260906-00002`, `HALC-20260907-00003`, `HALC-20260905-00001`
63. Klik `(←)` pada kotak Search
64. Klik ikon Filter
65. Klik `[Clear Field]`, klik `[Apply]`
66. Tutup Filter Panel (klik ikon Filter)
67. Klik header kolom aktif hingga netral (indikator sort hilang)

### TC-AC-ACHA-346: Pindah target sort mempertahankan Search dan Filter

68. Ketik Search `Budi`, tekan Enter
69. Klik ikon Filter
70. Pilih Status `Completed`, klik `[Apply]`
71. Tutup Filter Panel (klik ikon Filter)
72. Klik header kolom Quantity sekali (ascending)
73. Klik header kolom Client
74. Verifikasi sort berpindah ke Client ascending (indikator `↑` pada Client, indikator Quantity netral)
75. Verifikasi kotak Search masih berisi `Budi` dan badge titik pada ikon Filter masih tampil (Search dan Filter tidak direset)
76. Verifikasi baris teratas `HALC-20260906-00002`, `HALC-20260902-00001`, `HALC-20260901-00001`
77. Klik `(←)` pada kotak Search
78. Klik ikon Filter
79. Klik `[Clear Field]`, klik `[Apply]`
80. Tutup Filter Panel (klik ikon Filter)
81. Klik header kolom aktif hingga netral (indikator sort hilang)

### TC-AC-ACHA-348: Pagination tidak mereset kontrol lain

82. Ketik Search `Budi`, tekan Enter
83. Klik ikon Filter
84. Pilih Status `Completed`, klik `[Apply]`
85. Tutup Filter Panel (klik ikon Filter)
86. Klik header kolom Quantity sekali (ascending)
87. Ubah Page size menjadi `50`
88. Verifikasi kotak Search masih berisi `Budi` (tidak direset oleh Page size)
89. Verifikasi badge titik pada ikon Filter masih tampil (Filter tidak direset oleh Page size)
90. Verifikasi indikator sort Quantity ascending (`↑`) tetap (Sort tidak direset oleh Page size)
91. Verifikasi seluruh 3 hasil tampil pada satu halaman
92. Klik `(←)` pada kotak Search
93. Klik ikon Filter
94. Klik `[Clear Field]`, klik `[Apply]`
95. Tutup Filter Panel (klik ikon Filter)
96. Klik header kolom aktif hingga netral (indikator sort hilang)
97. Ubah Page size menjadi `10`

### TC-AC-ACHA-347: Create yang tidak cocok dengan Filter tidak tampil

98. Klik ikon Filter
99. Pilih Status `Rejected`, klik `[Apply]`
100. Tutup Filter Panel (klik ikon Filter)
101. Pelaku kedua (sesi API Total Control Principal) membuat alokasi baru yang langsung Completed hingga alokasi tersimpan; Allocation ID baru ditangkap
102. Klik ikon Search, tekan Enter pada input kosong (memuat ulang tabel)
103. Verifikasi tabel menampilkan 4 baris Rejected
104. Verifikasi alokasi baru berstatus Completed tidak muncul pada tabel yang difilter Status `Rejected`
105. Klik `(←)` pada kotak Search
106. Klik ikon Filter
107. Klik `[Clear Field]`, klik `[Apply]`
108. Tutup Filter Panel (klik ikon Filter)

## Notes

- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-4). Seluruh TC primer spec ini (TC-AC-ACHA-342 sampai 348) dikerjakan di sini.
- Urutan dalam spec menyimpang dari urutan nomor TC: TC-AC-ACHA-347 paling akhir karena membuat alokasi baru yang menambah baris dan mengubah dataset TC lain.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): bagian "reset" di akhir tiap TC (`(←)` pada Search, `[Clear Field]` lalu `[Apply]`, penutupan Filter Panel, sort netral, Page size kembali `10`) sebagai pemulihan state (S-09); penutupan Filter Panel sesudah `[Apply]`. Pelaku kedua TC-AC-ACHA-347 memakai sesi API aktor (bukan konteks UI kedua) sehingga tidak memakai `P-2`.
- Asersi tambahan (S-03): "tidak direset" pada TC-AC-ACHA-342 dan TC-AC-ACHA-348 dipecah menjadi tiga `Verifikasi` (Search, Filter, Sort) yang diamati lewat isi kotak Search, badge titik pada ikon Filter, dan indikator sort. TC-AC-ACHA-347 memakai empat baris Rejected sebagai anchor positif sebelum asersi alokasi baru tidak muncul.
- Spec memiliki 108 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (kombinasi kontrol List) pada dataset seed dan akun yang sama; tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna; sebagian besar langkah adalah penyiapan Search, Filter, dan Sort yang diulang per TC serta pemulihannya.
- Pemisahan topik satu dataset (prinsip 1): Search, Filter Panel, Sort, Setup Column, kombinasi kontrol, dan Pagination List memakai dataset Seed List yang sama (Pre-setup #48) dan dipisah menjadi spec 036 sampai 041 karena gabungannya jauh melewati batas ukuran (spec kombinasi kontrol ini saja 108 langkah). Pemisahan per kontrol dipertahankan karena tiap spec memulai dari kondisi default yang dipulihkan di akhir spec dan di hook `after` (Search kosong, tanpa Filter, sort netral, dan Page size 10), sehingga kegagalan keras satu spec tidak membuat spec lain kehilangan makna; di dalam spec ini tiap TC mengakhiri dengan pemulihan state (S-09) dan tidak bergantung pada hasil TC lain, sehingga spec tetap satu (tanpa pemisah nyata: akun, kelas harness, dan dataset sama).
- Temuan untuk QA:
  - TC-AC-ACHA-347 langkah uji kedua ("Pada sesi lain Principal membuat alokasi baru yang langsung Completed") tidak menyebut Category, Client, dan Quantity; spec memakai nilai minimal yang menghasilkan alokasi Completed lewat jalur langsung (disediakan tim FE/BE, R-20).
  - TC-AC-ACHA-347 langkah uji ketiga ("Muat ulang tabel dengan tombol Search Enter ulang") tidak menyebut apakah memuat ulang lewat Enter pada Search kosong; spec memakai klik ikon Search lalu Enter pada input kosong.
