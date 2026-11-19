---
id: TC-FA-ASTL-E2E-037-changelog-asset-dep-asset-detail
title: "Changelog Asset dan modal Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-15x", "ASTL-LOGIC-15y", "ASTL-LOGIC-15z", "§4.1i#b11", "§5#r7", "§8#r1", "§8#r2", "§8#r3", "§8#r4", "§8#r5", "§8#r6", "§8#b2", "EB-LOG-1", "EB-LOG-2"]
smoke: []
dependsOn: ["Asset Detail: modal Changelog Asset"]
trace:
  "ASTL-LOGIC-15x": 58
  "ASTL-LOGIC-15y": 62
  "ASTL-LOGIC-15z": 71
  "§4.1i#b11": [16, 121]
  "§5#r7": 2
  "§8#r1": 16
  "§8#r2": 16
  "§8#r3": [14, 41, 111]
  "§8#r4": [14, 32, 41]
  "§8#r5": [32, 50, 82, 85, 95]
  "§8#r6": [62, 114, 115]
  "§8#b2": 58
  "EB-LOG-1": [14, 15]
  "EB-LOG-2": 23
anchor: []
coverage:
  web: automated
---

# Changelog Asset dan modal Changelog

## Prerequisites
- Aktor: Hendra Saputra (akun uji ber-{runId}), Total Control dengan cakupan seluruh client; langkah akhir memakai `Dewi Anggraini {runId}`, pemegang role Manage asset & TAG (Read) dengan cakupan Group `IT {runId}` beserta descendant, tanpa hak Manage purchase
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-037-1: aset `Server Rack {runId} - 1`, Group `IT {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `Rp 52.000.000,00` dari `52000000`, Purchase Complete.
  - DU-037-4: aset `Tablet Inventaris {runId} - 1`, Group `Cabang Medan {runId}`, Unmanaged; Available license group itu `0`.
  - DU-037-5: aset `Printer Laser {runId} - 1`, Group `Cabang Medan {runId}`, managed.
  - DU-037-6: aset `Scanner Gudang {runId} - 1`, Group `Cabang Surabaya {runId}`, Unmanaged; Available license group itu `0`.
  - DU-037-7: aset `Kamera Mirrorless {runId} - 1`, Group `Cabang Surabaya {runId}`, managed.
  - DU-037-8: aset `Laptop Pro 16 {runId} - 1`, Group `IT {runId}`.
  - DU-037-9: aset `Proyektor X2 {runId} - 1`, Group `IT {runId}`.
  - DU-037-10: label manual `Aset Kantor {runId}` ada di katalog label.
  - DU-037-12: aset `Monitor Gudang A {runId} - 1`, Group `Cabang Makassar {runId}`, Unmanaged; Available license group itu `0`.
  - DU-037-13: aset `Monitor Gudang B {runId} - 1`, Group `Cabang Makassar {runId}`, Unmanaged.
  - DU-037-14: aset `Rak Server A {runId} - 1`, Group `Cabang Makassar {runId}`, managed.
  - DU-037-15: aset `Rak Server B {runId} - 1`, Group `Cabang Makassar {runId}`, managed.
  - DU-037-16: nilai Edit Purchase pada `Server Rack {runId} - 1`: Reference Price Currency `USD` jumlah `3500`, Document No. `DOC-{runId}`, Warranty `Service warranty` sampai `T0 + 365 hari`, Additional costs `Ongkos kirim` sebesar `250000`.
  - DU-037-17: nilai Bulk Edit Purchase dua field pada `Laptop Pro 16 {runId} - 1` dan `Proyektor X2 {runId} - 1`: Purchase Date `T0 − 20 hari` dan Purchase Cost `13000000`.
  - DU-037-18: User, Name `Dewi Anggraini {runId}`, Role `Manage asset & TAG` (Read), Cakupan `Group IT {runId} beserta descendant`.

## Test Steps

### Ikon Changelog membuka modal Changelog
1. Klik ikon `Changelog` pada toolbar
2. Verifikasi modal Changelog Asset tampil
3. Tutup modal Changelog

### Edit Purchase dua field menghasilkan dua entri
4. Ketik Search `Server Rack {runId}`, tekan Enter
5. Klik ikon `Changelog` pada toolbar
6. Catat entri teratas modal Changelog untuk `Server Rack {runId} - 1`
7. Tutup modal Changelog
8. Buka menu `⋯` baris `Server Rack {runId} - 1`
9. Klik `Edit Purchase`
10. Ubah Purchase Date menjadi `T0 − 10 hari`
11. Isi Purchase Cost `55000000`
12. Klik `[Save]`
13. Klik ikon `Changelog` pada toolbar
14. Verifikasi modal Changelog memuat dua entri baru untuk `Server Rack {runId} - 1` di atas entri yang dicatat, satu untuk field `Purchase Date` dan satu untuk field `Purchase Cost` dengan nilai baru `Rp 55.000.000,00`
15. Verifikasi modal Changelog tidak memuat entri baru untuk field `Reference Price` maupun `Warranty` pada `Server Rack {runId} - 1`, karena keduanya tidak diubah
16. Verifikasi entri-entri tersebut dicatat satu per field yang berubah dengan entity `Asset` dan tampil bagi Hendra Saputra sebagai pemegang hak kelompok Purchasing
17. Tutup modal Changelog

### Edit kedua tidak mengubah entri pertama
18. Buka menu `⋯` baris `Server Rack {runId} - 1`
19. Klik `Edit Purchase`
20. Isi Purchase Cost `58000000`
21. Klik `[Save]`
22. Klik ikon `Changelog` pada toolbar
23. Verifikasi entri Purchase Cost pertama tetap menampilkan nilai lama `Rp 52.000.000,00` dan nilai baru `Rp 55.000.000,00`, sedangkan entri Purchase Cost kedua menampilkan `Rp 55.000.000,00` menjadi `Rp 58.000.000,00`
24. Tutup modal Changelog

### Add Label dan Remove Label massal satu entri per aset
25. Ketik Search `{runId}`, tekan Enter
26. Centang baris `Laptop Pro 16 {runId} - 1`
27. Centang baris `Proyektor X2 {runId} - 1`
28. Klik Bulk Action `Add Label`
29. Pilih label `Aset Kantor {runId}`
30. Klik `[Apply]`
31. Klik ikon `Changelog` pada toolbar
32. Verifikasi modal Changelog memuat satu entri baru Add Label untuk `Laptop Pro 16 {runId} - 1` dan satu entri baru Add Label untuk `Proyektor X2 {runId} - 1`, tanpa entri tambahan per label
33. Tutup modal Changelog
34. Klik `×` pada bar Bulk untuk membatalkan seleksi
35. Centang baris `Laptop Pro 16 {runId} - 1`
36. Centang baris `Proyektor X2 {runId} - 1`
37. Klik Bulk Action `Remove Label`
38. Pilih label `Aset Kantor {runId}`
39. Klik `[Apply]`
40. Klik ikon `Changelog` pada toolbar
41. Verifikasi modal Changelog memuat entri baru Remove Label untuk field `Label` pada `Laptop Pro 16 {runId} - 1` dan pada `Proyektor X2 {runId} - 1`
42. Tutup modal Changelog

### Edit Purchase massal satu entri per field per aset
43. Klik `×` pada bar Bulk untuk membatalkan seleksi
44. Centang baris `Laptop Pro 16 {runId} - 1`
45. Centang baris `Proyektor X2 {runId} - 1`
46. Klik Bulk Action `Edit Purchase`
47. Isi Purchase Cost (per asset) `12000000`
48. Klik `[Save]`
49. Klik ikon `Changelog` pada toolbar
50. Verifikasi modal Changelog memuat satu entri baru field `Purchase Cost` dengan nilai baru `Rp 12.000.000,00` untuk `Laptop Pro 16 {runId} - 1` dan satu untuk `Proyektor X2 {runId} - 1`
51. Tutup modal Changelog

### Manage dengan Switch tercatat per aset
52. Ketik Search `Tablet Inventaris {runId}`, tekan Enter
53. Buka menu `⋯` baris `Tablet Inventaris {runId} - 1`
54. Klik `Manage`
55. Centang baris `Printer Laser {runId} - 1` pada dialog `Switch Manage Asset`
56. Klik `[Switch]`
57. Klik ikon `Changelog` pada toolbar
58. Verifikasi modal Changelog memuat entri field `License` `Unmanaged` ke `Pending Activation` untuk `Tablet Inventaris {runId} - 1` dan entri field `License` `Managed` ke `Unmanaged` untuk `Printer Laser {runId} - 1`, masing-masing satu entri
59. Tutup modal Changelog

### Aktivasi berhasil ditulis oleh System
60. Jeda transisi Manage untuk `Tablet Inventaris {runId} - 1` berakhir dan aktivasi berhasil
61. Klik ikon `Changelog` pada toolbar
62. Verifikasi modal Changelog memuat entri field `License` `Pending Activation` ke `Managed` untuk `Tablet Inventaris {runId} - 1` dengan Modified By `System`
63. Tutup modal Changelog

### Aktivasi gagal ditulis oleh System
64. Ketik Search `Scanner Gudang {runId}`, tekan Enter
65. Buka menu `⋯` baris `Scanner Gudang {runId} - 1`
66. Klik `Manage`
67. Centang baris `Kamera Mirrorless {runId} - 1` pada dialog `Switch Manage Asset`
68. Klik `[Switch]`
69. Jeda transisi Manage untuk `Scanner Gudang {runId} - 1` berakhir dan aktivasi gagal
70. Klik ikon `Changelog` pada toolbar
71. Verifikasi modal Changelog memuat entri field `License` `Pending Activation` ke `Unmanaged` untuk `Scanner Gudang {runId} - 1` dan entri `Unmanaged` ke `Managed` untuk `Kamera Mirrorless {runId} - 1`, keduanya dengan Modified By `System`
72. Tutup modal Changelog

### Manage massal satu entri per aset
73. Ketik Search `{runId}`, tekan Enter
74. Klik `×` pada bar Bulk untuk membatalkan seleksi
75. Centang baris `Monitor Gudang A {runId} - 1`
76. Centang baris `Monitor Gudang B {runId} - 1`
77. Klik Bulk Action `Manage`
78. Centang baris `Rak Server A {runId} - 1` pada dialog `Switch Manage Asset`
79. Centang baris `Rak Server B {runId} - 1` pada dialog `Switch Manage Asset`
80. Klik `[Switch]`
81. Klik ikon `Changelog` pada toolbar
82. Verifikasi modal Changelog memuat satu entri baru field `License` `Unmanaged` ke `Pending Activation` untuk `Monitor Gudang A {runId} - 1` dan satu untuk `Monitor Gudang B {runId} - 1`
83. Tutup modal Changelog

### Bulk Manage dengan Switch mencatat aset yang ditukar
84. Klik ikon `Changelog` pada toolbar
85. Verifikasi modal Changelog memuat satu entri baru field `License` `Managed` ke `Unmanaged` untuk `Rak Server A {runId} - 1` dan satu untuk `Rak Server B {runId} - 1`
86. Tutup modal Changelog

### Bulk Edit Purchase dua field satu entri per field per aset
87. Klik `×` pada bar Bulk untuk membatalkan seleksi
88. Centang baris `Laptop Pro 16 {runId} - 1`
89. Centang baris `Proyektor X2 {runId} - 1`
90. Klik Bulk Action `Edit Purchase`
91. Ubah Purchase Date menjadi `T0 − 20 hari`
92. Isi Purchase Cost (per asset) `13000000`
93. Klik `[Save]`
94. Klik ikon `Changelog` pada toolbar
95. Verifikasi modal Changelog memuat dua entri baru untuk `Laptop Pro 16 {runId} - 1`, satu field `Purchase Date` dan satu field `Purchase Cost` dengan nilai baru `Rp 13.000.000,00`, serta dua entri baru dengan field yang sama untuk `Proyektor X2 {runId} - 1`
96. Tutup modal Changelog

### Edit Purchase Reference Price, Warranty, Additional costs, dan Document No. satu entri per field
97. Ketik Search `Server Rack {runId}`, tekan Enter
98. Buka menu `⋯` baris `Server Rack {runId} - 1`
99. Klik `Edit Purchase`
100. Pilih Currency `USD` pada Reference Price
101. Isi jumlah Reference Price `3500`
102. Isi Document No. `DOC-{runId}`
103. Klik `[+ Add warranty]`
104. Isi Warranty name `Service warranty`
105. Ubah Warranty until menjadi `T0 + 365 hari`
106. Klik `[+ Add additional cost]`
107. Isi Name Additional costs `Ongkos kirim`
108. Isi Amount Additional costs `250000`
109. Klik `[Save]`
110. Klik ikon `Changelog` pada toolbar
111. Verifikasi modal Changelog memuat entri baru untuk `Server Rack {runId} - 1`, satu per field yang berubah: `Reference Price`, `Document No.`, `Warranty`, dan `Additional costs`
112. Tutup modal Changelog

### Aktivasi berhasil tercatat di Activity Log oleh System
113. Buka Activity Log FAMS tab User Action
114. Verifikasi tab User Action memuat entri `License` `Pending Activation` ke `Managed` untuk `Tablet Inventaris {runId} - 1` dengan Modified By `System`
115. Verifikasi System Log aktor tidak memuat entri untuk penyelesaian jeda transisi Manage atas `Tablet Inventaris {runId} - 1` oleh `System`

### Pemegang hak non-Purchasing tidak melihat entri Purchasing
116. Keluar dari akun
117. Masuk sebagai `Dewi Anggraini {runId}`
118. Klik menu `Fixed Asset > Assets` pada sidebar
119. Ketik Search `Server Rack {runId}`, tekan Enter
120. Klik ikon `Changelog` pada toolbar
121. Verifikasi modal Changelog tidak memuat entri field `Purchase Date` maupun `Purchase Cost` untuk `Server Rack {runId} - 1`, karena perubahan kelompok Purchasing hanya terlihat oleh pemegang haknya
122. Tutup modal Changelog
