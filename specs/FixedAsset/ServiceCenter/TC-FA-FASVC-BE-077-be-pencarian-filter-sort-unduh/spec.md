---
id: TC-FA-FASVC-BE-077-be-pencarian-filter-sort-unduh
title: "Server: Search per Kelas Kolom, Filter AND dan OR, Sort per Tipe, dan Isi Berkas Unduhan"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§5#b2", "§5#b3", "§5#b4", "EB-SRC-1", "EB-FLT-3", "EB-SRT-1", "EB-SRT-2", "EB-DL-4", "EB-DL-5"]
smoke: []
dependsOn: []
trace:
  "§5#b2": [22, 24, 28, 38, 40]
  "§5#b3": [30, 34, 36]
  "§5#b4": [14, 16, 18, 20, 22, 24, 26, 30, 32, 91, 93]
  "EB-SRC-1": [2, 4, 6, 8, 10, 12, 14]
  "EB-FLT-3": [28, 38, 40, 42, 44, 46]
  "EB-SRT-1": [48, 50, 52, 54, 56, 58, 60]
  "EB-SRT-2": [52, 54, 56, 62]
  "EB-DL-4": [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 75, 77, 79, 81, 83, 85, 89]
  "EB-DL-5": [87, 89]
anchor: []
---

# Server: Search per Kelas Kolom, Filter AND dan OR, Sort per Tipe, dan Isi Berkas Unduhan

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` pada client suite.
- Data:
  - DU-077-1: User `Rina Wulandari {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group.
  - DU-077-2: Group `Region Jawa {runId}`, anak langsung root pohon Group, ada di client suite.
  - DU-077-3: Group `Cabang Surabaya {runId}`, anak dari `Region Jawa {runId}`, ada di client suite.
  - DU-077-4: Group `Cabang Malang {runId}`, anak dari `Region Jawa {runId}`, ada di client suite.
  - DU-077-5: Group `Cabang Bekasi {runId}`, anak langsung root pohon Group, ada di client suite.
  - DU-077-6: Category `Elektronik {runId}`, ada di client suite.
  - DU-077-7: Category `AC {runId}`, anak dari `Elektronik {runId}`, ada di client suite.
  - DU-077-8: Category `Genset {runId}`, tanpa induk, ada di client suite.
  - DU-077-9: Category `Kendaraan {runId}`, tanpa induk, ada di client suite.
  - DU-077-10: Brand `Daikin {runId}`, ada di client suite.
  - DU-077-11: Brand `LG {runId}`, ada di client suite.
  - DU-077-12: Brand `Panasonic {runId}`, ada di client suite.
  - DU-077-13: Service Center `Alfa Servis Teknik {runId}`, Service type `Routine, Repair`, Specialization `AC {runId}`, Brands `Daikin {runId}`, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@daftar077.co.id`, Status `Active`, tanpa rujukan Schedule, Task, maupun Work Order, dibuat dan terakhir diubah oleh `Rina Wulandari {runId}`.
  - DU-077-14: Service Center `bravo servis mekanik {runId}`, Service type `Repair`, Specialization `Kendaraan {runId}`, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Bandung`, Company email `kontak@daftar077.co.id`, Status `Inactive`, tanpa rujukan Schedule, Task, maupun Work Order, dibuat dan terakhir diubah oleh `Rina Wulandari {runId}`.
  - DU-077-15: Service Center `Charlie Kalibrasi Pratama {runId}`, Service type `Routine`, Specialization kosong, Brands `Daikin {runId}, LG {runId}`, Available to `Region Jawa {runId}`, Country `Indonesia`, City `Malang`, Company email `kontak@daftar077.co.id`, Status `Active`, tanpa rujukan Schedule, Task, maupun Work Order, dibuat dan terakhir diubah oleh `Rina Wulandari {runId}`.
  - DU-077-16: Service Center `Delta Servis Terpadu {runId}`, Service type `Routine`, Specialization `AC {runId}, Genset {runId}, Kendaraan {runId}`, Brands `Daikin {runId}, LG {runId}, Panasonic {runId}`, Available to `Cabang Surabaya {runId}, Cabang Malang {runId}, Cabang Bekasi {runId}`, Country `Indonesia`, City `Jakarta Selatan`, Company email `kontak@daftar077.co.id`, Status `Active`, tanpa rujukan Schedule, Task, maupun Work Order, dibuat dan terakhir diubah oleh `Rina Wulandari {runId}`.
  - DU-077-17: Service Center `Echo Servis Perkasa {runId}`, Service type `Repair`, Specialization kosong, Brands kosong, Available to `Cabang Bekasi {runId}`, Country `Indonesia`, City `Medan`, Company email `kontak@daftar077.co.id`, Status `Active`, tanpa rujukan Schedule, Task, maupun Work Order, dibuat dan terakhir diubah oleh `Rina Wulandari {runId}`.
  - DU-077-18: Service Center `Servis Massal {n} {runId}`, 12 record (n = 1 sampai 12), Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Medan`, Company email `kontak@daftar077.co.id`, Status `Active`, dibuat dan terakhir diubah oleh `Rina Wulandari {runId}`.
  - DU-077-19: Service Center `Foxtrot Servis Elektronik {runId}`, Service type `Routine`, Specialization `Elektronik {runId}`, Brands `Daikin {runId}`, Available to `Cabang Malang {runId}`, Country `Indonesia`, City `Semarang`, Company email `kontak@daftar077.co.id`, Status `Active`, tanpa rujukan Schedule, Task, maupun Work Order, dibuat dan terakhir diubah oleh `Rina Wulandari {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.
  - Kolom daftar yang tampil adalah kolom bawaan, semuanya tampil, dan sort aktif adalah Name A-Z kecuali disebut di langkah.
## Test Steps
### Search mencocokkan substring tanpa membedakan huruf besar-kecil pada kolom teks dan badge
1. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `kalibrasi`
2. Verifikasi hasil memuat `Charlie Kalibrasi Pratama {runId}` dan tidak memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Delta Servis Terpadu {runId}`, dan `Echo Servis Perkasa {runId}`, karena pencarian mencocokkan substring di tengah Name tanpa membedakan huruf besar-kecil
3. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `KALIBRASI`
4. Verifikasi hasil sama dengan pencarian huruf kecil sebelumnya, yaitu memuat `Charlie Kalibrasi Pratama {runId}`
5. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `Repair`
6. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Echo Servis Perkasa {runId}` dan tidak memuat `Charlie Kalibrasi Pratama {runId}` dan `Delta Servis Terpadu {runId}`, karena kolom Service Type ikut dicari
7. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `Active`
8. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}` dan juga `bravo servis mekanik {runId}`, karena pencarian mencocokkan substring tanpa membedakan huruf besar-kecil sehingga `Active` juga cocok dengan nilai Status `Inactive`
9. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `Inactive`
10. Verifikasi hasil memuat `bravo servis mekanik {runId}` dan tidak memuat `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}`
11. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `zzqx077`
12. Verifikasi hasil tidak memuat satu pun dari `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}`

### Search pada kolom chip mencocokkan seluruh nilai termasuk yang tersembunyi dan teks All categories dan All brands
13. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `Panasonic {runId}`
14. Verifikasi hasil memuat `Delta Servis Terpadu {runId}`, karena Brands `Panasonic {runId}` ada di balik `+1 more` pada kolom Brands, dan tidak memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, dan `Echo Servis Perkasa {runId}`
15. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `Cabang Bekasi {runId}`
16. Verifikasi hasil memuat `Delta Servis Terpadu {runId}` dan `Echo Servis Perkasa {runId}` dan tidak memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, dan `Charlie Kalibrasi Pratama {runId}`, karena Available to `Delta Servis Terpadu {runId}` dan `Echo Servis Perkasa {runId}` memuat `Cabang Bekasi {runId}`
17. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `all categories`
18. Verifikasi hasil memuat `Charlie Kalibrasi Pratama {runId}` dan `Echo Servis Perkasa {runId}` dan tidak memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, dan `Delta Servis Terpadu {runId}`, karena teks tampilan `All categories` dicocokkan sebagai substring tanpa membedakan huruf besar-kecil
19. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `ALL BRANDS`
20. Verifikasi hasil memuat `bravo servis mekanik {runId}` dan `Echo Servis Perkasa {runId}` dan tidak memuat `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, dan `Delta Servis Terpadu {runId}`, karena teks tampilan `All brands` dicocokkan sebagai substring tanpa membedakan huruf besar-kecil

### Filter Available To memilih Service Center yang tersedia untuk salah satu node terpilih termasuk All groups dan kerabatnya
21. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Available To `Cabang Surabaya {runId}`
22. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}` dan tidak memuat `Echo Servis Perkasa {runId}`: `Alfa Servis Teknik {runId}` dan `Delta Servis Terpadu {runId}` karena memuat `Cabang Surabaya {runId}`, `bravo servis mekanik {runId}` karena `All groups` cocok dengan semua node, dan `Charlie Kalibrasi Pratama {runId}` karena `Region Jawa {runId}` adalah induk dari `Cabang Surabaya {runId}`
23. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Available To `Cabang Malang {runId}`
24. Verifikasi hasil memuat `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}` dan tidak memuat `Alfa Servis Teknik {runId}` dan `Echo Servis Perkasa {runId}`
25. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Available To `Region Jawa {runId}`, yang memilih juga `Cabang Surabaya {runId}` dan `Cabang Malang {runId}`
26. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}` dan tidak memuat `Echo Servis Perkasa {runId}`, karena memilih node induk memilih seluruh turunannya
27. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Available To `Cabang Surabaya {runId}` dan `Cabang Bekasi {runId}` sekaligus
28. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}`, karena Service Center cocok bila tersedia untuk salah satu node terpilih

### Filter Specialization dan Brands menyertakan vendor yang kosong
29. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Specialization `AC {runId}`
30. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}` dan tidak memuat `bravo servis mekanik {runId}`: `Alfa Servis Teknik {runId}` dan `Delta Servis Terpadu {runId}` karena memuat `AC {runId}`, serta `Charlie Kalibrasi Pratama {runId}` dan `Echo Servis Perkasa {runId}` karena Specialization kosong tidak membatasi kategori
31. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Specialization `Elektronik {runId}`, yang memilih juga `AC {runId}`
32. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}` dan tidak memuat `bravo servis mekanik {runId}`
33. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Brands `LG {runId}`
34. Verifikasi hasil memuat `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}` dan tidak memuat `Alfa Servis Teknik {runId}`: `Charlie Kalibrasi Pratama {runId}` dan `Delta Servis Terpadu {runId}` karena memuat `LG {runId}`, serta `bravo servis mekanik {runId}` dan `Echo Servis Perkasa {runId}` karena Brands kosong berarti semua brand
35. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Brands `Panasonic {runId}`
36. Verifikasi hasil memuat `bravo servis mekanik {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}` dan tidak memuat `Alfa Servis Teknik {runId}` dan `Charlie Kalibrasi Pratama {runId}`

### Filter antar field berlaku AND dan dalam satu field berlaku OR
37. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Available To `Cabang Surabaya {runId}` dan filter Status `Inactive`
38. Verifikasi hasil memuat `bravo servis mekanik {runId}` dan tidak memuat `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, dan `Echo Servis Perkasa {runId}`, karena hanya `bravo servis mekanik {runId}` memenuhi kedua filter
39. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Available To `Cabang Surabaya {runId}` dan filter Status `Active`
40. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, dan `Delta Servis Terpadu {runId}` dan tidak memuat `bravo servis mekanik {runId}` dan `Echo Servis Perkasa {runId}`
41. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `{runId}` dan filter Status `Active` dan `Inactive` sekaligus
42. Verifikasi hasil memuat `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}`, karena opsi dalam satu field digabung dengan OR
43. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `{runId}`, filter Service Type `Repair`, dan filter Status `Active`
44. Verifikasi hasil memuat `Alfa Servis Teknik {runId}` dan `Echo Servis Perkasa {runId}` dan tidak memuat `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, dan `Delta Servis Terpadu {runId}`
45. Baca seluruh halaman hasil daftar Service Center client suite dengan pencarian `Repair` dan filter Status `Active`
46. Verifikasi hasil memuat `Alfa Servis Teknik {runId}` dan `Echo Servis Perkasa {runId}` dan tidak memuat `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, dan `Delta Servis Terpadu {runId}`, karena hasilnya adalah irisan pencarian dan filter

### Sort mengikuti tipe kolom, nilai kosong, dan Name sebagai pemecah seri
47. Baca daftar Service Center client suite dengan pencarian `{runId}` dan sort Name A-Z
48. Verifikasi urutan di antara kelimanya `Alfa Servis Teknik {runId}`, `bravo servis mekanik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `Echo Servis Perkasa {runId}`, karena sort alfabetis tidak membedakan huruf besar-kecil sehingga `bravo servis mekanik {runId}` yang berawalan huruf kecil `b` tetap di antara `Alfa Servis Teknik {runId}` dan `Charlie Kalibrasi Pratama {runId}`
49. Baca daftar Service Center client suite dengan pencarian `{runId}` dan sort Name Z-A
50. Verifikasi urutan di antara kelimanya `Echo Servis Perkasa {runId}`, `Delta Servis Terpadu {runId}`, `Charlie Kalibrasi Pratama {runId}`, `bravo servis mekanik {runId}`, `Alfa Servis Teknik {runId}`
51. Baca daftar Service Center client suite dengan pencarian `{runId}` dan sort Service Type A-Z
52. Verifikasi urutan di antara kelimanya `bravo servis mekanik {runId}`, `Echo Servis Perkasa {runId}`, `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, karena Service Type diurutkan menurut daftar nilai terurut yang digabung `, ` yaitu `Repair`, `Repair, Routine`, dan `Routine`, dengan pemecah seri Name A-Z
53. Baca daftar Service Center client suite dengan pencarian `{runId}` dan sort Brands A-Z
54. Verifikasi urutan di antara kelimanya `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, `bravo servis mekanik {runId}`, `Echo Servis Perkasa {runId}`, karena jumlah nilai dikurangi 2 (minimum 0) adalah kunci utama, dan Brands kosong ada di akhir saat ascending
55. Baca daftar Service Center client suite dengan pencarian `{runId}` dan sort Brands Z-A
56. Verifikasi `bravo servis mekanik {runId}` dan `Echo Servis Perkasa {runId}` berada sebelum `Delta Servis Terpadu {runId}`, `Alfa Servis Teknik {runId}`, dan `Charlie Kalibrasi Pratama {runId}`, dan `Delta Servis Terpadu {runId}` berada sebelum `Alfa Servis Teknik {runId}` dan `Charlie Kalibrasi Pratama {runId}`, karena Brands kosong ada di awal saat descending
57. Baca daftar Service Center client suite dengan pencarian `{runId}` dan sort Status A-Z
58. Verifikasi `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, dan `Echo Servis Perkasa {runId}` berada sebelum `bravo servis mekanik {runId}`, karena `Active` sebelum `Inactive`
59. Baca daftar Service Center client suite dengan pencarian `{runId}` dan sort Status Z-A
60. Verifikasi `bravo servis mekanik {runId}` berada sebelum `Alfa Servis Teknik {runId}`, `Charlie Kalibrasi Pratama {runId}`, `Delta Servis Terpadu {runId}`, dan `Echo Servis Perkasa {runId}`
61. Baca halaman pertama dan halaman kedua daftar Service Center client suite dengan pencarian `{runId}`, sort Service Type A-Z, dan ukuran halaman 10
62. Verifikasi setiap Service Center muncul tepat sekali di antara kedua halaman dan urutan keduanya sama dengan urutan sort Service Type A-Z pada pembacaan tanpa pagination

### Download memuat isi sel per tipe kolom, mengikuti filter dan sort, dan seluruh baris bukan satu halaman
63. Unduh daftar Service Center sebagai CSV dengan pencarian `Delta Servis Terpadu {runId}`
64. Verifikasi berkas berenkode UTF-8 dengan BOM dan bernama `Service-Centers`
65. Verifikasi baris pertama berkas memuat header `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, dan `Last Updated`
66. Verifikasi berkas memuat tepat satu baris data dengan Name `Delta Servis Terpadu {runId}`
67. Verifikasi sel Service Type baris itu `Routine`
68. Verifikasi sel Specialization baris itu memuat seluruh item tanpa pemotongan `+N more`, yaitu `Elektronik {runId} > AC {runId}, Genset {runId}, Kendaraan {runId}`, dengan hierarki penuh dari akar
69. Verifikasi sel Available To baris itu `Cabang Bekasi {runId}, Region Jawa {runId} > Cabang Malang {runId}, Region Jawa {runId} > Cabang Surabaya {runId}`
70. Verifikasi sel Brands baris itu `Daikin {runId}, LG {runId}, Panasonic {runId}`, tanpa hierarki
71. Verifikasi sel Usage baris itu `0`
72. Verifikasi sel Status baris itu `Active`, tanpa warna badge
73. Verifikasi sel Modified By baris itu nama lengkap utuh `Rina Wulandari {runId}`, bukan format tampilan `[First Name] [Last Initial]`
74. Unduh daftar Service Center sebagai CSV dengan pencarian `Alfa Servis Teknik {runId}`
75. Verifikasi sel Service Type baris itu `Repair, Routine`, dipisah koma dan spasi
76. Unduh daftar Service Center sebagai CSV dengan pencarian `bravo servis mekanik {runId}`
77. Verifikasi sel Specialization baris itu `Kendaraan {runId}`, sel Brands baris itu `-`, dan sel Status baris itu `Inactive`
78. Unduh daftar Service Center sebagai CSV dengan pencarian `Charlie Kalibrasi Pratama {runId}`
79. Verifikasi sel Specialization baris itu `-`, karena nilai kosong ditulis hyphen tunggal, bukan `All categories`
80. Unduh daftar Service Center sebagai XLSX dengan pencarian `Delta Servis Terpadu {runId}`
81. Verifikasi berkas bernama `Service-Centers`, memuat satu sheet bernama `Sheet1`, dan sel Usage baris itu berupa angka `0`, bukan teks
82. Unduh daftar Service Center sebagai CSV dengan pencarian `{runId}`, filter Status `Active`, dan sort Name Z-A
83. Verifikasi berkas memuat `Echo Servis Perkasa {runId}`, `Delta Servis Terpadu {runId}`, `Charlie Kalibrasi Pratama {runId}`, dan `Alfa Servis Teknik {runId}` dalam urutan itu dan tidak memuat `bravo servis mekanik {runId}`, karena berkas mengikuti filter dan sort aktif
84. Unduh daftar Service Center sebagai CSV dengan pencarian `zzqx077`
85. Verifikasi berkas hanya memuat baris header kolom yang tampil, tanpa baris data
86. Baca daftar Service Center client suite dengan pencarian `Servis Massal` dan ukuran halaman 10
87. Verifikasi halaman pertama memuat 10 Service Center dan total hasil adalah 12
88. Unduh daftar Service Center sebagai CSV dengan pencarian `Servis Massal` dan ukuran halaman 10
89. Verifikasi berkas memuat 12 baris data, yaitu seluruh hasil pencarian dan bukan hanya halaman yang tampil

### Filter Specialization menyertakan Service Center ber-Specialization induk dari node terpilih
90. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Specialization `AC {runId}`
91. Verifikasi hasil memuat `Foxtrot Servis Elektronik {runId}`, karena `Elektronik {runId}` adalah induk dari `AC {runId}` dan Service Center cocok bila node Specialization miliknya merupakan ancestor dari node terpilih
92. Baca seluruh halaman hasil daftar Service Center client suite dengan filter Specialization `Genset {runId}`
93. Verifikasi hasil memuat `Delta Servis Terpadu {runId}` dan tidak memuat `Foxtrot Servis Elektronik {runId}`, karena `Elektronik {runId}` bukan induk dan bukan turunan dari `Genset {runId}` dan Specialization-nya tidak kosong
