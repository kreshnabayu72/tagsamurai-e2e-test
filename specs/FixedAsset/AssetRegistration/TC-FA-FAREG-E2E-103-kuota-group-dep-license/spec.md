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
  F-FAREG-05.k1: [14, 29, 48]
  FAREG-LOGIC-05a: [14, 48]
  FAREG-LOGIC-05g: [9, 14]
  FAREG-LOGIC-05i: [9, 19, 22, 26]
  §9.2#p33: 7
  §9.2#p35: 11
  §9.2#p37: 14
  §9.2#p38: [14, 19]
  §9.2#p39: [16, 19]
  §9.4.2#r3: [7, 9, 14, 79, 80, 81, 92]
  §9.4.2#r9: [14, 48]
  §9.4.2#r11: [14, 19]
  EB-CON-4: [29, 35]
  EB-XM-2@license: [39, 44, 54, 59, 64, 86]
  FAREG-LOGIC-05n: [11, 13]
  D-REG-08: [13, 14, 48]
  V-REG-17: 7
anchor: [85]
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
3. Pilih Asset Name `Meja Kuota {runId}` pada Item pertama
4. Pilih Brand `Ergotec`
5. Pilih Model `No Model`
6. Isi Quantity `10`
7. Verifikasi error pada Quantity `Only 8 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`

### Save draft tetap berjalan dan Activate ditolak seluruhnya
8. Klik `[Save draft]`
9. Verifikasi toast `Success, draft has been saved.`
10. Klik `[Submit]`
11. Verifikasi dialog konfirmasi tampil lebih dulu dengan `Are you sure you want to activate it?`
12. Klik `[Activate]`
13. Verifikasi judul dialog `Cannot Activate` dan tombol `[OK]` tampil
14. Verifikasi dialog memuat `Group quota exceeded. Available slots: 8. Please contact administrator to increase quota.`
15. Klik `[OK]`
16. Verifikasi `Remaining Quota: 8` tetap tampil di samping field Group

### Draft tetap dapat dibaca dan diekspor saat kuota tidak cukup
17. Klik `[Cancel]`
18. Ketik Search `Gudang Kuota {runId}`, tekan Enter
19. Verifikasi baris batch `Gudang Kuota {runId}` tetap di sub tab Draft dengan Total Asset `10`
20. Klik `[Download]`
21. Pilih `Download as CSV`
22. Verifikasi berkas `Registration-Drafts` terunduh

### Aset ke-N diterima dan ke-N+1 ditolak
23. Klik row action `Edit` pada baris batch `Gudang Kuota {runId}`
24. Ganti Quantity menjadi `9`
25. Klik `[Save draft]`
26. Verifikasi toast `Success, draft has been saved.`
27. Klik `[Submit]`
28. Klik `[Activate]`
29. Verifikasi dialog memuat `Group quota exceeded. Available slots: 8. Please contact administrator to increase quota.`
30. Klik `[OK]`
31. Ganti Quantity menjadi `8`
32. Klik `[Save draft]`
33. Klik `[Submit]`
34. Klik `[Activate]`
35. Verifikasi toast `Success, asset has been activated.`

### Sisa kuota Group habis tercermin di form Register Asset
36. Buka Fixed Asset > Assets > Registration > Draft
37. Klik `[+ Register Asset]`
38. Pilih Group `Gudang Kuota {runId}`
39. Verifikasi `Remaining Quota: 0` tampil di samping field Group
40. Pilih Asset Name `Meja Kuota {runId}` pada Item pertama
41. Pilih Brand `Ergotec`
42. Pilih Model `No Model`
43. Isi Quantity `1`
44. Verifikasi error pada Quantity `No more assets can be added to Gudang Kuota {runId}.`

### Activate ditolak saat sisa kuota Group habis
45. Klik `[Save draft]`
46. Klik `[Submit]`
47. Klik `[Activate]`
48. Verifikasi dialog memuat `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
49. Klik `[OK]`
50. Klik `[Cancel]`

### Kuota Group dinaikkan di License tercermin pada Remaining Quota dan pesan Quantity
51. Admin License menaikkan kuota Group `Gudang Kuota {runId}` sehingga sisa kuota Group menjadi `4`
52. Klik `[+ Register Asset]`
53. Pilih Group `Gudang Kuota {runId}`
54. Verifikasi `Remaining Quota: 4` tampil di samping field Group
55. Pilih Asset Name `Meja Kuota {runId}` pada Item pertama
56. Pilih Brand `Ergotec`
57. Pilih Model `No Model`
58. Isi Quantity `5`
59. Verifikasi error pada Quantity `Only 4 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`
60. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Kuota Group diturunkan di License dan error ditandai pada Item yang melampaui sisa
61. Admin License menurunkan kuota Group `Gudang Kuota {runId}` sehingga sisa kuota Group menjadi `2`
62. Klik `[+ Register Asset]`
63. Pilih Group `Gudang Kuota {runId}`
64. Verifikasi `Remaining Quota: 2` tampil di samping field Group
65. Pilih Asset Name `Meja Kuota {runId}` pada Item pertama
66. Pilih Brand `Ergotec` pada Item pertama
67. Pilih Model `No Model` pada Item pertama
68. Isi Quantity `2` pada Item pertama
69. Klik `[+ Asset Name]` untuk menambah Item kedua
70. Pilih Asset Name `Kursi Kuota {runId}` pada Item kedua
71. Pilih Brand `Ergotec` pada Item kedua
72. Pilih Model `No Model` pada Item kedua
73. Isi Quantity `1` pada Item kedua
74. Klik `[+ Asset Name]` untuk menambah Item ketiga
75. Pilih Asset Name `Lemari Kuota {runId}` pada Item ketiga
76. Pilih Brand `Ergotec` pada Item ketiga
77. Pilih Model `No Model` pada Item ketiga
78. Isi Quantity `1` pada Item ketiga
79. Verifikasi error pada Quantity Item `Kursi Kuota {runId}` `Only 2 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`
80. Verifikasi error pada Quantity Item `Lemari Kuota {runId}` `Only 2 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`
81. Verifikasi Quantity Item `Meja Kuota {runId}` tanpa error
82. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Group tanpa batas menyembunyikan Remaining Quota dan pergantian Group memicu error
83. Klik `[+ Register Asset]`
84. Pilih Group `Gudang Tanpa Batas {runId}`
85. Verifikasi field Group menampilkan `Gudang Tanpa Batas {runId}`
86. Verifikasi `Remaining Quota` tidak tampil di samping field Group
87. Pilih Asset Name `Meja Kuota {runId}` pada Item pertama
88. Pilih Brand `Ergotec`
89. Pilih Model `No Model`
90. Isi Quantity `3`
91. Pilih Group `Gudang Kuota {runId}`
92. Verifikasi error pada Quantity `Only 2 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`
