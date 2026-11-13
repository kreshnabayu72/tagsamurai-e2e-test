---
id: TC-FA-FAREG-UI-008-draft-dialog-delete
title: "Sub tab Draft: dialog Delete Draft, dialog blok, dan toast hapus"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["D-REG-01", "D-REG-27", "D-REG-28", "T-REG-04", "T-REG-06", "T-REG-12", "T-REG-13", "T-REG-18", "V-REG-19", "V-REG-22", "§4.8#p2", "§7.2#p1", "§9.6#r6", "§9.6#r7", "EB-ERR-1@delete-draft", "EB-ERR-2@dialog-delete-draft", "EB-FB-1@delete-draft", "EB-FB-2@cancel-dialog"]
smoke: []
dependsOn: []
trace:
  D-REG-01: [3, 4, 5, 6, 9, 65, 66, 67, 74, 75, 76, 77, 78, 79, 88, 89, 90, 91, 92, 93, 114, 130, 131, 132, 133, 149, 150]
  D-REG-27: [41, 42, 43, 46]
  D-REG-28: [102, 103, 104, 105, 106, 107, 108, 123, 124, 157, 158, 159, 161, 162, 163, 170, 171, 172, 173, 174]
  T-REG-04: [13, 81]
  T-REG-06: 37
  T-REG-12: [50, 140]
  T-REG-13: 58
  T-REG-18: [95, 116]
  V-REG-19: [41, 42]
  V-REG-22: 37
  "§4.8#p2": [39, 41]
  "§7.2#p1": [41, 44]
  "§9.6#r6": [13, 50]
  "§9.6#r7": [81, 95, 140]
  EB-ERR-1@delete-draft: [50, 51, 52, 54, 58, 59, 60, 141]
  EB-ERR-2@dialog-delete-draft: [22, 24, 26, 27, 28, 32, 33]
  EB-FB-1@delete-draft: [13, 50]
  EB-FB-2@cancel-dialog: [18, 19]
anchor: [17]
coverage:
  web: automated
---

# Sub tab Draft: dialog Delete Draft, dialog blok, dan toast hapus

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Komponen: Sub tab `Draft` (TBL-REG-01)
- Data:
  - DU-008-1: batch Draft Group `Gudang 1`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-09T08:15:00Z`.
  - DU-008-2: batch Draft Group `Gudang 2`, Origin `—`, Total Asset `5`, Progress `60%`, Requested By `Siti Nurbaya`, Last Updated `2026-11-08T16:40:00Z`, dikunci sesi edit oleh `Dewi Anggraini`.
  - DU-008-3: batch Draft yang Group-nya belum dipilih, Origin `—`, Total Asset `8`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-06T13:10:00Z`.
  - DU-008-4: batch Draft Group `Kantor Pusat`, Origin `—`, Total Asset `30`, Progress `100%`, Requested By `Agus Prasetyo`, Last Updated `2026-11-07T09:05:00Z`.
  - DU-008-5: 30 batch Draft Group `Gudang Distribusi Regional Jawa Barat Wilayah Kerja {n}` (n = 1 sampai 30), Origin `—`, Total Asset `4`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-05T10:00:00Z`.
  - DU-008-6: batch Draft Group `Gudang 6`, Origin `—`, Total Asset `7`, Progress `0%`, Requested By `Hadi Kusuma`, Last Updated `2026-11-04T14:45:00Z`, sudah dihapus pihak lain.
  - DU-008-7: batch Draft Group `Gudang 7`, Origin `—`, Total Asset `9`, Progress `0%`, Requested By `Budi Santoso`, Last Updated `2026-11-03T08:00:00Z`, aktor tidak memiliki hak menghapusnya.
  - Pertanyaan konfirmasi bulk yang diharapkan `Are you sure you want to delete them?`, dari `Are you sure you want to delete it?` dalam bentuk jamak.
- Kondisi:
  - K1: daftar berisi DU-008-1, DU-008-3, dan DU-008-4; semua dapat dihapus; hapus berhasil.
  - K2: sama dengan K1; hapus DU-008-1 gagal karena error server pada percobaan pertama dan berhasil pada percobaan kedua.
  - K3: sama dengan K1; hapus gagal karena timeout.
  - K4: sama dengan K1; DU-008-1 sudah dihapus pihak lain sehingga hapus ditolak.
  - K5: daftar berisi DU-008-2.
  - K6: daftar berisi DU-008-1, DU-008-2, dan DU-008-6; hanya DU-008-1 yang dapat dihapus; hapus DU-008-1 berhasil.
  - K7: daftar berisi DU-008-2, DU-008-6, dan DU-008-7; tidak satu pun dapat dihapus.
  - K8: daftar berisi DU-008-1 dan DU-008-4; keduanya dapat dihapus saat dialog terbuka, lalu DU-008-4 dikunci sesi edit oleh `Dewi Anggraini` sebelum `[Delete]` diklik; hapus DU-008-1 berhasil dan DU-008-4 dilewati.
  - K9: sama dengan K8, tetapi DU-008-1 juga dikunci sesi edit oleh `Dewi Anggraini` sebelum `[Delete]` diklik; tidak satu pun dapat dihapus.
  - K10: daftar berisi DU-008-5; hapus berhasil.
  - K11: sama dengan K1; hapus massal gagal karena error server.
  - K12: daftar berisi DU-008-1, DU-008-2, DU-008-6, dan DU-008-7; hanya DU-008-1 yang dapat dihapus; DU-008-2 dikunci user lain, DU-008-6 sudah dihapus pihak lain, dan DU-008-7 tanpa hak hapus.
  - K13: daftar berisi DU-008-5; seluruh batch dikunci sesi edit oleh `Dewi Anggraini` sebelum `[Delete]` diklik, sehingga tidak satu pun dapat dihapus.

## Test Steps

### Dialog Delete Draft untuk satu batch
1. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
2. Klik aksi `Delete` pada baris `Gudang 1`
3. Verifikasi judul dialog `Delete Draft`
4. Verifikasi dialog memuat bullet `Gudang 1 · 12 assets`
5. Verifikasi dialog memuat `Are you sure you want to delete it? This action cannot be undone.`
6. Verifikasi dialog memuat tombol `[Cancel]` dan `[Delete]`

### Batch tanpa Group memakai No group yet pada bullet
7. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
8. Klik aksi `Delete` pada baris dengan Total Asset `8`
9. Verifikasi dialog memuat bullet `No group yet · 8 assets`

### Hapus satu batch berhasil
10. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
11. Klik aksi `Delete` pada baris `Gudang 1`
12. Klik `[Delete]` pada dialog
13. Verifikasi toast `Success, draft has been deleted.`

### Cancel tidak menghapus dan tanpa toast
14. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
15. Klik aksi `Delete` pada baris `Gudang 1`
16. Klik `[Cancel]` pada dialog
17. Verifikasi dialog Delete Draft tertutup
18. Verifikasi baris `Gudang 1` tampil sesudah Cancel
19. Verifikasi toast tidak tampil sesudah Cancel pada dialog Delete Draft

### Esc menutup dialog, fokus terkunci di dialog dan kembali ke pemicu
20. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
21. Klik aksi `Delete` pada baris `Gudang 1`
22. Verifikasi fokus berada di dalam dialog
23. Tekan `Tab` lima kali
24. Verifikasi fokus tetap berada di dalam dialog
25. Tekan `Esc`
26. Verifikasi dialog Delete Draft tertutup
27. Verifikasi fokus kembali ke aksi `Delete` pada baris `Gudang 1`
28. Verifikasi baris `Gudang 1` tampil sesudah Esc

### Klik ganda Delete menghapus sekali dengan satu toast
29. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
30. Klik aksi `Delete` pada baris `Gudang 1`
31. Klik ganda `[Delete]` pada dialog
32. Verifikasi toast `Success, draft has been deleted.` tampil
33. Verifikasi hanya satu toast yang tampil

### Draft sudah dihapus pihak lain
34. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K4
35. Klik aksi `Delete` pada baris `Gudang 1`
36. Klik `[Delete]` pada dialog
37. Verifikasi toast `This draft is no longer available.`

### Batch dikunci user lain tidak Disabled dan membuka dialog blok
38. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K5
39. Verifikasi aksi `Delete` pada baris `Gudang 2` enabled
40. Klik aksi `Delete` pada baris `Gudang 2`
41. Verifikasi judul dialog `Draft Is Being Edited`
42. Verifikasi isi dialog `Dewi Anggraini is editing this draft. It can't be deleted right now.`
43. Verifikasi dialog memuat tombol `[OK]`
44. Verifikasi judul dialog `Cannot Delete Draft` tidak tampil
45. Klik `[OK]`
46. Verifikasi dialog blok tertutup

### Hapus gagal karena error server lalu berhasil pada percobaan berikutnya
47. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
48. Klik aksi `Delete` pada baris `Gudang 1`
49. Klik `[Delete]` pada dialog
50. Verifikasi toast `Error, failed to delete draft.`
51. Verifikasi dialog Delete Draft tetap terbuka
52. Verifikasi tombol `[Delete]` enabled
53. Klik `[Delete]` pada dialog
54. Verifikasi toast `Success, draft has been deleted.`

### Hapus gagal karena timeout
55. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K3
56. Klik aksi `Delete` pada baris `Gudang 1`
57. Klik `[Delete]` pada dialog
58. Verifikasi toast `Connection problem. Please try again.`
59. Verifikasi dialog Delete Draft tetap terbuka
60. Verifikasi tombol `[Delete]` enabled

### Bulk Delete dengan satu batch terpilih memakai dialog tunggal
61. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
62. Centang baris `Gudang 1`
63. Klik `Bulk Action`
64. Klik `Delete`
65. Verifikasi judul dialog `Delete Draft`
66. Verifikasi dialog memuat bullet `Gudang 1 · 12 assets`
67. Verifikasi dialog memuat `Are you sure you want to delete it? This action cannot be undone.`

### Bulk Delete beberapa batch memakai dialog jamak
68. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
69. Centang baris `Gudang 1`
70. Centang baris `Kantor Pusat`
71. Centang baris dengan Total Asset `8`
72. Klik `Bulk Action`
73. Klik `Delete`
74. Verifikasi judul dialog `Delete Drafts`
75. Verifikasi dialog memuat bullet `Gudang 1 · 12 assets`
76. Verifikasi dialog memuat bullet `Kantor Pusat · 30 assets`
77. Verifikasi dialog memuat bullet `No group yet · 8 assets`
78. Verifikasi dialog memuat `Are you sure you want to delete them?`
79. Verifikasi dialog memuat `This action cannot be undone.`
80. Klik `[Delete]` pada dialog
81. Verifikasi toast `Success, draft has been deleted.`

### Bulk Delete campuran dibagi dua kelompok
82. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K6
83. Centang baris `Gudang 1`
84. Centang baris `Gudang 2`
85. Centang baris `Gudang 6`
86. Klik `Bulk Action`
87. Klik `Delete`
88. Verifikasi dialog memuat label kelompok `The following will be deleted:`
89. Verifikasi kelompok tersebut memuat bullet `Gudang 1 · 12 assets`
90. Verifikasi dialog memuat label kelompok `The following can't be deleted and will be skipped:`
91. Verifikasi kelompok tersebut memuat bullet `Gudang 2 · 5 assets` dan `Gudang 6 · 7 assets`
92. Verifikasi dialog memuat tombol `[Cancel]` dan `[Continue]`[^drift-1]
93. Verifikasi dialog memuat `Are you sure you want to continue?`[^drift-1]
94. Klik `[Continue]` pada dialog
95. Verifikasi toast `Success, draft has been deleted. Some items were skipped.`

### Bulk Delete tanpa batch yang dapat dihapus membuka dialog blok
96. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K7
97. Centang baris `Gudang 2`
98. Centang baris `Gudang 6`
99. Centang baris `Gudang 7`
100. Klik `Bulk Action`
101. Klik `Delete`
102. Verifikasi judul dialog `Cannot Delete Drafts`
103. Verifikasi dialog memuat bullet `Gudang 2 · 5 assets`
104. Verifikasi dialog memuat bullet `Gudang 6 · 7 assets`
105. Verifikasi dialog memuat bullet `Gudang 7 · 9 assets`
106. Verifikasi isi dialog `None of the selected drafts can be deleted right now. They are being edited by another user, already deleted, or you don't have permission.`
107. Verifikasi dialog memuat tombol `[OK]`
108. Verifikasi toast tidak tampil saat dialog blok `Cannot Delete Drafts` muncul

### Batch menjadi tidak dapat dihapus saat Delete diklik, sebagian dilewati
109. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K8
110. Centang baris `Gudang 1`
111. Centang baris `Kantor Pusat`
112. Klik `Bulk Action`
113. Klik `Delete`
114. Verifikasi judul dialog `Delete Drafts`
115. Klik `[Delete]` pada dialog
116. Verifikasi toast `Success, draft has been deleted. Some items were skipped.`

### Batch menjadi tidak dapat dihapus saat Delete diklik, semua ditolak
117. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K9
118. Centang baris `Gudang 1`
119. Centang baris `Kantor Pusat`
120. Klik `Bulk Action`
121. Klik `Delete`
122. Klik `[Delete]` pada dialog
123. Verifikasi judul dialog `Cannot Delete Drafts`
124. Verifikasi toast tidak tampil saat semua batch ditolak

### Daftar bullet panjang tidak diringkas
125. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K10
126. Pilih ukuran halaman `50`
127. Centang checkbox header
128. Klik `Bulk Action`
129. Klik `Delete`
130. Verifikasi dialog memuat bullet `Gudang Distribusi Regional Jawa Barat Wilayah Kerja 1 · 4 assets`
131. Verifikasi dialog memuat bullet `Gudang Distribusi Regional Jawa Barat Wilayah Kerja 30 · 4 assets`
132. Verifikasi daftar bullet pada dialog dapat digulir
133. Verifikasi dialog tidak memuat ringkasan `...and N more`

### Bulk Delete gagal karena error server
134. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K11
135. Centang baris `Gudang 1`
136. Centang baris `Kantor Pusat`
137. Klik `Bulk Action`
138. Klik `Delete`
139. Klik `[Delete]` pada dialog
140. Verifikasi toast `Error, failed to delete draft.`
141. Verifikasi dialog Delete Drafts tetap terbuka

### Bulk Delete campuran memuat batch tanpa hak pada kelompok yang dilewati
142. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K12
143. Centang baris `Gudang 1`
144. Centang baris `Gudang 2`
145. Centang baris `Gudang 6`
146. Centang baris `Gudang 7`
147. Klik `Bulk Action`
148. Klik `Delete`
149. Verifikasi kelompok `The following will be deleted:` memuat bullet `Gudang 1 · 12 assets`
150. Verifikasi kelompok `The following can't be deleted and will be skipped:` memuat bullet `Gudang 7 · 9 assets`

### Dialog blok bulk yang semuanya ditolak memuat daftar dan mempertahankan seleksi
151. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K9
152. Centang baris `Gudang 1`
153. Centang baris `Kantor Pusat`
154. Klik `Bulk Action`
155. Klik `Delete`
156. Klik `[Delete]` pada dialog
157. Verifikasi dialog `Cannot Delete Drafts` memuat bullet `Gudang 1 · 12 assets`
158. Verifikasi dialog `Cannot Delete Drafts` memuat bullet `Kantor Pusat · 30 assets`
159. Verifikasi isi dialog `None of the selected drafts can be deleted right now. They are being edited by another user, already deleted, or you don't have permission.`
160. Klik `[OK]`
161. Verifikasi baris `Gudang 1` tetap tercentang
162. Verifikasi baris `Kantor Pusat` tetap tercentang
163. Verifikasi bar Bulk Action tetap tampil

### Dialog blok dengan daftar panjang tidak diringkas
164. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K13
165. Pilih ukuran halaman `50`
166. Centang checkbox header
167. Klik `Bulk Action`
168. Klik `Delete`
169. Klik `[Delete]` pada dialog
170. Verifikasi judul dialog `Cannot Delete Drafts`
171. Verifikasi dialog memuat bullet `Gudang Distribusi Regional Jawa Barat Wilayah Kerja 1 · 4 assets`
172. Verifikasi dialog memuat bullet `Gudang Distribusi Regional Jawa Barat Wilayah Kerja 30 · 4 assets`
173. Verifikasi daftar bullet pada dialog dapat digulir
174. Verifikasi dialog tidak memuat ringkasan `...and N more`


[^drift-1]: Drift PRD vs foundation. PRD §7.2 `D-REG-01`: pilihan campuran dibagi dua kelompok bullet dengan pertanyaan konfirmasi untuk kelompok pertama, tombol `[Cancel]` `[Delete]`. foundation `functions/toast-copy.md` Aturan Terkunci #10: bulk dengan outcome campuran memakai `Are you sure you want to continue?` dan tombol `[Continue]`. Diasersi: foundation, karena dialog konfirmasi bulk adalah pola bersama (SB-4).
