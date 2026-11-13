---
id: TC-FA-FAREG-E2E-103-kuota-group-dep-license
title: "Kuota Group: pesan Quantity, Remaining Quota nyata, dan blok Activate"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [F-FAREG-05.k1, FAREG-LOGIC-05a, FAREG-LOGIC-05g, FAREG-LOGIC-05i, §9.2#p33, §9.2#p35, §9.2#p37, §9.2#p38, §9.2#p39, §9.4.2#r3, §9.4.2#r9, §9.4.2#r11, EB-CON-4, EB-XM-2@license, FAREG-LOGIC-05n, D-REG-08, V-REG-17]
smoke: [FAREG-LOGIC-05n, D-REG-08, V-REG-17]
dependsOn: ["License: kuota Group"]
trace:
  F-FAREG-05.k1: [15, 30, 50]
  FAREG-LOGIC-05a: [15, 50]
  FAREG-LOGIC-05g: [10, 15]
  FAREG-LOGIC-05i: [10, 20, 23, 27]
  §9.2#p33: 8
  §9.2#p35: 12
  §9.2#p37: 15
  §9.2#p38: [15, 20]
  §9.2#p39: [17, 20]
  §9.4.2#r3: [8, 10, 15, 83, 84, 85, 97]
  §9.4.2#r9: [15, 50]
  §9.4.2#r11: [15, 20]
  EB-CON-4: [30, 36]
  EB-XM-2@license: [40, 46, 56, 62, 67, 90]
  FAREG-LOGIC-05n: [12, 14]
  D-REG-08: [14, 15, 50]
  V-REG-17: 8
anchor: [89]
coverage:
  web: automated
---

# Kuota Group: pesan Quantity, Remaining Quota nyata, dan blok Activate

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Kuota {runId}` dan `Gudang Tanpa Batas {runId}`.
  - Admin License, aktor License yang mengubah kuota Group, hanya sebagai aktor lain yang memicu perubahan.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-103-1: Group `Gudang Kuota {runId}` dengan sisa kuota Group `8`, ada di entitas aktor.
  - DU-103-2: Asset Name `Meja Kuota {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-103-3: Quantity `10` pada Item `Meja Kuota {runId}`, melebihi sisa kuota Group.
  - DU-103-4: Quantity `9` pada Item `Meja Kuota {runId}`, satu di atas sisa kuota Group.
  - DU-103-5: Quantity `8` pada Item `Meja Kuota {runId}`, tepat sama dengan sisa kuota Group.
  - DU-103-6: Quantity `1` pada Item `Meja Kuota {runId}`, saat sisa kuota Group `0`.
  - DU-103-7: Asset Name `Kursi Kuota {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-103-8: Asset Name `Lemari Kuota {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-103-9: Group `Gudang Tanpa Batas {runId}` tanpa batas kuota Group, ada di entitas aktor.
  - DU-103-10: Quantity `5` pada Item `Meja Kuota {runId}`, saat sisa kuota Group `4`, melebihi sisa.
  - DU-103-11: Tiga Item `Meja Kuota {runId}` Quantity `2`, `Kursi Kuota {runId}` Quantity `1`, dan `Lemari Kuota {runId}` Quantity `1`, saat sisa kuota Group `2`: total kumulatif `2`, `3`, dan `4`.
  - DU-103-12: Quantity `3` pada Item `Meja Kuota {runId}`, saat sisa kuota Group `2`, melebihi sisa.
- Kondisi:
  - approval registrasi pada Group `Gudang Kuota {runId}` bernilai OFF.
  - sisa kuota tenant lebih besar dari `8`, sehingga sisa terkecil adalah sisa kuota Group.
  - sisa kuota Group `Gudang Kuota {runId}` diubah oleh Admin License di langkah yang menyebutnya.

## Test Steps

### Quantity melebihi sisa kuota Group langsung diberi pesan
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Kuota {runId}`
3. Klik `[+ Asset Name]`
4. Pilih Asset Name `Meja Kuota {runId}`
5. Pilih Brand `Ergotec`
6. Pilih Model `No Model`
7. Isi Quantity `10`
8. Verifikasi error pada Quantity `Only 8 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`

### Save draft tetap berjalan dan Activate ditolak seluruhnya
9. Klik `[Save draft]`
10. Verifikasi toast `Success, draft has been saved.`
11. Klik `[Submit]`
12. Verifikasi dialog konfirmasi tampil lebih dulu dengan `Are you sure you want to activate it?`
13. Klik `[Activate]`
14. Verifikasi judul dialog `Cannot Activate` dan tombol `[OK]` tampil
15. Verifikasi dialog memuat `Group quota exceeded. Available slots: 8. Please contact administrator to increase quota.`
16. Klik `[OK]`
17. Verifikasi `Remaining Quota: 8` tetap tampil di samping field Group

### Draft tetap dapat dibaca dan diekspor saat kuota tidak cukup
18. Klik `[Cancel]`
19. Ketik Search `Gudang Kuota {runId}`, tekan Enter
20. Verifikasi baris batch `Gudang Kuota {runId}` tetap di sub tab Draft dengan Total Asset `10`
21. Klik `[Download]`
22. Pilih `Download as CSV`
23. Verifikasi berkas `Registration-Drafts` terunduh

### Aset ke-N diterima dan ke-N+1 ditolak
24. Klik row action `Edit` pada baris batch `Gudang Kuota {runId}`
25. Ganti Quantity menjadi `9`
26. Klik `[Save draft]`
27. Verifikasi toast `Success, draft has been saved.`
28. Klik `[Submit]`
29. Klik `[Activate]`
30. Verifikasi dialog memuat `Group quota exceeded. Available slots: 8. Please contact administrator to increase quota.`
31. Klik `[OK]`
32. Ganti Quantity menjadi `8`
33. Klik `[Save draft]`
34. Klik `[Submit]`
35. Klik `[Activate]`
36. Verifikasi toast `Success, asset has been activated.`

### Sisa kuota Group habis tercermin di form Register Asset
37. Buka Fixed Asset > Assets > Registration > Draft
38. Klik `[+ Register Asset]`
39. Pilih Group `Gudang Kuota {runId}`
40. Verifikasi `Remaining Quota: 0` tampil di samping field Group
41. Klik `[+ Asset Name]`
42. Pilih Asset Name `Meja Kuota {runId}`
43. Pilih Brand `Ergotec`
44. Pilih Model `No Model`
45. Isi Quantity `1`
46. Verifikasi error pada Quantity `No more assets can be added to Gudang Kuota {runId}.`

### Activate ditolak saat sisa kuota Group habis
47. Klik `[Save draft]`
48. Klik `[Submit]`
49. Klik `[Activate]`
50. Verifikasi dialog memuat `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
51. Klik `[OK]`
52. Klik `[Cancel]`

### Kuota Group dinaikkan di License tercermin pada Remaining Quota dan pesan Quantity
53. Admin License menaikkan kuota Group `Gudang Kuota {runId}` sehingga sisa kuota Group menjadi `4`
54. Klik `[+ Register Asset]`
55. Pilih Group `Gudang Kuota {runId}`
56. Verifikasi `Remaining Quota: 4` tampil di samping field Group
57. Klik `[+ Asset Name]`
58. Pilih Asset Name `Meja Kuota {runId}`
59. Pilih Brand `Ergotec`
60. Pilih Model `No Model`
61. Isi Quantity `5`
62. Verifikasi error pada Quantity `Only 4 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`
63. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Kuota Group diturunkan di License dan error ditandai pada Item yang melampaui sisa
64. Admin License menurunkan kuota Group `Gudang Kuota {runId}` sehingga sisa kuota Group menjadi `2`
65. Klik `[+ Register Asset]`
66. Pilih Group `Gudang Kuota {runId}`
67. Verifikasi `Remaining Quota: 2` tampil di samping field Group
68. Klik `[+ Asset Name]`
69. Pilih Asset Name `Meja Kuota {runId}`
70. Pilih Brand `Ergotec`
71. Pilih Model `No Model`
72. Isi Quantity `2`
73. Klik `[+ Asset Name]`
74. Pilih Asset Name `Kursi Kuota {runId}`
75. Pilih Brand `Ergotec`
76. Pilih Model `No Model`
77. Isi Quantity `1`
78. Klik `[+ Asset Name]`
79. Pilih Asset Name `Lemari Kuota {runId}`
80. Pilih Brand `Ergotec`
81. Pilih Model `No Model`
82. Isi Quantity `1`
83. Verifikasi error pada Quantity Item `Kursi Kuota {runId}` `Only 2 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`
84. Verifikasi error pada Quantity Item `Lemari Kuota {runId}` `Only 2 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`
85. Verifikasi Quantity Item `Meja Kuota {runId}` tanpa error
86. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Group tanpa batas menyembunyikan Remaining Quota dan pergantian Group memicu error
87. Klik `[+ Register Asset]`
88. Pilih Group `Gudang Tanpa Batas {runId}`
89. Verifikasi field Group menampilkan `Gudang Tanpa Batas {runId}`
90. Verifikasi `Remaining Quota` tidak tampil di samping field Group
91. Klik `[+ Asset Name]`
92. Pilih Asset Name `Meja Kuota {runId}`
93. Pilih Brand `Ergotec`
94. Pilih Model `No Model`
95. Isi Quantity `3`
96. Pilih Group `Gudang Kuota {runId}`
97. Verifikasi error pada Quantity `Only 2 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`
