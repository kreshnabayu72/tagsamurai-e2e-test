---
id: TC-FA-FACO-E2E-014-changelog-filter
title: "Filter Panel modal Changelog menyaring entri dan memuat opsi dari data log"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1.1#r21", "§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§4.1.1#r27", "EB-FLT-1@tabel-changelog", "EB-FLT-4@tabel-changelog"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r21": [85, 88, 91]
  "§4.1.1#r22": [28, 57, 58, 59]
  "§4.1.1#r23": [36, 37]
  "§4.1.1#r24": [31, 32, 45, 46]
  "§4.1.1#r27": [41, 49, 50, 51, 52]
  "EB-FLT-1@tabel-changelog": [28, 31, 32, 36, 37, 41, 101]
  "EB-FLT-4@tabel-changelog": [45, 61, 64, 72, 76, 77]
anchor: [69]
coverage:
  web: automated
---

# Filter Panel modal Changelog menyaring entri dan memuat opsi dari data log

## Prerequisites
- Aktor: pengguna Total Control (aktor M). Aktor lain: Admin B (DU-014-9).
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - Seluruh Account Code berbentuk FC-{runId}-huruf, sehingga Search `FC-{runId}` pada modal Changelog hanya menampilkan entri milik spec ini. Setiap akun di bawah menghasilkan tepat satu entri Changelog pada langkah spec ini.
  - DU-014-1: akun `FC-{runId}-a`, Account Name `Filter Awal A {runId}`, Account Function `Asset Cost`, Status `Active`. Aktor M mengubah Account Name menjadi `Filter Akhir A {runId}` (entri Edit, Field `Account Name`).
  - DU-014-2: akun `FC-{runId}-b`, Account Name `Filter Awal B {runId}`, Account Function `Asset Cost`, Status `Active`. Aktor M mengubah Account Name menjadi `Filter Akhir B {runId}` (entri Edit, Field `Account Name`).
  - DU-014-3: akun `FC-{runId}-c`, Account Name `Filter Fungsi C {runId}`, Account Function `Asset Cost`, Status `Active`. Aktor M mengubah Account Function menjadi `Gain on Disposal` (entri Edit, Field `Account Function`).
  - DU-014-4: akun `FC-{runId}-d`, dibuat aktor M lewat form dengan Account Name `Filter Buat D {runId}` dan Account Function `Asset Cost` (entri Create, Field `Account Code`).
  - DU-014-5: akun `FC-{runId}-e`, Account Name `Filter Hapus E {runId}`, Account Function `Asset Cost`, Status `Active`. Aktor M menghapus akun ini (entri Delete, Field `Account Code`).
  - DU-014-6: akun `FC-{runId}-f`, Account Name `Filter Awal F {runId}`, Account Function `Asset Cost`, Status `Active`. Admin B mengubah Account Name menjadi `Filter Akhir F {runId}` (entri Edit, Field `Account Name`, Modified By Admin B).
  - DU-014-7: akun `FC-{runId}-i`, Account Name `Filter Fungsi I {runId}`, Account Function `Asset Cost`, Status `Active`. Admin B mengubah Account Function menjadi `Gain on Disposal` (entri Edit, Field `Account Function`, Modified By Admin B).
  - DU-014-8: akun `FC-{runId}-j`, Account Name `Filter Baru J {runId}`, Account Function `Asset Cost`, Status `Active`. Belum punya entri Changelog sampai langkah spec ini mengubah Account Name menjadi `Filter Baru Akhir J {runId}`.
  - DU-014-9: Admin B, nama lengkap `Rani Pratama`, role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Seluruh entri dibuat pada hari run (T0).
  - Ukuran halaman modal Changelog adalah 10 baris (nilai bawaan).

## Test Steps
### Opsi filter berisi nilai yang ada di log
1. Ketik Search `FC-{runId}-a`, tekan Enter
2. Klik `⋯` pada baris `FC-{runId}-a` > `Edit`
3. Ganti isi Account Name dengan `Filter Akhir A {runId}`
4. Klik `[Save]`
5. Ganti isi kotak Search dengan `FC-{runId}-b`, tekan Enter
6. Klik `⋯` pada baris `FC-{runId}-b` > `Edit`
7. Ganti isi Account Name dengan `Filter Akhir B {runId}`
8. Klik `[Save]`
9. Ganti isi kotak Search dengan `FC-{runId}-c`, tekan Enter
10. Klik `⋯` pada baris `FC-{runId}-c` > `Edit`
11. Pilih `Gain on Disposal` pada field Account Function
12. Klik `[Save]`
13. Klik `(←)` pada kotak Search
14. Klik `[+ Account]`
15. Isi Account Code `FC-{runId}-d`
16. Isi Account Name `Filter Buat D {runId}`
17. Pilih `Asset Cost` pada field Account Function
18. Klik `[Submit]`
19. Ganti isi kotak Search dengan `FC-{runId}-e`, tekan Enter
20. Klik `⋯` pada baris `FC-{runId}-e` > `Delete`
21. Klik `[Delete]` pada dialog `Delete Account`
22. Admin B mengubah Account Name `FC-{runId}-f` menjadi `Filter Akhir F {runId}`
23. Admin B mengubah Account Function `FC-{runId}-i` menjadi `Gain on Disposal`
24. Klik ikon Changelog
25. Ketik Search `FC-{runId}` pada modal Changelog, tekan Enter
26. Klik ikon Filter pada modal Changelog
27. Buka dropdown field Action
28. Verifikasi opsi field Action adalah `Create`, `Edit`, dan `Delete`
29. Tutup dropdown field Action
30. Buka dropdown field Field
31. Verifikasi opsi `Account Name` tampil satu kali walau banyak entri memuat nilai itu
32. Verifikasi opsi `Account Function` dan `Account Code` tampil di field Field
33. Tutup dropdown field Field
34. Buka dropdown field Account Code
35. Ketik `FC-{runId}` pada pencarian dropdown field Account Code
36. Verifikasi opsi `FC-{runId}-a` tampil di field Account Code
37. Verifikasi opsi `FC-{runId}-e` tampil di field Account Code walau akunnya sudah dihapus, karena entri log tetap tersimpan
38. Tutup dropdown field Account Code
39. Buka dropdown field Modified By
40. Ketik `Rani Pratama` pada pencarian dropdown field Modified By
41. Verifikasi opsi untuk Admin B (`Rani Pratama`) tampil di field Modified By
42. Tutup dropdown field Modified By

### Filter satu field menampilkan entri yang cocok
43. Pilih `Account Name` pada field Field
44. Klik `[Apply]`
45. Verifikasi entri `FC-{runId}-a`, `FC-{runId}-b`, dan `FC-{runId}-f` tampil karena Field-nya `Account Name`
46. Verifikasi entri `FC-{runId}-c` tidak tampil karena Field-nya `Account Function`

### Beberapa field berlaku AND
47. Pilih `Rani Pratama` pada field Modified By
48. Klik `[Apply]`
49. Verifikasi entri `FC-{runId}-f` tampil karena Field-nya `Account Name` dan Modified By-nya Admin B
50. Verifikasi entri `FC-{runId}-a` tidak tampil karena hanya cocok dengan Field `Account Name`
51. Verifikasi entri `FC-{runId}-i` tidak tampil karena hanya cocok dengan Modified By Admin B
52. Verifikasi entri `FC-{runId}-c` tidak tampil karena tidak cocok dengan keduanya

### Beberapa nilai dalam satu field berlaku OR
53. Klik `[Clear Field]` pada field Field
54. Klik `[Clear Field]` pada field Modified By
55. Pilih `Create` dan `Delete` pada field Action
56. Klik `[Apply]`
57. Verifikasi entri `FC-{runId}-d` tampil karena Action-nya `Create`
58. Verifikasi entri `FC-{runId}-e` tampil karena Action-nya `Delete`
59. Verifikasi entri `FC-{runId}-a` tidak tampil karena Action-nya `Edit`

### Search dan Filter berlaku bersamaan dengan irisan kosong yang pulih saat satu saringan dilepas
60. Ganti isi kotak Search modal Changelog dengan `FC-{runId}-a`, tekan Enter
61. Verifikasi `No results found` tampil di modal Changelog karena entri `FC-{runId}-a` cocok dengan Search tetapi bukan `Create` atau `Delete`, dan entri `FC-{runId}-d` cocok dengan Filter tetapi tidak dengan Search
62. Klik `[Clear Field]` pada field Action
63. Klik `[Apply]`
64. Verifikasi entri `FC-{runId}-a` tampil kembali karena hanya Search yang tersisa

### Clear Filter mempertahankan Search dan Sort, Clear Search mempertahankan Filter dan Sort
65. Ganti isi kotak Search modal Changelog dengan `FC-{runId}`, tekan Enter
66. Klik header kolom Account Code pada modal Changelog (klik pertama)
67. Pilih `Create` dan `Delete` pada field Action
68. Klik `[Apply]`
69. Verifikasi entri `FC-{runId}-d` tampil di atas entri `FC-{runId}-e` sesuai urutan Account Code menaik
70. Klik `[Clear Field]` pada field Action
71. Klik `[Apply]`
72. Verifikasi urutan entri menaik menurut Account Code tetap berlaku dan Search `FC-{runId}` tetap berlaku: `FC-{runId}-a`, `FC-{runId}-b`, `FC-{runId}-c`, `FC-{runId}-d`, `FC-{runId}-e`, `FC-{runId}-f`, `FC-{runId}-i`
73. Pilih `Create` dan `Delete` pada field Action
74. Klik `[Apply]`
75. Klik `(←)` pada kotak Search modal Changelog
76. Verifikasi nilai `Create` dan `Delete` pada field Action di Filter Panel tetap terpilih
77. Verifikasi entri `FC-{runId}-d` tampil di atas entri `FC-{runId}-e` sesuai urutan Account Code menaik
78. Klik `[Clear Field]` pada field Action
79. Klik `[Apply]`
80. Klik header kolom Account Code pada modal Changelog (klik kedua)
81. Klik header kolom Account Code pada modal Changelog (klik ketiga)
82. Ketik Search `FC-{runId}` pada modal Changelog, tekan Enter

### Filter Date dengan rentang tanggal inklusif
83. Pilih rentang tanggal dari T0 sampai T0 (satu hari) pada field Date
84. Klik `[Apply]`
85. Verifikasi entri `FC-{runId}-a` tampil karena Date-nya T0 ada di dalam rentang satu hari
86. Pilih rentang tanggal dari T0 + 1 hari sampai T0 + 7 hari pada field Date
87. Klik `[Apply]`
88. Verifikasi `No results found` tampil di modal Changelog karena T0 di luar rentang
89. Klik `[Clear Field]` pada field Date
90. Klik `[Apply]`
91. Verifikasi entri `FC-{runId}-a` tampil kembali karena Filter dilepas

### Entri baru menambah opsi filter tanpa muat ulang
92. Tutup modal Changelog
93. Ganti isi kotak Search dengan `FC-{runId}-j`, tekan Enter
94. Klik `⋯` pada baris `FC-{runId}-j` > `Edit`
95. Ganti isi Account Name dengan `Filter Baru Akhir J {runId}`
96. Klik `[Save]`
97. Klik ikon Changelog
98. Klik ikon Filter pada modal Changelog
99. Buka dropdown field Account Code
100. Ketik `FC-{runId}` pada pencarian dropdown field Account Code
101. Verifikasi opsi `FC-{runId}-j` tampil di field Account Code tanpa memuat ulang halaman
102. Tutup dropdown field Account Code
