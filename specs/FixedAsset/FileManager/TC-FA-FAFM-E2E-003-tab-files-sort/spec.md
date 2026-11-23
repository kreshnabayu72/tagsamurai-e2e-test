---
id: TC-FA-FAFM-E2E-003-tab-files-sort
title: "Sort tab Files: urutan default dan urutan per kolom"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FAFM-01", "TBL-04a", "TBL-04e", "EB-SRT-1", "EB-SRT-2", "EB-SRT-3@tabel-files"]
smoke: []
dependsOn: []
trace:
  "T-FAFM-01": [4, 6, 8, 16, 21, 28, 30, 36, 38, 43, 46, 52, 54, 59, 61, 64, 66, 79, 81, 84, 86, 89, 91, 94, 96, 99, 101]
  "TBL-04a": [4, 10, 26, 50, 77]
  "TBL-04e": [6, 8, 28, 30]
  "EB-SRT-1": [6, 14, 28, 36, 38, 43, 52, 59]
  "EB-SRT-2": [43, 44, 46, 70, 72]
  "EB-SRT-3@tabel-files": [10, 32]
anchor: [3, 12, 19, 25, 34, 41, 49, 57, 76]
coverage:
  web: automated
---

# Sort tab Files: urutan default dan urutan per kolom

## Prerequisites
- Aktor: Total Control, user `Sari Utami {runId}` (tampil `Sari U`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman Settings > File Manager.
- Data:
  - Group `Aset Alfa {runId}`, `Aset Beta {runId}`, dan `Aset Gamma {runId}` ada di entitas aktor. Aset `Laptop Dell Latitude 5420 {runId}`, `Aset Urut Alfa {runId}`, dan `Aset Urut Beta {runId}` ada di entitas aktor; Reference `Kartu Urut {runId}` adalah nama custom field.
  - User `Budi Sanjaya {runId}`, `Budi Santoso {runId}`, dan `Agus Wibowo {runId}` ada di entitas aktor; nama tampilnya `Budi S`, `Budi S`, dan `Agus W`.
  - Urutan pembuatan dari paling lama ke paling baru, dengan selisih waktu unggah minimal satu menit antar baris, kecuali dinyatakan bersamaan: DU-003-1, DU-003-2, DU-003-3; DU-003-4, DU-003-5, DU-003-6; DU-003-7, DU-003-8, DU-003-9; DU-003-10, DU-003-11, DU-003-12, DU-003-13, DU-003-14; DU-003-15, DU-003-16, DU-003-17; DU-003-18, DU-003-19, DU-003-20, DU-003-21, lalu DU-003-22 bersamaan dengan DU-003-23; DU-003-24, DU-003-25, DU-003-26; DU-003-27 dibuat berurutan menurut nomor `{n}` dari 1 sampai 12; dan DU-003-36 dibuat lebih dulu daripada DU-003-37.
  - DU-003-1: File File Name `charlie-nm-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-2: File File Name `alpha-nm-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-3: File File Name `Bravo-nm-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-4: File File Name `Ezra-ak-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-5: File File Name `Elan-ak-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-6: File File Name `Élan-ak-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-7: File File Name `alpha-sy-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-8: File File Name `3D-printer-sy-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-9: File File Name `#gudang-sy-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-10: File File Name `s100-sz-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-11: File File Name `s2-sz-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `2.0 KB`, Uploaded By `Sari U`.
  - DU-003-12: File File Name `s1200-sz-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `1.2 MB`, Uploaded By `Sari U`.
  - DU-003-13: File File Name `s10-sz-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `10.0 KB`, Uploaded By `Sari U`.
  - DU-003-14: File File Name `s900-sz-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `900.0 KB`, Uploaded By `Sari U`.
  - DU-003-15: File File Name `tgl1-dt-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-16: File File Name `tgl2-dt-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-17: File File Name `tgl3-dt-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-18: File File Name `grp1-gr-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-19: File File Name `grp2-gr-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Beta {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-20: File File Name `grp3-gr-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-21: File File Name `grp4-gr-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Beta {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-22: File File Name `tie1-gr-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Gamma {runId}`, Size `100.0 KB`, Uploaded By `Sari U` (diunggah bersamaan dengan DU-003-23).
  - DU-003-23: File File Name `tie2-gr-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Gamma {runId}`, Size `100.0 KB`, Uploaded By `Sari U` (diunggah bersamaan dengan DU-003-22).
  - DU-003-24: File File Name `up2-up-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Budi S`, Nama Lengkap Pengunggah `Budi Sanjaya {runId}`.
  - DU-003-25: File File Name `up3-up-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Agus W`, Nama Lengkap Pengunggah `Agus Wibowo {runId}`.
  - DU-003-26: File File Name `up1-up-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Budi S`, Nama Lengkap Pengunggah `Budi Santoso {runId}`.
  - DU-003-27: File File Name `vol-{n}-pg-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Aset Alfa {runId}`, Size `{n}0.0 KB`, Uploaded By `Sari U`.
  - DU-003-36: File File Name `ala-az-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Urut Beta {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
  - DU-003-37: File File Name `bmb-az-{runId}.jpg`, File Format `JPG`, Source `Custom Field Document`, Reference `Kartu Urut {runId}`, Asset `Aset Urut Alfa {runId}`, Group `Aset Alfa {runId}`, Size `100.0 KB`, Uploaded By `Sari U`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Urutan default Upload Date terbaru di atas dan sort File Name tiga klik
1. Klik tab `Asset Documents`
2. Ketik Search `-nm-{runId}`, tekan Enter
3. Verifikasi baris `alpha-nm-{runId}.pdf`, `Bravo-nm-{runId}.pdf`, dan `charlie-nm-{runId}.pdf` tampil
4. Verifikasi urutan baris dari atas ke bawah: `Bravo-nm-{runId}.pdf`, `alpha-nm-{runId}.pdf`, `charlie-nm-{runId}.pdf`
5. Klik ikon sort pada header kolom `File Name`
6. Verifikasi urutan baris dari atas ke bawah: `alpha-nm-{runId}.pdf`, `Bravo-nm-{runId}.pdf`, `charlie-nm-{runId}.pdf`
7. Klik ikon sort pada header kolom `File Name` sekali lagi
8. Verifikasi urutan baris dari atas ke bawah: `charlie-nm-{runId}.pdf`, `Bravo-nm-{runId}.pdf`, `alpha-nm-{runId}.pdf`
9. Klik ikon sort pada header kolom `File Name` untuk ketiga kalinya
10. Verifikasi urutan baris dari atas ke bawah kembali ke urutan default: `Bravo-nm-{runId}.pdf`, `alpha-nm-{runId}.pdf`, `charlie-nm-{runId}.pdf`

### Sort File Name dengan huruf beraksen
11. Ganti isi kotak search dengan `-ak-{runId}`, tekan Enter
12. Verifikasi baris `Ezra-ak-{runId}.pdf`, `Elan-ak-{runId}.pdf`, dan `Élan-ak-{runId}.pdf` tampil
13. Klik ikon sort pada header kolom `File Name`
14. Verifikasi baris `Ezra-ak-{runId}.pdf` berada di urutan terakhir
15. Klik ikon sort pada header kolom `File Name` sekali lagi
16. Verifikasi baris `Ezra-ak-{runId}.pdf` berada di urutan pertama
17. Klik ikon sort pada header kolom `File Name` untuk ketiga kalinya

### Sort File Name dengan nilai diawali angka dan simbol
18. Ganti isi kotak search dengan `-sy-{runId}`, tekan Enter
19. Verifikasi baris `alpha-sy-{runId}.pdf`, `3D-printer-sy-{runId}.pdf`, dan `#gudang-sy-{runId}.pdf` tampil
20. Klik ikon sort pada header kolom `File Name`
21. Verifikasi baris `alpha-sy-{runId}.pdf`, `3D-printer-sy-{runId}.pdf`, dan `#gudang-sy-{runId}.pdf` masing-masing tampil satu kali
22. Klik ikon sort pada header kolom `File Name` sekali lagi
23. Klik ikon sort pada header kolom `File Name` untuk ketiga kalinya

### Sort Size numerik menurut nilai byte dan bukan teks terformat
24. Ganti isi kotak search dengan `-sz-{runId}`, tekan Enter
25. Verifikasi baris `s100-sz-{runId}.pdf`, `s2-sz-{runId}.pdf`, `s1200-sz-{runId}.pdf`, `s10-sz-{runId}.pdf`, dan `s900-sz-{runId}.pdf` tampil
26. Verifikasi urutan baris default dari atas ke bawah: `s900-sz-{runId}.pdf`, `s10-sz-{runId}.pdf`, `s1200-sz-{runId}.pdf`, `s2-sz-{runId}.pdf`, `s100-sz-{runId}.pdf`
27. Klik ikon sort pada header kolom `Size`
28. Verifikasi urutan Size dari atas ke bawah: `2.0 KB`, `10.0 KB`, `100.0 KB`, `900.0 KB`, `1.2 MB`
29. Klik ikon sort pada header kolom `Size` sekali lagi
30. Verifikasi urutan Size dari atas ke bawah: `1.2 MB`, `900.0 KB`, `100.0 KB`, `10.0 KB`, `2.0 KB`
31. Klik ikon sort pada header kolom `Size` untuk ketiga kalinya
32. Verifikasi urutan baris kembali ke urutan default: `s900-sz-{runId}.pdf`, `s10-sz-{runId}.pdf`, `s1200-sz-{runId}.pdf`, `s2-sz-{runId}.pdf`, `s100-sz-{runId}.pdf`

### Sort Upload Date Oldest First dan Newest First
33. Ganti isi kotak search dengan `-dt-{runId}`, tekan Enter
34. Verifikasi baris `tgl1-dt-{runId}.pdf`, `tgl2-dt-{runId}.pdf`, dan `tgl3-dt-{runId}.pdf` tampil
35. Klik ikon sort pada header kolom `Upload Date`
36. Verifikasi urutan baris dari atas ke bawah: `tgl1-dt-{runId}.pdf`, `tgl2-dt-{runId}.pdf`, `tgl3-dt-{runId}.pdf`
37. Klik ikon sort pada header kolom `Upload Date` sekali lagi
38. Verifikasi urutan baris dari atas ke bawah: `tgl3-dt-{runId}.pdf`, `tgl2-dt-{runId}.pdf`, `tgl1-dt-{runId}.pdf`
39. Klik ikon sort pada header kolom `Upload Date` untuk ketiga kalinya

### Sort Group A-Z dengan nilai sama diurutkan menurut default sort
40. Ganti isi kotak search dengan `-gr-{runId}`, tekan Enter
41. Verifikasi baris `grp1-gr-{runId}.pdf`, `grp2-gr-{runId}.pdf`, `grp3-gr-{runId}.pdf`, `grp4-gr-{runId}.pdf`, `tie1-gr-{runId}.pdf`, dan `tie2-gr-{runId}.pdf` tampil
42. Klik ikon sort pada header kolom `Group`
43. Verifikasi empat baris pertama dari atas ke bawah: `grp3-gr-{runId}.pdf`, `grp1-gr-{runId}.pdf`, `grp4-gr-{runId}.pdf`, `grp2-gr-{runId}.pdf`
44. Verifikasi baris `tie1-gr-{runId}.pdf` dan `tie2-gr-{runId}.pdf` masing-masing tampil satu kali sesudah baris `grp2-gr-{runId}.pdf`
45. Klik ikon sort pada header kolom `Group` sekali lagi
46. Verifikasi empat baris sesudah dua baris `tie1-gr-{runId}.pdf` dan `tie2-gr-{runId}.pdf` dari atas ke bawah: `grp4-gr-{runId}.pdf`, `grp2-gr-{runId}.pdf`, `grp3-gr-{runId}.pdf`, `grp1-gr-{runId}.pdf`
47. Klik ikon sort pada header kolom `Group` untuk ketiga kalinya

### Sort Uploaded By menurut nama lengkap
48. Ganti isi kotak search dengan `-up-{runId}`, tekan Enter
49. Verifikasi baris `up1-up-{runId}.pdf`, `up2-up-{runId}.pdf`, dan `up3-up-{runId}.pdf` tampil
50. Verifikasi urutan baris default dari atas ke bawah: `up1-up-{runId}.pdf`, `up3-up-{runId}.pdf`, `up2-up-{runId}.pdf`
51. Klik ikon sort pada header kolom `Uploaded By`
52. Verifikasi urutan baris dari atas ke bawah menurut nama lengkap pengunggah `Agus Wibowo {runId}`, `Budi Sanjaya {runId}`, `Budi Santoso {runId}`: `up3-up-{runId}.pdf`, `up2-up-{runId}.pdf`, `up1-up-{runId}.pdf`
53. Klik ikon sort pada header kolom `Uploaded By` sekali lagi
54. Verifikasi urutan baris dari atas ke bawah: `up1-up-{runId}.pdf`, `up2-up-{runId}.pdf`, `up3-up-{runId}.pdf`
55. Klik ikon sort pada header kolom `Uploaded By` untuk ketiga kalinya

### Sort lintas halaman dan nilai sama melintasi halaman
56. Ganti isi kotak search dengan `-pg-{runId}`, tekan Enter
57. Verifikasi baris `vol-12-pg-{runId}.pdf` tampil di halaman 1 dan baris `vol-1-pg-{runId}.pdf` tampil di halaman 2
58. Klik ikon sort pada header kolom `Size`
59. Verifikasi baris `vol-1-pg-{runId}.pdf` berada di urutan pertama halaman 1
60. Klik halaman `2` pada Pagination
61. Verifikasi halaman 2 memuat baris `vol-11-pg-{runId}.pdf` dan `vol-12-pg-{runId}.pdf`
62. Klik halaman `1` pada Pagination
63. Klik ikon sort pada header kolom `Size` sekali lagi
64. Verifikasi baris `vol-12-pg-{runId}.pdf` berada di urutan pertama halaman 1
65. Klik halaman `2` pada Pagination
66. Verifikasi halaman 2 memuat baris `vol-2-pg-{runId}.pdf` lalu `vol-1-pg-{runId}.pdf`
67. Klik ikon sort pada header kolom `Size` untuk ketiga kalinya
68. Klik halaman `1` pada Pagination
69. Klik ikon sort pada header kolom `Group`
70. Verifikasi baris `vol-12-pg-{runId}.pdf` berada di urutan pertama halaman 1 karena semua baris bernilai Group sama
71. Klik halaman `2` pada Pagination
72. Verifikasi halaman 2 memuat baris `vol-2-pg-{runId}.pdf` lalu `vol-1-pg-{runId}.pdf`
73. Klik ikon sort pada header kolom `Group` sekali lagi
74. Klik ikon sort pada header kolom `Group` untuk ketiga kalinya

### Sort A-Z kolom File Format, Source, Reference, Asset, dan Asset ID
75. Ganti isi kotak search dengan `-az-{runId}`, tekan Enter
76. Verifikasi baris `ala-az-{runId}.pdf` dan `bmb-az-{runId}.jpg` tampil
77. Verifikasi urutan baris default dari atas ke bawah: `bmb-az-{runId}.jpg`, `ala-az-{runId}.pdf`
78. Klik ikon sort pada header kolom `File Format`
79. Verifikasi urutan File Format dari atas ke bawah: `JPG`, `PDF`
80. Klik ikon sort pada header kolom `File Format` sekali lagi
81. Verifikasi urutan File Format dari atas ke bawah: `PDF`, `JPG`
82. Klik ikon sort pada header kolom `File Format` untuk ketiga kalinya
83. Klik ikon sort pada header kolom `Source`
84. Verifikasi urutan Source dari atas ke bawah: `Attachment`, `Custom Field Document`
85. Klik ikon sort pada header kolom `Source` sekali lagi
86. Verifikasi urutan Source dari atas ke bawah: `Custom Field Document`, `Attachment`
87. Klik ikon sort pada header kolom `Source` untuk ketiga kalinya
88. Klik ikon sort pada header kolom `Reference`
89. Verifikasi urutan Reference dari atas ke bawah: `General`, `Kartu Urut {runId}`
90. Klik ikon sort pada header kolom `Reference` sekali lagi
91. Verifikasi urutan Reference dari atas ke bawah: `Kartu Urut {runId}`, `General`
92. Klik ikon sort pada header kolom `Reference` untuk ketiga kalinya
93. Klik ikon sort pada header kolom `Asset`
94. Verifikasi urutan baris dari atas ke bawah menurut Asset: `bmb-az-{runId}.jpg` (aset `Aset Urut Alfa {runId}`), `ala-az-{runId}.pdf` (aset `Aset Urut Beta {runId}`)
95. Klik ikon sort pada header kolom `Asset` sekali lagi
96. Verifikasi urutan baris dari atas ke bawah menurut Asset: `ala-az-{runId}.pdf` (aset `Aset Urut Beta {runId}`), `bmb-az-{runId}.jpg` (aset `Aset Urut Alfa {runId}`)
97. Klik ikon sort pada header kolom `Asset` untuk ketiga kalinya
98. Klik ikon sort pada header kolom `Asset ID`
99. Verifikasi Asset ID baris pertama mendahului Asset ID baris kedua menurut urutan alfabetis, dibaca dari tabel
100. Klik ikon sort pada header kolom `Asset ID` sekali lagi
101. Verifikasi Asset ID baris pertama menyusul Asset ID baris kedua menurut urutan alfabetis, dibaca dari tabel
102. Klik ikon sort pada header kolom `Asset ID` untuk ketiga kalinya
103. Klik `(←)` pada kotak Search
