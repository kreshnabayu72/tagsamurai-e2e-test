---
id: TC-FA-ASTL-UI-070-dialog-delete-asset-data
title: "Dialog Delete Asset Data"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-17s", "ASTL-LOGIC-17t", "ASTL-LOGIC-17w", "FI-15", "V-04", "V-05", "T-11", "T-25", "D-05", "FLD-41", "§6#r9", "EB-FB-1@delete-asset-data", "EB-FB-2@delete-asset-data", "EB-FRM-1@delete-asset-data", "EB-ERR-1@delete-asset-data", "EB-ERR-2@delete-asset-data"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-17s": [7, 9]
  "ASTL-LOGIC-17t": [16, 18]
  "ASTL-LOGIC-17w": [3, 14]
  "FI-15": [7, 9, 11, 18]
  "V-04": [7, 9, 11]
  "V-05": [53, 54, 59, 60, 65, 66, 71, 72, 77, 78, 83, 84, 89, 90, 99, 100, 104, 105]
  "T-11": [27, 43]
  "T-25": 39
  "D-05": [2, 3, 4, 5, 6, 13, 14, 15]
  "FLD-41": [5, 7, 9]
  "§6#r9": [39, 48]
  "EB-FB-1@delete-asset-data": [27, 39, 43]
  "EB-FB-2@delete-asset-data": [34, 55, 61, 67, 73, 79, 85, 91, 95]
  "EB-FRM-1@delete-asset-data": [22, 23, 25, 28]
  "EB-ERR-1@delete-asset-data": [39, 40, 41, 44, 48, 49]
  "EB-ERR-2@delete-asset-data": [25, 27, 31, 33, 35]
anchor: [94]
coverage:
  web: automated
---
# Dialog Delete Asset Data

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Delete Asset Data
- Data:
  - DU-070-1: Aset `Genset 20kVA - 1`, Asset ID `AST-0060`, Group `Cabang Medan`, Status `Disposed`.
  - DU-070-2: Aset `Genset 20kVA - 2`, Asset ID `AST-0061`, Group `Cabang Medan`, Status `Disposed`.
  - DU-070-3: Aset Unmanaged `Genset 20kVA - 3`, Asset ID `AST-0062`, Group `Cabang Medan`, Custody `Borrowed`.
- Kondisi:
  - K1: seleksi berisi DU-070-1; hapus berhasil.
  - K2: seleksi berisi DU-070-1 dan DU-070-2; hapus berhasil.
  - K3: seleksi berisi DU-070-1; hapus berhasil setelah respons tertunda.
  - K4: seleksi berisi DU-070-1; hapus pertama gagal karena error server, hapus berikutnya berhasil.
  - K5: seleksi berisi DU-070-1; hapus gagal karena timeout atau jaringan terputus.
  - K6: seleksi berisi DU-070-1; hapus ditolak server karena jejak Posted: aset punya penyusutan atau jurnal Posted.
  - K7: seleksi berisi DU-070-1; hapus ditolak server karena Disposal Executed yang jurnal pelepasannya belum Posted.
  - K8: seleksi berisi DU-070-1; hapus ditolak server karena aset punya record Missing berjalan.
  - K9: seleksi berisi DU-070-1; hapus ditolak server karena aset punya Disposal Report Reported atau DSP aktif.
  - K10: seleksi berisi DU-070-1; hapus ditolak server karena aset terkunci Activity Lock In Audit.
  - K11: seleksi berisi DU-070-1; hapus ditolak server karena aset terkunci Activity Lock Under Maintenance.
  - K12: seleksi berisi DU-070-3; hapus ditolak server karena aset tidak memenuhi syarat Delete Asset Data.
  - K13: seleksi Bulk berisi DU-070-1 dan DU-070-2; hapus ditolak server karena DU-070-1 berjejak Posted dan DU-070-2 punya Disposal Report Reported atau DSP aktif.
  - K14: seleksi Bulk berisi DU-070-1 dan DU-070-3; hapus ditolak server karena DU-070-1 berjejak Posted dan DU-070-3 tidak memenuhi syarat Delete Asset Data.

## Test Steps

### Tampilan untuk satu aset dan Delete menunggu konfirmasi
1. Tampilkan Dialog Delete Asset Data dengan kondisi K1
2. Verifikasi dialog berjudul `Delete Asset Data` tampil dengan bullet `Genset 20kVA - 1`
3. Verifikasi teks `All attachments of the selected asset in File Manager will also be deleted.` tampil
4. Verifikasi teks `Are you sure you want to delete it? This action cannot be undone.` tampil
5. Verifikasi checkbox konfirmasi `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.` tampil dan tidak tercentang
6. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil
7. Verifikasi `[Delete]` Disabled
8. Centang checkbox konfirmasi
9. Verifikasi `[Delete]` aktif
10. Hapus centang checkbox konfirmasi
11. Verifikasi `[Delete]` Disabled kembali

### Tampilan untuk dua aset dengan satu konfirmasi
12. Tampilkan Dialog Delete Asset Data dengan kondisi K2
13. Verifikasi bullet `Genset 20kVA - 1` dan `Genset 20kVA - 2` tampil
14. Verifikasi teks `All attachments of the selected assets in File Manager will also be deleted.` tampil
15. Verifikasi teks `Are you sure you want to delete them? This action cannot be undone.` tampil
16. Verifikasi hanya satu checkbox konfirmasi `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.` untuk kedua aset
17. Centang checkbox konfirmasi
18. Verifikasi `[Delete]` aktif untuk kedua aset terpilih

### Delete menghapus satu kali dengan satu toast
19. Tampilkan Dialog Delete Asset Data dengan kondisi K3
20. Centang checkbox konfirmasi
21. Klik `[Delete]`
22. Verifikasi `[Delete]` tidak bisa diklik selama permintaan berjalan
23. Verifikasi checkbox konfirmasi, tombol `[Cancel]`, dan tombol tutup `✕` Disabled selama permintaan berjalan
24. Klik ganda `[Delete]` saat permintaan masih berjalan
25. Verifikasi permintaan hapus hanya terkirim satu kali
26. Respons hapus berhasil diterima
27. Verifikasi toast `Success, asset data has been deleted.` tampil
28. Verifikasi dialog `Delete Asset Data` tertutup

### Esc dan fokus dialog
29. Tampilkan Dialog Delete Asset Data dengan kondisi K1
30. Tekan Tab berulang sampai fokus berpindah melewati tombol `[Delete]`
31. Verifikasi fokus tetap berada di dalam dialog
32. Tekan Esc
33. Verifikasi dialog `Delete Asset Data` tertutup tanpa permintaan hapus terkirim
34. Verifikasi tidak ada toast yang tampil
35. Verifikasi fokus kembali ke pemicu dialog

### Kegagalan server mempertahankan dialog
36. Tampilkan Dialog Delete Asset Data dengan kondisi K4
37. Centang checkbox konfirmasi
38. Klik `[Delete]`
39. Verifikasi toast `Error, failed to delete asset data.` tampil
40. Verifikasi dialog `Delete Asset Data` tetap terbuka dengan checkbox konfirmasi masih tercentang dan `[Delete]` aktif kembali
41. Verifikasi toast `Error, failed to delete asset data.` tidak memiliki tombol aksi seperti `[Try Again]`
42. Klik `[Delete]`
43. Verifikasi toast `Success, asset data has been deleted.` tampil
44. Verifikasi dialog `Delete Asset Data` tertutup dan hapus berhasil tepat satu kali

### Timeout mempertahankan dialog
45. Tampilkan Dialog Delete Asset Data dengan kondisi K5
46. Centang checkbox konfirmasi
47. Klik `[Delete]`
48. Verifikasi toast `Connection problem. Please try again.` tampil
49. Verifikasi dialog `Delete Asset Data` tetap terbuka dengan checkbox konfirmasi masih tercentang dan `[Delete]` aktif kembali

### Penolakan server: jejak Posted: aset punya penyusutan atau jurnal Posted
50. Tampilkan Dialog Delete Asset Data dengan kondisi K6
51. Centang checkbox konfirmasi
52. Klik `[Delete]`
53. Verifikasi alert inline `Asset has posted depreciation or journal entries. Use Disposal.` tampil di dalam dialog
54. Verifikasi dialog `Delete Asset Data` tetap terbuka
55. Verifikasi tidak ada toast yang tampil

### Penolakan server: Disposal Executed yang jurnal pelepasannya belum Posted
56. Tampilkan Dialog Delete Asset Data dengan kondisi K7
57. Centang checkbox konfirmasi
58. Klik `[Delete]`
59. Verifikasi alert inline `Asset has a disposal that is not posted yet.` tampil di dalam dialog
60. Verifikasi dialog `Delete Asset Data` tetap terbuka
61. Verifikasi tidak ada toast yang tampil

### Penolakan server: aset punya record Missing berjalan
62. Tampilkan Dialog Delete Asset Data dengan kondisi K8
63. Centang checkbox konfirmasi
64. Klik `[Delete]`
65. Verifikasi alert inline `Asset has an ongoing missing record. Complete or close the record first.` tampil di dalam dialog
66. Verifikasi dialog `Delete Asset Data` tetap terbuka
67. Verifikasi tidak ada toast yang tampil

### Penolakan server: aset punya Disposal Report Reported atau DSP aktif
68. Tampilkan Dialog Delete Asset Data dengan kondisi K9
69. Centang checkbox konfirmasi
70. Klik `[Delete]`
71. Verifikasi alert inline `Asset has an open disposal report or request. Cancel or complete it first.` tampil di dalam dialog
72. Verifikasi dialog `Delete Asset Data` tetap terbuka
73. Verifikasi tidak ada toast yang tampil

### Penolakan server: aset terkunci Activity Lock In Audit
74. Tampilkan Dialog Delete Asset Data dengan kondisi K10
75. Centang checkbox konfirmasi
76. Klik `[Delete]`
77. Verifikasi alert inline `Asset is in audit. Complete or cancel the audit to continue.` tampil di dalam dialog
78. Verifikasi dialog `Delete Asset Data` tetap terbuka
79. Verifikasi tidak ada toast yang tampil

### Penolakan server: aset terkunci Activity Lock Under Maintenance
80. Tampilkan Dialog Delete Asset Data dengan kondisi K11
81. Centang checkbox konfirmasi
82. Klik `[Delete]`
83. Verifikasi alert inline `Asset is under maintenance. Complete the maintenance task to continue.` tampil di dalam dialog
84. Verifikasi dialog `Delete Asset Data` tetap terbuka
85. Verifikasi tidak ada toast yang tampil

### Penolakan server: aset tidak memenuhi syarat Delete Asset Data
86. Tampilkan Dialog Delete Asset Data dengan kondisi K12
87. Centang checkbox konfirmasi
88. Klik `[Delete]`
89. Verifikasi alert inline `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil di dalam dialog
90. Verifikasi dialog `Delete Asset Data` tetap terbuka
91. Verifikasi tidak ada toast yang tampil

### Cancel menutup dialog tanpa toast
92. Tampilkan Dialog Delete Asset Data dengan kondisi K1
93. Klik `[Cancel]`
94. Verifikasi dialog `Delete Asset Data` tertutup
95. Verifikasi tidak ada toast yang tampil dan tidak ada permintaan hapus yang terkirim

### Beberapa penyebab pada Bulk: hanya penyebab yang didahulukan tampil
96. Tampilkan Dialog Delete Asset Data dengan kondisi K13
97. Centang checkbox konfirmasi
98. Klik `[Delete]`
99. Verifikasi alert inline `Asset has posted depreciation or journal entries. Use Disposal.` tampil tepat satu kali di dalam dialog
100. Verifikasi alert inline `Asset has an open disposal report or request. Cancel or complete it first.` tidak tampil
101. Tampilkan Dialog Delete Asset Data dengan kondisi K14
102. Centang checkbox konfirmasi
103. Klik `[Delete]`
104. Verifikasi alert inline `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil tepat satu kali di dalam dialog
105. Verifikasi alert inline `Asset has posted depreciation or journal entries. Use Disposal.` tidak tampil
