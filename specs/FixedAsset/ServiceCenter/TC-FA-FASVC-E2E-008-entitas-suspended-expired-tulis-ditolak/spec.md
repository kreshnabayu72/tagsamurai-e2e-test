---
id: TC-FA-FASVC-E2E-008-entitas-suspended-expired-tulis-ditolak
title: "Entitas Suspended dan Expired: Data Terbaca, Setiap Aksi Tulis Ditolak"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["EC-FASVC-35", "F-FASVC-01.k5", "§9.4.1#r1", "EB-AKS-7"]
smoke: []
dependsOn: []
trace:
  "EC-FASVC-35": [15, 17, 19, 27, 36, 43, 51, 58, 66, 68, 70, 78, 87, 94, 102, 109]
  "F-FASVC-01.k5": [27, 36, 43, 51, 58, 78, 87, 94, 102, 109]
  "§9.4.1#r1": [27, 36, 43, 51, 58, 78, 87, 94, 102, 109]
  "EB-AKS-7": [15, 17, 19, 27, 30, 31, 36, 39, 43, 46, 51, 54, 58, 61, 66, 68, 70, 78, 81, 82, 87, 90, 94, 97, 102, 105, 109, 112]
anchor: [10]
coverage:
  web: automated
---

# Entitas Suspended dan Expired: Data Terbaca, Setiap Aksi Tulis Ditolak

## Prerequisites
- Aktor: Total Control `Tomi Control {runId}` pada entitas khusus `Entitas Uji Status {runId}`, dan Operator Admin Console yang mengubah status entitas itu. Spec ini memakai entitas khusus yang tidak dipakai spec lain.
- Layar awal: Dashboard Fixed Asset.
- Data:
  - DU-008-1: Entitas `Entitas Uji Status {runId}`, Status `Active`, tidak dipakai spec lain.
  - DU-008-2: Entitas `Entitas Uji Status {runId}` dengan Status `Suspended`, hasil perubahan oleh Operator Admin Console.
  - DU-008-3: Entitas `Entitas Uji Status {runId}` dengan Status `Expired`, hasil perubahan oleh Operator Admin Console.
  - DU-008-4: Aktor `Tomi Control {runId}` dengan Role `Total Control`, ada di entitas `Entitas Uji Status {runId}`.
  - DU-008-5: Service Center `Servis Status Aktif {runId}`, Service type `Routine`, Available to `All groups`, City `Surabaya`, Company email `kontak@statusaktif.co.id`, Status `Active`, ada di entitas `Entitas Uji Status {runId}`. Usage `0`.
  - DU-008-6: Service Center `Servis Status Nonaktif {runId}`, Service type `Routine`, Available to `All groups`, City `Malang`, Company email `kontak@statusnonaktif.co.id`, Status `Inactive`, ada di entitas `Entitas Uji Status {runId}`. Usage `0`.
  - DU-008-7: Service Center `Servis Baseline {runId}`, Service type `Routine`, City `Surabaya`, Company email `kontak@baselinestatus.co.id`, dibuat oleh `Tomi Control {runId}` saat entitas Active.
  - DU-008-8: Service Center `Servis Ditolak Suspended {runId}`, Service type `Routine`, City `Malang`, Company email `kontak@ditolaksuspended.co.id`, dicoba dibuat saat entitas Suspended dan ditolak.
  - DU-008-9: Service Center `Servis Ditolak Expired {runId}`, Service type `Routine`, City `Malang`, Company email `kontak@ditolakexpired.co.id`, dicoba dibuat saat entitas Expired dan ditolak.
- Kondisi:
  - Lisensi addon Maintenance aktif untuk entitas `Entitas Uji Status {runId}`.
  - Akun `Tomi Control {runId}` aktif dan kredensialnya disediakan fase 2.
  - Master Data Count Limit bernilai `1000` dan entitas `Entitas Uji Status {runId}` berisi kurang dari 1.000 Service Center.

## Test Steps

### Entitas Active: Create berhasil sebagai pembanding
1. Masuk sebagai `Tomi Control {runId}`
2. Buka menu `Add-ons` pada sidebar
3. Klik `Service Center`
4. Klik `[+ Service Center]`
5. Isi Name `Servis Baseline {runId}`
6. Centang Service type `Routine`
7. Isi City `Surabaya`
8. Isi Company email `kontak@baselinestatus.co.id`
9. Klik `[Submit]`
10. Verifikasi toast `Success, Servis Baseline {runId} has been added.` tampil

### Entitas Suspended: halaman daftar dan Detail tetap terbaca
11. Operator Admin Console mengubah status entitas `Entitas Uji Status {runId}` menjadi `Suspended`
12. Masuk sebagai `Tomi Control {runId}`
13. Buka menu `Add-ons` pada sidebar
14. Klik `Service Center`
15. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi baris `Servis Status Aktif {runId}` tampil di tabel
18. Klik Name `Servis Status Aktif {runId}`
19. Verifikasi halaman Detail menampilkan nama `Servis Status Aktif {runId}`
20. Klik breadcrumb `Service Center`

### Entitas Suspended: Create ditolak
21. Klik `[+ Service Center]`
22. Isi Name `Servis Ditolak Suspended {runId}`
23. Centang Service type `Routine`
24. Isi City `Malang`
25. Isi Company email `kontak@ditolaksuspended.co.id`
26. Klik `[Submit]`
27. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
28. Muat ulang halaman
29. Ketik Search `{runId}`, tekan Enter
30. Verifikasi baris `Servis Status Aktif {runId}` tampil di tabel
31. Verifikasi baris `Servis Ditolak Suspended {runId}` tidak tampil di tabel

### Entitas Suspended: Edit ditolak
32. Klik `⋯` pada baris `Servis Status Aktif {runId}`
33. Klik `Edit`
34. Ganti isi City dengan `Sidoarjo`
35. Klik `[Save]`
36. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
37. Muat ulang halaman
38. Ketik Search `Servis Status Aktif {runId}`, tekan Enter
39. Verifikasi kolom City pada baris `Servis Status Aktif {runId}` menampilkan `Surabaya`

### Entitas Suspended: Inactivate ditolak
40. Klik `⋯` pada baris `Servis Status Aktif {runId}`
41. Klik `Inactivate`
42. Klik `[Inactivate]`
43. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
44. Muat ulang halaman
45. Ketik Search `Servis Status Aktif {runId}`, tekan Enter
46. Verifikasi kolom Status pada baris `Servis Status Aktif {runId}` menampilkan `Active`

### Entitas Suspended: Activate ditolak
47. Ganti isi kotak search dengan `Servis Status Nonaktif {runId}`, tekan Enter
48. Klik `⋯` pada baris `Servis Status Nonaktif {runId}`
49. Klik `Activate`
50. Klik `[Activate]`
51. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
52. Muat ulang halaman
53. Ketik Search `Servis Status Nonaktif {runId}`, tekan Enter
54. Verifikasi kolom Status pada baris `Servis Status Nonaktif {runId}` menampilkan `Inactive`

### Entitas Suspended: Delete ditolak
55. Klik `⋯` pada baris `Servis Status Nonaktif {runId}`
56. Klik `Delete`
57. Klik `[Delete]`
58. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
59. Muat ulang halaman
60. Ketik Search `Servis Status Nonaktif {runId}`, tekan Enter
61. Verifikasi baris `Servis Status Nonaktif {runId}` tampil di tabel

### Entitas Expired: halaman daftar dan Detail tetap terbaca
62. Operator Admin Console mengubah status entitas `Entitas Uji Status {runId}` menjadi `Expired`
63. Masuk sebagai `Tomi Control {runId}`
64. Buka menu `Add-ons` pada sidebar
65. Klik `Service Center`
66. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
67. Ketik Search `{runId}`, tekan Enter
68. Verifikasi baris `Servis Status Aktif {runId}` tampil di tabel
69. Klik Name `Servis Status Aktif {runId}`
70. Verifikasi halaman Detail menampilkan nama `Servis Status Aktif {runId}`
71. Klik breadcrumb `Service Center`

### Entitas Expired: Create ditolak
72. Klik `[+ Service Center]`
73. Isi Name `Servis Ditolak Expired {runId}`
74. Centang Service type `Routine`
75. Isi City `Malang`
76. Isi Company email `kontak@ditolakexpired.co.id`
77. Klik `[Submit]`
78. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
79. Muat ulang halaman
80. Ketik Search `{runId}`, tekan Enter
81. Verifikasi baris `Servis Status Aktif {runId}` tampil di tabel
82. Verifikasi baris `Servis Ditolak Expired {runId}` tidak tampil di tabel

### Entitas Expired: Edit ditolak
83. Klik `⋯` pada baris `Servis Status Aktif {runId}`
84. Klik `Edit`
85. Ganti isi City dengan `Sidoarjo`
86. Klik `[Save]`
87. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
88. Muat ulang halaman
89. Ketik Search `Servis Status Aktif {runId}`, tekan Enter
90. Verifikasi kolom City pada baris `Servis Status Aktif {runId}` menampilkan `Surabaya`

### Entitas Expired: Inactivate ditolak
91. Klik `⋯` pada baris `Servis Status Aktif {runId}`
92. Klik `Inactivate`
93. Klik `[Inactivate]`
94. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
95. Muat ulang halaman
96. Ketik Search `Servis Status Aktif {runId}`, tekan Enter
97. Verifikasi kolom Status pada baris `Servis Status Aktif {runId}` menampilkan `Active`

### Entitas Expired: Activate ditolak
98. Ganti isi kotak search dengan `Servis Status Nonaktif {runId}`, tekan Enter
99. Klik `⋯` pada baris `Servis Status Nonaktif {runId}`
100. Klik `Activate`
101. Klik `[Activate]`
102. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
103. Muat ulang halaman
104. Ketik Search `Servis Status Nonaktif {runId}`, tekan Enter
105. Verifikasi kolom Status pada baris `Servis Status Nonaktif {runId}` menampilkan `Inactive`

### Entitas Expired: Delete ditolak
106. Klik `⋯` pada baris `Servis Status Nonaktif {runId}`
107. Klik `Delete`
108. Klik `[Delete]`
109. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
110. Muat ulang halaman
111. Ketik Search `Servis Status Nonaktif {runId}`, tekan Enter
112. Verifikasi baris `Servis Status Nonaktif {runId}` tampil di tabel
