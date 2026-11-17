---
id: TC-FA-FATR-E2E-121-tab-audit-geolocation
title: "Tab Audit dan Geolocation: tanpa Sidebar Category Tree, isi sama di setiap node, dan Save Changes tercatat di Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r109", "§Aturan Logika Modul#r110", "§Aturan Logika Modul#r118", "§4.3#r20", "§Aturan Logika Modul#r114", "§9.4.2#r65", "§9.4.2#r68", "§4.1#r58", "§4.1#r59", "§4.1#r242", "§4.1#r4", "§4.1#r6", "§Aturan Logika Modul#r117", "§9.10.5#b4"]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#r109": [26, 27, 34, 35, 65]
  "§Aturan Logika Modul#r110": [28, 30, 37]
  "§Aturan Logika Modul#r118": [3, 4, 10, 11, 67]
  "§4.3#r20": [4, 6, 11, 13, 17, 19, 21, 28, 30, 37]
  "§Aturan Logika Modul#r114": [51, 52]
  "§9.4.2#r65": [46, 48, 57]
  "§9.4.2#r68": [54, 59]
  "§4.1#r58": [57, 59, 90, 91]
  "§4.1#r59": 59
  "§4.1#r242": [75, 79, 82, 83, 86]
  "§4.1#r4": [4, 11]
  "§4.1#r6": [19, 28]
  "§Aturan Logika Modul#r117": [10, 67]
  "§9.10.5#b4": 26
anchor: [15]
coverage:
  web: automated
---

# Tab Audit dan Geolocation: tanpa Sidebar Category Tree, isi sama di setiap node, dan Save Changes tercatat di Changelog

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-121-1: Entitas `Citra Audit {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan transaksi Borrow. Addon Audit dan addon Maintenance aktif pada subscription FAMS-nya. Entitas ini belum memiliki entri Changelog Transaction Settings.
  - DU-121-2: Category leaf `Forklift {runId}`, tanpa sub-Category, ada di entitas DU-121-1. Semua field Inherit.
- Kondisi:
  - Company default entitas DU-121-1 bernilai bawaan: Grace period `3`, Require location Audit `OFF`, Require location Maintenance `OFF`.

## Test Steps

### Tab Audit menyembunyikan Sidebar Category Tree dan isinya sama di setiap node
1. Klik `All categories` pada Sidebar Category Tree
2. Klik tab `Audit`
3. Verifikasi field `Grace period` bernilai `3`
4. Verifikasi Sidebar Category Tree tidak tampil
5. Klik tab `Borrow`
6. Verifikasi Sidebar Category Tree tampil kembali dengan node `All categories` terpilih
7. Ketik Search Sidebar Category Tree `Forklift {runId}`, tekan Enter
8. Klik Category leaf `Forklift {runId}`
9. Klik tab `Audit`
10. Verifikasi field `Grace period` bernilai `3`
11. Verifikasi Sidebar Category Tree tidak tampil
12. Klik tab `Borrow`
13. Verifikasi Sidebar Category Tree tampil kembali dengan node `Forklift {runId}` terpilih

### Tombol pembuka Sidebar Category Tree yang collapsed tidak tampil di tab Audit dan Geolocation
14. Collapse Sidebar Category Tree
15. Verifikasi tombol pembuka Sidebar Category Tree tampil
16. Klik tab `Audit`
17. Verifikasi tombol pembuka Sidebar Category Tree tidak tampil
18. Klik tab `Geolocation`
19. Verifikasi tombol pembuka Sidebar Category Tree tidak tampil
20. Klik tab `Borrow`
21. Verifikasi tombol pembuka Sidebar Category Tree tampil kembali
22. Klik tombol pembuka Sidebar Category Tree

### Tab Geolocation menyembunyikan Sidebar Category Tree dan isinya sama di setiap node
23. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
24. Klik `All categories`
25. Klik tab `Geolocation`
26. Verifikasi baris `Audit` pada Require location bernilai `OFF`
27. Verifikasi baris `Maintenance` pada Require location bernilai `OFF`
28. Verifikasi Sidebar Category Tree tidak tampil
29. Klik tab `Borrow`
30. Verifikasi Sidebar Category Tree tampil kembali dengan node `All categories` terpilih
31. Ketik Search Sidebar Category Tree `Forklift {runId}`, tekan Enter
32. Klik Category leaf `Forklift {runId}`
33. Klik tab `Geolocation`
34. Verifikasi baris `Audit` pada Require location bernilai `OFF`
35. Verifikasi baris `Maintenance` pada Require location bernilai `OFF`
36. Klik tab `Borrow`
37. Verifikasi Sidebar Category Tree tampil kembali dengan node `Forklift {runId}` terpilih

### Satu Save Changes menyimpan Grace period dan Require location
38. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
39. Klik `All categories`
40. Klik tab `Audit`
41. Isi `Grace period` `0`
42. Klik tab `Geolocation`
43. Klik switch baris `Audit` pada Require location sehingga bernilai `ON`
44. Klik switch baris `Maintenance` pada Require location sehingga bernilai `ON`
45. Klik `[Save]`
46. Verifikasi paragraf `The changes apply to new transactions.` tampil pada dialog Save Changes
47. Klik `[Save]` pada dialog Save Changes
48. Verifikasi toast `Success, settings have been saved.`
49. Muat ulang halaman
50. Klik tab `Geolocation`
51. Verifikasi baris `Audit` pada Require location bernilai `ON`
52. Verifikasi baris `Maintenance` pada Require location bernilai `ON`
53. Klik tab `Audit`
54. Verifikasi field `Grace period` bernilai `0`

### Changelog mencatat perubahan tab Audit dan Geolocation dengan Category All categories
55. Klik ikon Changelog di header
56. Ketik Search `Audit (Require location)`, tekan Enter
57. Verifikasi tabel Changelog memuat 1 baris dengan Field `Audit (Require location)` dan Category `All categories`
58. Ganti isi kotak search dengan `Audit (Grace period)`, tekan Enter
59. Verifikasi tabel Changelog memuat 1 baris dengan Field `Audit (Grace period)`, Category `All categories`, dan New Value `No grace period`
60. Tekan `Esc` untuk menutup dialog Changelog

### Nilai tersimpan tampil sama di node Category lain
61. Klik tab `Borrow`
62. Ketik Search Sidebar Category Tree `Forklift {runId}`, tekan Enter
63. Klik Category leaf `Forklift {runId}`
64. Klik tab `Geolocation`
65. Verifikasi baris `Audit` pada Require location bernilai `ON`
66. Klik tab `Audit`
67. Verifikasi field `Grace period` bernilai `0`

### Reset to Default di tab Geolocation berlaku setelah Save
68. Klik tab `Borrow`
69. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
70. Klik `All categories`
71. Klik tab `Geolocation`
72. Klik `[Reset to Default]`
73. Klik ikon Changelog di header
74. Ketik Search `Audit (Require location)`, tekan Enter
75. Verifikasi tabel Changelog memuat 1 baris dengan Field `Audit (Require location)`
76. Tekan `Esc` untuk menutup dialog Changelog
77. Klik `[Save]`
78. Klik `[Save]` pada dialog Save Changes
79. Verifikasi toast `Success, settings have been saved.`
80. Muat ulang halaman
81. Klik tab `Geolocation`
82. Verifikasi baris `Audit` pada Require location bernilai `OFF`
83. Verifikasi baris `Maintenance` pada Require location bernilai `OFF`
84. Klik ikon Changelog di header
85. Ketik Search `Audit (Require location)`, tekan Enter
86. Verifikasi tabel Changelog memuat 2 baris dengan Field `Audit (Require location)`
87. Tekan `Esc` untuk menutup dialog Changelog

### Changelog mencatat perubahan Require location Maintenance dengan Category All categories
88. Klik ikon Changelog di header
89. Ketik Search `Maintenance (Require location)`, tekan Enter
90. Verifikasi tabel Changelog memuat 2 baris dengan Field `Maintenance (Require location)`
91. Verifikasi setiap baris Changelog itu memuat Category `All categories`
92. Tekan `Esc` untuk menutup dialog Changelog
