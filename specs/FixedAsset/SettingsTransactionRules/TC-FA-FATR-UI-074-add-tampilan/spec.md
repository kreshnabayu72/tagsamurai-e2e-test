---
id: TC-FA-FATR-UI-074-add-tampilan
title: "Dialog Add override: tampilan awal, Scope, Target, dan baris Field + Value"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§Aturan Logika Modul#r49, §Aturan Logika Modul#r50, §Aturan Logika Modul#r51, §Aturan Logika Modul#r52, §Aturan Logika Modul#r54, §Aturan Logika Modul#r69, §Aturan Logika Modul#r102, §4.1#r11, §4.1#r309, §4.1#r310, §4.1#r311, §4.1#r312, §4.1#r313, §4.1#r314, §4.1#r315, §4.1#r316, §4.1#r317, §4.1#r318, §4.1#r320, §4.1#r321, §4.1#r322, §4.1#r323, §4.1#r324, §4.1#r325, §4.1#r326, §4.1#r327, §4.1#r328, §4.1#r329, §4.1#r330, §4.1#r331, §4.1#r332, §4.1#r333, §4.1#r334, §4.1#r335, §4.1#r345, §4.1#p67, D-02, §9.2#b84, §9.2#b86, §9.2#b87, §9.2#b150, §9.2#b155, §9.2#b197, §9.4.2#r8, §9.4.2#r25, §9.4.4#r23, §9.5#r13, §9.5#r14, §9.5#r19, §9.5#r20, §9.5#r26, §9.9#r13, §9.9#r14, §9.9#r15, §9.9#r16, §9.10.1#b5, §9.10.2#b5, §10#b2, EB-FRM-7@add-override, EB-TBL-5@hapus-baris-field, FLD-43]
smoke: []
dependsOn: []
trace:
  §Aturan Logika Modul#r49: 5
  §Aturan Logika Modul#r50: 46
  §Aturan Logika Modul#r51: 59
  §Aturan Logika Modul#r52: 69
  §Aturan Logika Modul#r54: 21
  §Aturan Logika Modul#r69: 48
  §Aturan Logika Modul#r102: [47, 48, 49]
  §4.1#r11: [4, 15, 21, 22, 170, 171]
  §4.1#r309: 28
  §4.1#r310: [15, 31, 38]
  §4.1#r311: 17
  §4.1#r312: [33, 40]
  §4.1#r313: 26
  §4.1#r314: [21, 22]
  §4.1#r315: [23, 25]
  §4.1#r316: 36
  §4.1#r317: 43
  §4.1#r318: 8
  §4.1#r320: 64
  §4.1#r321: [69, 75, 140]
  §4.1#r322: 82
  §4.1#r323: 72
  §4.1#r324: 73
  §4.1#r325: 92
  §4.1#r326: 93
  §4.1#r327: 46
  §4.1#r328: [75, 78]
  §4.1#r329: 95
  §4.1#r330: [46, 146, 150, 186, 187, 188, 191]
  §4.1#r331: [59, 61, 64, 66]
  §4.1#r332: 98
  §4.1#r333: 100
  §4.1#r334: 86
  §4.1#r335: 6
  §4.1#r345: 66
  §4.1#p67: [23, 25]
  D-02: [2, 3, 4, 80, 142]
  §9.2#b84: [46, 49, 50, 145, 146, 149, 150]
  §9.2#b86: 46
  §9.2#b87: [53, 56, 161]
  §9.2#b150: [115, 151, 152, 155, 156, 157, 195, 197, 199, 203, 205]
  §9.2#b155: [107, 108, 111, 112]
  §9.2#b197: 47
  §9.4.2#r8: 104
  §9.4.2#r25: [115, 117, 195, 197, 199, 203, 205]
  §9.4.4#r23: [115, 117, 195, 197, 199, 203, 205]
  §9.5#r13: [7, 8]
  §9.5#r14: 10
  §9.5#r19: 12
  §9.5#r20: [46, 50, 146, 150]
  §9.5#r26: 46
  §9.9#r13: 7
  §9.9#r14: 9
  §9.9#r15: 8
  §9.9#r16: [59, 61]
  §9.10.1#b5: [115, 117, 195, 197, 199, 203, 205]
  §9.10.2#b5: [118, 120, 121, 123]
  §10#b2: 12
  EB-FRM-7@add-override: [125, 126, 127, 130, 132, 135, 177, 180, 183, 208, 210]
  EB-TBL-5@hapus-baris-field: 100
  FLD-43: 145
anchor: [90, 168]
coverage:
  web: automated
---

# Dialog Add override: tampilan awal, Scope, Target, dan baris Field + Value

## Prerequisites
- Aktor: Total Control (cakupan semua Group). K5 memakai aktor Manage asset & TAG (Read + Update) pada Group `Proyek Karawang`. K6 memakai aktor Manage transaction settings (Read + Update).
- Layar awal: Settings > Transaction Settings, tab Borrow, Assign, Transfer, atau Disposal, dengan Dialog Add override dibuka dari tombol `[+ Override]`.
- Komponen: Dialog Add override
- Data:
  - DU-074-1: Group `Proyek Karawang` (hierarki `Region Jawa > Proyek Karawang`) dengan turunan `Workshop`.
  - DU-074-2: Group `Proyek Bekasi` (hierarki `Region Jawa > Proyek Bekasi`).
  - DU-074-3: Asset Name `Excavator PC200`, Code `EXC-PC200`, Category `Machinery`.
  - DU-074-4: aset `EXC-0001`, Name `Excavator PC200 - 1`, Category `Machinery`.
  - DU-074-5: Value `30`.
  - DU-074-6: Value `400`.
  - DU-074-7: Value `5`.
  - DU-074-8: nilai berlaku Borrow: Max duration `14 days`, Duration unit `Days`, Max extensions `1`, Allow Borrow `Allow`.
  - DU-074-9: nilai berlaku Allow Borrow `Deny`.
  - DU-074-10: field yang ditawarkan pada transaksi Borrow: `Allow Borrow`, `Duration unit`, `Max duration`, `Max extensions`, `Max assets per borrower (concurrent)`, `Allowed borrower`, `Block new borrow when overdue`, `Photo at start`, `Photo at end`, `Require approval`, `Self service`, `Auto-approve`, `Auto-approve when duration ≤`, `Approval type`, `Due date reminders`.
  - DU-074-11: nilai berlaku Borrow Max assets per borrower (concurrent) `3 assets`.
  - DU-074-12: field yang ditawarkan pada transaksi Disposal: `Allow Disposal`, `Min asset age warning`, `Max deviation from book value`, `Max price drop from approved price`, `Require approval`, `Approval type`.
  - DU-074-13: sebagian field yang ditawarkan pada transaksi Transfer: `Allow Transfer`, `Destination scope`, `In-transit overdue after`.
  - DU-074-14: field lain yang ditawarkan pada transaksi Transfer: `Destination quota check`, `Photo at start`, `Photo at end`, `Require approval`, `Auto-approve`, `Approval type`.
  - DU-074-15: field yang ditawarkan pada transaksi Assign: `Allow Assign`, `Allowed assignee: Employee`, `Allowed assignee: Division`, `Max assets per assignee (concurrent)`, `Need recipient confirmation`, `Photo at start`, `Photo at end`, `Require approval`, `Approval type`.
- Kondisi:
  - K1: Dialog Add override - Borrow dibuka dari Category leaf `Vehicle > Pool car`; nilai berlaku di Category adalah DU-074-8 dan DU-074-11; plan entitas memuat Approval Workflow, Borrowing penuh, dan Assignment penuh; tree Group memuat DU-074-1 dan DU-074-2; picker Asset Name memuat DU-074-3; picker Select Asset memuat DU-074-4.
  - K2: sama dengan K1, tetapi dialog dibuka dari All categories dan nilai Company default adalah DU-074-8.
  - K3: sama dengan K1, tetapi plan entitas tidak memuat Approval Workflow dan Borrowing bukan versi penuh.
  - K4: Dialog Add override - Assign dibuka dari Category leaf `Vehicle > Pool car`.
  - K5: sama dengan K1, dengan aktor Manage asset & TAG (Read + Update) pada Group `Proyek Karawang`.
  - K6: sama dengan K1, dengan aktor Manage transaction settings (Read + Update).
  - K7: sama dengan K1, tetapi nilai berlaku di Category adalah DU-074-9.
  - K8: Dialog Add override - Disposal dibuka dari Category leaf `Vehicle > Pool car`; plan entitas memuat Approval Workflow.
  - K9: Dialog Add override - Transfer dibuka dari Category leaf `Vehicle > Pool car`; plan entitas tidak memuat Approval Workflow.

## Test Steps

### Tampilan awal dialog
1. Tampilkan Dialog Add override dengan kondisi K1
2. Verifikasi judul dialog `Add override - Borrow`
3. Verifikasi keterangan `Categories: Vehicle > Pool car` tampil di bawah judul
4. Verifikasi dialog memuat kontrol Scope, tombol pemilih Target, dan satu baris Field + Value
5. Verifikasi dialog tidak memuat kontrol pemilih tipe override
6. Verifikasi label `Scope` dan `Target` bertanda wajib `*`
7. Verifikasi kontrol Scope menampilkan placeholder `Select scope` tanpa opsi terpilih
8. Verifikasi baris Field + Value pertama kosong, dengan kontrol Field menampilkan placeholder `Select field`
9. Verifikasi belum ada badge target terpilih
10. Verifikasi checkbox `Stay on this form after submitting` tidak tercentang
11. Klik kontrol Scope
12. Verifikasi opsi Scope hanya `Group`, `Asset Name`, dan `Asset`

### Target Group lewat tree picker dan badge target terpilih
13. Tampilkan Dialog Add override dengan kondisi K1
14. Pilih Scope `Group`
15. Verifikasi tombol pemilih Target berlabel `Select Group`
16. Klik `[Select Group]`
17. Verifikasi dialog tree picker tampil dengan checkbox pada tiap node
18. Centang node `Proyek Karawang`
19. Centang node `Proyek Bekasi`
20. Klik `[Select]`
21. Verifikasi badge `Proyek Karawang` dan `Proyek Bekasi` tampil di bawah tombol `Select Group`, dua target terpilih sekaligus
22. Verifikasi setiap badge target memiliki tombol close
23. Verifikasi badge target Group menampilkan nama Group `Proyek Karawang`[^drift-1]
24. Arahkan kursor ke badge `Proyek Karawang`
25. Verifikasi hierarki lengkap `Region Jawa > Proyek Karawang` tersampaikan pada badge[^drift-1]
26. Verifikasi tombol pemilih Target tetap berlabel `Select Group` sesudah target terpilih
27. Pilih Scope `Asset Name`
28. Verifikasi badge target `Proyek Karawang` dan `Proyek Bekasi` dikosongkan tanpa dialog konfirmasi

### Target Asset Name dan Asset lewat dialog picker
29. Tampilkan Dialog Add override dengan kondisi K1
30. Pilih Scope `Asset Name`
31. Verifikasi tombol pemilih Target berlabel `Select Asset Name`
32. Klik `[Select Asset Name]`
33. Verifikasi dialog picker Select Asset Name tampil dengan checkbox pada tiap baris
34. Centang baris `Excavator PC200`
35. Klik `[Select]`
36. Verifikasi badge `Excavator PC200` tampil di bawah tombol `Select Asset Name`
37. Pilih Scope `Asset`
38. Verifikasi tombol pemilih Target berlabel `Select Asset`
39. Klik `[Select Asset]`
40. Verifikasi dialog picker Select Asset tampil dengan checkbox pada tiap baris
41. Centang baris `Excavator PC200 - 1`
42. Klik `[Select]`
43. Verifikasi badge `EXC-0001 · Excavator PC200 - 1` tampil di bawah tombol `Select Asset`

### Opsi Field pada transaksi Borrow
44. Tampilkan Dialog Add override dengan kondisi K1
45. Klik kontrol Field pada baris Field + Value pertama
46. Verifikasi opsi Field memuat `Allow Borrow`, `Duration unit`, `Max duration`, `Max extensions`, `Max assets per borrower (concurrent)`, `Allowed borrower`, `Block new borrow when overdue`, `Photo at start`, `Photo at end`, `Require approval`, `Self service`, `Auto-approve`, `Auto-approve when duration ≤`, `Approval type`, `Due date reminders` (DU-074-10)
47. Verifikasi opsi Field tidak memuat `Transaction timeout`
48. Verifikasi opsi Field tidak memuat `Send email notifications`
49. Verifikasi opsi Field tidak memuat `Change Cost Center with Group`
50. Verifikasi opsi Field tidak memuat `Allowed disposal types`
51. Pilih Scope `Asset Name`
52. Klik kontrol Field pada baris Field + Value pertama
53. Verifikasi opsi Field untuk Scope `Asset Name` sama dengan DU-074-10, termasuk `Self service`
54. Pilih Scope `Asset`
55. Klik kontrol Field pada baris Field + Value pertama
56. Verifikasi opsi Field untuk Scope `Asset` sama dengan DU-074-10, termasuk `Self service`

### Value sesuai jenis field
57. Tampilkan Dialog Add override dengan kondisi K1
58. Pilih Field `Max duration` pada baris pertama
59. Verifikasi Value berupa input angka dengan placeholder `Enter value`
60. Pilih Field `Allowed borrower` pada baris pertama
61. Verifikasi Value berupa pilihan dengan placeholder `Select value`
62. Pilih Field `Allow Borrow` pada baris pertama
63. Klik kontrol Value pada baris pertama
64. Verifikasi opsi Value hanya `Allow` dan `Deny`
65. Pilih Field `Self service` pada baris pertama
66. Verifikasi Value berupa switch yang langsung bernilai OFF

### Teks bantu nilai berlaku dan pergantian Field
67. Tampilkan Dialog Add override dengan kondisi K1
68. Pilih Field `Max duration` pada baris pertama
69. Verifikasi teks bantu `Current value: 14 days` tampil di bawah baris pertama, dari nilai berlaku DU-074-8
70. Isi Value `30` pada baris pertama
71. Pilih Field `Max extensions` pada baris pertama
72. Verifikasi teks bantu diperbarui menjadi `Current value: 1`
73. Verifikasi Value baris pertama kosong
74. Pilih Field `Allow Borrow` pada baris pertama
75. Verifikasi teks bantu `Current value: Allow` tampil di bawah baris pertama

### Teks bantu nilai Deny
76. Tampilkan Dialog Add override dengan kondisi K7
77. Pilih Field `Allow Borrow` pada baris pertama
78. Verifikasi teks bantu `Current value: Deny` tampil di bawah baris pertama

### Teks bantu Company default dari All categories
79. Tampilkan Dialog Add override dengan kondisi K2
80. Verifikasi keterangan `All categories` tampil di bawah judul
81. Pilih Field `Max duration` pada baris pertama
82. Verifikasi teks bantu `Company default: 14 days` tampil di bawah baris pertama

### Mengganti Field membersihkan error baris itu tetapi tidak memengaruhi baris lain
83. Tampilkan Dialog Add override dengan kondisi K1
84. Pilih Field `Max duration` pada baris pertama
85. Klik `[+ Add field]`
86. Verifikasi baris Field + Value kedua tampil
87. Pilih Field `Max assets per borrower (concurrent)` pada baris kedua
88. Isi Value `5` pada baris kedua
89. Klik `[Submit]`
90. Verifikasi error inline `You must enter a value` tampil pada baris pertama
91. Pilih Field `Max extensions` pada baris pertama
92. Verifikasi error inline `You must enter a value` pada baris pertama hilang
93. Verifikasi Value `5` pada baris kedua tetap terisi
94. Klik kontrol Field pada baris kedua
95. Verifikasi opsi Field pada baris kedua tidak memuat `Max extensions` yang sudah dipilih pada baris pertama

### Tombol hapus baris Field + Value
96. Tampilkan Dialog Add override dengan kondisi K1
97. Klik `[+ Add field]`
98. Verifikasi setiap baris Field + Value memiliki tombol hapus baris yang aktif
99. Klik tombol hapus baris pada baris kedua
100. Verifikasi tombol hapus baris pada baris tersisa disabled

### Peringatan Max duration melebihi satu tahun
101. Tampilkan Dialog Add override dengan kondisi K1
102. Pilih Field `Max duration` pada baris pertama
103. Isi Value `400` pada baris pertama
104. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di dialog

### Opsi Scope dibatasi menurut role
105. Tampilkan Dialog Add override dengan kondisi K5
106. Klik kontrol Scope
107. Verifikasi opsi `Group` dan `Asset` aktif
108. Verifikasi opsi `Asset Name` disabled
109. Tampilkan Dialog Add override dengan kondisi K6
110. Klik kontrol Scope
111. Verifikasi opsi `Asset Name` aktif
112. Verifikasi opsi `Group` dan `Asset` disabled

### Opsi field bergerbang plan Borrowing dan Approval disabled
113. Tampilkan Dialog Add override dengan kondisi K3
114. Klik kontrol Field pada baris Field + Value pertama
115. Verifikasi opsi `Require approval` disabled
116. Arahkan kursor ke opsi `Require approval`
117. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada opsi
118. Verifikasi opsi `Self service` disabled
119. Arahkan kursor ke opsi `Self service`
120. Verifikasi alasan `Available on plans with full Borrowing.` tersampaikan pada opsi
121. Verifikasi opsi `Duration unit` disabled
122. Arahkan kursor ke opsi `Duration unit`
123. Verifikasi alasan `Available on plans with full Borrowing.` tersampaikan pada opsi

### Aksesibilitas form, focus trap, dan fokus kembali
124. Tampilkan Dialog Add override dengan kondisi K1
125. Verifikasi fokus berada di dalam dialog sesudah dialog tampil
126. Verifikasi kontrol Scope dan Target dinyatakan wajib bagi teknologi bantu
127. Verifikasi tombol hapus baris Field + Value memiliki label aksesibel
128. Pilih Field `Max duration` pada baris pertama
129. Klik `[Submit]`
130. Verifikasi kontrol Value pada baris pertama terhubung dengan pesan error inline-nya bagi teknologi bantu
131. Tekan `Tab` berulang kali sampai melewati kontrol terakhir dialog
132. Verifikasi fokus tetap berada di dalam dialog
133. Klik `✕` pada dialog
134. Klik `[Leave]` pada dialog Unsaved Changes
135. Verifikasi fokus kembali ke tombol `[+ Override]` yang membuka dialog

### Teks bantu nilai berlaku pada baris Field + Value kedua
136. Tampilkan Dialog Add override dengan kondisi K1
137. Pilih Field `Max duration` pada baris pertama
138. Klik `[+ Add field]`
139. Pilih Field `Max assets per borrower (concurrent)` pada baris kedua
140. Verifikasi teks bantu `Current value: 3 assets` tampil di bawah baris kedua, dari nilai berlaku DU-074-11

### Judul Dialog Add override untuk transaksi Assign
141. Tampilkan Dialog Add override dengan kondisi K4
142. Verifikasi judul dialog `Add override - Assign`

### Daftar Field pada Dialog Add override - Disposal
143. Tampilkan Dialog Add override dengan kondisi K8
144. Klik kontrol Field pada baris Field + Value pertama
145. Verifikasi opsi Field memuat `Allow Disposal`, `Min asset age warning`, `Max deviation from book value`, `Max price drop from approved price`, `Require approval`, `Approval type` (DU-074-12)
146. Verifikasi opsi Field tidak memuat `Allowed disposal types`

### Daftar Field dan field Approval bergerbang pada Dialog Add override - Transfer
147. Tampilkan Dialog Add override dengan kondisi K9
148. Klik kontrol Field pada baris Field + Value pertama
149. Verifikasi opsi Field memuat `Allow Transfer`, `Destination scope`, `In-transit overdue after` (DU-074-13)
150. Verifikasi opsi Field tidak memuat `Change Cost Center with Group`
151. Verifikasi opsi `Approval scope` disabled
152. Verifikasi opsi `Auto-approve when destination in same parent Group` disabled

### Field Approval lain pada transaksi Borrow disabled tanpa Approval Workflow
153. Tampilkan Dialog Add override dengan kondisi K3
154. Klik kontrol Field pada baris Field + Value pertama
155. Verifikasi opsi `Auto-approve` disabled
156. Verifikasi opsi `Auto-approve when duration ≤` disabled
157. Verifikasi opsi `Approval type` disabled

### Opsi Field untuk Scope Group
158. Tampilkan Dialog Add override dengan kondisi K1
159. Pilih Scope `Group`
160. Klik kontrol Field pada baris Field + Value pertama
161. Verifikasi opsi Field untuk Scope `Group` sama dengan DU-074-10, termasuk `Self service`

### Melepas target lewat tombol close pada badge
162. Tampilkan Dialog Add override dengan kondisi K1
163. Pilih Scope `Group`
164. Klik `[Select Group]`
165. Centang node `Proyek Karawang`
166. Centang node `Proyek Bekasi`
167. Klik `[Select]`
168. Verifikasi badge `Proyek Karawang` dan `Proyek Bekasi` tampil di bawah tombol `Select Group`
169. Klik tombol close pada badge `Proyek Bekasi`
170. Verifikasi badge `Proyek Karawang` tetap tampil
171. Verifikasi badge `Proyek Bekasi` tidak tampil


### Label aksesibel tombol close pada badge target
172. Tampilkan Dialog Add override dengan kondisi K1
173. Pilih Scope `Group`
174. Klik `[Select Group]`
175. Centang node `Proyek Karawang`
176. Klik `[Select]`
177. Verifikasi tombol close pada badge `Proyek Karawang` memiliki label aksesibel

### Error inline Scope dan Target terhubung dengan kontrolnya
178. Tampilkan Dialog Add override dengan kondisi K1
179. Klik `[Submit]`
180. Verifikasi kontrol Scope terhubung dengan pesan error inline `You must pick a scope` bagi teknologi bantu
181. Pilih Scope `Group`
182. Klik `[Submit]`
183. Verifikasi tombol pemilih Target terhubung dengan pesan error inline `You must pick a group` bagi teknologi bantu

### Daftar Field pada Dialog Add override - Assign
184. Tampilkan Dialog Add override dengan kondisi K4
185. Klik kontrol Field pada baris Field + Value pertama
186. Verifikasi opsi Field memuat `Allow Assign`, `Allowed assignee: Employee`, `Allowed assignee: Division`, `Max assets per assignee (concurrent)`, `Need recipient confirmation`, `Photo at start`, `Photo at end`, `Require approval`, `Approval type` (DU-074-15)
187. Verifikasi opsi Field tidak memuat `Transaction timeout`
188. Verifikasi opsi Field tidak memuat `Send email notifications`

### Daftar Field lain pada Dialog Add override - Transfer
189. Tampilkan Dialog Add override dengan kondisi K9
190. Klik kontrol Field pada baris Field + Value pertama
191. Verifikasi opsi Field memuat `Destination quota check`, `Photo at start`, `Photo at end`, `Require approval`, `Auto-approve`, `Approval type` (DU-074-14)

### Alasan plan pada opsi Field Approval lain di Dialog Add override - Borrow
192. Tampilkan Dialog Add override dengan kondisi K3
193. Klik kontrol Field pada baris Field + Value pertama
194. Arahkan kursor ke opsi `Auto-approve`
195. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada opsi `Auto-approve`
196. Arahkan kursor ke opsi `Auto-approve when duration ≤`
197. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada opsi `Auto-approve when duration ≤`
198. Arahkan kursor ke opsi `Approval type`
199. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada opsi `Approval type`

### Alasan plan pada opsi Field Approval lain di Dialog Add override - Transfer
200. Tampilkan Dialog Add override dengan kondisi K9
201. Klik kontrol Field pada baris Field + Value pertama
202. Arahkan kursor ke opsi `Approval scope`
203. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada opsi `Approval scope`
204. Arahkan kursor ke opsi `Auto-approve when destination in same parent Group`
205. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada opsi `Auto-approve when destination in same parent Group`

### Error inline Field terhubung dengan kontrolnya
206. Tampilkan Dialog Add override dengan kondisi K1
207. Klik `[Submit]`
208. Verifikasi kontrol Field pada baris pertama terhubung dengan pesan error inline `You must pick a field` bagi teknologi bantu

### Label aksesibel tombol close pada header dialog
209. Tampilkan Dialog Add override dengan kondisi K1
210. Verifikasi tombol `✕` pada header dialog memiliki label aksesibel `Close dialog`

[^drift-1]: Drift PRD vs foundation. PRD §4.1 `FLD-35l`: «Target: `Badge` target terpilih untuk Group berisi full path.», dan catatan Deviasi §4.1: badge target Group menampilkan full path Group, bukan nama leaf dengan hover. Foundation `prd-conventions.md` §9.14 (Aturan hover): badge Group berisi nama, hover tooltip berisi «Hierarki lengkap dari parent paling atas: `[Parent] > [Child] > [Grandchild]`». Diasersi: foundation, karena badge Group kontekstual adalah komponen bersama (SB-4).
