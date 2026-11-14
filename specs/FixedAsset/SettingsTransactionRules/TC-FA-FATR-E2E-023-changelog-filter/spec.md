---
id: TC-FA-FATR-E2E-023-changelog-filter
title: "Filter tabel Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [§4.1#r398, §4.1#r400, §4.1#r401, §4.1#r404, EB-FLT-1@changelog, EB-FLT-4@changelog]
smoke: []
dependsOn: []
trace:
  §4.1#r398: [42, 43, 44]
  §4.1#r400: [11, 12]
  §4.1#r401: [20, 21]
  §4.1#r404: [25, 28, 29, 33, 34, 37, 38]
  EB-FLT-1@changelog: [7, 8, 17, 85, 89]
  EB-FLT-4@changelog: [54, 55, 56, 58, 59, 60, 62, 63, 66, 67, 68, 71, 74, 93]
anchor: [3, 49, 92]
coverage:
  web: automated
---

# Filter tabel Changelog

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-023-1: entri Changelog Category `Vehicle > Pool car {runId}`, Field `Borrow (Max duration)`, Old Value `14 days`, New Value `30 days`, Modified By `Rina Wulandari` (tampil `Rina W`; pengguna dengan Global Role Manage transaction settings Read + Update), Action `Edit`, Date `T0 − 10 hari`.
  - DU-023-2: entri Changelog Category `Vehicle > Pool car {runId}`, Field `Borrow (Allow Borrow)`, Old Value `Allow`, New Value `Deny`, Modified By `Budi Santoso` (tampil `Budi S`; pengguna dengan Global Role Manage transaction settings Read + Update), Action `Edit`, Date `T0 − 5 hari`.
  - DU-023-3: entri Changelog Category `Machinery {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, New Value `10 days`, Modified By `Rina Wulandari`, Action `Edit`, Date `T0 − 5 hari`.
  - DU-023-4: entri Changelog Category `Machinery {runId}`, Field `Transfer (Approval scope)`, Old Value `Both`, New Value `Origin only`, Modified By `Budi Santoso`, Action `Edit`, Date `T0 − 2 hari`.
  - DU-023-5: entri Changelog Category `Machinery {runId}`, Field `Disposal (Allowed disposal types)`, Old Value `Sell, Scrap, Lost, Donate, Trade-in, Write-off`, New Value `Sell, Scrap`, Modified By `Dewi Anggraini` (tampil `Dewi A`; pengguna ini sudah dinonaktifkan sesudah entri tercatat), Action `Edit`, Date `T0 − 5 hari`.
  - DU-023-6: Category `Furniture {runId}` ada di master data Category dan tidak memiliki entri Changelog.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Dialog Changelog dipersempit ke data spec
1. Klik ikon Changelog di header
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris Category `Vehicle > Pool car {runId}` dengan Field `Borrow (Max duration)` tampil

### Opsi filter Category berasal dari data tabel
4. Klik tombol filter di toolbar dialog Changelog
5. Klik field `Category` pada panel filter
6. Ketik `{runId}` pada kotak cari opsi Category
7. Verifikasi opsi `Vehicle > Pool car {runId}` dan opsi `Machinery {runId}` tampil
8. Verifikasi opsi `Furniture {runId}` tidak tampil

### Filter Category menyaring baris
9. Pilih opsi `Vehicle > Pool car {runId}`
10. Klik `[Apply]`
11. Verifikasi baris Field `Borrow (Max duration)` dan baris Field `Borrow (Allow Borrow)` dengan Category `Vehicle > Pool car {runId}` tampil
12. Verifikasi tidak ada baris dengan Category `Machinery {runId}`

### Filter Field menyaring baris dan opsinya tidak berulang
13. Klik `[Clear Field]`
14. Klik `[Apply]`
15. Klik field `Field` pada panel filter
16. Ketik `Max duration` pada kotak cari opsi Field
17. Verifikasi opsi `Borrow (Max duration)` tampil satu kali
18. Pilih opsi `Borrow (Max duration)`
19. Klik `[Apply]`
20. Verifikasi baris Field `Borrow (Max duration)` dengan Category `Vehicle > Pool car {runId}` dan baris Field `Borrow (Max duration)` dengan Category `Machinery {runId}` tampil
21. Verifikasi tidak ada baris dengan Field `Borrow (Allow Borrow)`

### Filter Modified By: satu pengubah, dua pengubah, dan pengubah nonaktif
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Klik field `Modified By` pada panel filter
25. Verifikasi opsi untuk pengubah `Dewi Anggraini` tampil walau pengguna itu sudah dinonaktifkan
26. Pilih opsi untuk pengubah `Dewi Anggraini`
27. Klik `[Apply]`
28. Verifikasi baris Field `Disposal (Allowed disposal types)` dengan Category `Machinery {runId}` tampil
29. Verifikasi tidak ada baris dengan Field `Borrow (Allow Borrow)`
30. Klik `[Clear Field]`
31. Pilih opsi untuk pengubah `Rina Wulandari` pada field `Modified By`
32. Klik `[Apply]`
33. Verifikasi baris Field `Borrow (Max duration)` dengan Category `Vehicle > Pool car {runId}` dan baris Field `Borrow (Max duration)` dengan Category `Machinery {runId}` tampil
34. Verifikasi tidak ada baris dengan Field `Borrow (Allow Borrow)` maupun Field `Transfer (Approval scope)`
35. Pilih opsi untuk pengubah `Budi Santoso` pada field `Modified By`
36. Klik `[Apply]`
37. Verifikasi baris Field `Borrow (Max duration)`, `Borrow (Allow Borrow)`, dan `Transfer (Approval scope)` tampil
38. Verifikasi tidak ada baris dengan Field `Disposal (Allowed disposal types)`

### Filter Date menyaring rentang tanggal
39. Klik `[Clear Field]`
40. Pada field `Date`, pilih rentang dari `T0 − 6 hari` sampai `T0 − 4 hari`
41. Klik `[Apply]`
42. Verifikasi baris Field `Borrow (Allow Borrow)`, baris Field `Borrow (Max duration)` dengan Category `Machinery {runId}`, dan baris Field `Disposal (Allowed disposal types)` tampil
43. Verifikasi tidak ada baris Field `Borrow (Max duration)` dengan Category `Vehicle > Pool car {runId}`
44. Verifikasi tidak ada baris Field `Transfer (Approval scope)`

### Search dan Filter menghasilkan irisan, Search lebih dulu
45. Klik `[Clear Field]`
46. Klik `[Apply]`
47. Ganti isi kotak search dengan `Vehicle > Pool car {runId}`, tekan Enter
48. Klik header kolom `Field`
49. Verifikasi baris Field `Borrow (Allow Borrow)` tampil di atas baris Field `Borrow (Max duration)`
50. Pilih opsi untuk pengubah `Budi Santoso` pada field `Modified By`
51. Pilih opsi `Vehicle > Pool car {runId}` pada field `Category`
52. Pilih opsi `Machinery {runId}` pada field `Category`
53. Klik `[Apply]`
54. Verifikasi baris Field `Borrow (Allow Borrow)` dengan Category `Vehicle > Pool car {runId}` tampil
55. Verifikasi tidak ada baris Field `Borrow (Max duration)` dengan Category `Vehicle > Pool car {runId}`
56. Verifikasi tidak ada baris dengan Category `Machinery {runId}`

### Mengosongkan Search mempertahankan Filter dan Sort
57. Klik `(←)` pada kotak Search
58. Verifikasi baris Field `Borrow (Allow Borrow)` dan baris Field `Transfer (Approval scope)` tampil
59. Verifikasi baris Field `Borrow (Allow Borrow)` tampil di atas baris Field `Transfer (Approval scope)`
60. Verifikasi tidak ada baris Field `Borrow (Max duration)`

### Search sesudah Filter menghasilkan irisan yang sama
61. Ganti isi kotak search dengan `Vehicle > Pool car {runId}`, tekan Enter
62. Verifikasi baris Field `Borrow (Allow Borrow)` dengan Category `Vehicle > Pool car {runId}` tampil sebagai satu-satunya hasil irisan
63. Verifikasi tidak ada baris dengan Category `Machinery {runId}`

### Clear Field mempertahankan Search dan Sort
64. Klik `[Clear Field]`
65. Klik `[Apply]`
66. Verifikasi baris Field `Borrow (Max duration)` dan baris Field `Borrow (Allow Borrow)` dengan Category `Vehicle > Pool car {runId}` tampil
67. Verifikasi baris Field `Borrow (Allow Borrow)` tampil di atas baris Field `Borrow (Max duration)`
68. Verifikasi tidak ada baris dengan Category `Machinery {runId}`

### Irisan kosong dan pemulihan dari empty state
69. Pilih opsi untuk pengubah `Dewi Anggraini` pada field `Modified By`
70. Klik `[Apply]`
71. Verifikasi tabel Changelog menampilkan empty state `No results found` untuk irisan Search dan Filter
72. Klik `[Clear Field]`
73. Klik `[Apply]`
74. Verifikasi baris Field `Borrow (Max duration)` dan baris Field `Borrow (Allow Borrow)` dengan Category `Vehicle > Pool car {runId}` tampil kembali

### Entri baru dari Save menjadi opsi filter tanpa muat ulang dan tidak tampil bila tidak cocok dengan Filter
75. Klik `✕` pada dialog Changelog
76. Ketik Search Sidebar Category Tree `Furniture {runId}`, tekan Enter
77. Klik node `Furniture {runId}` di Sidebar Category Tree
78. Klik tab `Borrow`
79. Klik `[Set own value]` pada field Max duration
80. Isi Max duration `18`
81. Klik `[Save]`
82. Klik `[Save]` pada dialog Save Changes
83. Klik ikon Changelog di header
84. Ketik Search `{runId}`, tekan Enter
85. Verifikasi ada baris dengan Category `Furniture {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, dan New Value `18 days`
86. Klik tombol filter di toolbar dialog Changelog
87. Klik field `Category` pada panel filter
88. Ketik `{runId}` pada kotak cari opsi Category
89. Verifikasi opsi `Furniture {runId}` tampil tanpa muat ulang halaman
90. Pilih opsi `Vehicle > Pool car {runId}`
91. Klik `[Apply]`
92. Verifikasi baris Field `Borrow (Max duration)` dan baris Field `Borrow (Allow Borrow)` dengan Category `Vehicle > Pool car {runId}` tampil
93. Verifikasi tidak ada baris dengan Category `Furniture {runId}` karena entri barunya tidak cocok dengan Filter Category aktif
