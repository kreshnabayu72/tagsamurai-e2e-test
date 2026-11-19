---
id: TC-FA-FASVC-BE-068-be-validasi-alamat-dan-kontak
title: "Server: Validasi Alamat, Country, Kontak Perusahaan, dan Contact Persons"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["V-FASVC-06", "V-FASVC-07", "V-FASVC-09", "V-FASVC-11", "V-FASVC-16", "V-FASVC-18", "V-FASVC-19", "V-FASVC-23", "V-FASVC-24", "V-FASVC-25", "V-FASVC-27", "V-FASVC-28", "V-FASVC-29", "V-FASVC-33", "V-FASVC-34", "V-FASVC-35", "FLD-FASVC-06", "FLD-FASVC-07", "FLD-FASVC-08", "FLD-FASVC-09", "FLD-FASVC-10", "FLD-FASVC-11", "FLD-FASVC-12", "FLD-FASVC-13", "FLD-FASVC-14", "FLD-FASVC-15", "FLD-FASVC-16", "FLD-FASVC-17", "FASVC-LOGIC-02o", "FASVC-LOGIC-02p", "EC-FASVC-18", "EC-FASVC-19", "EC-FASVC-55", "EC-FASVC-54", "F-FASVC-02.k8", "F-FASVC-02.k15", "F-FASVC-02.k16", "EB-FRM-4@province-state", "EB-FRM-4@city", "EB-FRM-4@postal-code", "EB-FRM-4@address-line", "EB-FRM-4@notes", "EB-FRM-4@company-email", "EB-FRM-4@contact-name", "EB-FRM-4@contact-email"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-06": [9]
  "V-FASVC-07": [11, 97]
  "V-FASVC-09": [18, 20]
  "V-FASVC-11": [28, 30, 64]
  "V-FASVC-16": [41, 45, 77]
  "V-FASVC-18": [34, 68]
  "V-FASVC-19": [32, 36, 66]
  "V-FASVC-23": [3]
  "V-FASVC-24": [26, 63]
  "V-FASVC-25": [16]
  "V-FASVC-27": [7, 85, 95]
  "V-FASVC-28": [24, 62]
  "V-FASVC-29": [22, 61]
  "V-FASVC-33": [5]
  "V-FASVC-34": [50, 54, 69]
  "V-FASVC-35": [52, 56, 67, 108, 110, 115, 117, 119]
  "FLD-FASVC-06": [5, 16, 75]
  "FLD-FASVC-07": [22, 61]
  "FLD-FASVC-08": [3, 24, 62, 90]
  "FLD-FASVC-09": [26, 63]
  "FLD-FASVC-10": [28, 64]
  "FLD-FASVC-11": [7, 50, 52, 67, 73, 108, 112]
  "FLD-FASVC-12": [7, 18, 32, 66]
  "FLD-FASVC-13": [41, 70, 74]
  "FLD-FASVC-14": [9, 34, 68]
  "FLD-FASVC-15": [11, 54, 56, 69, 110, 113]
  "FLD-FASVC-16": [11, 20, 36, 68]
  "FLD-FASVC-17": [30, 65]
  "FASVC-LOGIC-02o": [13, 38, 58]
  "FASVC-LOGIC-02p": [43, 45, 47, 70, 77, 83]
  "EC-FASVC-18": [7, 11, 85]
  "EC-FASVC-19": [73]
  "EC-FASVC-55": [74]
  "EC-FASVC-54": [80, 83]
  "F-FASVC-02.k8": [7, 11, 85, 87, 95, 97, 99, 101, 103]
  "F-FASVC-02.k15": [75, 90]
  "F-FASVC-02.k16": [74, 80, 83]
  "EB-FRM-4@province-state": [22, 61]
  "EB-FRM-4@city": [24, 62]
  "EB-FRM-4@postal-code": [26, 63]
  "EB-FRM-4@address-line": [28, 64]
  "EB-FRM-4@notes": [30, 65]
  "EB-FRM-4@company-email": [32, 66]
  "EB-FRM-4@contact-name": [34, 68]
  "EB-FRM-4@contact-email": [36, 68]
anchor: []
---

# Server: Validasi Alamat, Country, Kontak Perusahaan, dan Contact Persons

## Prerequisites
- Aktor: Total Control pada client suite.
- Data:
  - DU-068-1: Service Center `CV Genset Prima {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company phone Dial Code `+62` dan nomor `8123456789`, Company email `servis@gensetprima.co.id`, Contact persons `Dewi Anggraini` (Primary, `dewi.anggraini@gensetprima.co.id`) dan `Budi Santoso` (`budi.santoso@gensetprima.co.id`), Status `Active`, ada di client suite.
  - Setiap Create yang dikirim memuat field wajib lain bernilai Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `kontak@gensetprima.co.id`, kecuali yang disebut di langkah; Name dikirim sesuai langkah.
  - Setiap Edit yang dikirim memuat versi data terkini dan nilai tersimpan untuk semua field selain yang disebut di langkah.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.

## Test Steps
### Field wajib kosong ditolak
1. Baca daftar Service Center client suite dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N0
2. Kirim Create dengan Name `Sinar Teknik Utama {runId}` dan City dikosongkan
3. Verifikasi permintaan ditolak dengan pesan `City must not be empty`
4. Kirim Create dengan Name `Mitra Servis Prima {runId}` dan Country dikosongkan
5. Verifikasi permintaan ditolak dengan pesan `Country must not be empty`
6. Kirim Create dengan Name `Karya Mandiri Teknik {runId}`, Company email dikosongkan, dan tanpa Company phone
7. Verifikasi permintaan ditolak dengan pesan `Add a company phone or email`
8. Kirim Create dengan Name `Bintang Servis Abadi {runId}` dan satu Contact person Primary dengan Contact email `budi.santoso@gensetprima.co.id` dan Contact name dikosongkan
9. Verifikasi permintaan ditolak dengan pesan `Contact name must not be empty`
10. Kirim Create dengan Name `Citra Kalibrasi Nusantara {runId}` dan satu Contact person `Agus Wijaya` (Primary) tanpa Phone dan tanpa Email
11. Verifikasi permintaan ditolak dengan pesan `Add a phone or email`
12. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
13. Verifikasi jumlah baris tetap N0, sehingga kelima permintaan tidak membuat Service Center

### Country di luar daftar, format email, dan batas panjang teks ditolak
14. Baca daftar Service Center client suite dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N1
15. Kirim Create dengan Name `Garuda Pendingin Servis {runId}` dan Country `Atlantis`
16. Verifikasi permintaan ditolak dengan pesan `Select a valid country`
17. Kirim Create dengan Name `Tirta Mesin Sejahtera {runId}` dan Company email `kontak.gensetprima.co.id`
18. Verifikasi permintaan ditolak dengan pesan `Enter a valid email`
19. Kirim Create dengan Name `Sumber Daya Teknik {runId}` dan satu Contact person `Dewi Anggraini` (Primary) dengan Contact email `dewi@gensetprima.c`
20. Verifikasi permintaan ditolak dengan pesan `Enter a valid email`
21. Kirim Create dengan Name `Bumi Perkasa Servis {runId}` dan Province / State `Kecamatan Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Depok Tegal Solab` (121 karakter)
22. Verifikasi permintaan ditolak dengan pesan `Max. 120 characters`
23. Kirim Create dengan Name `Laksana Teknik Mandiri {runId}` dan City `Kota Administrasi Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Pasuruaab` (121 karakter)
24. Verifikasi permintaan ditolak dengan pesan `Max. 120 characters`
25. Kirim Create dengan Name `Prima Dinamika Servis {runId}` dan Postal code `Kode Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Depok Bekasi Pasuruaab` (121 karakter)
26. Verifikasi permintaan ditolak dengan pesan `Max. 120 characters`
27. Kirim Create dengan Name `Cahaya Mesin Industri {runId}` dan Address line `Jalan Raya Industri Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Pergudangan Terpadu Utara Selatan Barat Timur Pusat Lantai Gedung Ruko Sentra Niaga Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Pergudangan Terpadu Utara Selatan Barat Timur Pusat Lantai Gedung Ruko Sentra Niaga Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Utara Rukab` (361 karakter)
28. Verifikasi permintaan ditolak dengan pesan `Max. 360 characters`
29. Kirim Create dengan Name `Nusa Karya Perawatan {runId}` dan Notes `Vendor resmi Vendor servis resmi untuk genset pendingin ruangan kompresor dan panel listrik dengan jadwal kunjungan bulanan serta layanan darurat di luar jam kerja tersedia melalui kontak utama Vendor servis resmi untuk genset pendingin ruangan kompresor dan panel listrik dengan jadwal kunjungan bulanan serta layanan darurat di luar jam kerja tersedia kontaab` (361 karakter)
30. Verifikasi permintaan ditolak dengan pesan `Max. 360 characters`
31. Kirim Create dengan Name `Tunas Baru Teknik {runId}` dan Company email `kontak1@layanan-layanan-servis-terpadu-nusantara-wilayah-pusat.kalibrasi-genset-industri-mandiri-servis-pusat-pusat.co.id` (121 karakter)
32. Verifikasi permintaan ditolak dengan pesan `Max. 120 characters`
33. Kirim Create dengan Name `Mega Servis Konstruksi {runId}` dan satu Contact person Primary dengan Contact name `Dewi Anggraini Putri Maharani Budi Santoso Siti Nur Rahmawati Agus Wijaya Rina Wulandari Hendra Kusuma Eka Pratama Putrab` (121 karakter) dan Contact email `budi.santoso@gensetprima.co.id`
34. Verifikasi permintaan ditolak dengan pesan `Max. 120 characters`
35. Kirim Create dengan Name `Surya Teknik Elektrik {runId}` dan satu Contact person `Siti Rahmawati` (Primary) dengan Contact email `kontak1@pusat-layanan-servis-terpadu-nusantara-wilayah-pusat.kalibrasi-genset-industri-mandiri-layanan-servis-pusat.co.id` (121 karakter)
36. Verifikasi permintaan ditolak dengan pesan `Max. 120 characters`
37. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
38. Verifikasi jumlah baris tetap N1, sehingga kesebelas permintaan tidak membuat Service Center

### Contact persons lebih dari 3 baris atau tanpa tepat satu Primary ditolak
39. Baca daftar Service Center client suite dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N2
40. Kirim Create dengan Name `Harapan Jaya Mekanik {runId}` dan empat Contact persons: Dewi Anggraini (Primary, dewi.anggraini@gensetprima.co.id); Budi Santoso (budi.santoso@gensetprima.co.id); Siti Rahmawati (siti.rahmawati@gensetprima.co.id); Agus Wijaya (agus.wijaya@gensetprima.co.id)
41. Verifikasi permintaan ditolak dengan pesan `Up to 3 contact persons, with one primary.`
42. Kirim Create dengan Name `Mulia Abadi Perkakas {runId}` dan tiga Contact persons tanpa Primary: Dewi Anggraini (dewi.anggraini@gensetprima.co.id); Budi Santoso (budi.santoso@gensetprima.co.id); Siti Rahmawati (siti.rahmawati@gensetprima.co.id)
43. Verifikasi permintaan ditolak dengan pesan `Up to 3 contact persons, with one primary.`
44. Kirim Create dengan Name `Sentral Montir Prima {runId}` dan dua Contact persons yang keduanya Primary: Dewi Anggraini (Primary, dewi.anggraini@gensetprima.co.id); Budi Santoso (Primary, budi.santoso@gensetprima.co.id)
45. Verifikasi permintaan ditolak dengan pesan `Up to 3 contact persons, with one primary.`
46. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
47. Verifikasi jumlah baris tetap N2, sehingga ketiga permintaan tidak membuat Service Center

### Nomor telepon kurang dari 4 digit atau lebih dari 15 digit ditolak
48. Baca daftar Service Center client suite dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N3
49. Kirim Create dengan Name `Jaya Utama Refrigerasi {runId}` dan Company phone dengan Dial Code `+62` dan nomor `812` (3 digit)
50. Verifikasi permintaan ditolak dengan pesan `Min. 4 characters`
51. Kirim Create dengan Name `Teknik Sejuk Perkasa {runId}` dan Company phone dengan Dial Code `+62` dan nomor `8123456789012345` (16 digit)
52. Verifikasi permintaan ditolak dengan pesan `Max. 15 characters`
53. Kirim Create dengan Name `Anugerah Tekno Servis {runId}` dan satu Contact person `Dewi Anggraini` (Primary) dengan Contact phone Dial Code `+62` dan nomor `812` (3 digit)
54. Verifikasi permintaan ditolak dengan pesan `Min. 4 characters`
55. Kirim Create dengan Name `Bahari Mesin Teknik {runId}` dan satu Contact person `Budi Santoso` (Primary) dengan Contact phone Dial Code `+62` dan nomor `8123456789012345` (16 digit)
56. Verifikasi permintaan ditolak dengan pesan `Max. 15 characters`
57. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
58. Verifikasi jumlah baris tetap N3, sehingga keempat permintaan tidak membuat Service Center

### Create dengan semua isian tepat di batas diterima
59. Kirim Create dengan Name `Pusat Servis Batas Isian {runId}`, Province / State `Kecamatan Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Depok Tegal Solo` (120 karakter), City `Kota Administrasi Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Pasuruan` (120 karakter), Postal code `Kode Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Depok Bekasi Pasuruan` (120 karakter), Address line `Jalan Raya Industri Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Pergudangan Terpadu Utara Selatan Barat Timur Pusat Lantai Gedung Ruko Sentra Niaga Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Pergudangan Terpadu Utara Selatan Barat Timur Pusat Lantai Gedung Ruko Sentra Niaga Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Utara Ruko` (360 karakter), Notes `Vendor resmi Vendor servis resmi untuk genset pendingin ruangan kompresor dan panel listrik dengan jadwal kunjungan bulanan serta layanan darurat di luar jam kerja tersedia melalui kontak utama Vendor servis resmi untuk genset pendingin ruangan kompresor dan panel listrik dengan jadwal kunjungan bulanan serta layanan darurat di luar jam kerja tersedia kontak` (360 karakter), Company email `kontak@layanan-layanan-servis-terpadu-nusantara-wilayah-pusat.kalibrasi-genset-industri-mandiri-servis-pusat-pusat.co.id` (120 karakter), Company phone dengan Dial Code `+62` dan nomor `812345678901234` (15 digit), dan tiga Contact persons: `Dewi Anggraini Putri Maharani Budi Santoso Siti Nur Rahmawati Agus Wijaya Rina Wulandari Hendra Kusuma Eka Pratama Putri` (120 karakter) sebagai Primary dengan email `kontak@pusat-layanan-servis-terpadu-nusantara-wilayah-pusat.kalibrasi-genset-industri-mandiri-layanan-servis-pusat.co.id` (120 karakter), `Budi Santoso` dengan Phone Dial Code `+62` dan nomor `8123`, dan `Siti Rahmawati` dengan email `siti.rahmawati@gensetprima.co.id`
60. Baca daftar Service Center client suite dengan pencarian `Pusat Servis Batas Isian {runId}`
61. Verifikasi Province / State tersimpan utuh `Kecamatan Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Depok Tegal Solo`
62. Verifikasi City tersimpan utuh `Kota Administrasi Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Pasuruan`
63. Verifikasi Postal code tersimpan utuh `Kode Jawa Barat Timur Tengah Utara Selatan Kota Raya Baru Lama Bandung Medan Surabaya Malang Bogor Depok Bekasi Pasuruan`
64. Verifikasi Address line tersimpan utuh `Jalan Raya Industri Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Pergudangan Terpadu Utara Selatan Barat Timur Pusat Lantai Gedung Ruko Sentra Niaga Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Pergudangan Terpadu Utara Selatan Barat Timur Pusat Lantai Gedung Ruko Sentra Niaga Jalan Raya Industri Nomor Kawasan Blok Gudang Komplek Utara Ruko`
65. Verifikasi Notes tersimpan utuh `Vendor resmi Vendor servis resmi untuk genset pendingin ruangan kompresor dan panel listrik dengan jadwal kunjungan bulanan serta layanan darurat di luar jam kerja tersedia melalui kontak utama Vendor servis resmi untuk genset pendingin ruangan kompresor dan panel listrik dengan jadwal kunjungan bulanan serta layanan darurat di luar jam kerja tersedia kontak`
66. Verifikasi Company email tersimpan utuh `kontak@layanan-layanan-servis-terpadu-nusantara-wilayah-pusat.kalibrasi-genset-industri-mandiri-servis-pusat-pusat.co.id`
67. Verifikasi Company phone tersimpan dengan Dial Code `+62` dan nomor `812345678901234`, karena batas 15 karakter dihitung pada nomor tanpa Dial Code
68. Verifikasi Contact person pertama tersimpan sebagai Primary dengan nama `Dewi Anggraini Putri Maharani Budi Santoso Siti Nur Rahmawati Agus Wijaya Rina Wulandari Hendra Kusuma Eka Pratama Putri` dan email `kontak@pusat-layanan-servis-terpadu-nusantara-wilayah-pusat.kalibrasi-genset-industri-mandiri-layanan-servis-pusat.co.id`
69. Verifikasi Contact person `Budi Santoso` tersimpan dengan Phone Dial Code `+62` dan nomor `8123`
70. Verifikasi tiga Contact persons tersimpan dengan tepat satu Primary

### Vendor luar negeri tanpa Contact persons dengan nomor internasional diterima
71. Kirim Create dengan Name `Singa Teknik Servis {runId}`, Country `Singapore`, City `Singapore`, Company phone dengan Dial Code `+65` dan nomor `61234567`, tanpa Company email, dan tanpa Contact persons
72. Baca daftar Service Center client suite dengan pencarian `Singa Teknik Servis {runId}`
73. Verifikasi Company phone tersimpan dengan Dial Code `+65` dan nomor `61234567`
74. Verifikasi Service Center tersimpan tanpa Contact persons dan tanpa Company email, karena Company phone saja sudah memenuhi kontak perusahaan
75. Verifikasi Country tersimpan `Singapore` dan City tersimpan `Singapore`

### Edit Contact persons dan kontak perusahaan
76. Kirim Edit atas `CV Genset Prima {runId}` dengan Primary `Dewi Anggraini` dihapus dan sisa baris `Budi Santoso` tidak ditandai Primary
77. Verifikasi permintaan ditolak dengan pesan `Up to 3 contact persons, with one primary.`
78. Kirim Edit atas `CV Genset Prima {runId}` dengan Primary `Dewi Anggraini` dihapus dan sisa baris `Budi Santoso` ditandai Primary
79. Baca Service Center `CV Genset Prima {runId}` dari daftar dengan pencarian `CV Genset Prima {runId}`
80. Verifikasi Contact persons tersimpan hanya `Budi Santoso` sebagai Primary
81. Kirim Edit atas `CV Genset Prima {runId}` dengan seluruh Contact persons dihapus sehingga jumlahnya `0`
82. Baca ulang Service Center `CV Genset Prima {runId}` dari daftar dengan pencarian `CV Genset Prima {runId}`
83. Verifikasi Service Center tersimpan tanpa Contact persons dan tanpa Primary
84. Kirim Edit atas `CV Genset Prima {runId}` dengan Company phone dan Company email sama-sama dikosongkan
85. Verifikasi permintaan ditolak dengan pesan `Add a company phone or email`
86. Baca ulang Service Center `CV Genset Prima {runId}` dari daftar dengan pencarian `CV Genset Prima {runId}`
87. Verifikasi Company phone tersimpan tetap Dial Code `+62` dan nomor `8123456789`, dan Company email tersimpan tetap `servis@gensetprima.co.id`
88. Kirim Edit atas `CV Genset Prima {runId}` dengan City diganti `Jaksel`
89. Baca ulang Service Center `CV Genset Prima {runId}` dari daftar dengan pencarian `CV Genset Prima {runId}`
90. Verifikasi City tersimpan apa adanya `Jaksel`

### Penolakan kontak tidak lengkap tidak menulis log
91. Baca jumlah entri Changelog yang menyebut Service Center `CV Genset Prima {runId}` dan catat sebagai LC
92. Baca jumlah entri Activity Log yang menyebut Service Center `CV Genset Prima {runId}` dan catat sebagai LA
93. Baca jumlah entri System Log yang menyebut Service Center `CV Genset Prima {runId}` dan catat sebagai LS
94. Kirim Edit atas `CV Genset Prima {runId}` dengan Company phone dan Company email sama-sama dikosongkan
95. Verifikasi permintaan ditolak dengan pesan `Add a company phone or email`
96. Kirim Edit atas `CV Genset Prima {runId}` dengan satu Contact person `Agus Wijaya` (Primary) tanpa Phone dan tanpa Email
97. Verifikasi permintaan ditolak dengan pesan `Add a phone or email`
98. Baca ulang jumlah entri Changelog yang menyebut Service Center `CV Genset Prima {runId}`
99. Verifikasi jumlah entri Changelog tetap LC, sehingga kedua penolakan tidak menulis Changelog
100. Baca ulang jumlah entri Activity Log yang menyebut Service Center `CV Genset Prima {runId}`
101. Verifikasi jumlah entri Activity Log tetap LA, sehingga kedua penolakan tidak menulis Activity Log
102. Baca ulang jumlah entri System Log yang menyebut Service Center `CV Genset Prima {runId}`
103. Verifikasi jumlah entri System Log tetap LS, sehingga kedua penolakan tidak menulis System Log

### Nomor lebih dari 15 digit lewat permintaan langsung ditolak tanpa mengubah data dan tanpa log
104. Baca jumlah entri Changelog yang menyebut Service Center `CV Genset Prima {runId}` dan catat sebagai LC2
105. Baca jumlah entri Activity Log yang menyebut Service Center `CV Genset Prima {runId}` dan catat sebagai LA2
106. Baca jumlah entri System Log yang menyebut Service Center `CV Genset Prima {runId}` dan catat sebagai LS2
107. Kirim Edit atas `CV Genset Prima {runId}` dengan Company phone Dial Code `+62` dan nomor `8123456789012345` (16 digit)
108. Verifikasi permintaan ditolak dengan pesan `Max. 15 characters`
109. Kirim Edit atas `CV Genset Prima {runId}` dengan satu Contact person `Agus Wijaya` (Primary) dengan Contact email `agus.wijaya@gensetprima.co.id` dan Contact phone Dial Code `+62` dan nomor `8123456789012345` (16 digit)
110. Verifikasi permintaan ditolak dengan pesan `Max. 15 characters`
111. Baca ulang Service Center `CV Genset Prima {runId}` dari daftar dengan pencarian `CV Genset Prima {runId}`
112. Verifikasi Company phone tersimpan tetap Dial Code `+62` dan nomor `8123456789`, sehingga penolakan nomor 16 digit tidak mengubah data
113. Verifikasi Service Center tersimpan tetap tanpa Contact persons, sehingga penolakan Contact phone 16 digit tidak menambah Contact person
114. Baca ulang jumlah entri Changelog yang menyebut Service Center `CV Genset Prima {runId}`
115. Verifikasi jumlah entri Changelog tetap LC2, sehingga kedua penolakan nomor 16 digit tidak menulis Changelog
116. Baca ulang jumlah entri Activity Log yang menyebut Service Center `CV Genset Prima {runId}`
117. Verifikasi jumlah entri Activity Log tetap LA2, sehingga kedua penolakan nomor 16 digit tidak menulis Activity Log
118. Baca ulang jumlah entri System Log yang menyebut Service Center `CV Genset Prima {runId}`
119. Verifikasi jumlah entri System Log tetap LS2, sehingga kedua penolakan nomor 16 digit tidak menulis System Log
