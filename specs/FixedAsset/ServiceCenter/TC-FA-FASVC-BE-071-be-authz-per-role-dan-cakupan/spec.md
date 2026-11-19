---
id: TC-FA-FASVC-BE-071-be-authz-per-role-dan-cakupan
title: "Server: Aksi Tulis Ditolak Tanpa Hak atau di Luar Cakupan Kelola; Urutan 403 dan 404"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["FASVC-LOGIC-08j", "FASVC-LOGIC-08g", "FASVC-LOGIC-08e", "FASVC-LOGIC-08f", "FASVC-LOGIC-08k", "§9.3#b1", "§9.3#b2", "§9.3#b3", "V-FASVC-39", "EB-AKS-3@create-service-center", "EB-AKS-3@edit-service-center", "EB-AKS-3@inactivate-service-center", "EB-AKS-3@activate-service-center", "EB-AKS-3@delete-service-center"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-08j": [3, 5, 7, 9, 11, 13, 15, 24, 146, 159]
  "FASVC-LOGIC-08g": [24, 26, 28, 30, 32, 34, 36, 48, 50, 53, 74, 76, 78, 81, 83, 85, 87, 90, 92, 94, 96, 99, 146, 148, 150, 152, 154, 156]
  "FASVC-LOGIC-08e": [55, 58]
  "FASVC-LOGIC-08f": [39, 41, 43, 46]
  "FASVC-LOGIC-08k": [62, 64, 102, 105, 108, 111]
  "§9.3#b1": [32, 70, 72, 146, 148, 150, 152, 154, 156, 159, 161, 163, 165, 167, 169, 171, 173, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144]
  "§9.3#b2": [66, 68]
  "§9.3#b3": [13, 15, 17]
  "V-FASVC-39": [66]
  "EB-AKS-3@create-service-center": [3, 17, 159, 169]
  "EB-AKS-3@edit-service-center": [5, 19, 161, 171]
  "EB-AKS-3@inactivate-service-center": [7, 20, 163, 171]
  "EB-AKS-3@activate-service-center": [9, 22, 165, 173]
  "EB-AKS-3@delete-service-center": [11, 17, 167, 171]
anchor: []
---

# Server: Aksi Tulis Ditolak Tanpa Hak atau di Luar Cakupan Kelola; Urutan 403 dan 404

## Prerequisites
- Aktor: Total Control pada client suite dan user pada Data sesuai langkah.
- Data:
  - DU-071-1: User `Hendra Kusuma {runId}` dengan Role `Group Manager`, dan cakupan Group seluruh pohon Group (node root).
  - DU-071-2: User `Siti Rahmawati {runId}` dengan Role `Group Manager`, dan cakupan Group `Cabang Surabaya {runId}` saja.
  - DU-071-3: User `Rina Wulandari {runId}` dengan Role `Asset Admin`, Role Transaksi `Maintenance Routine`, dan cakupan Group `Cabang Surabaya {runId}` saja.
  - DU-071-4: User `Agus Wijaya {runId}` dengan Role `Asset Admin`, Role Transaksi `Repair`, dan cakupan Group seluruh pohon Group (node root).
  - DU-071-5: User `Wulan Maharani {runId}` dengan Role `Asset Admin`, Role Transaksi `Maintenance Routine`, dan cakupan Group `Cabang Malang {runId}` saja, setelah sebelumnya `Cabang Surabaya {runId}` saja.
  - DU-071-6: User `Yoga Saputra {runId}` dengan Role `Read Only`, dan cakupan Group seluruh pohon Group (node root).
  - DU-071-7: User `Budi Santoso {runId}` dengan Role `Staff`, dan cakupan Group `Cabang Surabaya {runId}` saja.
  - DU-071-8: User `Sari Utami {runId}` dengan Role `Monitoring & Report`, Role Transaksi `Maintenance Routine`, dan cakupan Group seluruh pohon Group (node root).
  - DU-071-9: Service Center `PT Sejuk Abadi Teknik {runId}`, Service type `Routine, Repair`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `layanan@hakkelola.co.id`, Status `Active`, ada di client suite.
  - DU-071-10: Service Center `Servis Elektrik Surabaya {runId}`, Service type `Routine`, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `layanan@hakkelola.co.id`, Status `Active`, ada di client suite.
  - DU-071-11: Service Center `Servis Terpadu Surabaya Malang {runId}`, Service type `Routine`, Available to `Cabang Surabaya {runId}` dan `Cabang Malang {runId}`, Country `Indonesia`, City `Surabaya`, Company email `layanan@hakkelola.co.id`, Status `Active`, ada di client suite.
  - DU-071-12: Service Center `Bengkel Maju Motor {runId}`, Service type `Repair`, Available to `Cabang Surabaya {runId}` dan `Cabang Malang {runId}`, Country `Indonesia`, City `Bandung`, Company email `layanan@hakkelola.co.id`, Status `Inactive`, ada di client suite.
  - DU-071-13: Service Center `Servis Repair Surabaya {runId}`, Service type `Repair`, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `layanan@hakkelola.co.id`, Status `Active`, ada di client suite.
  - DU-071-32: User `Dwi Hartono {runId}` dengan Role `Approver`, dan cakupan Group `Cabang Surabaya {runId}` saja.
  - DU-071-33: Service Center `Servis Nonaktif Surabaya {runId}`, Service type `Routine`, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `layanan@hakkelola.co.id`, Status `Inactive`, ada di client suite.
  - DU-071-35: User `Lina Pratiwi {runId}` dengan Role `Asset Admin`, tanpa Role Transaksi apa pun, dan cakupan Group seluruh pohon Group (node root).
  - Group `Cabang Surabaya {runId}` dan `Cabang Malang {runId}` adalah anak langsung root pohon Group di client suite.
  - Setiap Create yang dikirim memuat field wajib lain bernilai Service type `Routine`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `layanan@hakkelola.co.id`, kecuali yang disebut di langkah; Name dikirim sesuai langkah.
  - Setiap Edit, Inactivate, Activate, dan Delete yang dikirim memuat versi data terkini dan nilai tersimpan untuk semua field selain yang disebut di langkah.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.
  - Service Center `Servis Telah Dihapus {runId}` sudah dihapus dari client suite, sehingga ID-nya tidak ada.
  - Cakupan Group `Wulan Maharani {runId}` sudah berubah dari `Cabang Surabaya {runId}` menjadi `Cabang Malang {runId}` sesudah dialog Edit atas `Servis Elektrik Surabaya {runId}` dibuka, dan versi data `Servis Elektrik Surabaya {runId}` yang dikirim adalah versi saat dialog dibuka.

## Test Steps
### Aktor tanpa hak tulis ditolak untuk Create, Edit, Inactivate, Activate, dan Delete
1. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N0
2. `Yoga Saputra {runId}` mengirim Create dengan Name `Mitra Teknik Baru {runId}` dan Available to `All groups`
3. Verifikasi permintaan ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
4. `Yoga Saputra {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan Name diganti `PT Sejuk Abadi Teknik Raya {runId}`
5. Verifikasi permintaan Edit ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
6. `Yoga Saputra {runId}` mengirim Inactivate atas `PT Sejuk Abadi Teknik {runId}`
7. Verifikasi permintaan Inactivate ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
8. `Yoga Saputra {runId}` mengirim Activate atas `Bengkel Maju Motor {runId}`
9. Verifikasi permintaan Activate ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
10. `Yoga Saputra {runId}` mengirim Delete atas `Servis Elektrik Surabaya {runId}`
11. Verifikasi permintaan Delete ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
12. `Budi Santoso {runId}` mengirim Create dengan Name `Mitra Teknik Staff {runId}` dan Available to `Cabang Surabaya {runId}`
13. Verifikasi permintaan Create oleh Staff ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
14. `Sari Utami {runId}` mengirim Create dengan Name `Mitra Teknik Pantau {runId}` dan Available to `All groups`
15. Verifikasi permintaan Create oleh Monitoring & Report ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
16. Baca ulang daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
17. Verifikasi jumlah baris tetap N0, sehingga Create dan Delete yang ditolak tidak mengubah data
18. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
19. Verifikasi Name tersimpan tetap `PT Sejuk Abadi Teknik {runId}`
20. Verifikasi Status tersimpan tetap `Active`
21. Baca `Bengkel Maju Motor {runId}` dari daftar dengan pencarian `Bengkel Maju Motor {runId}`
22. Verifikasi Status tersimpan tetap `Inactive`

### Asset Admin di luar cakupan kelola ditolak
23. `Rina Wulandari {runId}` mengirim Edit atas `Servis Terpadu Surabaya Malang {runId}` dengan Name diganti `Servis Terpadu Surabaya Raya {runId}`
24. Verifikasi permintaan ditolak karena Available to tidak seluruhnya dalam cakupan pengirim, dengan pesan `You don't have permission to do this.`
25. `Rina Wulandari {runId}` mengirim Inactivate atas `Servis Terpadu Surabaya Malang {runId}`
26. Verifikasi permintaan Inactivate ditolak dengan pesan `You don't have permission to do this.`
27. `Rina Wulandari {runId}` mengirim Activate atas `Bengkel Maju Motor {runId}`
28. Verifikasi permintaan Activate ditolak dengan pesan `You don't have permission to do this.`
29. `Rina Wulandari {runId}` mengirim Delete atas `Servis Terpadu Surabaya Malang {runId}`
30. Verifikasi permintaan Delete ditolak dengan pesan `You don't have permission to do this.`
31. `Rina Wulandari {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
32. Verifikasi permintaan Edit atas Service Center ber-`All groups` ditolak dengan pesan `You don't have permission to do this.`
33. Baca `Servis Terpadu Surabaya Malang {runId}` dari daftar sebagai Total Control dengan pencarian `Servis Terpadu Surabaya Malang {runId}`
34. Verifikasi Service Center itu masih ada dengan Status `Active` dan Name tersimpan tetap
35. Baca `Bengkel Maju Motor {runId}` dari daftar sebagai Total Control dengan pencarian `Bengkel Maju Motor {runId}`
36. Verifikasi Status tersimpan tetap `Inactive`, setelah Activate oleh Asset Admin ditolak

### All groups hanya bagi Total Control dan Group Manager root
37. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N1
38. `Siti Rahmawati {runId}` mengirim Create dengan Name `Mitra Nasional Cabang {runId}` dan Available to `All groups`
39. Verifikasi permintaan ditolak karena `All groups` hanya bagi Total Control dan Group Manager root
40. `Agus Wijaya {runId}` mengirim Create dengan Name `Mitra Nasional Admin {runId}` dan Available to `All groups`
41. Verifikasi permintaan ditolak walau cakupan pengirim mencakup seluruh pohon
42. Baca ulang daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
43. Verifikasi jumlah baris tetap N1, sehingga kedua Create yang ditolak tidak membuat Service Center
44. `Hendra Kusuma {runId}` mengirim Create dengan Name `Mitra Nasional Utama {runId}` dan Available to `All groups`
45. Baca `Mitra Nasional Utama {runId}` dari daftar dengan pencarian `Mitra Nasional Utama {runId}`
46. Verifikasi Service Center tersimpan dengan Available to `All groups`
47. `Siti Rahmawati {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
48. Verifikasi permintaan Edit oleh Group Manager cabang ditolak dengan pesan `You don't have permission to do this.`
49. `Agus Wijaya {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
50. Verifikasi permintaan Edit oleh Asset Admin berskop root ditolak dengan pesan `You don't have permission to do this.`
51. `Hendra Kusuma {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
52. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
53. Verifikasi City tersimpan `Jakarta Pusat`, karena Group Manager root boleh mengelola Service Center ber-`All groups`

### Available to saat Create dibatasi pada cakupan Group pembuat
54. `Siti Rahmawati {runId}` mengirim Create dengan Name `Servis Elektrik Malang {runId}` dan Available to `Cabang Malang {runId}`
55. Verifikasi permintaan ditolak karena Available to di luar cakupan pembuat
56. `Siti Rahmawati {runId}` mengirim Create dengan Name `Servis Elektrik Sidoarjo {runId}` dan Available to `Cabang Surabaya {runId}`
57. Baca `Servis Elektrik Sidoarjo {runId}` dari daftar dengan pencarian `Servis Elektrik Sidoarjo {runId}`
58. Verifikasi Service Center tersimpan dengan Available to `Cabang Surabaya {runId}`

### Asset Admin mengelola Service Center dengan Service type apa pun
59. `Rina Wulandari {runId}` mengirim Edit atas `Servis Repair Surabaya {runId}` dengan City diganti `Gresik`
60. `Agus Wijaya {runId}` mengirim Edit atas `Servis Elektrik Surabaya {runId}` dengan City diganti `Sidoarjo`
61. Baca `Servis Repair Surabaya {runId}` dari daftar dengan pencarian `Servis Repair Surabaya {runId}`
62. Verifikasi City tersimpan `Gresik`, karena Role Transaksi `Maintenance Routine` boleh mengelola Service Center ber-Service type `Repair`
63. Baca `Servis Elektrik Surabaya {runId}` dari daftar dengan pencarian `Servis Elektrik Surabaya {runId}`
64. Verifikasi City tersimpan `Sidoarjo`, karena Role Transaksi `Repair` boleh mengelola Service Center ber-Service type `Routine`

### Hak dievaluasi ulang di server dan sebelum keberadaan data
65. `Wulan Maharani {runId}` mengirim Edit atas `Servis Elektrik Surabaya {runId}` dengan City diganti `Mojokerto`, berdasarkan dialog Edit yang dibuka saat cakupannya masih `Cabang Surabaya {runId}`
66. Verifikasi permintaan ditolak dengan pesan `You don't have permission to do this.`
67. `Wulan Maharani {runId}` mengirim Edit atas `Servis Elektrik Surabaya {runId}` tanpa mengubah satu pun nilai
68. Verifikasi permintaan ditolak karena hak kelola sudah hilang, walau tidak ada perubahan nilai
69. `Yoga Saputra {runId}` mengirim Edit atas `Servis Telah Dihapus {runId}` yang ID-nya tidak ada
70. Verifikasi permintaan ditolak karena pengirim tidak punya hak dengan pesan `You don't have permission to do this.`, bukan karena data tidak ditemukan
71. `Rina Wulandari {runId}` mengirim Edit atas `Servis Telah Dihapus {runId}` yang ID-nya tidak ada
72. Verifikasi permintaan ditolak dengan pesan `This service center is no longer available.`

### Service Center ber-All groups: Inactivate, Activate, dan Delete hanya bagi Total Control dan Group Manager root
73. `Siti Rahmawati {runId}` mengirim Inactivate atas `PT Sejuk Abadi Teknik {runId}`
74. Verifikasi permintaan Inactivate oleh Group Manager cabang ditolak dengan pesan `You don't have permission to do this.`
75. `Agus Wijaya {runId}` mengirim Inactivate atas `PT Sejuk Abadi Teknik {runId}`
76. Verifikasi permintaan Inactivate oleh Asset Admin berskop root ditolak dengan pesan `You don't have permission to do this.`
77. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
78. Verifikasi Status tersimpan tetap `Active`, setelah kedua Inactivate ditolak
79. `Hendra Kusuma {runId}` mengirim Inactivate atas `PT Sejuk Abadi Teknik {runId}`
80. Baca ulang `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
81. Verifikasi Status tersimpan `Inactive`, karena Group Manager root boleh mengelola Service Center ber-`All groups`
82. `Siti Rahmawati {runId}` mengirim Activate atas `PT Sejuk Abadi Teknik {runId}`
83. Verifikasi permintaan Activate oleh Group Manager cabang ditolak dengan pesan `You don't have permission to do this.`
84. `Agus Wijaya {runId}` mengirim Activate atas `PT Sejuk Abadi Teknik {runId}`
85. Verifikasi permintaan Activate oleh Asset Admin berskop root ditolak dengan pesan `You don't have permission to do this.`
86. Baca ulang `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
87. Verifikasi Status tersimpan tetap `Inactive`, setelah kedua Activate ditolak
88. `Hendra Kusuma {runId}` mengirim Activate atas `PT Sejuk Abadi Teknik {runId}`
89. Baca ulang `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
90. Verifikasi Status tersimpan `Active`, karena Group Manager root boleh mengelola Service Center ber-`All groups`
91. `Siti Rahmawati {runId}` mengirim Delete atas `PT Sejuk Abadi Teknik {runId}`
92. Verifikasi permintaan Delete oleh Group Manager cabang ditolak dengan pesan `You don't have permission to do this.`
93. `Agus Wijaya {runId}` mengirim Delete atas `PT Sejuk Abadi Teknik {runId}`
94. Verifikasi permintaan Delete oleh Asset Admin berskop root ditolak dengan pesan `You don't have permission to do this.`
95. Baca ulang `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
96. Verifikasi Service Center itu masih ada, setelah kedua Delete ditolak
97. `Hendra Kusuma {runId}` mengirim Delete atas `PT Sejuk Abadi Teknik {runId}`
98. Baca daftar Service Center client suite dengan pencarian `PT Sejuk Abadi Teknik {runId}`
99. Verifikasi hasil pencarian tidak memuat Service Center `PT Sejuk Abadi Teknik {runId}`, karena Group Manager root boleh mengelola Service Center ber-`All groups`

### Asset Admin Role Transaksi Repair mengelola Service Center ber-Service type Routine
100. `Agus Wijaya {runId}` mengirim Create dengan Name `Servis Rutin Agus {runId}`, Service type `Routine`, dan Available to `Cabang Surabaya {runId}`
101. Baca `Servis Rutin Agus {runId}` dari daftar dengan pencarian `Servis Rutin Agus {runId}`
102. Verifikasi Service Center tersimpan dengan Service type `Routine`, karena Role Transaksi `Repair` boleh membuat Service Center ber-Service type `Routine`
103. `Agus Wijaya {runId}` mengirim Inactivate atas `Servis Rutin Agus {runId}`
104. Baca ulang `Servis Rutin Agus {runId}` dari daftar dengan pencarian `Servis Rutin Agus {runId}`
105. Verifikasi Status tersimpan `Inactive`, karena Role Transaksi `Repair` boleh menonaktifkan Service Center ber-Service type `Routine`
106. `Agus Wijaya {runId}` mengirim Activate atas `Servis Rutin Agus {runId}`
107. Baca ulang `Servis Rutin Agus {runId}` dari daftar dengan pencarian `Servis Rutin Agus {runId}`
108. Verifikasi Status tersimpan `Active`, karena Role Transaksi `Repair` boleh mengaktifkan Service Center ber-Service type `Routine`
109. `Agus Wijaya {runId}` mengirim Delete atas `Servis Rutin Agus {runId}`
110. Baca daftar Service Center client suite dengan pencarian `Servis Rutin Agus {runId}`
111. Verifikasi hasil pencarian tidak memuat Service Center `Servis Rutin Agus {runId}`, karena Role Transaksi `Repair` boleh menghapus Service Center ber-Service type `Routine`

### Staff, Approver, dan Monitoring & Report ditolak untuk Edit, Inactivate, Activate, dan Delete
112. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N2
113. `Budi Santoso {runId}` mengirim Edit atas `Servis Repair Surabaya {runId}` dengan City diganti `Pasuruan`
114. Verifikasi permintaan Edit oleh Staff ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
115. `Budi Santoso {runId}` mengirim Inactivate atas `Servis Repair Surabaya {runId}`
116. Verifikasi permintaan Inactivate oleh Staff ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
117. `Budi Santoso {runId}` mengirim Activate atas `Servis Nonaktif Surabaya {runId}`
118. Verifikasi permintaan Activate oleh Staff ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
119. `Budi Santoso {runId}` mengirim Delete atas `Servis Repair Surabaya {runId}`
120. Verifikasi permintaan Delete oleh Staff ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
121. `Dwi Hartono {runId}` mengirim Create dengan Name `Mitra Teknik Approver {runId}` dan Available to `Cabang Surabaya {runId}`
122. Verifikasi permintaan Create oleh Approver ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
123. `Dwi Hartono {runId}` mengirim Edit atas `Servis Repair Surabaya {runId}` dengan City diganti `Pasuruan`
124. Verifikasi permintaan Edit oleh Approver ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
125. `Dwi Hartono {runId}` mengirim Inactivate atas `Servis Repair Surabaya {runId}`
126. Verifikasi permintaan Inactivate oleh Approver ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
127. `Dwi Hartono {runId}` mengirim Activate atas `Servis Nonaktif Surabaya {runId}`
128. Verifikasi permintaan Activate oleh Approver ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
129. `Dwi Hartono {runId}` mengirim Delete atas `Servis Repair Surabaya {runId}`
130. Verifikasi permintaan Delete oleh Approver ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
131. `Sari Utami {runId}` mengirim Edit atas `Servis Repair Surabaya {runId}` dengan City diganti `Pasuruan`
132. Verifikasi permintaan Edit oleh Monitoring & Report ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
133. `Sari Utami {runId}` mengirim Inactivate atas `Servis Repair Surabaya {runId}`
134. Verifikasi permintaan Inactivate oleh Monitoring & Report ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
135. `Sari Utami {runId}` mengirim Activate atas `Servis Nonaktif Surabaya {runId}`
136. Verifikasi permintaan Activate oleh Monitoring & Report ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
137. `Sari Utami {runId}` mengirim Delete atas `Servis Repair Surabaya {runId}`
138. Verifikasi permintaan Delete oleh Monitoring & Report ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
139. Baca ulang daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
140. Verifikasi jumlah baris tetap N2, sehingga Create oleh Approver dan Delete yang ditolak tidak mengubah data
141. Baca `Servis Repair Surabaya {runId}` dari daftar dengan pencarian `Servis Repair Surabaya {runId}`
142. Verifikasi City tersimpan tetap `Gresik` dan Status tersimpan tetap `Active`
143. Baca `Servis Nonaktif Surabaya {runId}` dari daftar dengan pencarian `Servis Nonaktif Surabaya {runId}`
144. Verifikasi Status tersimpan tetap `Inactive`

### Group Manager cabang ditolak atas Service Center yang Available to-nya sebagian di luar cakupan kelola
145. `Siti Rahmawati {runId}` mengirim Edit atas `Servis Terpadu Surabaya Malang {runId}` dengan City diganti `Sidoarjo`
146. Verifikasi permintaan Edit oleh Group Manager cabang ditolak karena Available to tidak seluruhnya dalam cakupan pengirim, dengan pesan `You don't have permission to do this.`
147. `Siti Rahmawati {runId}` mengirim Inactivate atas `Servis Terpadu Surabaya Malang {runId}`
148. Verifikasi permintaan Inactivate oleh Group Manager cabang ditolak dengan pesan `You don't have permission to do this.`
149. `Siti Rahmawati {runId}` mengirim Activate atas `Bengkel Maju Motor {runId}`
150. Verifikasi permintaan Activate oleh Group Manager cabang ditolak dengan pesan `You don't have permission to do this.`
151. `Siti Rahmawati {runId}` mengirim Delete atas `Servis Terpadu Surabaya Malang {runId}`
152. Verifikasi permintaan Delete oleh Group Manager cabang ditolak dengan pesan `You don't have permission to do this.`
153. Baca `Servis Terpadu Surabaya Malang {runId}` dari daftar sebagai Total Control dengan pencarian `Servis Terpadu Surabaya Malang {runId}`
154. Verifikasi Service Center itu masih ada dengan City tersimpan tetap `Surabaya` dan Status tersimpan tetap `Active`
155. Baca `Bengkel Maju Motor {runId}` dari daftar sebagai Total Control dengan pencarian `Bengkel Maju Motor {runId}`
156. Verifikasi Status tersimpan tetap `Inactive`, setelah Activate oleh Group Manager cabang ditolak

### Asset Admin tanpa Role Transaksi ditolak untuk Create, Edit, Inactivate, Activate, dan Delete
157. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N3
158. `Lina Pratiwi {runId}` mengirim Create dengan Name `Mitra Teknik Tanpa Role {runId}` dan Available to `Cabang Surabaya {runId}`
159. Verifikasi permintaan Create oleh Asset Admin tanpa Role Transaksi ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
160. `Lina Pratiwi {runId}` mengirim Edit atas `Servis Repair Surabaya {runId}` dengan City diganti `Tuban`
161. Verifikasi permintaan Edit oleh Asset Admin tanpa Role Transaksi ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
162. `Lina Pratiwi {runId}` mengirim Inactivate atas `Servis Repair Surabaya {runId}`
163. Verifikasi permintaan Inactivate oleh Asset Admin tanpa Role Transaksi ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
164. `Lina Pratiwi {runId}` mengirim Activate atas `Servis Nonaktif Surabaya {runId}`
165. Verifikasi permintaan Activate oleh Asset Admin tanpa Role Transaksi ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
166. `Lina Pratiwi {runId}` mengirim Delete atas `Servis Repair Surabaya {runId}`
167. Verifikasi permintaan Delete oleh Asset Admin tanpa Role Transaksi ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
168. Baca ulang daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
169. Verifikasi jumlah baris tetap N3, sehingga Create dan Delete yang ditolak tidak mengubah data
170. Baca `Servis Repair Surabaya {runId}` dari daftar dengan pencarian `Servis Repair Surabaya {runId}`
171. Verifikasi City tersimpan tetap `Gresik` dan Status tersimpan tetap `Active`
172. Baca `Servis Nonaktif Surabaya {runId}` dari daftar dengan pencarian `Servis Nonaktif Surabaya {runId}`
173. Verifikasi Status tersimpan tetap `Inactive`
