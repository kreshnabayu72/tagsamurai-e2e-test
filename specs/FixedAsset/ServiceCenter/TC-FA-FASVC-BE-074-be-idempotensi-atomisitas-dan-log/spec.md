---
id: TC-FA-FASVC-BE-074-be-idempotensi-atomisitas-dan-log
title: "Server: Idempoten, Atomik, No-Op, Guard Create, dan Pencatatan Log Satu Transaksi"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["RS-FASVC-01a", "RS-FASVC-01b", "RS-FASVC-01c", "RS-FASVC-02a", "RS-FASVC-03", "RS-FASVC-04", "RS-FASVC-07", "RS-FASVC-08", "RS-FASVC-05b", "§9.6#r1", "§9.6#r2", "§9.6#r5", "§9.6#p4", "§Dependencies#b13", "EC-FASVC-33c", "EC-FASVC-36c", "EC-FASVC-37", "FASVC-LOGIC-09b", "EB-EDG-1", "EB-EDG-3", "EB-ERR-4", "RS-FASVC-02b", "RS-FASVC-02c", "RS-FASVC-02d"]
smoke: []
dependsOn: []
trace:
  "RS-FASVC-01a": [12]
  "RS-FASVC-01b": [4, 8]
  "RS-FASVC-01c": [14]
  "RS-FASVC-02a": [19, 175, 177, 178, 36, 103, 105, 107, 109, 111, 113]
  "RS-FASVC-03": [165, 170, 46, 50, 52, 55, 60, 122, 124, 126, 128, 130, 132, 142, 144, 146, 148, 150, 152]
  "RS-FASVC-04": [63, 66, 68]
  "RS-FASVC-07": [75, 81]
  "RS-FASVC-08": [89, 91]
  "RS-FASVC-05b": [95, 97]
  "§9.6#r1": [6, 8, 10, 156, 158, 160]
  "§9.6#r2": [19, 175, 177, 178, 28, 30, 32, 103, 105, 107, 109, 111]
  "§9.6#r5": [95, 97]
  "§9.6#p4": [19, 50, 52, 55, 60, 111, 122, 124, 126, 128, 130, 132, 142, 144, 146, 148, 150, 152]
  "§Dependencies#b13": [6, 28, 43, 46, 63]
  "EC-FASVC-33c": [21, 23, 25]
  "EC-FASVC-36c": [12, 14]
  "EC-FASVC-37": [85]
  "FASVC-LOGIC-09b": [75, 77, 79]
  "EB-EDG-1": [12, 19, 50, 66]
  "EB-EDG-3": [73, 77, 79]
  "EB-ERR-4": [38, 40]
  "RS-FASVC-02b": [19, 103, 175]
  "RS-FASVC-02c": [111]
  "RS-FASVC-02d": [21, 23, 25, 105, 107, 109]
anchor: []
---

# Server: Idempoten, Atomik, No-Op, Guard Create, dan Pencatatan Log Satu Transaksi

## Prerequisites
- Aktor: Total Control `Dewi Anggraini {runId}` pada client suite.
- Data:
  - DU-074-1: User `Dewi Anggraini {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group.
  - DU-074-2: Group `Cabang Surabaya {runId}`, anak langsung root pohon Group, ada di client suite.
  - DU-074-3: Group `Cabang Malang {runId}`, anak langsung root pohon Group, ada di client suite.
  - DU-074-4: Category `Generator {runId}`, ada di client suite.
  - DU-074-5: Brand `LG {runId}`, ada di client suite.
  - DU-074-6: Service Center `PT Sejuk Abadi Teknik {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `kontak@log074.co.id`, Status `Active`, ada di client suite.
  - DU-074-7: Service Center `Bengkel Maju Motor {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Bandung`, Company email `kontak@log074.co.id`, Status `Active`, ada di client suite.
  - DU-074-8: Service Center `CV Genset Prima {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@log074.co.id`, Status `Active`, ada di client suite.
  - DU-074-9: Service Center `Servis Elektrik Surabaya Malang {runId}`, Service type `Routine`, Available to `Cabang Surabaya {runId}` dan `Cabang Malang {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@log074.co.id`, Status `Active`, ada di client suite.
  - DU-074-10: Service Center `Servis Genset Spesialis {runId}`, Service type `Routine`, Available to `All groups`, Specialization `Generator {runId}`, Country `Indonesia`, City `Bogor`, Company email `kontak@log074.co.id`, Status `Active`, ada di client suite.
  - DU-074-11: Service Center `Servis Pendingin Merek {runId}`, Service type `Repair`, Available to `All groups`, Brands `LG {runId}`, Country `Indonesia`, City `Medan`, Company email `kontak@log074.co.id`, Status `Active`, ada di client suite.
  - DU-074-12: Service Center `UD Cahaya Servis {runId}`, Service type `Repair`, Available to kosong, Country `Indonesia`, City `Malang`, Company email `kontak@log074.co.id`, Status `Inactive`, ada di client suite.
  - DU-074-26: Service Center `Servis Chiller Terjadwal {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Tangerang`, Company email `kontak@log074.co.id`, Status `Active`, ada di client suite.
  - DU-074-27: Schedule Maintenance Routine `Servis Chiller Bulanan {runId}` berstatus `Active` dengan pelaksana default `Servis Chiller Terjadwal {runId}`.
  - DU-074-28: User `Bagus Prakoso {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group.
  - DU-074-29: Service Center `Teknik Pendingin Nusantara {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Semarang`, Company email `kontak@log074.co.id`, Status `Active`, ada di client suite.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.

## Test Steps
### Create menambah record dan log, tidak idempoten, dan dijaga keunikan Name
1. Baca System Log Detail User `Dewi Anggraini {runId}` dan catat jumlah entri Action `Created` sebagai S0
2. `Dewi Anggraini {runId}` mengirim Create dengan Name `Sentral Servis Terpadu {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `kontak@log074.co.id`
3. Baca daftar Service Center client suite dengan pencarian `Sentral Servis Terpadu {runId}`
4. Verifikasi hasil memuat tepat satu Service Center bernama `Sentral Servis Terpadu {runId}`
5. Baca Changelog Service Center dengan Service Center Name `Sentral Servis Terpadu {runId}`
6. Verifikasi Changelog memuat entri Action `Created` dengan Old Value `—` dan New Value nilai field yang dikirim
7. Baca Activity Log dengan Object `Service Center` dan Name `Sentral Servis Terpadu {runId}`
8. Verifikasi Activity Log memuat entri Action `Created`
9. Baca ulang System Log Detail User `Dewi Anggraini {runId}`
10. Verifikasi jumlah entri Action `Created` bertambah satu dari S0
11. `Dewi Anggraini {runId}` mengirim ulang Create yang sama persis, seolah respons permintaan pertama tidak pernah diterima
12. Verifikasi permintaan kedua ditolak dengan pesan `Name already exists`, sehingga Create tidak idempoten
13. Baca ulang daftar Service Center client suite dengan pencarian `Sentral Servis Terpadu {runId}`
14. Verifikasi hasil tetap memuat tepat satu Service Center bernama `Sentral Servis Terpadu {runId}`, karena keunikan Name mencegah duplikat

### Edit tanpa perubahan idempoten dan tidak menulis log
15. Baca Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}` dan catat jumlah entrinya sebagai L0
16. Baca Activity Log dengan Object `Service Center` dan Name `PT Sejuk Abadi Teknik {runId}` dan catat jumlah entrinya sebagai A0
17. Baca System Log Detail User `Dewi Anggraini {runId}` dan catat jumlah entri Action `Updated` sebagai S1
18. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan semua nilai sama dengan nilai tersimpan, termasuk City `Jakarta Selatan`
19. Verifikasi Edit diterima dengan sukses sebagai No-Op dengan pesan `No changes to save.`
20. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
21. Verifikasi jumlah entri Changelog tetap L0
22. Baca ulang Activity Log dengan Object `Service Center` dan Name `PT Sejuk Abadi Teknik {runId}`
23. Verifikasi jumlah entri Activity Log tetap A0
24. Baca ulang System Log Detail User `Dewi Anggraini {runId}`
25. Verifikasi jumlah entri Action `Updated` tetap S1
26. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
27. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
28. Verifikasi Changelog memuat entri Action `Updated` pada Field `City` dengan Old Value `Jakarta Selatan` dan New Value `Jakarta Pusat`
29. Baca ulang Activity Log dengan Object `Service Center` dan Name `PT Sejuk Abadi Teknik {runId}`
30. Verifikasi Activity Log memuat entri Action `Updated` untuk Edit yang berubah itu
31. Baca ulang System Log Detail User `Dewi Anggraini {runId}`
32. Verifikasi jumlah entri Action `Updated` bertambah satu dari S1
33. Catat jumlah entri Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}` sebagai L1
34. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City `Jakarta Pusat` yang sudah tersimpan
35. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
36. Verifikasi jumlah entri Changelog tetap L1, karena Edit yang mengulang keadaan yang sudah tercapai tidak menulis entri kedua
37. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan Notes diganti `Vendor resmi` dan Company email diganti `kontak.tanpa.at`
38. Verifikasi Edit yang memuat dua perubahan ditolak seluruhnya dengan pesan `Enter a valid email`
39. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
40. Verifikasi Notes tersimpan tetap kosong dan Company email tersimpan tetap `kontak@log074.co.id`, sehingga penolakan tidak mengubah data
41. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan Name diganti `PT Sejuk Abadi Teknik Raya {runId}`
42. Baca Changelog Service Center dengan Field `City` dan Action `Updated`
43. Verifikasi entri Changelog `Updated` pada Field `City` yang lama tetap bernama Service Center `PT Sejuk Abadi Teknik {runId}`, bukan `PT Sejuk Abadi Teknik Raya {runId}`, karena log adalah snapshot saat kejadian

### Inactivate dan Activate yang status tujuannya sudah tercapai adalah No-Op
44. `Dewi Anggraini {runId}` mengirim Inactivate atas `Bengkel Maju Motor {runId}`
45. Baca Changelog Service Center dengan Service Center Name `Bengkel Maju Motor {runId}`
46. Verifikasi Changelog memuat entri Action `Inactivated` pada Field `Status` dengan Old Value `Active` dan New Value `Inactive`
47. Catat jumlah entri Changelog dengan Service Center Name `Bengkel Maju Motor {runId}` sebagai L2, jumlah entri Activity Log dengan Object `Service Center` dan Name `Bengkel Maju Motor {runId}` sebagai A2, dan jumlah entri System Log Detail User `Dewi Anggraini {runId}` dengan Action `Inactivated` sebagai S2
48. `Dewi Anggraini {runId}` membaca `Bengkel Maju Motor {runId}` dan memegang versi datanya
49. `Dewi Anggraini {runId}` mengirim Inactivate atas `Bengkel Maju Motor {runId}` yang sudah `Inactive`
50. Verifikasi permintaan kedua berhasil tanpa kesalahan, karena status tujuan sudah tercapai
51. Baca ulang Changelog dengan Service Center Name `Bengkel Maju Motor {runId}`, Activity Log dengan Object `Service Center` dan Name `Bengkel Maju Motor {runId}`, dan System Log Detail User `Dewi Anggraini {runId}`
52. Verifikasi jumlah entri Changelog tetap L2, Activity Log tetap A2, dan System Log Action `Inactivated` tetap S2
53. `Dewi Anggraini {runId}` mengirim Edit atas `Bengkel Maju Motor {runId}` dengan City diganti `Cimahi` dan versi data yang dibaca sebelum Inactivate kedua
54. Baca `Bengkel Maju Motor {runId}` dari daftar dengan pencarian `Bengkel Maju Motor {runId}`
55. Verifikasi City tersimpan `Cimahi`, sehingga versi data tidak naik karena Inactivate kedua
56. `Dewi Anggraini {runId}` mengirim Activate atas `Bengkel Maju Motor {runId}`
57. Catat jumlah entri Changelog dengan Service Center Name `Bengkel Maju Motor {runId}` sebagai L3 dan jumlah entri System Log Detail User `Dewi Anggraini {runId}` dengan Action `Activated` sebagai S3
58. `Dewi Anggraini {runId}` mengirim Activate atas `Bengkel Maju Motor {runId}` yang sudah `Active`
59. Baca ulang Changelog dengan Service Center Name `Bengkel Maju Motor {runId}` dan System Log Detail User `Dewi Anggraini {runId}`
60. Verifikasi jumlah entri Changelog tetap L3 dan System Log Action `Activated` tetap S3, sehingga Activate kedua tidak menulis log

### Delete diulang tidak menimbulkan efek tambahan
61. `Dewi Anggraini {runId}` mengirim Delete atas `CV Genset Prima {runId}`
62. Baca Changelog Service Center dengan Service Center Name `CV Genset Prima {runId}` dan Action `Deleted`
63. Verifikasi Changelog memuat entri Action `Deleted` dengan New Value `—` dan Old Value nilai terakhir tiap field yang terisi
64. Catat jumlah entri Changelog dengan Service Center Name `CV Genset Prima {runId}` sebagai L4, jumlah entri Activity Log dengan Object `Service Center` dan Name `CV Genset Prima {runId}` sebagai A4, dan jumlah entri System Log Detail User `Dewi Anggraini {runId}` dengan Action `Deleted` sebagai S4
65. `Dewi Anggraini {runId}` mengirim Delete atas `CV Genset Prima {runId}` yang sudah terhapus
66. Verifikasi permintaan kedua ditolak dengan pesan `This service center is no longer available.`
67. Baca ulang Changelog dengan Service Center Name `CV Genset Prima {runId}`, Activity Log dengan Object `Service Center` dan Name `CV Genset Prima {runId}`, dan System Log Detail User `Dewi Anggraini {runId}`
68. Verifikasi jumlah entri Changelog tetap L4, Activity Log tetap A4, dan System Log Action `Deleted` tetap S4

### Perubahan oleh System atas rujukan master yang dihapus dicatat di Changelog dan Activity Log
69. Total Control menghapus `Cabang Malang {runId}` dari master sumber Available to
70. Total Control menghapus `Generator {runId}` dari master sumber Specialization
71. Total Control menghapus `LG {runId}` dari master sumber Brands
72. Baca `Servis Elektrik Surabaya Malang {runId}` dari daftar dengan pencarian `Servis Elektrik Surabaya Malang {runId}`
73. Verifikasi Available to tersimpan `Cabang Surabaya {runId}`, karena `Cabang Malang {runId}` dilepas
74. Baca Changelog Service Center dengan Service Center Name `Servis Elektrik Surabaya Malang {runId}` dan Modified By `System`
75. Verifikasi Changelog memuat tepat satu entri Action `Updated` pada Field `Available to` dengan Old Value memuat `Cabang Malang {runId}` dan `Cabang Surabaya {runId}` dan New Value `Cabang Surabaya {runId}`
76. Baca Changelog Service Center dengan Service Center Name `Servis Genset Spesialis {runId}` dan Modified By `System`
77. Verifikasi Changelog memuat tepat satu entri Action `Updated` pada Field `Specialization` dengan Old Value `Generator {runId}` dan New Value `All categories`
78. Baca Changelog Service Center dengan Service Center Name `Servis Pendingin Merek {runId}` dan Modified By `System`
79. Verifikasi Changelog memuat tepat satu entri Action `Updated` pada Field `Brands` dengan Old Value `LG {runId}` dan New Value `All brands`
80. Baca Activity Log dengan Object `Service Center` dan Name `Servis Elektrik Surabaya Malang {runId}`
81. Verifikasi Activity Log memuat entri Action `Updated` oleh `System` yang ditulis bersama entri Changelog yang sama

### Activate yang ditolak dan Download tidak menulis log
82. Catat jumlah entri Activity Log dengan Object `Service Center` dan Name `UD Cahaya Servis {runId}` sebagai A5 dan jumlah entri System Log Detail User `Dewi Anggraini {runId}` dengan Action `Activated` sebagai S5
83. `Dewi Anggraini {runId}` mengirim Activate atas `UD Cahaya Servis {runId}` yang berstatus `Inactive` dan Available to-nya kosong
84. Baca ulang Activity Log dengan Object `Service Center` dan Name `UD Cahaya Servis {runId}` dan System Log Detail User `Dewi Anggraini {runId}`
85. Verifikasi jumlah entri Activity Log tetap A5 dan System Log Action `Activated` tetap S5, sehingga Activate yang ditolak tidak menulis log
86. Catat jumlah entri Changelog Service Center dengan Service Center Name `Bengkel Maju Motor {runId}` sebagai L5 dan jumlah entri Activity Log dengan Object `Service Center` sebagai A6
87. `Dewi Anggraini {runId}` mengunduh daftar Service Center sebagai CSV dengan pencarian `{runId}`
88. `Dewi Anggraini {runId}` mengunduh daftar yang sama sekali lagi
89. Verifikasi kedua unduhan berhasil menghasilkan berkas
90. Baca ulang Changelog dengan Service Center Name `Bengkel Maju Motor {runId}` dan Activity Log dengan Object `Service Center`
91. Verifikasi jumlah entri Changelog tetap L5 dan Activity Log tetap A6, sehingga Download tidak dicatat

### Lampiran dikomit bersama Activity Log dan System Log milik Create
92. Baca System Log Detail User `Dewi Anggraini {runId}` dan catat jumlah entri Action `Created` sebagai S6
93. `Dewi Anggraini {runId}` mengirim Create dengan Name `Mitra Teknik Lampiran {runId}` dan lampiran `izin-usaha-mitra.pdf` (PDF, 500 KB)
94. Baca Activity Log dengan Object `Service Center` dan Name `Mitra Teknik Lampiran {runId}`
95. Verifikasi Activity Log memuat entri Action `Created` yang ditulis bersama entri `Attachment added` di Changelog
96. Baca ulang System Log Detail User `Dewi Anggraini {runId}`
97. Verifikasi jumlah entri Action `Created` bertambah satu dari S6, dan tidak ada entri terpisah untuk lampiran

### Edit yang mengulang keadaan tersimpan tidak menulis log di semua surface dan tidak menaikkan versi
98. `Dewi Anggraini {runId}` membaca `Bengkel Maju Motor {runId}` dan memegang versi datanya sebagai V0
99. Baca Changelog dengan Service Center Name `Bengkel Maju Motor {runId}` dan catat jumlah entrinya sebagai L6
100. Baca Activity Log dengan Object `Service Center` dan Name `Bengkel Maju Motor {runId}` dan catat jumlah entrinya sebagai A7
101. Baca System Log Detail User `Dewi Anggraini {runId}` dan catat jumlah entri Action `Updated` sebagai S7
102. `Dewi Anggraini {runId}` mengirim Edit atas `Bengkel Maju Motor {runId}` dengan City `Cimahi` yang sudah tersimpan, tanpa perubahan nilai lain
103. Verifikasi Edit diterima dengan sukses sebagai No-Op dengan pesan `No changes to save.`
104. Baca ulang Changelog dengan Service Center Name `Bengkel Maju Motor {runId}`
105. Verifikasi jumlah entri Changelog tetap L6
106. Baca ulang Activity Log dengan Object `Service Center` dan Name `Bengkel Maju Motor {runId}`
107. Verifikasi jumlah entri Activity Log tetap A7
108. Baca ulang System Log Detail User `Dewi Anggraini {runId}`
109. Verifikasi jumlah entri Action `Updated` tetap S7
110. `Dewi Anggraini {runId}` mengirim Edit atas `Bengkel Maju Motor {runId}` dengan Notes diganti `Vendor resmi Cimahi` dan versi data V0 yang dibaca sebelum Edit No-Op
111. Verifikasi Edit diterima tanpa konflik versi, sehingga Edit No-Op tidak menaikkan versi data
112. Baca `Bengkel Maju Motor {runId}` dari daftar dengan pencarian `Bengkel Maju Motor {runId}`
113. Verifikasi Notes tersimpan `Vendor resmi Cimahi`

### Activate yang status tujuannya sudah tercapai dinilai No-Op sebelum versi, tanpa log, tanpa notifikasi ganda, dan tanpa kenaikan versi
114. `Dewi Anggraini {runId}` membaca `Bengkel Maju Motor {runId}` yang berstatus `Active` dan memegang versi datanya sebagai V1
115. `Dewi Anggraini {runId}` mengirim Edit atas `Bengkel Maju Motor {runId}` dengan City diganti `Bandung Barat`, sehingga V1 menjadi usang
116. `Dewi Anggraini {runId}` membaca ulang `Bengkel Maju Motor {runId}` dan memegang versi datanya sebagai V2
117. Baca Changelog dengan Service Center Name `Bengkel Maju Motor {runId}` dan catat jumlah entrinya sebagai L7
118. Baca Activity Log dengan Object `Service Center` dan Name `Bengkel Maju Motor {runId}` dan catat jumlah entrinya sebagai A8
119. Baca System Log Detail User `Dewi Anggraini {runId}` dengan Action `Activated` dan catat jumlah entrinya sebagai S8
120. Baca jumlah notifikasi yang menyebut Service Center `Bengkel Maju Motor {runId}` dan catat sebagai T8
121. `Dewi Anggraini {runId}` mengirim Activate atas `Bengkel Maju Motor {runId}` yang sudah `Active` dengan versi data V1 yang usang
122. Verifikasi permintaan berhasil tanpa konflik versi, karena Activate yang status tujuannya sudah tercapai dinilai No-Op sebelum versi diperiksa
123. Baca ulang Changelog dengan Service Center Name `Bengkel Maju Motor {runId}`
124. Verifikasi jumlah entri Changelog tetap L7
125. Baca ulang Activity Log dengan Object `Service Center` dan Name `Bengkel Maju Motor {runId}`
126. Verifikasi jumlah entri Activity Log tetap A8
127. Baca ulang System Log Detail User `Dewi Anggraini {runId}` dengan Action `Activated`
128. Verifikasi jumlah entri System Log Action `Activated` tetap S8
129. Baca ulang jumlah notifikasi yang menyebut Service Center `Bengkel Maju Motor {runId}`
130. Verifikasi jumlah notifikasi tetap T8, sehingga Activate kedua tidak menimbulkan notifikasi ganda
131. `Dewi Anggraini {runId}` mengirim Edit atas `Bengkel Maju Motor {runId}` dengan Notes diganti `Vendor resmi Bandung Barat` dan versi data V2 yang dibaca sebelum Activate kedua
132. Verifikasi Edit diterima tanpa konflik versi, sehingga Activate kedua tidak menaikkan versi data

### Inactivate yang status tujuannya sudah tercapai dinilai No-Op sebelum versi, tanpa log, tanpa notifikasi ganda, dan tanpa kenaikan versi
133. `Dewi Anggraini {runId}` mengirim Inactivate atas `Bengkel Maju Motor {runId}`
134. `Dewi Anggraini {runId}` membaca `Bengkel Maju Motor {runId}` yang berstatus `Inactive` dan memegang versi datanya sebagai V3
135. `Dewi Anggraini {runId}` mengirim Edit atas `Bengkel Maju Motor {runId}` dengan City diganti `Bandung Timur`, sehingga V3 menjadi usang
136. `Dewi Anggraini {runId}` membaca ulang `Bengkel Maju Motor {runId}` dan memegang versi datanya sebagai V4
137. Baca Changelog dengan Service Center Name `Bengkel Maju Motor {runId}` dan catat jumlah entrinya sebagai L8
138. Baca Activity Log dengan Object `Service Center` dan Name `Bengkel Maju Motor {runId}` dan catat jumlah entrinya sebagai A9
139. Baca System Log Detail User `Dewi Anggraini {runId}` dengan Action `Inactivated` dan catat jumlah entrinya sebagai S9
140. Baca jumlah notifikasi yang menyebut Service Center `Bengkel Maju Motor {runId}` dan catat sebagai T9
141. `Dewi Anggraini {runId}` mengirim Inactivate atas `Bengkel Maju Motor {runId}` yang sudah `Inactive` dengan versi data V3 yang usang
142. Verifikasi permintaan berhasil tanpa konflik versi, karena Inactivate yang status tujuannya sudah tercapai dinilai No-Op sebelum versi diperiksa
143. Baca ulang Changelog dengan Service Center Name `Bengkel Maju Motor {runId}`
144. Verifikasi jumlah entri Changelog tetap L8
145. Baca ulang Activity Log dengan Object `Service Center` dan Name `Bengkel Maju Motor {runId}`
146. Verifikasi jumlah entri Activity Log tetap A9
147. Baca ulang System Log Detail User `Dewi Anggraini {runId}` dengan Action `Inactivated`
148. Verifikasi jumlah entri System Log Action `Inactivated` tetap S9
149. Baca ulang jumlah notifikasi yang menyebut Service Center `Bengkel Maju Motor {runId}`
150. Verifikasi jumlah notifikasi tetap T9, sehingga Inactivate kedua tidak menimbulkan notifikasi ganda
151. `Dewi Anggraini {runId}` mengirim Edit atas `Bengkel Maju Motor {runId}` dengan Notes diganti `Vendor resmi Bandung Timur` dan versi data V4 yang dibaca sebelum Inactivate kedua
152. Verifikasi Edit diterima tanpa konflik versi, sehingga Inactivate kedua tidak menaikkan versi data

### Create yang gagal validasi tidak menyimpan Service Center, lampiran, maupun entri Attachment added
153. Baca daftar Service Center client suite dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N5
154. Baca Changelog Service Center dengan Service Center Name `Sentral Atomik Lampiran {runId}` dan catat jumlah entrinya sebagai L9
155. `Dewi Anggraini {runId}` mengirim Create dengan Name `Sentral Atomik Lampiran {runId}`, lampiran valid `izin-usaha-atomik.pdf` (PDF, 500 KB), dan Country `Atlantis`
156. Verifikasi permintaan ditolak dengan pesan `Select a valid country`
157. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
158. Verifikasi jumlah baris tetap N5, sehingga tidak ada Service Center dan lampiran yang tersimpan
159. Baca ulang Changelog Service Center dengan Service Center Name `Sentral Atomik Lampiran {runId}`
160. Verifikasi jumlah entri tetap L9, sehingga tidak ada entri `Attachment added` yang tertulis

### Inactivate dan Activate kedua atas Service Center yang dipakai Schedule aktif tidak menggandakan notifikasi
161. `Dewi Anggraini {runId}` mengirim Inactivate atas `Servis Chiller Terjadwal {runId}` yang berstatus `Active`
162. Baca jumlah notifikasi yang menyebut Service Center `Servis Chiller Terjadwal {runId}` dan catat sebagai T10
163. `Dewi Anggraini {runId}` mengirim Inactivate atas `Servis Chiller Terjadwal {runId}` yang sudah `Inactive`
164. Baca ulang jumlah notifikasi yang menyebut Service Center `Servis Chiller Terjadwal {runId}`
165. Verifikasi jumlah notifikasi tetap T10, sehingga Inactivate kedua tidak menimbulkan notifikasi ganda walau Service Center dipakai Schedule aktif
166. `Dewi Anggraini {runId}` mengirim Activate atas `Servis Chiller Terjadwal {runId}` yang berstatus `Inactive`
167. Baca jumlah notifikasi yang menyebut Service Center `Servis Chiller Terjadwal {runId}` dan catat sebagai T11
168. `Dewi Anggraini {runId}` mengirim Activate atas `Servis Chiller Terjadwal {runId}` yang sudah `Active`
169. Baca ulang jumlah notifikasi yang menyebut Service Center `Servis Chiller Terjadwal {runId}`
170. Verifikasi jumlah notifikasi tetap T11, sehingga Activate kedua tidak menimbulkan notifikasi ganda walau Service Center dipakai Schedule aktif

### Edit tanpa perubahan tidak memperbarui Last Updated dan Modified By
171. `Bagus Prakoso {runId}` mengirim Edit atas `Teknik Pendingin Nusantara {runId}` dengan City diganti `Solo`
172. Waktu berlalu sampai 2 menit sejak Edit itu
173. Baca `Teknik Pendingin Nusantara {runId}` dari daftar dengan pencarian `Teknik Pendingin Nusantara {runId}` dan catat nilai Last Updated sebagai LU0 dan nilai Modified By sebagai MB0
174. `Dewi Anggraini {runId}` mengirim Edit atas `Teknik Pendingin Nusantara {runId}` dengan City `Solo` yang sudah tersimpan, tanpa perubahan nilai lain
175. Verifikasi Edit diterima dengan sukses sebagai No-Op dengan pesan `No changes to save.`
176. Baca ulang `Teknik Pendingin Nusantara {runId}` dari daftar dengan pencarian `Teknik Pendingin Nusantara {runId}`
177. Verifikasi nilai Last Updated tetap LU0
178. Verifikasi nilai Modified By tetap MB0
