---
id: TC-FA-FAFM-E2E-057-format-tanggal-dep-general-settings
title: "Format tanggal dan waktu General Settings tercermin di kolom tanggal"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-XM-1]
smoke: []
dependsOn: ["General Settings: Date Format dan Time Format"]
trace:
  EB-XM-1: [3, 11, 18, 25, 32, 39, 47, 54, 61, 83, 86, 90, 104]
anchor: []
coverage:
  web: automated
---

# Format tanggal dan waktu General Settings tercermin di kolom tanggal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-057-1: Pengaturan General Settings awal: Date Format `dd/MM/yy` dan Time Format `24 jam`.
  - DU-057-2: Date Format pengganti `M/d/yy`.
  - DU-057-3: Date Format pengganti `dd MMM yy`.
  - DU-057-4: Date Format pengganti `DDD, MMM dd, yy`.
  - DU-057-5: Date Format pengganti `DDD, MMM dd, yyyy`.
  - DU-057-6: Time Format pengganti `12 jam`.
  - DU-057-7: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki file DU-057-8.
  - DU-057-8: File `format-{runId}.jpg`, Category `Asset Photo`, aktif, dengan Upload Date yang dicatat server saat file disiapkan.
  - DU-057-9: Time Zone pengganti satu jam lebih maju dari Time Zone awal.
  - DU-057-10: File `format-hapus-{runId}.jpg`, Category `Asset Photo`, milik aset DU-057-7, aktif, di-Delete di dalam spec sehingga muncul di Recycle Bin dan Changelog File Manager.
  - DU-057-11: Aset `Camera Canon EOS R6 {runId}`, Status `Unmanaged`, Group `Head Office`, ada di entitas aktor, tampil di tab `Disposed & Unmanaged Assets` dengan Register Date yang dicatat server.

## Test Steps

### Format awal
1. Klik tab `Asset Photo`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi Upload Date baris file `format-{runId}.jpg` tampil dengan tanggal berpola `dd/MM/yy` dan jam berpola `HH:mm`
4. Catat tanggal dan jam Upload Date baris file `format-{runId}.jpg`

### Date Format M/d/yy
5. Buka General Settings
6. Ubah Date Format menjadi `M/d/yy`
7. Simpan perubahan General Settings
8. Buka Fixed Asset > Settings > File Manager
9. Klik tab `Asset Photo`
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi Upload Date baris file `format-{runId}.jpg` menampilkan tanggal yang dicatat pada langkah 4 dengan pola `M/d/yy` dan jam yang dicatat pada langkah 4

### Date Format dd MMM yy
12. Buka General Settings
13. Ubah Date Format menjadi `dd MMM yy`
14. Simpan perubahan General Settings
15. Buka Fixed Asset > Settings > File Manager
16. Klik tab `Asset Photo`
17. Ketik Search `{runId}`, tekan Enter
18. Verifikasi Upload Date baris file `format-{runId}.jpg` menampilkan tanggal yang dicatat pada langkah 4 dengan pola `dd MMM yy` dan jam yang dicatat pada langkah 4

### Date Format DDD, MMM dd, yy
19. Buka General Settings
20. Ubah Date Format menjadi `DDD, MMM dd, yy`
21. Simpan perubahan General Settings
22. Buka Fixed Asset > Settings > File Manager
23. Klik tab `Asset Photo`
24. Ketik Search `{runId}`, tekan Enter
25. Verifikasi Upload Date baris file `format-{runId}.jpg` menampilkan tanggal yang dicatat pada langkah 4 dengan pola `DDD, MMM dd, yy` dan jam yang dicatat pada langkah 4

### Date Format DDD, MMM dd, yyyy
26. Buka General Settings
27. Ubah Date Format menjadi `DDD, MMM dd, yyyy`
28. Simpan perubahan General Settings
29. Buka Fixed Asset > Settings > File Manager
30. Klik tab `Asset Photo`
31. Ketik Search `{runId}`, tekan Enter
32. Verifikasi Upload Date baris file `format-{runId}.jpg` menampilkan tanggal yang dicatat pada langkah 4 dengan pola `DDD, MMM dd, yyyy` dan jam yang dicatat pada langkah 4

### Time Format 12 jam
33. Buka General Settings
34. Ubah Time Format menjadi `12 jam`
35. Simpan perubahan General Settings
36. Buka Fixed Asset > Settings > File Manager
37. Klik tab `Asset Photo`
38. Ketik Search `{runId}`, tekan Enter
39. Verifikasi Upload Date baris file `format-{runId}.jpg` menampilkan tanggal yang dicatat pada langkah 4 dengan pola `DDD, MMM dd, yyyy` dan jam yang setara dengan jam yang dicatat pada langkah 4 dalam format 12 jam

### Format dikembalikan ke nilai awal
40. Buka General Settings
41. Ubah Date Format menjadi `dd/MM/yy`
42. Ubah Time Format menjadi `24 jam`
43. Simpan perubahan General Settings
44. Buka Fixed Asset > Settings > File Manager
45. Klik tab `Asset Photo`
46. Ketik Search `{runId}`, tekan Enter
47. Verifikasi Upload Date baris file `format-{runId}.jpg` menampilkan tanggal dan jam yang sama dengan nilai yang dicatat pada langkah 4

### Time Zone mengubah jam Upload Date
48. Buka General Settings
49. Ubah Time Zone menjadi zona waktu yang satu jam lebih maju dari Time Zone awal
50. Simpan perubahan General Settings
51. Buka Fixed Asset > Settings > File Manager
52. Klik tab `Asset Photo`
53. Ketik Search `{runId}`, tekan Enter
54. Verifikasi jam Upload Date baris file `format-{runId}.jpg` lebih maju satu jam dari jam yang dicatat pada langkah 4
55. Buka General Settings
56. Kembalikan Time Zone ke zona waktu awal
57. Simpan perubahan General Settings
58. Buka Fixed Asset > Settings > File Manager
59. Klik tab `Asset Photo`
60. Ketik Search `{runId}`, tekan Enter
61. Verifikasi jam Upload Date baris file `format-{runId}.jpg` sama dengan jam yang dicatat pada langkah 4

### Tanggal pada Recycle Bin, Changelog, dan tab Asset Data mengikuti Date Format
62. Klik tab `Asset Photo`
63. Ketik Search `format-hapus-{runId}.jpg`, tekan Enter
64. Klik aksi Delete pada baris file `format-hapus-{runId}.jpg`
65. Klik `[Delete]` pada dialog Delete File
66. Klik tombol Recycle Bin pada header kartu Storage Usage
67. Ketik Search `format-hapus-{runId}.jpg`, tekan Enter
68. Catat tanggal dan jam Deleted Date baris file `format-hapus-{runId}.jpg`
69. Tutup modal Recycle Bin
70. Klik tombol Changelog pada header kartu Storage Usage
71. Ketik Search `format-hapus-{runId}.jpg`, tekan Enter
72. Catat tanggal dan jam Date entri dengan Action `Delete` untuk File Name `format-hapus-{runId}.jpg`
73. Tutup modal Changelog
74. Klik tab `Disposed & Unmanaged Assets`
75. Ketik Search `Camera Canon EOS R6 {runId}`, tekan Enter
76. Catat tanggal dan jam Register Date baris aset `Camera Canon EOS R6 {runId}`
77. Buka General Settings
78. Ubah Date Format menjadi `dd MMM yy`
79. Simpan perubahan General Settings
80. Buka Fixed Asset > Settings > File Manager
81. Klik tab `Disposed & Unmanaged Assets`
82. Ketik Search `Camera Canon EOS R6 {runId}`, tekan Enter
83. Verifikasi Register Date baris aset `Camera Canon EOS R6 {runId}` menampilkan tanggal yang dicatat pada langkah 76 dengan pola `dd MMM yy` dan jam yang dicatat pada langkah 76
84. Klik tombol Recycle Bin pada header kartu Storage Usage
85. Ketik Search `format-hapus-{runId}.jpg`, tekan Enter
86. Verifikasi Deleted Date baris file `format-hapus-{runId}.jpg` menampilkan tanggal yang dicatat pada langkah 68 dengan pola `dd MMM yy` dan jam yang dicatat pada langkah 68
87. Tutup modal Recycle Bin
88. Klik tombol Changelog pada header kartu Storage Usage
89. Ketik Search `format-hapus-{runId}.jpg`, tekan Enter
90. Verifikasi Date entri dengan Action `Delete` untuk File Name `format-hapus-{runId}.jpg` menampilkan tanggal yang dicatat pada langkah 72 dengan pola `dd MMM yy` dan jam yang dicatat pada langkah 72
91. Tutup modal Changelog
92. Buka General Settings
93. Ubah Date Format menjadi `dd/MM/yy`
94. Simpan perubahan General Settings

### Tanggal pada berkas export tab Files mengikuti Date Format dan Time Format
95. Buka General Settings
96. Ubah Date Format menjadi `dd MMM yy`
97. Ubah Time Format menjadi `12 jam`
98. Simpan perubahan General Settings
99. Buka Fixed Asset > Settings > File Manager
100. Klik tab `Asset Photo`
101. Ketik Search `format-{runId}.jpg`, tekan Enter
102. Klik ikon Download
103. Klik `Download as CSV`
104. Verifikasi sel Upload Date baris `format-{runId}.jpg` pada berkas hasil export menampilkan tanggal yang dicatat pada langkah 4 dengan pola `dd MMM yy` dan jam yang setara dengan jam yang dicatat pada langkah 4 dalam format 12 jam
105. Buka General Settings
106. Ubah Date Format menjadi `dd/MM/yy`
107. Ubah Time Format menjadi `24 jam`
108. Simpan perubahan General Settings
