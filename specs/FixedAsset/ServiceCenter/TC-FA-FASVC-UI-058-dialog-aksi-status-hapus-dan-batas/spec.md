---
id: TC-FA-FASVC-UI-058-dialog-aksi-status-hapus-dan-batas
title: "Dialog Inactivate, Activate, Delete, Service Center Changed, Cannot Delete, dan Limit Reached"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["D-FASVC-04", "D-FASVC-05", "D-FASVC-06", "D-FASVC-07", "D-FASVC-09", "D-FASVC-10", "DO-FASVC-04", "DO-FASVC-05", "DO-FASVC-06", "DO-FASVC-07", "DO-FASVC-08", "DO-FASVC-09", "FASVC-LOGIC-05e", "FASVC-LOGIC-05f", "FASVC-LOGIC-06e", "FASVC-LOGIC-11a", "FASVC-LOGIC-11b", "FASVC-LOGIC-12a", "V-FASVC-15", "V-FASVC-22", "F-FASVC-03.k1", "F-FASVC-04.k3", "TS-FASVC-03", "TS-FASVC-04", "TS-FASVC-08", "§4.2.5#p1", "§4.2.5#p4", "§4.4#r7", "§4.4#r8", "RS-FASVC-04", "RS-FASVC-08", "EB-FB-1@inactivate-service-center", "EB-FB-1@activate-service-center", "EB-FB-1@delete-service-center", "EB-FB-2@cancel-dialog-konfirmasi", "EB-ERR-1@inactivate-service-center", "EB-ERR-1@activate-service-center", "EB-ERR-1@delete-service-center", "EB-ERR-2@delete-service-center", "EB-CON-4"]
smoke: []
dependsOn: []
trace:
  "D-FASVC-04": [4, 5, 6, 7, 8]
  "D-FASVC-05": [156, 157, 158, 160, 166, 168, 174, 176, 183, 186, 187, 193, 269, 271, 277, 279, 285, 287]
  "D-FASVC-06": [35, 36, 37, 38, 39]
  "D-FASVC-07": [144, 145, 146, 149]
  "D-FASVC-09": [20, 21, 22, 23, 24]
  "D-FASVC-10": [235, 236, 237, 254]
  "DO-FASVC-04": [4]
  "DO-FASVC-05": [20]
  "DO-FASVC-06": [35]
  "DO-FASVC-07": [156, 166, 174, 183, 269, 277, 285]
  "DO-FASVC-08": [144]
  "DO-FASVC-09": [193, 195, 196, 197]
  "FASVC-LOGIC-05e": [6]
  "FASVC-LOGIC-05f": [22]
  "FASVC-LOGIC-06e": [144]
  "FASVC-LOGIC-11a": [155, 165, 173, 182, 268, 276, 284]
  "FASVC-LOGIC-11b": [156, 166, 174, 183, 269, 277, 285]
  "FASVC-LOGIC-12a": [235, 236, 240, 254, 256, 257, 258]
  "V-FASVC-15": [144, 145, 147]
  "V-FASVC-22": [202, 203, 205, 291, 292, 293, 295]
  "F-FASVC-03.k1": [14, 16, 29, 31]
  "F-FASVC-04.k3": [144]
  "TS-FASVC-03": [15, 30, 73, 83]
  "TS-FASVC-04": [45, 93]
  "TS-FASVC-08": [210, 211, 216, 217, 222, 223, 230, 231, 232]
  "§4.2.5#p1": [4, 9]
  "§4.2.5#p4": [184]
  "§4.4#r7": [6]
  "§4.4#r8": [22]
  "RS-FASVC-04": [93, 95, 117, 118, 144, 150, 224]
  "RS-FASVC-08": [262, 263]
  "EB-FB-1@inactivate-service-center": [15, 73]
  "EB-FB-1@activate-service-center": [30, 83]
  "EB-FB-1@delete-service-center": [44, 45, 47, 93]
  "EB-FB-2@cancel-dialog-konfirmasi": [52, 53, 54, 59, 60, 61, 66, 67, 68]
  "EB-ERR-1@inactivate-service-center": [73, 74, 75, 76, 78, 103, 104, 105]
  "EB-ERR-1@activate-service-center": [83, 84, 85, 86, 88, 110, 111, 112]
  "EB-ERR-1@delete-service-center": [93, 94, 95, 96, 98, 117, 118, 119]
  "EB-ERR-2@delete-service-center": [124, 125, 130, 131, 132, 137, 139]
  "EB-CON-4": [235, 243, 244, 254, 256]
anchor: [46, 239, 247]
coverage:
  web: automated
---
# Dialog Inactivate, Activate, Delete, Service Center Changed, Cannot Delete, dan Limit Reached

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center, halaman daftar Service Center; untuk kondisi K15 sampai K17, halaman Detail Service Center.
- Komponen: Dialog konfirmasi dan info status Service Center
- Data:
  - DU-058-1: Service Center `CV Genset Prima`, Service Type `Routine`, Specialization `Generator`, Available To `Branch Surabaya, Branch Malang`, City `Surabaya`, Brands `All brands`, Usage `24`, Status `Active`, Modified By `Rina W`, Last Updated `10/03/26, 09:15`, versi data `7`.
  - DU-058-2: Service Center `Bengkel Maju Motor`, Service Type `Repair`, Specialization `Vehicle`, Available To `Head Office`, City `Bandung`, Brands `All brands`, Usage `0`, Status `Inactive`, Modified By `Rina W`, Last Updated `10/03/26, 09:20`, versi data `3`.
  - DU-058-3: Service Center `Lab Kalibrasi Pratama`, Service Type `Routine`, Specialization `All categories`, Available To `Head Office`, City `Johor Bahru, Malaysia`, Brands `All brands`, Usage `0`, Status `Active`, Modified By `Rina W`, Last Updated `10/03/26, 09:25`, versi data `4`.
  - DU-058-4: Hitungan dampak Inactivate untuk DU-058-1: `3` Schedule aktif dan `4` Task terbuka.
  - DU-058-5: Service Center `Servis Mesin Sentosa`, Service Type `Repair`, Specialization `Vehicle`, Available To `Head Office`, City `Semarang`, Brands `All brands`, Usage `0`, Status `Active`, Modified By `Rina W`, Last Updated `10/03/26, 09:30`, versi data `2`.
  - DU-058-6: Service Center `PT Sejuk Abadi Teknik`, Service Type `Routine, Repair`, Specialization `AC, Refrigeration`, Available To `All groups`, City `Jakarta Selatan`, Brands `Daikin`, Usage `148`, Status `Active`, Modified By `Rina W`, Last Updated `10/03/26, 09:35`, Notes `Kontrak servis AC tahunan`, versi data `9`. Data terbaru di server: Notes `Kontrak servis AC diperpanjang`.
  - DU-058-7: Service Center `CV Teknik Dingin Jaya`, Service Type `Routine`, Specialization `AC`, Available To `Head Office`, City `Surabaya`, Brands `Daikin, LG`, Usage `5`, Status `Active`, Modified By `Rina W`, Last Updated `10/03/26, 09:40`, Notes `Kontrak servis pendingin tahunan`. Data terbaru di server: Brands `Daikin` (Brand `LG` dihapus dari master).
  - DU-058-8: `1000` Service Center `Servis Teknik Nusantara {n}`, Service Type `Routine`, Status `Active`.
  - DU-058-9: `999` Service Center `Servis Teknik Nusantara {n}`, Service Type `Routine`, Status `Active`.
  - DU-058-10: Input Create: Name `Servis Pendingin Nusantara`, Service type `Routine`, Available to `Head Office`, City `Jakarta Selatan`, Company phone Dial Code `+62` nomor `81234567890`.
  - DU-058-11: Isi Notes baru pada Edit: `Kontrak servis AC dan chiller`.
  - DU-058-12: Isi Notes baru pada Edit: `Kontrak servis pendingin ruangan`.
  - DU-058-13: Service Center `Bengkel Cahaya Teknik`, Service Type `Repair`, Specialization `Vehicle`, Available To kosong (tanpa Group), City `Malang`, Brands `All brands`, Usage `0`, Status `Inactive`, Modified By `Rina W`, Last Updated `10/03/26, 09:45`, versi data `5`.
- Kondisi:
  - K1: daftar memuat DU-058-1, DU-058-2, dan DU-058-3 di halaman pertama; respons hitungan dampak Inactivate memakai DU-058-4; Inactivate, Activate, dan Delete berhasil, lalu daftar dimuat ulang dengan DU-058-1 `Inactive`, DU-058-2 `Active`, dan tanpa DU-058-3.
  - K2: daftar memuat DU-058-1, DU-058-2, dan DU-058-3; respons hitungan dampak memakai DU-058-4; setiap Inactivate, Activate, dan Delete gagal karena error server pada percobaan pertama dan berhasil pada percobaan kedua.
  - K3: daftar memuat DU-058-1, DU-058-2, dan DU-058-3; respons hitungan dampak memakai DU-058-4; setiap Inactivate, Activate, dan Delete tidak mendapat respons (timeout).
  - K4: daftar memuat DU-058-3; respons Delete tertunda beberapa detik lalu berhasil.
  - K5: daftar memuat DU-058-5; Delete ditolak karena Service Center sudah dipakai, lalu daftar dimuat ulang dengan DU-058-5 masih ada.
  - K6: daftar memuat DU-058-1, DU-058-2, dan DU-058-3 dengan versi data masing-masing; respons hitungan dampak memakai DU-058-4; Inactivate, Activate, dan Delete ditolak sebagai konflik versi karena Service Center sudah diubah pengguna lain.
  - K7: daftar memuat DU-058-6; Edit ditolak sebagai konflik versi karena Notes sudah diubah pengguna lain, dan data terbaru diberikan.
  - K8: daftar memuat DU-058-7; Edit ditolak sebagai konflik versi karena Brand `LG` dihapus dari master oleh sistem, dan data terbaru diberikan.
  - K9: daftar memuat DU-058-2 dengan Available to terisi; Activate ditolak server karena Available to Service Center itu sudah kosong.
  - K10: daftar memuat DU-058-1, DU-058-2, DU-058-3, dan DU-058-6; respons hitungan dampak memakai DU-058-4; setiap Inactivate, Activate, Delete, dan Save Edit dijawab data tidak ditemukan karena sudah dihapus pengguna lain; daftar dimuat ulang tanpa Service Center itu.
  - K11: Master Data Count Limit bernilai `1000`; respons daftar memuat DU-058-8 beserta nilai batas `1000`.
  - K12: Master Data Count Limit bernilai `1000`; respons daftar memuat DU-058-9 beserta nilai batas `1000`.
  - K13: Master Data Count Limit bernilai `1000`; respons daftar memuat DU-058-9 beserta nilai batas `1000`; Submit DU-058-10 ditolak karena batas sudah tercapai saat Submit (Service Center ke-1000 dibuat pengguna lain setelah form dibuka).
  - K14: daftar memuat DU-058-1; Download berhasil.
  - K15: halaman Detail DU-058-1 terbuka; respons hitungan dampak memakai DU-058-4; Inactivate ditolak sebagai konflik versi karena Service Center sudah diubah pengguna lain, lalu Detail dimuat ulang dengan data terbaru.
  - K16: halaman Detail DU-058-2 terbuka; Activate ditolak sebagai konflik versi karena Service Center sudah diubah pengguna lain, lalu Detail dimuat ulang dengan data terbaru.
  - K17: halaman Detail DU-058-3 terbuka; Delete ditolak sebagai konflik versi karena Service Center sudah diubah pengguna lain, lalu Detail dimuat ulang dengan data terbaru.
  - K18: daftar memuat DU-058-13 dengan Available to kosong.

## Test Steps

### Dialog Inactivate menyebut hitungan Schedule aktif dan Task terbuka
1. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
2. Klik `⋯` pada baris `CV Genset Prima`
3. Pilih `Inactivate`
4. Verifikasi dialog `Inactivate Service Center` tampil
5. Verifikasi isi dialog memuat `• CV Genset Prima`
6. Verifikasi isi dialog memuat `It won't appear when assigning work. 3 active schedules keep using it. 4 open tasks keep using it, except tasks not yet in progress, which are released from it on their start date. A task left without an assignee, and the next tasks of those schedules, will wait for assignment.`
7. Verifikasi pertanyaan `Are you sure you want to inactivate it?` tampil
8. Verifikasi tombol `[Cancel]` dan `[Inactivate]` tampil di dialog
9. Verifikasi isi dialog tidak memuat `Deactivate`

### Inactivate berhasil: toast sukses dan daftar dimuat ulang
10. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
11. Klik `⋯` pada baris `CV Genset Prima`
12. Pilih `Inactivate`
13. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
14. Verifikasi dialog `Inactivate Service Center` tertutup
15. Verifikasi toast `Success, CV Genset Prima has been inactivated.` tampil
16. Verifikasi baris `CV Genset Prima` menampilkan Status `Inactive`

### Dialog Activate menyebut Service Center muncul lagi di pemilih
17. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
18. Klik `⋯` pada baris `Bengkel Maju Motor`
19. Pilih `Activate`
20. Verifikasi dialog `Activate Service Center` tampil
21. Verifikasi isi dialog memuat `• Bengkel Maju Motor`
22. Verifikasi isi dialog memuat `It will appear again when assigning work.`
23. Verifikasi pertanyaan `Are you sure you want to activate it?` tampil
24. Verifikasi tombol `[Cancel]` dan `[Activate]` tampil di dialog

### Activate berhasil: toast sukses dan daftar dimuat ulang
25. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
26. Klik `⋯` pada baris `Bengkel Maju Motor`
27. Pilih `Activate`
28. Klik `[Activate]` pada dialog `Activate Service Center`
29. Verifikasi dialog `Activate Service Center` tertutup
30. Verifikasi toast `Success, Bengkel Maju Motor has been activated.` tampil
31. Verifikasi baris `Bengkel Maju Motor` menampilkan Status `Active`

### Dialog Delete menyebut penghapusan permanen beserta lampiran
32. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
33. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
34. Pilih `Delete`
35. Verifikasi dialog `Delete Service Center` tampil
36. Verifikasi isi dialog memuat `• Lab Kalibrasi Pratama`
37. Verifikasi isi dialog memuat `It will be permanently deleted with its attachments.`
38. Verifikasi pertanyaan `Are you sure you want to delete it? This action cannot be undone.` tampil
39. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil di dialog

### Delete berhasil: toast sukses dan baris hilang dari daftar
40. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
41. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
42. Pilih `Delete`
43. Klik `[Delete]` pada dialog `Delete Service Center`
44. Verifikasi dialog `Delete Service Center` tertutup
45. Verifikasi toast `Success, Lab Kalibrasi Pratama has been deleted.` tampil
46. Verifikasi baris `CV Genset Prima` tampil di daftar
47. Verifikasi baris `Lab Kalibrasi Pratama` tidak tampil di daftar

### Cancel pada dialog Inactivate menutup dialog tanpa toast dan tanpa perubahan
48. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
49. Klik `⋯` pada baris `CV Genset Prima`
50. Pilih `Inactivate`
51. Klik `[Cancel]` pada dialog `Inactivate Service Center`
52. Verifikasi dialog `Inactivate Service Center` tertutup
53. Verifikasi toast tidak tampil
54. Verifikasi baris `CV Genset Prima` tetap menampilkan Status `Active`

### Cancel pada dialog Activate menutup dialog tanpa toast dan tanpa perubahan
55. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
56. Klik `⋯` pada baris `Bengkel Maju Motor`
57. Pilih `Activate`
58. Klik `[Cancel]` pada dialog `Activate Service Center`
59. Verifikasi dialog `Activate Service Center` tertutup
60. Verifikasi toast tidak tampil
61. Verifikasi baris `Bengkel Maju Motor` tetap menampilkan Status `Inactive`

### Cancel pada dialog Delete menutup dialog tanpa toast dan tanpa perubahan
62. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
63. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
64. Pilih `Delete`
65. Klik `[Cancel]` pada dialog `Delete Service Center`
66. Verifikasi dialog `Delete Service Center` tertutup
67. Verifikasi toast tidak tampil
68. Verifikasi baris `Lab Kalibrasi Pratama` tetap tampil di daftar

### Inactivate gagal karena error server: dialog tetap terbuka dan ulang berhasil
69. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K2
70. Klik `⋯` pada baris `CV Genset Prima`
71. Pilih `Inactivate`
72. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
73. Verifikasi toast `Error, failed to inactivate service center.` tampil
74. Verifikasi toast tidak memuat tombol `[Try Again]`
75. Verifikasi dialog `Inactivate Service Center` tetap terbuka
76. Verifikasi tombol `[Inactivate]` aktif lagi
77. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
78. Verifikasi toast `Success, CV Genset Prima has been inactivated.` tampil satu kali

### Activate gagal karena error server: dialog tetap terbuka dan ulang berhasil
79. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K2
80. Klik `⋯` pada baris `Bengkel Maju Motor`
81. Pilih `Activate`
82. Klik `[Activate]` pada dialog `Activate Service Center`
83. Verifikasi toast `Error, failed to activate service center.` tampil
84. Verifikasi toast tidak memuat tombol `[Try Again]`
85. Verifikasi dialog `Activate Service Center` tetap terbuka
86. Verifikasi tombol `[Activate]` aktif lagi
87. Klik `[Activate]` pada dialog `Activate Service Center`
88. Verifikasi toast `Success, Bengkel Maju Motor has been activated.` tampil satu kali

### Delete gagal karena error server: dialog tetap terbuka dan ulang berhasil
89. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K2
90. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
91. Pilih `Delete`
92. Klik `[Delete]` pada dialog `Delete Service Center`
93. Verifikasi toast `Error, failed to delete service center.` tampil
94. Verifikasi toast tidak memuat tombol `[Try Again]`
95. Verifikasi dialog `Delete Service Center` tetap terbuka
96. Verifikasi tombol `[Delete]` aktif lagi
97. Klik `[Delete]` pada dialog `Delete Service Center`
98. Verifikasi toast `Success, Lab Kalibrasi Pratama has been deleted.` tampil satu kali

### Inactivate tanpa respons: pesan koneksi dan dialog tetap terbuka
99. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K3
100. Klik `⋯` pada baris `CV Genset Prima`
101. Pilih `Inactivate`
102. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
103. Verifikasi toast `Connection problem. Please try again.` tampil
104. Verifikasi dialog `Inactivate Service Center` tetap terbuka
105. Verifikasi tombol `[Inactivate]` aktif lagi

### Activate tanpa respons: pesan koneksi dan dialog tetap terbuka
106. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K3
107. Klik `⋯` pada baris `Bengkel Maju Motor`
108. Pilih `Activate`
109. Klik `[Activate]` pada dialog `Activate Service Center`
110. Verifikasi toast `Connection problem. Please try again.` tampil
111. Verifikasi dialog `Activate Service Center` tetap terbuka
112. Verifikasi tombol `[Activate]` aktif lagi

### Delete tanpa respons: pesan koneksi dan dialog tetap terbuka
113. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K3
114. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
115. Pilih `Delete`
116. Klik `[Delete]` pada dialog `Delete Service Center`
117. Verifikasi toast `Connection problem. Please try again.` tampil
118. Verifikasi dialog `Delete Service Center` tetap terbuka
119. Verifikasi tombol `[Delete]` aktif lagi

### Klik ganda Delete menghapus sekali dengan satu toast
120. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K4
121. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
122. Pilih `Delete`
123. Klik ganda `[Delete]` pada dialog `Delete Service Center`
124. Verifikasi permintaan Delete terkirim satu kali
125. Verifikasi toast `Success, Lab Kalibrasi Pratama has been deleted.` tampil satu kali

### Esc menutup dialog Delete tanpa menghapus
126. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
127. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
128. Pilih `Delete`
129. Tekan Esc
130. Verifikasi dialog `Delete Service Center` tertutup
131. Verifikasi baris `Lab Kalibrasi Pratama` tetap tampil di daftar
132. Verifikasi permintaan Delete belum terkirim

### Fokus terkunci di dialog Delete dan kembali ke pemicu
133. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K1
134. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
135. Pilih `Delete`
136. Tekan Tab tiga kali
137. Verifikasi fokus tetap berada di dalam dialog `Delete Service Center`
138. Tekan Esc
139. Verifikasi fokus kembali ke tombol `⋯` pada baris `Lab Kalibrasi Pratama`

### Delete ditolak karena sudah dipakai: dialog Cannot Delete tanpa toast tambahan
140. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K5
141. Klik `⋯` pada baris `Servis Mesin Sentosa`
142. Pilih `Delete`
143. Klik `[Delete]` pada dialog `Delete Service Center`
144. Verifikasi dialog `Cannot Delete Service Center` tampil
145. Verifikasi isi dialog memuat `This service center has been used and can't be deleted. Inactivate it instead.`
146. Verifikasi tombol `[OK]` tampil di dialog
147. Verifikasi toast tidak tampil
148. Klik `[OK]` pada dialog `Cannot Delete Service Center`
149. Verifikasi daftar dimuat ulang
150. Verifikasi baris `Servis Mesin Sentosa` tetap tampil di daftar

### Inactivate dengan versi usang menampilkan dialog Service Center Changed
151. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K6
152. Klik `⋯` pada baris `CV Genset Prima`
153. Pilih `Inactivate`
154. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
155. Verifikasi permintaan Inactivate membawa versi data `7`
156. Verifikasi dialog `Service Center Changed` tampil
157. Verifikasi isi dialog memuat `This service center was changed by someone else. Please review.`
158. Verifikasi tombol `[OK]` tampil di dialog
159. Klik `[OK]` pada dialog `Service Center Changed`
160. Verifikasi daftar dimuat ulang

### Activate dengan versi usang menampilkan dialog Service Center Changed
161. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K6
162. Klik `⋯` pada baris `Bengkel Maju Motor`
163. Pilih `Activate`
164. Klik `[Activate]` pada dialog `Activate Service Center`
165. Verifikasi permintaan Activate membawa versi data `3`
166. Verifikasi dialog `Service Center Changed` tampil
167. Klik `[OK]` pada dialog `Service Center Changed`
168. Verifikasi daftar dimuat ulang

### Delete dengan versi usang menampilkan dialog Service Center Changed
169. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K6
170. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
171. Pilih `Delete`
172. Klik `[Delete]` pada dialog `Delete Service Center`
173. Verifikasi permintaan Delete membawa versi data `4`
174. Verifikasi dialog `Service Center Changed` tampil
175. Klik `[OK]` pada dialog `Service Center Changed`
176. Verifikasi daftar dimuat ulang

### Edit dengan versi usang mengisi ulang form dengan data terbaru
177. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K7
178. Klik `⋯` pada baris `PT Sejuk Abadi Teknik`
179. Pilih `Edit`
180. Ganti isi Notes dengan `Kontrak servis AC dan chiller`
181. Klik `[Save]`
182. Verifikasi permintaan Edit membawa versi data `9`
183. Verifikasi dialog `Service Center Changed` tampil
184. Verifikasi dialog `Narrow Coverage` dan `Widen Coverage` tidak tampil
185. Klik `[OK]` pada dialog `Service Center Changed`
186. Verifikasi dialog `Edit Service Center` tetap terbuka
187. Verifikasi Notes menampilkan `Kontrak servis AC diperpanjang`

### Edit saat Brand dihapus dari master: Service Center Changed dan form terbaru
188. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K8
189. Klik `⋯` pada baris `CV Teknik Dingin Jaya`
190. Pilih `Edit`
191. Ganti isi Notes dengan `Kontrak servis pendingin ruangan`
192. Klik `[Save]`
193. Verifikasi dialog `Service Center Changed` tampil
194. Klik `[OK]` pada dialog `Service Center Changed`
195. Verifikasi dialog `Edit Service Center` tetap terbuka
196. Verifikasi Brands menampilkan `Daikin`
197. Verifikasi Brands tidak memuat `LG`

### Activate ditolak server karena Available to kosong: dialog info dengan OK
198. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K9
199. Klik `⋯` pada baris `Bengkel Maju Motor`
200. Pilih `Activate`
201. Klik `[Activate]` pada dialog `Activate Service Center`
202. Verifikasi dialog info dengan pesan `Add at least one group before activating.` tampil
203. Verifikasi tombol `[OK]` tampil di dialog
204. Klik `[OK]` pada dialog info
205. Verifikasi baris `Bengkel Maju Motor` tetap menampilkan Status `Inactive`

### Inactivate pada Service Center yang sudah dihapus pengguna lain
206. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K10
207. Klik `⋯` pada baris `CV Genset Prima`
208. Pilih `Inactivate`
209. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
210. Verifikasi toast `This service center is no longer available.` tampil
211. Verifikasi daftar dimuat ulang

### Activate pada Service Center yang sudah dihapus pengguna lain
212. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K10
213. Klik `⋯` pada baris `Bengkel Maju Motor`
214. Pilih `Activate`
215. Klik `[Activate]` pada dialog `Activate Service Center`
216. Verifikasi toast `This service center is no longer available.` tampil
217. Verifikasi daftar dimuat ulang

### Delete pada Service Center yang sudah dihapus pengguna lain
218. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K10
219. Klik `⋯` pada baris `Lab Kalibrasi Pratama`
220. Pilih `Delete`
221. Klik `[Delete]` pada dialog `Delete Service Center`
222. Verifikasi toast `This service center is no longer available.` tampil
223. Verifikasi daftar dimuat ulang
224. Verifikasi toast `Success, Lab Kalibrasi Pratama has been deleted.` tidak tampil

### Save Edit pada Service Center yang sudah dihapus pengguna lain
225. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K10
226. Klik `⋯` pada baris `PT Sejuk Abadi Teknik`
227. Pilih `Edit`
228. Ganti isi Notes dengan `Kontrak servis AC dan chiller`
229. Klik `[Save]`
230. Verifikasi toast `This service center is no longer available.` tampil
231. Verifikasi dialog `Edit Service Center` tertutup
232. Verifikasi daftar dimuat ulang

### Klik tambah saat batas tercapai menampilkan dialog Limit Reached
233. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K11
234. Klik `[+ Service Center]`
235. Verifikasi dialog `Service Center Limit Reached` tampil
236. Verifikasi isi dialog memuat `You've reached the platform limit of 1000 service centers. Contact support if you need a higher limit.`
237. Verifikasi tombol `[OK]` tampil di dialog
238. Klik `[OK]` pada dialog `Service Center Limit Reached`
239. Verifikasi dialog `Service Center Limit Reached` tertutup
240. Verifikasi dialog `Add Service Center` tidak tampil

### Klik tambah satu di bawah batas membuka form Create
241. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K12
242. Klik `[+ Service Center]`
243. Verifikasi dialog `Add Service Center` tampil
244. Verifikasi dialog `Service Center Limit Reached` tidak tampil

### Submit melampaui batas ditolak dengan dialog Limit Reached dan input terjaga
245. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K13
246. Klik `[+ Service Center]`
247. Verifikasi dialog `Add Service Center` tampil
248. Isi Name `Servis Pendingin Nusantara`
249. Centang `Routine` pada Service type
250. Pilih `Head Office` pada Available to
251. Isi City `Jakarta Selatan`
252. Isi Company phone dengan Dial Code `+62` dan nomor `81234567890`
253. Klik `[Submit]`
254. Verifikasi dialog `Service Center Limit Reached` tampil
255. Klik `[OK]` pada dialog `Service Center Limit Reached`
256. Verifikasi dialog `Add Service Center` tetap terbuka
257. Verifikasi Name menampilkan `Servis Pendingin Nusantara`
258. Verifikasi toast tidak tampil

### Download berhasil tanpa toast
259. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K14
260. Klik `Download`
261. Pilih `Download as CSV`
262. Verifikasi satu berkas terunduh
263. Verifikasi toast tidak tampil

### Inactivate dari halaman Detail dengan versi usang memuat ulang Detail
264. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K15
265. Klik `⋯` pada header halaman Detail
266. Pilih `Inactivate`
267. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
268. Verifikasi permintaan Inactivate membawa versi data `7`
269. Verifikasi dialog `Service Center Changed` tampil
270. Klik `[OK]` pada dialog `Service Center Changed`
271. Verifikasi halaman Detail `CV Genset Prima` dimuat ulang

### Activate dari halaman Detail dengan versi usang memuat ulang Detail
272. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K16
273. Klik `⋯` pada header halaman Detail
274. Pilih `Activate`
275. Klik `[Activate]` pada dialog `Activate Service Center`
276. Verifikasi permintaan Activate membawa versi data `3`
277. Verifikasi dialog `Service Center Changed` tampil
278. Klik `[OK]` pada dialog `Service Center Changed`
279. Verifikasi halaman Detail `Bengkel Maju Motor` dimuat ulang

### Delete dari halaman Detail dengan versi usang memuat ulang Detail
280. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K17
281. Klik `⋯` pada header halaman Detail
282. Pilih `Delete`
283. Klik `[Delete]` pada dialog `Delete Service Center`
284. Verifikasi permintaan Delete membawa versi data `4`
285. Verifikasi dialog `Service Center Changed` tampil
286. Klik `[OK]` pada dialog `Service Center Changed`
287. Verifikasi halaman Detail `Lab Kalibrasi Pratama` dimuat ulang

### Activate saat Available to kosong: dialog blok tampil saat klik
288. Tampilkan Dialog konfirmasi dan info status Service Center dengan kondisi K18
289. Klik `⋯` pada baris `Bengkel Cahaya Teknik`
290. Pilih `Activate`
291. Verifikasi dialog blok dengan pesan `Add at least one group before activating.` tampil
292. Verifikasi tombol `[OK]` tampil di dialog
293. Verifikasi permintaan Activate belum terkirim
294. Klik `[OK]` pada dialog blok
295. Verifikasi baris `Bengkel Cahaya Teknik` tetap menampilkan Status `Inactive`
