---
id: TC-FA-FATR-UI-075-add-validasi
title: "Dialog Add override: validasi dan error inline"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules:
  - "§4.1#r122"
  - "§4.1#r279"
  - "§4.1#r280"
  - "§4.1#r293"
  - "§4.1#r310"
  - "§4.1#r311"
  - "§4.1#r312"
  - "§4.1#r313"
  - "§4.1#r314"
  - "§4.1#r315"
  - "§4.1#r316"
  - "§4.1#r317"
  - "§4.1#r318"
  - "§4.1#r320"
  - "§4.1#r321"
  - "§4.1#r322"
  - "§4.1#r323"
  - "§4.4#r12"
  - "§6#r2"
  - "§6#r4"
  - "§6#r5"
  - "§6#r6"
  - "§6#r7"
  - "§6#r9"
  - "§6#r10"
  - "§6#r13"
  - "§6#r18"
  - "§6#r19"
  - "§6#r24"
  - "§6#r25"
  - "§6#r26"
  - "§6#r39"
  - "AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d"
  - "FI-01sampaiFI-14"
  - "§9.2#b98"
  - "§9.2#b99"
  - "§9.2#b100"
  - "§9.2#b171"
  - "§9.2#b172"
  - "§9.4.2#r22"
  - "§9.4.2#r71"
  - "§9.4.2#r108"
  - "§9.4.2#r109"
  - "§9.4.4#r21"
  - "§9.4.4#r29"
  - "§9.9#r13"
  - "§9.9#r14"
  - "§9.9#r15"
  - "§9.9#r16"
  - "§9.9#r17"
  - "§9.9#r18"
  - "§9.9#r19"
  - "§9.9#r20"
  - "§9.9#r21"
smoke: []
dependsOn: []
trace:
  §4.1#r122: [78, 88]
  §4.1#r279: [64, 66]
  §4.1#r280: 67
  §4.1#r293: 52
  §4.1#r310: 2
  §4.1#r311: [5, 6, 7]
  §4.1#r312: 6
  §4.1#r313: [12, 15, 18]
  §4.1#r314: 7
  §4.1#r315: 22
  §4.1#r316: 25
  §4.1#r317: 30
  §4.1#r318: [44, 46]
  §4.1#r320: [77, 87]
  §4.1#r321: 78
  §4.1#r322: 78
  §4.1#r323: 88
  §4.4#r12: 5
  §6#r2: 78
  §6#r4: 6
  §6#r5: 12
  §6#r6: 7
  §6#r7: [22, 25]
  §6#r9: [30, 34, 38, 168, 177, 181]
  §6#r10: 63
  §6#r13: [156, 200, 202, 210]
  §6#r18: 156
  §6#r19: [157, 159]
  §6#r24: 78
  §6#r25: 88
  §6#r26: [100, 112, 124, 136, 148]
  §6#r39: 78
  "AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d": [77, 78, 88, 100, 112, 124, 136, 148]
  FI-01sampaiFI-14: [77, 78, 100, 112, 124, 136, 148]
  §9.2#b98: 63
  §9.2#b99: [64, 66]
  §9.2#b100: [62, 67]
  §9.2#b171: 7
  §9.2#b172: [5, 190, 191, 192]
  §9.4.2#r22: [5, 62, 190, 191, 192]
  §9.4.2#r71: [78, 88]
  §9.4.2#r108: 63
  §9.4.2#r109: [64, 66]
  §9.4.4#r21: 63
  §9.4.4#r29: 8
  §9.9#r13: 6
  §9.9#r14: 12
  §9.9#r15: 7
  §9.9#r16: [22, 25, 30]
  §9.9#r17: [78, 88]
  §9.9#r18: 12
  §9.9#r19: 15
  §9.9#r20: 18
  §9.9#r21: 63
anchor: [42, 51, 98, 110, 122, 134, 146]
coverage:
  web: automated
---

# Dialog Add override: validasi dan error inline

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings, tab Borrow, Assign, Transfer, atau Disposal, dengan Dialog Add override dibuka dari tombol `[+ Override]`.
- Komponen: Dialog Add override
- Data:
  - DU-075-1: Group `Proyek Karawang` (hierarki `Region Jawa > Proyek Karawang`) dengan turunan `Workshop`.
  - DU-075-2: Group `Proyek Bekasi` (hierarki `Region Jawa > Proyek Bekasi`).
  - DU-075-3: Asset Name `Excavator PC200`, Code `EXC-PC200`, Category `Machinery`.
  - DU-075-4: aset `EXC-0001`, Name `Excavator PC200 - 1`, Category `Machinery`.
  - DU-075-5: Value `0`.
  - DU-075-6: Value `5`.
  - DU-075-7: Value `14`.
  - DU-075-8: Value `400`.
  - DU-075-9: nilai berlaku Borrow di Category: Max duration `14 days`, Duration unit `Days`.
  - DU-075-10: override aktif Scope `Group`, Target `Proyek Karawang`, Overridden `Max duration (30 days)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-15 14:05`.
  - DU-075-11: isian Scope dan Target belum dipilih.
  - DU-075-12: isian Field `Max duration` dengan Value kosong.
  - DU-075-13: isian Field `Allowed borrower` dengan Value belum dipilih.
  - DU-075-14: nilai berlaku Borrow di Category: Max duration `100 hours`, Duration unit `Hours`.
  - DU-075-15: nilai berlaku Borrow di Category: Max duration `9000 days`, Duration unit `Days`.
  - DU-075-16: Value `9000`.
- Kondisi:
  - K1: Dialog Add override - Borrow dibuka dari Category leaf `Vehicle > Pool car`; nilai berlaku adalah DU-075-9; tree Group memuat DU-075-1 dan DU-075-2; picker Asset Name memuat DU-075-3; picker Select Asset memuat DU-075-4; Submit belum mengirim permintaan yang valid sehingga tidak ada respons server yang dipakai.
  - K2: sama dengan K1; server menolak Submit karena DU-075-10 sudah ada untuk Target `Proyek Karawang`, sedangkan `Proyek Bekasi` belum punya override aktif.
  - K3: Dialog Add override - Assign dibuka dari Category leaf `Vehicle > Pool car`; pilihan Field memuat `Allowed assignee: Employee`, `Allowed assignee: Division`, dan `Allow Assign`; server menolak Submit karena kombinasi efektif `Allowed assignee: Employee` dan `Allowed assignee: Division` target keduanya OFF; tree Group memuat DU-075-1 dan DU-075-2.
  - K4: sama dengan K3; server menolak Submit field `Allow Assign` bernilai Allow karena membuka aset berkombinasi OFF/OFF, dan dialog tidak memuat baris `Allowed assignee`.
  - K5: sama dengan K1; server menerima Submit.
  - K6: sama dengan K1, tetapi nilai berlaku adalah DU-075-14.
  - K7: sama dengan K1, tetapi nilai berlaku adalah DU-075-15.
  - K8: Dialog Add override - Transfer dibuka dari Category leaf `Vehicle > Pool car`; tree Group memuat DU-075-1 dan DU-075-2.
  - K9: Dialog Add override - Disposal dibuka dari Category leaf `Vehicle > Pool car`; tree Group memuat DU-075-1 dan DU-075-2.

## Test Steps

### Submit selalu aktif
1. Tampilkan Dialog Add override dengan kondisi K1
2. Verifikasi tombol `[Submit]` aktif walau belum ada isian yang diisi

### Submit dengan Scope, Target, dan Field belum diisi (DU-075-11)
3. Tampilkan Dialog Add override dengan kondisi K1
4. Klik `[Submit]` dengan isian sesuai DU-075-11
5. Verifikasi dialog tetap terbuka
6. Verifikasi error inline `You must pick a scope` tampil di bawah Scope
7. Verifikasi error inline `You must pick a field` tampil di bawah Select field
8. Verifikasi tidak ada permintaan simpan yang dikirim

### Target kosong menurut Scope
9. Tampilkan Dialog Add override dengan kondisi K1
10. Pilih Scope `Group`
11. Klik `[Submit]`
12. Verifikasi error inline `You must pick a group` tampil di bawah Target
13. Pilih Scope `Asset Name`
14. Klik `[Submit]`
15. Verifikasi error inline `You must pick an asset name` tampil di bawah Target
16. Pilih Scope `Asset`
17. Klik `[Submit]`
18. Verifikasi error inline `You must pick an asset` tampil di bawah Target

### Value kosong menurut jenis field (DU-075-12, DU-075-13)
19. Tampilkan Dialog Add override dengan kondisi K1
20. Pilih Field `Max duration` pada baris pertama
21. Klik `[Submit]`
22. Verifikasi error inline `You must enter a value` tampil di bawah input Value
23. Pilih Field `Allowed borrower` pada baris pertama
24. Klik `[Submit]`
25. Verifikasi error inline `You must pick a value` tampil di bawah pilihan Value

### Value 0 pada field angka berminimum 1 (DU-075-5)
26. Tampilkan Dialog Add override dengan kondisi K1
27. Pilih Field `Max duration` pada baris pertama
28. Isi Value `0` pada baris pertama
29. Klik `[Submit]`
30. Verifikasi error inline `Value must be at least 1` tampil di bawah input Value baris pertama
31. Pilih Field `Max assets per borrower (concurrent)` pada baris pertama
32. Isi Value `0` pada baris pertama
33. Klik `[Submit]`
34. Verifikasi error inline `Value must be at least 1` tampil di bawah input Value
35. Pilih Field `Auto-approve when duration ≤` pada baris pertama
36. Isi Value `0` pada baris pertama
37. Klik `[Submit]`
38. Verifikasi error inline `Value must be at least 1` tampil di bawah input Value

### Error inline hilang saat isian diisi
39. Tampilkan Dialog Add override dengan kondisi K1
40. Pilih Field `Max duration` pada baris pertama
41. Klik `[Submit]`
42. Verifikasi error inline `You must pick a scope` dan `You must enter a value` tampil
43. Pilih Scope `Group`
44. Verifikasi error inline `You must pick a scope` hilang
45. Isi Value `5` pada baris pertama
46. Verifikasi error inline `You must enter a value` hilang

### Value sama dengan nilai berlaku tidak error (DU-075-7)
47. Tampilkan Dialog Add override dengan kondisi K1
48. Pilih Field `Max duration` pada baris pertama
49. Isi Value `14` pada baris pertama
50. Klik `[Submit]`
51. Verifikasi error inline `You must pick a scope` tampil
52. Verifikasi tidak ada error inline di bawah input Value baris pertama

### Target duplikat ditolak server
53. Tampilkan Dialog Add override dengan kondisi K2
54. Pilih Scope `Group`
55. Klik `[Select Group]`
56. Centang node `Proyek Karawang`
57. Centang node `Proyek Bekasi`
58. Klik `[Select]`
59. Pilih Field `Max duration` pada baris pertama
60. Isi Value `5` pada baris pertama
61. Klik `[Submit]`
62. Verifikasi dialog tetap terbuka dan seluruh isian dialog dipertahankan
63. Verifikasi pesan `An active override already exists for this target, category, and transaction. Delete it first` tampil di bawah Target
64. Verifikasi badge `Proyek Karawang` diberi tanda danger
65. Arahkan kursor ke badge `Proyek Karawang`
66. Verifikasi tooltip `Active override already exists` tampil pada badge
67. Verifikasi badge `Proyek Bekasi` tetap tampil tanpa tanda danger

### Guard Allowed assignee: pesan di bawah kedua baris
68. Tampilkan Dialog Add override dengan kondisi K3
69. Pilih Scope `Group`
70. Klik `[Select Group]`
71. Centang node `Proyek Karawang`
72. Klik `[Select]`
73. Pilih Field `Allowed assignee: Employee` pada baris pertama
74. Klik `[+ Add field]`
75. Pilih Field `Allowed assignee: Division` pada baris kedua
76. Klik `[Submit]`
77. Verifikasi dialog tetap terbuka
78. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris pertama dan baris kedua

### Guard dari field Allow Assign saat dialog tanpa baris Allowed assignee
79. Tampilkan Dialog Add override dengan kondisi K4
80. Pilih Scope `Group`
81. Klik `[Select Group]`
82. Centang node `Proyek Karawang`
83. Klik `[Select]`
84. Pilih Field `Allow Assign` pada baris pertama
85. Pilih Value `Allow` pada baris pertama
86. Klik `[Submit]`
87. Verifikasi dialog tetap terbuka
88. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris `Allow Assign`

### Pesan guard hilang saat Value baris diubah
89. Tampilkan Dialog Add override dengan kondisi K3
90. Pilih Scope `Group`
91. Klik `[Select Group]`
92. Centang node `Proyek Karawang`
93. Klik `[Select]`
94. Pilih Field `Allowed assignee: Employee` pada baris pertama
95. Klik `[+ Add field]`
96. Pilih Field `Allowed assignee: Division` pada baris kedua
97. Klik `[Submit]`
98. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris pertama dan baris kedua
99. Ubah Value baris pertama menjadi `ON`
100. Verifikasi pesan `At least one assignee type must be enabled` hilang

### Pesan guard hilang saat Field baris diganti
101. Tampilkan Dialog Add override dengan kondisi K3
102. Pilih Scope `Group`
103. Klik `[Select Group]`
104. Centang node `Proyek Karawang`
105. Klik `[Select]`
106. Pilih Field `Allowed assignee: Employee` pada baris pertama
107. Klik `[+ Add field]`
108. Pilih Field `Allowed assignee: Division` pada baris kedua
109. Klik `[Submit]`
110. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris pertama dan baris kedua
111. Pilih Field `Allow Assign` pada baris pertama
112. Verifikasi pesan `At least one assignee type must be enabled` hilang

### Pesan guard hilang saat baris dihapus
113. Tampilkan Dialog Add override dengan kondisi K3
114. Pilih Scope `Group`
115. Klik `[Select Group]`
116. Centang node `Proyek Karawang`
117. Klik `[Select]`
118. Pilih Field `Allowed assignee: Employee` pada baris pertama
119. Klik `[+ Add field]`
120. Pilih Field `Allowed assignee: Division` pada baris kedua
121. Klik `[Submit]`
122. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris pertama dan baris kedua
123. Klik tombol hapus baris pada baris kedua
124. Verifikasi pesan `At least one assignee type must be enabled` hilang

### Pesan guard hilang saat Target diubah
125. Tampilkan Dialog Add override dengan kondisi K3
126. Pilih Scope `Group`
127. Klik `[Select Group]`
128. Centang node `Proyek Karawang`
129. Klik `[Select]`
130. Pilih Field `Allowed assignee: Employee` pada baris pertama
131. Klik `[+ Add field]`
132. Pilih Field `Allowed assignee: Division` pada baris kedua
133. Klik `[Submit]`
134. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris pertama dan baris kedua
135. Klik tombol close pada badge `Proyek Karawang`
136. Verifikasi pesan `At least one assignee type must be enabled` hilang

### Pesan guard hilang saat Clear Field diklik
137. Tampilkan Dialog Add override dengan kondisi K3
138. Pilih Scope `Group`
139. Klik `[Select Group]`
140. Centang node `Proyek Karawang`
141. Klik `[Select]`
142. Pilih Field `Allowed assignee: Employee` pada baris pertama
143. Klik `[+ Add field]`
144. Pilih Field `Allowed assignee: Division` pada baris kedua
145. Klik `[Submit]`
146. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris pertama dan baris kedua
147. Klik `[Clear Field]`
148. Verifikasi pesan `At least one assignee type must be enabled` hilang

### Peringatan Max duration di atas satu tahun tidak menghalangi Submit (DU-075-8)
149. Tampilkan Dialog Add override dengan kondisi K5
150. Pilih Scope `Group`
151. Klik `[Select Group]`
152. Centang node `Proyek Karawang`
153. Klik `[Select]`
154. Pilih Field `Max duration` pada baris pertama
155. Isi Value `400` pada baris pertama
156. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di dialog
157. Verifikasi tombol `[Submit]` aktif
158. Klik `[Submit]`
159. Verifikasi Submit diterima: Dialog Add override tidak lagi tampil

### Value 0 pada field angka berminimum 1 di dialog Transfer
160. Tampilkan Dialog Add override dengan kondisi K8
161. Pilih Scope `Group`
162. Klik `[Select Group]`
163. Centang node `Proyek Karawang`
164. Klik `[Select]`
165. Pilih Field `In-transit overdue after` pada baris pertama
166. Isi Value `0` pada baris pertama
167. Klik `[Submit]`
168. Verifikasi error inline `Value must be at least 1` tampil di bawah input Value

### Value 0 pada field angka berminimum 1 di dialog Disposal
169. Tampilkan Dialog Add override dengan kondisi K9
170. Pilih Scope `Group`
171. Klik `[Select Group]`
172. Centang node `Proyek Karawang`
173. Klik `[Select]`
174. Pilih Field `Min asset age warning` pada baris pertama
175. Isi Value `0` pada baris pertama
176. Klik `[Submit]`
177. Verifikasi error inline `Value must be at least 1` tampil di bawah input Value
178. Pilih Field `Max deviation from book value` pada baris pertama
179. Isi Value `0` pada baris pertama
180. Klik `[Submit]`
181. Verifikasi error inline `Value must be at least 1` tampil di bawah input Value

### Value 0 dengan Scope, Target, dan Field terisi
182. Tampilkan Dialog Add override dengan kondisi K1
183. Pilih Scope `Group`
184. Klik `[Select Group]`
185. Centang node `Proyek Karawang`
186. Klik `[Select]`
187. Pilih Field `Max duration` pada baris pertama
188. Isi Value `0` pada baris pertama
189. Klik `[Submit]`
190. Verifikasi error inline `Value must be at least 1` tampil di bawah input Value baris pertama
191. Verifikasi dialog tetap terbuka
192. Verifikasi tidak ada error inline selain `Value must be at least 1` pada dialog

### Peringatan Max duration mengikuti Duration unit berlaku Hours
193. Tampilkan Dialog Add override dengan kondisi K6
194. Pilih Scope `Group`
195. Klik `[Select Group]`
196. Centang node `Proyek Karawang`
197. Klik `[Select]`
198. Pilih Field `Max duration` pada baris pertama
199. Isi Value `9000` pada baris pertama
200. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di dialog
201. Isi Value `400` pada baris pertama
202. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` hilang

### Peringatan Max duration saat hanya Duration unit yang di-override
203. Tampilkan Dialog Add override dengan kondisi K7
204. Pilih Scope `Group`
205. Klik `[Select Group]`
206. Centang node `Proyek Karawang`
207. Klik `[Select]`
208. Pilih Field `Duration unit` pada baris pertama
209. Pilih Value `Hours` pada baris pertama
210. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di dialog
