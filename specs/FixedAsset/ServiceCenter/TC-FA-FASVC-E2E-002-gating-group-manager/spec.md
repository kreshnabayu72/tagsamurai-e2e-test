---
id: TC-FA-FASVC-E2E-002-gating-group-manager
title: "Gating Group Manager: Cakupan Baca dan Kelola, All groups hanya Group Manager root"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "RA-FASVC-01", "RA-FASVC-02", "RA-FASVC-03", "RA-FASVC-04", "RA-FASVC-05", "FASVC-LOGIC-08a", "FASVC-LOGIC-08d", "FASVC-LOGIC-08e", "FASVC-LOGIC-08f", "FASVC-LOGIC-08g", "FASVC-LOGIC-08h", "FASVC-LOGIC-08i", "§Aturan Logika Modul#p4", "§2.1#b2"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [5, 59, 74, 101, 111]
  "§2.1#r2": [24, 39, 50, 89]
  "§2.1#r3": [68, 69, 124, 125, 130, 131, 138, 139, 190, 191, 197, 198]
  "§2.1#r4": [144, 145, 192, 199]
  "§2.1#r5": 10
  "§4.8#r1": [3, 72]
  "§4.8#r2": [53, 96, 106, 189, 196]
  "§4.8#r3": [6, 75]
  "§4.8#r4": [54, 55, 97, 98, 107, 108, 116, 117, 191, 198]
  "§4.8#r5": [133, 138, 190, 197]
  "§4.8#r6": [56, 99, 109, 118, 144, 192, 199]
  "§4.8#r7": [7, 76]
  "§4.8#r8": [8, 13, 77]
  "RA-FASVC-01": [53, 96, 106, 189, 196]
  "RA-FASVC-02": [54, 116, 191, 198]
  "RA-FASVC-03": [57, 119, 133, 136, 190, 197]
  "RA-FASVC-04": [55, 117, 128, 134]
  "RA-FASVC-05": [56, 118, 142, 192, 199]
  "FASVC-LOGIC-08a": [26, 59, 91, 92, 93, 94]
  "FASVC-LOGIC-08d": [24, 39, 50, 89]
  "FASVC-LOGIC-08e": [82, 84]
  "FASVC-LOGIC-08f": [19, 27, 83]
  "FASVC-LOGIC-08g": [55, 65, 68, 107, 108, 109, 116, 117, 118, 121, 124, 130, 138, 144, 190, 191, 192, 197, 198, 199]
  "FASVC-LOGIC-08h": [96, 97, 98, 99, 106, 107, 108, 109, 189, 190, 191, 192, 196, 197, 198, 199]
  "FASVC-LOGIC-08i": [60, 102, 112]
  "§Aturan Logika Modul#p4": [19, 27, 55, 60, 68, 83, 107, 108, 109, 112, 153, 184]
  "§2.1#b2": [91, 92, 94, 97, 98, 99]
anchor: [170, 175, 183]
coverage:
  web: automated
---

# Gating Group Manager: Cakupan Baca dan Kelola, All groups hanya Group Manager root

## Prerequisites
- Aktor: Group Manager root `Gita Root {runId}` (ditugaskan pada `Head Office`) dan Group Manager `Bima Surabaya {runId}` (ditugaskan pada `Branch Surabaya`).
- Layar awal: Dashboard Fixed Asset.
- Data:
  - DU-002-1: Group `Head Office`, node root pohon Group entitas aktor.
  - DU-002-2: Group `Branch Surabaya`, anak dari `Head Office`.
  - DU-002-3: Group `Branch Malang`, anak dari `Head Office`.
  - DU-002-4: Aktor `Gita Root {runId}` dengan Role `Group Manager`, cakupan `Head Office` (node root pohon Group).
  - DU-002-5: Aktor `Bima Surabaya {runId}` dengan Role `Group Manager`, cakupan `Branch Surabaya`.
  - DU-002-6: Service Center `Servis Semua Cabang {runId}`, Service type `Routine`, Available to `All groups`, City `Surabaya`, Company email `layanan@teknikmandiri.co.id`, dibuat oleh `Gita Root {runId}` dan diubah City-nya menjadi `Sidoarjo`. Usage `0`.
  - DU-002-7: Service Center `Servis Dua Cabang {runId}`, Service type `Routine`, Available to `Branch Surabaya` dan `Branch Malang`, City `Surabaya`, Company email `layanan@duacabang.co.id`, dibuat oleh `Gita Root {runId}`. Usage `0`.
  - DU-002-8: Service Center `Servis Malang {runId}`, Service type `Routine`, Available to `Branch Malang`, City `Malang`, Company email `kontak@servismalang.co.id`, dibuat oleh `Gita Root {runId}`. Usage `0`.
  - DU-002-9: Service Center `Servis Surabaya {runId}`, Service type `Routine`, Available to `Branch Surabaya`, City `Surabaya`, Company email `info@servissurabaya.co.id`, dibuat oleh `Bima Surabaya {runId}`, diubah City-nya menjadi `Gresik`, di-Inactivate, di-Activate, lalu dihapus. Usage `0`.
  - DU-002-10: Service Center `Servis Edit Surabaya {runId}`, Service type `Routine`, Available to `Branch Surabaya`, City `Surabaya`, Company email `layanan@editsurabaya.co.id`, dibuat oleh `Gita Root {runId}`. Status `Active`. Usage `0`.
  - Status akhir `Servis Dua Cabang {runId}` dan `Servis Semua Cabang {runId}` adalah `Inactive`, setelah di-Inactivate oleh `Gita Root {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif untuk entitas aktor.
  - Akun `Gita Root {runId}` dan `Bima Surabaya {runId}` aktif dan kredensialnya disediakan fase 2.
  - Master Data Count Limit bernilai `1000` dan entitas aktor berisi kurang dari 1.000 Service Center.

## Test Steps

### Menu Service Center dan toolbar bagi Group Manager root
1. Masuk sebagai `Gita Root {runId}`
2. Buka menu `Add-ons` pada sidebar
3. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
4. Klik `Service Center`
5. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
6. Verifikasi tombol `[+ Service Center]` tampil
7. Verifikasi tombol `[Download]` tampil
8. Verifikasi tombol `[Changelog]` tampil

### Download menyediakan pilihan unduhan
9. Klik `[Download]`
10. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
11. Tutup popover Download

### Changelog gabungan terbuka
12. Klik `[Changelog]`
13. Verifikasi modal `Changelog: Service Center` terbuka
14. Klik ikon close pada modal Changelog

### Create dengan All groups oleh Group Manager root
15. Klik `[+ Service Center]`
16. Isi Name `Servis Semua Cabang {runId}`
17. Centang Service type `Routine`
18. Klik field Available to
19. Verifikasi node `All groups` tampil pada tree Available to dan tercentang
20. Klik `[Cancel]` pada dialog tree Available to
21. Isi City `Surabaya`
22. Isi Company email `layanan@teknikmandiri.co.id`
23. Klik `[Submit]`
24. Verifikasi toast `Success, Servis Semua Cabang {runId} has been added.` tampil
25. Ketik Search `Servis Semua Cabang {runId}`, tekan Enter
26. Verifikasi baris `Servis Semua Cabang {runId}` tampil di tabel
27. Verifikasi kolom Available To pada baris itu menampilkan `All groups`

### Create untuk dua Branch oleh Group Manager root
28. Klik `[+ Service Center]`
29. Isi Name `Servis Dua Cabang {runId}`
30. Centang Service type `Routine`
31. Klik field Available to
32. Hapus centang node `All groups`
33. Centang node `Branch Surabaya`
34. Centang node `Branch Malang`
35. Klik `[Select]`
36. Isi City `Surabaya`
37. Isi Company email `layanan@duacabang.co.id`
38. Klik `[Submit]`
39. Verifikasi toast `Success, Servis Dua Cabang {runId} has been added.` tampil

### Create untuk Branch Malang saja oleh Group Manager root
40. Klik `[+ Service Center]`
41. Isi Name `Servis Malang {runId}`
42. Centang Service type `Routine`
43. Klik field Available to
44. Hapus centang node `All groups`
45. Centang node `Branch Malang`
46. Klik `[Select]`
47. Isi City `Malang`
48. Isi Company email `kontak@servismalang.co.id`
49. Klik `[Submit]`
50. Verifikasi toast `Success, Servis Malang {runId} has been added.` tampil

### Group Manager root mengelola Service Center All groups
51. Ketik Search `Servis Semua Cabang {runId}`, tekan Enter
52. Klik `⋯` pada baris `Servis Semua Cabang {runId}`
53. Verifikasi aksi `Detail` tampil
54. Verifikasi aksi `Edit` tampil
55. Verifikasi aksi `Inactivate` tampil
56. Verifikasi aksi `Delete` tampil dan tidak disabled
57. Verifikasi aksi `Activate` tidak tampil
58. Klik `Detail`
59. Verifikasi halaman Detail menampilkan nama `Servis Semua Cabang {runId}`
60. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil
61. Klik breadcrumb `Service Center`

### Group Manager root mengedit Service Center All groups
62. Ganti isi kotak search dengan `Servis Semua Cabang {runId}`, tekan Enter
63. Klik `⋯` pada baris `Servis Semua Cabang {runId}`
64. Klik `Edit`
65. Verifikasi dialog `Edit Service Center` terbuka
66. Ganti isi City dengan `Sidoarjo`
67. Klik `[Save]`
68. Verifikasi toast `Success, Servis Semua Cabang {runId} has been updated.` tampil
69. Verifikasi kolom City pada baris `Servis Semua Cabang {runId}` menampilkan `Sidoarjo`

### Menu dan toolbar bagi Group Manager non-root
70. Masuk sebagai `Bima Surabaya {runId}`
71. Buka menu `Add-ons` pada sidebar
72. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
73. Klik `Service Center`
74. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
75. Verifikasi tombol `[+ Service Center]` tampil
76. Verifikasi tombol `[Download]` tampil
77. Verifikasi tombol `[Changelog]` tampil

### Create dibatasi cakupan Group pembuat tanpa All groups
78. Klik `[+ Service Center]`
79. Isi Name `Servis Surabaya {runId}`
80. Centang Service type `Routine`
81. Klik field Available to
82. Verifikasi node `Branch Surabaya` tampil pada tree Available to dan tercentang
83. Verifikasi node `All groups` tidak tampil pada tree Available to
84. Verifikasi node `Branch Malang` tidak tampil pada tree Available to
85. Klik `[Cancel]` pada dialog tree Available to
86. Isi City `Surabaya`
87. Isi Company email `info@servissurabaya.co.id`
88. Klik `[Submit]`
89. Verifikasi toast `Success, Servis Surabaya {runId} has been added.` tampil

### Cakupan baca mengikuti irisan Available to dengan cakupan Group
90. Ketik Search `{runId}`, tekan Enter
91. Verifikasi baris `Servis Surabaya {runId}` tampil di tabel
92. Verifikasi baris `Servis Dua Cabang {runId}` tampil di tabel
93. Verifikasi baris `Servis Semua Cabang {runId}` tampil di tabel
94. Verifikasi baris `Servis Malang {runId}` tidak tampil di tabel

### Service Center sebagian di luar cakupan kelola hanya punya aksi Detail
95. Klik `⋯` pada baris `Servis Dua Cabang {runId}`
96. Verifikasi aksi `Detail` tampil
97. Verifikasi aksi `Edit` tidak tampil
98. Verifikasi aksi `Inactivate` tidak tampil
99. Verifikasi aksi `Delete` tidak tampil
100. Klik `Detail`
101. Verifikasi halaman Detail menampilkan nama `Servis Dua Cabang {runId}`
102. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tampil
103. Klik breadcrumb `Service Center`

### Service Center All groups read-only bagi Group Manager non-root
104. Ketik Search `Servis Semua Cabang {runId}`, tekan Enter
105. Klik `⋯` pada baris `Servis Semua Cabang {runId}`
106. Verifikasi aksi `Detail` tampil
107. Verifikasi aksi `Edit` tidak tampil
108. Verifikasi aksi `Inactivate` tidak tampil
109. Verifikasi aksi `Delete` tidak tampil
110. Klik `Detail`
111. Verifikasi halaman Detail menampilkan nama `Servis Semua Cabang {runId}`
112. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tampil
113. Klik breadcrumb `Service Center`

### Group Manager non-root mengedit Service Center dalam cakupan kelola
114. Ganti isi kotak search dengan `Servis Surabaya {runId}`, tekan Enter
115. Klik `⋯` pada baris `Servis Surabaya {runId}`
116. Verifikasi aksi `Edit` tampil
117. Verifikasi aksi `Inactivate` tampil
118. Verifikasi aksi `Delete` tampil dan tidak disabled
119. Verifikasi aksi `Activate` tidak tampil
120. Klik `Edit`
121. Verifikasi dialog `Edit Service Center` terbuka
122. Ganti isi City dengan `Gresik`
123. Klik `[Save]`
124. Verifikasi toast `Success, Servis Surabaya {runId} has been updated.` tampil
125. Verifikasi kolom City pada baris `Servis Surabaya {runId}` menampilkan `Gresik`

### Group Manager non-root meng-Inactivate dan meng-Activate
126. Klik `⋯` pada baris `Servis Surabaya {runId}`
127. Klik `Inactivate`
128. Verifikasi dialog `Inactivate Service Center` tampil
129. Klik `[Inactivate]`
130. Verifikasi toast `Success, Servis Surabaya {runId} has been inactivated.` tampil
131. Verifikasi kolom Status pada baris `Servis Surabaya {runId}` menampilkan `Inactive`
132. Klik `⋯` pada baris `Servis Surabaya {runId}`
133. Verifikasi aksi `Activate` tampil dan tidak disabled
134. Verifikasi aksi `Inactivate` tidak tampil
135. Klik `Activate`
136. Verifikasi dialog `Activate Service Center` tampil
137. Klik `[Activate]`
138. Verifikasi toast `Success, Servis Surabaya {runId} has been activated.` tampil
139. Verifikasi kolom Status pada baris `Servis Surabaya {runId}` menampilkan `Active`

### Group Manager non-root menghapus Service Center dalam cakupan kelola
140. Klik `⋯` pada baris `Servis Surabaya {runId}`
141. Klik `Delete`
142. Verifikasi dialog `Delete Service Center` tampil
143. Klik `[Delete]`
144. Verifikasi toast `Success, Servis Surabaya {runId} has been deleted.` tampil
145. Verifikasi empty state `No results found` tampil untuk Search `Servis Surabaya {runId}`

### Group Manager root mempertahankan All groups pada dialog Edit
146. Masuk sebagai `Gita Root {runId}`
147. Buka menu `Add-ons` pada sidebar
148. Klik `Service Center`
149. Ketik Search `Servis Semua Cabang {runId}`, tekan Enter
150. Klik `⋯` pada baris `Servis Semua Cabang {runId}`
151. Klik `Edit`
152. Klik field Available to
153. Verifikasi node `All groups` tampil pada tree Available to dan tercentang
154. Klik `[Cancel]` pada dialog tree Available to
155. Klik `✕` pada dialog `Edit Service Center` yang belum diubah

### Group Manager root menyiapkan Service Center sebagai pemicu
156. Klik `[+ Service Center]`
157. Isi Name `Servis Edit Surabaya {runId}`
158. Centang Service type `Routine`
159. Klik field Available to
160. Hapus centang node `All groups`
161. Centang node `Branch Surabaya`
162. Klik `[Select]`
163. Isi City `Surabaya`
164. Isi Company email `layanan@editsurabaya.co.id`
165. Klik `[Submit]`
166. Ganti isi kotak search dengan `Servis Dua Cabang {runId}`, tekan Enter
167. Klik `⋯` pada baris `Servis Dua Cabang {runId}`
168. Klik `Inactivate`
169. Klik `[Inactivate]`
170. Verifikasi kolom Status pada baris `Servis Dua Cabang {runId}` menampilkan `Inactive`
171. Ganti isi kotak search dengan `Servis Semua Cabang {runId}`, tekan Enter
172. Klik `⋯` pada baris `Servis Semua Cabang {runId}`
173. Klik `Inactivate`
174. Klik `[Inactivate]`
175. Verifikasi kolom Status pada baris `Servis Semua Cabang {runId}` menampilkan `Inactive`

### Group Manager non-root tidak bisa menetapkan All groups lewat dialog Edit
176. Masuk sebagai `Bima Surabaya {runId}`
177. Buka menu `Add-ons` pada sidebar
178. Klik `Service Center`
179. Ketik Search `Servis Edit Surabaya {runId}`, tekan Enter
180. Klik `⋯` pada baris `Servis Edit Surabaya {runId}`
181. Klik `Edit`
182. Klik field Available to
183. Verifikasi node `Branch Surabaya` tampil pada tree Available to dan tercentang
184. Verifikasi node `All groups` tidak tampil pada tree Available to
185. Klik `[Cancel]` pada dialog tree Available to
186. Klik `✕` pada dialog `Edit Service Center` yang belum diubah

### Service Center Inactive sebagian di luar cakupan kelola tanpa aksi Activate bagi Group Manager non-root
187. Ganti isi kotak search dengan `Servis Dua Cabang {runId}`, tekan Enter
188. Klik `⋯` pada baris `Servis Dua Cabang {runId}`
189. Verifikasi aksi `Detail` tampil
190. Verifikasi aksi `Activate` tidak tampil
191. Verifikasi aksi `Edit` tidak tampil
192. Verifikasi aksi `Delete` tidak tampil
193. Tutup menu aksi baris
194. Ganti isi kotak search dengan `Servis Semua Cabang {runId}`, tekan Enter
195. Klik `⋯` pada baris `Servis Semua Cabang {runId}`
196. Verifikasi aksi `Detail` tampil
197. Verifikasi aksi `Activate` tidak tampil
198. Verifikasi aksi `Edit` tidak tampil
199. Verifikasi aksi `Delete` tidak tampil
