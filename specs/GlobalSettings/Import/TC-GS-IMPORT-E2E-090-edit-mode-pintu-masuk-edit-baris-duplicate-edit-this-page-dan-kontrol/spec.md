---
id: TC-GS-IMPORT-E2E-090-edit-mode-pintu-masuk-edit-baris-duplicate-edit-this-page-dan-kontrol
title: "Edit Mode: pintu masuk (Edit baris, Duplicate, Edit this page) dan kontrol yang Disabled atau Hidden selama sesi edit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-190
  - TC-GS-IMPORT-192
  - TC-GS-IMPORT-193
  - TC-GS-IMPORT-196
  - TC-GS-IMPORT-197
  - TC-GS-IMPORT-198
  - TC-GS-IMPORT-199
  - TC-GS-IMPORT-200
  - TC-GS-IMPORT-203
  - TC-GS-IMPORT-664
coverage:
  web: automated
---

# Edit Mode: pintu masuk (Edit baris, Duplicate, Edit this page) dan kontrol yang Disabled atau Hidden selama sesi edit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis: draft dasar Client A D-01 (Draft Brand 12 baris `pending` dari `brand-12.csv`: #1 `Acme Corp`, #2 `Lenovo`, #3 `Zebra Technologies`, #4 `Honeywell`, #5 `Dell`, #6 `HP Inc`, #7 `Canon`, #8 `Epson`, #9 `Brother`, #10 `Logitech`, #11 `Cisco`, #12 `Asus`), dipulihkan ke kondisi Population oleh hook `beforeEach` sesuai Kontrak Fixture R2; nama literal karena asersi bergantung pada isi D-01 (pengecualian S-12). Tidak ada sel yang diubah nilainya oleh spec ini; semua sesi edit ditutup tanpa perubahan.
- Kemampuan teknis: hover untuk tooltip, klik Breadcrumb, tombol paginator, skrip pemulihan draft D-01 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`). Sesi edit Duplicate terakhir (langkah 76) tidak ditutup oleh spec; hook `afterEach` memulihkan draft D-01 dan melepas kunci sesi (disediakan tim FE/BE).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Brand Client A dipulihkan ke D-01 dan kunci sesi edit dilepas lewat skrip pemulihan.

## Test Steps

### TC-GS-IMPORT-190: Edit baris tunggal lewat row action

1. Klik `⋯` pada baris #3, pilih `Edit`
2. Verifikasi seluruh sel baris #3 (`Zebra Technologies`) menjadi input aktif
3. Verifikasi footer `[Import (12)]` tidak tampil
4. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
5. Verifikasi kolom Checkbox Hidden di seluruh tabel
6. Verifikasi kolom Actions Hidden di seluruh tabel
7. Klik `[Cancel]`

### TC-GS-IMPORT-196: Footer Import (N) digantikan Cancel dan Save

8. Klik `⋯` pada baris #1, pilih `Edit`
9. Verifikasi footer `[Import (12)]` tidak tampil
10. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
11. Klik `[Cancel]`
12. Verifikasi footer `[Import (12)]` tampil kembali
13. Verifikasi footer tidak menampilkan `[Cancel]` dan `[Save]`

### TC-GS-IMPORT-203: Klik sel baris lain tanpa perubahan

14. Klik `⋯` pada baris #1, pilih `Edit`
15. Klik sel baris #4 tanpa mengubah apa pun
16. Verifikasi tidak ada dialog yang tampil
17. Verifikasi footer tetap `[Cancel]` dan `[Save]`
18. Verifikasi baris #1 tetap input aktif
19. Verifikasi baris #4 tetap tampil sebagai teks
20. Klik `[Cancel]`

### TC-GS-IMPORT-198: Paginator dan page size Disabled dengan tooltip

21. Klik `⋯` pada baris #1, pilih `Edit`
22. Arahkan kursor ke tombol halaman 2 pada paginator
23. Verifikasi tombol halaman 2 tampil Disabled
24. Verifikasi tooltip pada tombol halaman 2: "Finish or cancel the current edit first."
25. Arahkan kursor ke Rows per page
26. Verifikasi Rows per page tampil Disabled
27. Verifikasi tooltip pada Rows per page: "Finish or cancel the current edit first."
28. Klik `[Cancel]`

### TC-GS-IMPORT-199: Sub-Tab Disabled dengan tooltip

29. Klik `⋯` pada baris #1, pilih `Edit`
30. Arahkan kursor ke Sub-Tab Measurement
31. Verifikasi Sub-Tab Measurement tampil Disabled
32. Verifikasi tooltip pada Sub-Tab Measurement: "Finish or cancel the current edit first."
33. Klik Sub-Tab Measurement
34. Verifikasi Breadcrumb tetap `Import > Brand`
35. Verifikasi baris #1 tetap input aktif
36. Klik `[Cancel]`

### TC-GS-IMPORT-200: Staging Metric Cards tidak dapat diklik

37. Klik `⋯` pada baris #1, pilih `Edit`
38. Arahkan kursor ke kartu Ready to Import
39. Verifikasi kartu Ready to Import tampil Disabled
40. Verifikasi tooltip pada kartu Ready to Import: "Finish or cancel the current edit first."
41. Klik kartu Ready to Import
42. Verifikasi tabel tidak berubah (filter tidak diterapkan)
43. Verifikasi kartu Total Rows tetap tampil Active
44. Klik `[Cancel]`

### TC-GS-IMPORT-197: Kolom Checkbox, kolom Actions, dan Bulk Action Bar Hidden serta seleksi dibuang

45. Centang baris #1 dan #2
46. Verifikasi Bulk Action Bar tampil dengan "2 Rows selected"
47. Aktifkan Switch `Edit this page`
48. Verifikasi kolom Checkbox Hidden
49. Verifikasi kolom Actions (`⋯`) Hidden
50. Verifikasi Bulk Action Bar Hidden
51. Klik `[Cancel]`
52. Verifikasi kolom Checkbox tampil kembali
53. Verifikasi baris #1 dan #2 tidak tercentang
54. Verifikasi Bulk Action Bar tidak tampil

### TC-GS-IMPORT-193 dan TC-GS-IMPORT-664 varian 2: Edit this page

55. Aktifkan Switch `Edit this page`
56. Verifikasi seluruh 10 baris halaman 1 (`Row #` 1 sampai 10) menjadi input aktif
57. Verifikasi footer `[Import (12)]` tidak tampil
58. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
59. Arahkan kursor ke tombol halaman 2 pada paginator
60. Verifikasi tombol halaman 2 tampil Disabled
61. Verifikasi tooltip pada tombol halaman 2: "Finish or cancel the current edit first."
62. Arahkan kursor ke Rows per page
63. Verifikasi Rows per page tampil Disabled
64. Verifikasi tooltip pada Rows per page: "Finish or cancel the current edit first."
65. Klik tombol halaman 2 pada paginator
66. Verifikasi halaman aktif tetap halaman 1
67. Klik `[Cancel]`

### TC-GS-IMPORT-664 varian 3: Edit baris

68. Klik `⋯` pada baris #4, pilih `Edit`
69. Arahkan kursor ke tombol halaman 2 pada paginator
70. Verifikasi tombol halaman 2 tampil Disabled dan tooltip "Finish or cancel the current edit first."
71. Arahkan kursor ke Rows per page
72. Verifikasi Rows per page tampil Disabled dan tooltip "Finish or cancel the current edit first."
73. Klik tombol halaman 2 pada paginator
74. Verifikasi halaman aktif tetap halaman 1
75. Klik `[Cancel]`

### TC-GS-IMPORT-192 dan TC-GS-IMPORT-664 varian 1: Duplicate (sesi terakhir, tidak ditutup spec)

76. Klik `⋯` pada baris #2 `Lenovo`, pilih `Duplicate`
77. Verifikasi baris salinan muncul tepat di bawah baris #2 dalam mode penyuntingan
78. Verifikasi penomoran Row #: baris sumber #2, salinan #3, baris `Zebra Technologies` bergeser menjadi #4
79. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
80. Arahkan kursor ke tombol halaman 2 pada paginator
81. Verifikasi tombol halaman 2 tampil Disabled
82. Verifikasi tooltip pada tombol halaman 2: "Finish or cancel the current edit first."
83. Arahkan kursor ke Rows per page
84. Verifikasi Rows per page tampil Disabled
85. Verifikasi tooltip pada Rows per page: "Finish or cancel the current edit first."
86. Klik tombol halaman 2 pada paginator
87. Verifikasi halaman aktif tetap halaman 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-664 dipecah per varian dan ditempel pada sesi edit TC lain yang sudah dibuka (varian 2 pada TC-193, varian 1 pada TC-192) supaya tidak membuka sesi Duplicate dan Edit this page dua kali; varian 3 (Edit baris #4) berdiri sendiri. Sesi Duplicate dijalankan paling akhir karena penutupan sesi Duplicate tanpa perubahan tidak dispesifikasi TC dan dikerjakan hook `afterEach` (prinsip 5 bagian 3).
- Langkah penghubung (tanpa `Verifikasi`): `[Cancel]` pada langkah 7, 11, 20, 28, 36, 44, 51, 67, 75 menutup sesi edit tanpa perubahan (tanpa dialog, sesuai Expected TC-196 dan TC-203) agar TC berikutnya dimulai dari tampilan normal; langkah 45 menjalankan langkah 1 TC-197.
- Spec berisi 87 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (Edit Mode), tiap blok membuka dan menutup sesi sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-201, 202, dan 235 (Edit Mode: Error Callout, Upload File, keyboard) ada di spec 091; TC-GS-IMPORT-204 di spec 097.
- Temuan untuk QA:
  - TC-GS-IMPORT-192 dan TC-GS-IMPORT-664 varian 1 (Duplicate) tidak menyebut cara mengakhiri sesi Duplicate tanpa perubahan (apakah `[Cancel]` memunculkan dialog Discard Changes); spec tidak menutup sesi itu dan menyerahkannya ke hook `afterEach` (pemulihan draft dan pelepasan kunci disediakan tim FE/BE).
  - TC-GS-IMPORT-199 Expected b menyebut "Setelah klik Breadcrumb tetap `Import > Brand`" padahal Langkah 4 mengklik Sub-Tab Measurement, bukan Breadcrumb; spec mengasersi Breadcrumb tetap `Import > Brand` setelah klik Sub-Tab (langkah 33 sampai 34).
  - TC-GS-IMPORT-197 Expected b menyebut tiga elemen Hidden (kolom Checkbox, kolom Actions, Bulk Action Bar); dipecah menjadi langkah 48, 49, 50 (S-01).
  - Post Condition semua TC di spec ini kosong atau tidak ada observasi; tidak diasersi (S-01).
