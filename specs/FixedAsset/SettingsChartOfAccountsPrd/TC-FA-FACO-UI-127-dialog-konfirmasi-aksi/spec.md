---
id: TC-FA-FACO-UI-127-dialog-konfirmasi-aksi
title: "Tab Chart of Accounts: dialog konfirmasi Activate, Deactivate, Delete dan reaksi atas respons"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-01", "D-02", "D-07", "D-08", "D-14", "D-15", "R-05", "R-06", "T-03", "T-04", "T-05", "T-06", "T-12", "§4.1.1#p4", "§4.2f#b2", "§4.5#b2", "§7.2#r14", "§7.2#r15", "§7.2#r16", "§7.2#r17", "§7.2#r18", "§7.2#r19", "§7.2#p2", "§7.3#b1", "§7.3#b2", "§7.3#b4", "§7.3#b5", "§[F-FACO-03] Activate Account#p1", "§[F-FACO-05] Delete Account#p2", "§9.4.2#r36", "EB-FB-1@activate-account", "EB-FB-1@deactivate-account", "EB-FB-1@delete-account", "EB-FB-2@batal-dialog", "EB-ERR-1@activate-account", "EB-ERR-1@deactivate-account", "EB-ERR-1@delete-account", "EB-ERR-2@dialog-delete-account"]
smoke: []
dependsOn: []
trace:
  "D-01": [16, 17, 18]
  "D-02": [24, 25, 26]
  "D-07": [30, 31, 32]
  "D-08": [38, 39, 40]
  "D-14": [3, 4, 5]
  "D-15": [11, 12, 13]
  "R-05": [193, 194, 238, 239]
  "R-06": [203, 204, 206, 247, 248]
  "T-03": [274, 275, 279, 280, 287]
  "T-04": [103, 104, 116, 155, 159, 183]
  "T-05": [108, 109, 125, 142, 163, 167, 193]
  "T-06": [98, 134, 150, 172, 176, 203]
  "T-12": [253, 254, 255, 260, 261, 262, 269]
  "§4.1.1#p4": [45, 46, 50, 51, 57, 58, 62, 63, 68, 69]
  "§4.2f#b2": [45, 46, 50, 51]
  "§4.5#b2": [91, 93]
  "§7.2#r14": [108, 125]
  "§7.2#r15": 142
  "§7.2#r16": [163, 193]
  "§7.2#r17": [98, 134]
  "§7.2#r18": 150
  "§7.2#r19": [172, 203]
  "§7.2#p2": [184, 194, 204, 238, 239, 247, 248]
  "§7.3#b1": [156, 164, 173, 185, 195, 205, 211, 219, 228, 238, 240, 247, 249]
  "§7.3#b2": [76, 117, 118, 126, 127, 135, 143, 151, 184, 194, 204, 239, 248, 270, 288]
  "§7.3#b4": [253, 254, 255, 260, 261, 262, 269, 270]
  "§7.3#b5": [274, 275, 279, 280, 287, 288]
  "§[F-FACO-03] Activate Account#p1": [183, 184, 186, 196]
  "§[F-FACO-05] Delete Account#p2": [203, 204, 206]
  "§9.4.2#r36": [45, 46, 50, 51]
  "EB-FB-1@activate-account": [103, 116, 155]
  "EB-FB-1@deactivate-account": [108, 125, 163]
  "EB-FB-1@delete-account": [98, 134, 172]
  "EB-FB-2@batal-dialog": [76, 77, 78]
  "EB-ERR-1@activate-account": [155, 156, 157, 159, 210, 211, 212, 214]
  "EB-ERR-1@deactivate-account": [163, 164, 165, 167, 218, 219, 220, 222]
  "EB-ERR-1@delete-account": [172, 173, 174, 176, 227, 228, 229, 231]
  "EB-ERR-2@dialog-delete-account": [83, 84, 85, 86, 91, 93, 98, 99]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: dialog konfirmasi Activate, Deactivate, Delete dan reaksi atas respons

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-127-1: Account `5-1001`, Name `Kas Operasional`, Function `Asset Cost`, status Active, Used By `0`, Last Used in Journal kosong.
  - DU-127-2: Account `5-1002`, Name `Bank Operasional`, Function `Asset Cost`, status Active, Used By `0`, Last Used in Journal kosong.
  - DU-127-3: Account `6-1001`, Name `Beban Sewa`, Function `Asset Cost`, status Inactive, Used By `0`, Last Used in Journal kosong.
  - DU-127-4: Account `6-1002`, Name `Beban Listrik`, Function `Asset Cost`, status Inactive, Used By `0`, Last Used in Journal kosong.
  - DU-127-5: Account `7-1001`, Name `Persediaan`, Function `Asset Cost`, status Active, Used By `2`, Last Used in Journal kosong.
  - DU-127-6: Account `8-1001`, Name `Pendapatan Jasa`, Function `Asset Cost`, status Active, Used By `0`, Last Used in Journal `Oct 2026`.
- Kondisi:
  - K1: tabel berisi DU-127-1 sampai DU-127-6; server menerima setiap aksi dan mencatat setiap permintaan yang diterimanya.
  - K2: seperti K1; server menolak permintaan aksi pertama dengan error 5xx dan menerima permintaan aksi berikutnya.
  - K3: seperti K1; server tidak menjawab permintaan aksi pertama sampai batas waktu dan menerima permintaan aksi berikutnya.
  - K4: seperti K1; akun yang dikonfirmasi sudah dihapus pengguna lain, server menjawab bahwa akun tidak tersedia, dan daftar yang dimuat ulang tidak memuat akun itu.
  - K5: seperti K1; akun yang dikonfirmasi sudah berstatus target (data usang), dan daftar yang dimuat ulang memuat status terkini.

## Test Steps

### Dialog Activate single
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik switch baris `6-1001`
3. Verifikasi judul dialog `Activate Account` tampil
4. Verifikasi kalimat `Are you sure you want to activate it?` tampil
5. Verifikasi tombol `[Cancel]` dan `[Activate]` tampil

### Dialog Activate bulk
6. Tampilkan Tab Chart of Accounts dengan kondisi K1
7. Centang baris `6-1001`
8. Centang baris `6-1002`
9. Klik `Bulk Action`
10. Klik `Activate`
11. Verifikasi judul dialog `Activate Accounts` tampil
12. Verifikasi kalimat `Are you sure you want to activate them?` tampil
13. Verifikasi tombol `[Cancel]` dan `[Activate]` tampil

### Dialog Deactivate single
14. Tampilkan Tab Chart of Accounts dengan kondisi K1
15. Klik switch baris `5-1001`
16. Verifikasi judul dialog `Deactivate Account` tampil
17. Verifikasi kalimat `Are you sure you want to deactivate it?` tampil
18. Verifikasi tombol `[Cancel]` dan `[Deactivate]` tampil

### Dialog Deactivate bulk
19. Tampilkan Tab Chart of Accounts dengan kondisi K1
20. Centang baris `5-1001`
21. Centang baris `5-1002`
22. Klik `Bulk Action`
23. Klik `Deactivate`
24. Verifikasi judul dialog `Deactivate Accounts` tampil
25. Verifikasi kalimat `Are you sure you want to deactivate them?` tampil
26. Verifikasi tombol `[Cancel]` dan `[Deactivate]` tampil

### Dialog Delete single
27. Tampilkan Tab Chart of Accounts dengan kondisi K1
28. Klik `⋯` pada baris `5-1001`
29. Klik `Delete`
30. Verifikasi judul dialog `Delete Account` tampil
31. Verifikasi kalimat `This action cannot be undone. Are you sure you want to delete it?` tampil
32. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil

### Dialog Delete bulk
33. Tampilkan Tab Chart of Accounts dengan kondisi K1
34. Centang baris `5-1001`
35. Centang baris `5-1002`
36. Klik `Bulk Action`
37. Klik `Delete`
38. Verifikasi judul dialog `Delete Accounts` tampil
39. Verifikasi kalimat `This action cannot be undone. Are you sure you want to delete them?` tampil
40. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil

### Bulk dengan satu akun diproses memakai dialog single
41. Tampilkan Tab Chart of Accounts dengan kondisi K1
42. Centang baris `5-1001`
43. Klik `Bulk Action`
44. Klik `Deactivate`
45. Verifikasi judul dialog `Deactivate Account` tampil
46. Verifikasi kalimat `Are you sure you want to deactivate it?` tampil
47. Klik `[Cancel]`
48. Klik `Bulk Action`
49. Klik `Delete`
50. Verifikasi judul dialog `Delete Account` tampil
51. Verifikasi kalimat `This action cannot be undone. Are you sure you want to delete it?` tampil

### Seleksi campuran hanya memproses akun yang bukan berstatus target
52. Tampilkan Tab Chart of Accounts dengan kondisi K1
53. Centang baris `5-1001`
54. Centang baris `6-1001`
55. Klik `Bulk Action`
56. Klik `Activate`
57. Verifikasi judul dialog `Activate Account` tampil
58. Verifikasi kalimat `Are you sure you want to activate it?` tampil
59. Klik `[Cancel]`
60. Klik `Bulk Action`
61. Klik `Deactivate`
62. Verifikasi judul dialog `Deactivate Account` tampil
63. Verifikasi kalimat `Are you sure you want to deactivate it?` tampil
64. Klik `[Cancel]`
65. Centang baris `6-1002`
66. Klik `Bulk Action`
67. Klik `Activate`
68. Verifikasi judul dialog `Activate Accounts` tampil
69. Verifikasi kalimat `Are you sure you want to activate them?` tampil

### Cancel menutup dialog tanpa toast dan seleksi dipertahankan
70. Tampilkan Tab Chart of Accounts dengan kondisi K1
71. Centang baris `5-1001`
72. Centang baris `5-1002`
73. Klik `Bulk Action`
74. Klik `Delete`
75. Klik `[Cancel]`
76. Verifikasi counter `2 Accounts selected` tampil
77. Verifikasi baris `5-1001` tampil
78. Verifikasi tidak ada toast yang tampil

### Esc menutup dialog Delete tanpa menghapus
79. Tampilkan Tab Chart of Accounts dengan kondisi K1
80. Klik `⋯` pada baris `5-1001`
81. Klik `Delete`
82. Tekan `Esc`
83. Verifikasi baris `5-1001` tampil
84. Verifikasi fokus kembali ke tombol `⋯` pada baris `5-1001`
85. Verifikasi dialog `Delete Account` tidak tampil
86. Verifikasi tidak ada toast yang tampil

### Fokus terkunci di dalam dialog
87. Tampilkan Tab Chart of Accounts dengan kondisi K1
88. Klik `⋯` pada baris `5-1001`
89. Klik `Delete`
90. Tekan Tab lima kali
91. Verifikasi fokus berada di dalam dialog `Delete Account`
92. Tekan Shift+Tab lima kali
93. Verifikasi fokus berada di dalam dialog `Delete Account`

### Klik ganda Delete menghapus sekali
94. Tampilkan Tab Chart of Accounts dengan kondisi K1
95. Klik `⋯` pada baris `5-1001`
96. Klik `Delete`
97. Klik ganda `[Delete]` pada dialog `Delete Account`
98. Verifikasi toast `Success, account has been deleted.` tampil satu kali
99. Verifikasi server menerima satu permintaan hapus untuk akun `5-1001`

### Activate single berhasil
100. Tampilkan Tab Chart of Accounts dengan kondisi K1
101. Klik switch baris `6-1001`
102. Klik `[Activate]` pada dialog `Activate Account`
103. Verifikasi toast `Success, account has been activated.` tampil
104. Verifikasi dialog `Activate Account` tidak tampil

### Deactivate single berhasil
105. Tampilkan Tab Chart of Accounts dengan kondisi K1
106. Klik switch baris `5-1001`
107. Klik `[Deactivate]` pada dialog `Deactivate Account`
108. Verifikasi toast `Success, account has been deactivated.` tampil
109. Verifikasi dialog `Deactivate Account` tidak tampil

### Bulk Activate berhasil dan seleksi di-reset
110. Tampilkan Tab Chart of Accounts dengan kondisi K1
111. Centang baris `6-1001`
112. Centang baris `6-1002`
113. Klik `Bulk Action`
114. Klik `Activate`
115. Klik `[Activate]` pada dialog `Activate Accounts`
116. Verifikasi toast `Success, account has been activated.` tampil
117. Verifikasi Bulk Action Bar tidak tampil
118. Verifikasi baris `6-1001` tidak terpilih

### Bulk Deactivate berhasil dan seleksi di-reset
119. Tampilkan Tab Chart of Accounts dengan kondisi K1
120. Centang baris `5-1001`
121. Centang baris `5-1002`
122. Klik `Bulk Action`
123. Klik `Deactivate`
124. Klik `[Deactivate]` pada dialog `Deactivate Accounts`
125. Verifikasi toast `Success, account has been deactivated.` tampil
126. Verifikasi Bulk Action Bar tidak tampil
127. Verifikasi baris `5-1001` tidak terpilih

### Bulk Delete berhasil dan seleksi di-reset
128. Tampilkan Tab Chart of Accounts dengan kondisi K1
129. Centang baris `5-1001`
130. Centang baris `5-1002`
131. Klik `Bulk Action`
132. Klik `Delete`
133. Klik `[Delete]` pada dialog `Delete Accounts`
134. Verifikasi toast `Success, account has been deleted.` tampil
135. Verifikasi Bulk Action Bar tidak tampil

### Bulk Deactivate parsial dan seleksi di-reset
136. Tampilkan Tab Chart of Accounts dengan kondisi K1
137. Centang baris `5-1001`
138. Centang baris `7-1001`
139. Klik `Bulk Action`
140. Klik `Deactivate`
141. Klik `[Continue]` pada dialog `Deactivate Accounts`
142. Verifikasi toast `Success, account has been deactivated. Some items were skipped (still in use).` tampil
143. Verifikasi Bulk Action Bar tidak tampil

### Bulk Delete parsial dan seleksi di-reset
144. Tampilkan Tab Chart of Accounts dengan kondisi K1
145. Centang baris `5-1001`
146. Centang baris `8-1001`
147. Klik `Bulk Action`
148. Klik `Delete`
149. Klik `[Continue]` pada dialog `Delete Accounts`
150. Verifikasi toast `Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company).` tampil
151. Verifikasi Bulk Action Bar tidak tampil

### Activate single gagal karena error server
152. Tampilkan Tab Chart of Accounts dengan kondisi K2
153. Klik switch baris `6-1001`
154. Klik `[Activate]` pada dialog `Activate Account`
155. Verifikasi toast `Error, failed to activate account.` tampil
156. Verifikasi dialog `Activate Account` tetap tampil
157. Verifikasi tombol `[Activate]` enabled
158. Klik `[Activate]` pada dialog `Activate Account`
159. Verifikasi toast `Success, account has been activated.` tampil

### Deactivate single gagal karena error server
160. Tampilkan Tab Chart of Accounts dengan kondisi K2
161. Klik switch baris `5-1001`
162. Klik `[Deactivate]` pada dialog `Deactivate Account`
163. Verifikasi toast `Error, failed to deactivate account.` tampil
164. Verifikasi dialog `Deactivate Account` tetap tampil
165. Verifikasi tombol `[Deactivate]` enabled
166. Klik `[Deactivate]` pada dialog `Deactivate Account`
167. Verifikasi toast `Success, account has been deactivated.` tampil

### Delete single gagal karena error server
168. Tampilkan Tab Chart of Accounts dengan kondisi K2
169. Klik `⋯` pada baris `5-1001`
170. Klik `Delete`
171. Klik `[Delete]` pada dialog `Delete Account`
172. Verifikasi toast `Error, failed to delete account.` tampil
173. Verifikasi dialog `Delete Account` tetap tampil
174. Verifikasi tombol `[Delete]` enabled
175. Klik `[Delete]` pada dialog `Delete Account`
176. Verifikasi toast `Success, account has been deleted.` tampil

### Bulk Activate gagal karena error server
177. Tampilkan Tab Chart of Accounts dengan kondisi K2
178. Centang baris `6-1001`
179. Centang baris `6-1002`
180. Klik `Bulk Action`
181. Klik `Activate`
182. Klik `[Activate]` pada dialog `Activate Accounts`
183. Verifikasi toast `Error, failed to activate account.` tampil
184. Verifikasi counter `2 Accounts selected` tampil
185. Verifikasi dialog `Activate Accounts` tetap tampil
186. Verifikasi permintaan daftar akun dikirim ulang ke server

### Bulk Deactivate gagal karena error server
187. Tampilkan Tab Chart of Accounts dengan kondisi K2
188. Centang baris `5-1001`
189. Centang baris `5-1002`
190. Klik `Bulk Action`
191. Klik `Deactivate`
192. Klik `[Deactivate]` pada dialog `Deactivate Accounts`
193. Verifikasi toast `Error, failed to deactivate account.` tampil
194. Verifikasi counter `2 Accounts selected` tampil
195. Verifikasi dialog `Deactivate Accounts` tetap tampil
196. Verifikasi permintaan daftar akun dikirim ulang ke server

### Bulk Delete gagal karena error server
197. Tampilkan Tab Chart of Accounts dengan kondisi K2
198. Centang baris `5-1001`
199. Centang baris `5-1002`
200. Klik `Bulk Action`
201. Klik `Delete`
202. Klik `[Delete]` pada dialog `Delete Accounts`
203. Verifikasi toast `Error, failed to delete account.` tampil
204. Verifikasi counter `2 Accounts selected` tampil
205. Verifikasi dialog `Delete Accounts` tetap tampil
206. Verifikasi permintaan daftar akun dikirim ulang ke server

### Activate single gagal karena timeout
207. Tampilkan Tab Chart of Accounts dengan kondisi K3
208. Klik switch baris `6-1001`
209. Klik `[Activate]` pada dialog `Activate Account`
210. Verifikasi toast `Connection problem. Please try again.` tampil
211. Verifikasi dialog `Activate Account` tetap tampil
212. Verifikasi tombol `[Activate]` enabled
213. Klik `[Activate]` pada dialog `Activate Account`
214. Verifikasi toast `Success, account has been activated.` tampil

### Deactivate single gagal karena timeout
215. Tampilkan Tab Chart of Accounts dengan kondisi K3
216. Klik switch baris `5-1001`
217. Klik `[Deactivate]` pada dialog `Deactivate Account`
218. Verifikasi toast `Connection problem. Please try again.` tampil
219. Verifikasi dialog `Deactivate Account` tetap tampil
220. Verifikasi tombol `[Deactivate]` enabled
221. Klik `[Deactivate]` pada dialog `Deactivate Account`
222. Verifikasi toast `Success, account has been deactivated.` tampil

### Delete single gagal karena timeout
223. Tampilkan Tab Chart of Accounts dengan kondisi K3
224. Klik `⋯` pada baris `5-1001`
225. Klik `Delete`
226. Klik `[Delete]` pada dialog `Delete Account`
227. Verifikasi toast `Connection problem. Please try again.` tampil
228. Verifikasi dialog `Delete Account` tetap tampil
229. Verifikasi tombol `[Delete]` enabled
230. Klik `[Delete]` pada dialog `Delete Account`
231. Verifikasi toast `Success, account has been deleted.` tampil

### Bulk Deactivate gagal karena timeout
232. Tampilkan Tab Chart of Accounts dengan kondisi K3
233. Centang baris `5-1001`
234. Centang baris `5-1002`
235. Klik `Bulk Action`
236. Klik `Deactivate`
237. Klik `[Deactivate]` pada dialog `Deactivate Accounts`
238. Verifikasi toast `Connection problem. Please try again.` tampil
239. Verifikasi counter `2 Accounts selected` tampil
240. Verifikasi dialog `Deactivate Accounts` tetap tampil

### Bulk Delete gagal karena timeout
241. Tampilkan Tab Chart of Accounts dengan kondisi K3
242. Centang baris `5-1001`
243. Centang baris `5-1002`
244. Klik `Bulk Action`
245. Klik `Delete`
246. Klik `[Delete]` pada dialog `Delete Accounts`
247. Verifikasi toast `Connection problem. Please try again.` tampil
248. Verifikasi counter `2 Accounts selected` tampil
249. Verifikasi dialog `Delete Accounts` tetap tampil

### Akun sudah dihapus pengguna lain saat Activate
250. Tampilkan Tab Chart of Accounts dengan kondisi K4
251. Klik switch baris `6-1001`
252. Klik `[Activate]` pada dialog `Activate Account`
253. Verifikasi toast `This account is no longer available.` tampil
254. Verifikasi dialog `Activate Account` tidak tampil
255. Verifikasi baris `6-1001` tidak tampil

### Akun sudah dihapus pengguna lain saat Delete
256. Tampilkan Tab Chart of Accounts dengan kondisi K4
257. Klik `⋯` pada baris `5-1001`
258. Klik `Delete`
259. Klik `[Delete]` pada dialog `Delete Account`
260. Verifikasi toast `This account is no longer available.` tampil
261. Verifikasi dialog `Delete Account` tidak tampil
262. Verifikasi baris `5-1001` tidak tampil

### Seluruh akun terpilih sudah dihapus pengguna lain
263. Tampilkan Tab Chart of Accounts dengan kondisi K4
264. Centang baris `5-1001`
265. Centang baris `5-1002`
266. Klik `Bulk Action`
267. Klik `Delete`
268. Klik `[Delete]` pada dialog `Delete Accounts`
269. Verifikasi toast `This account is no longer available.` tampil sebagai satu-satunya toast
270. Verifikasi Bulk Action Bar tidak tampil

### Activate atas akun yang sudah berstatus target
271. Tampilkan Tab Chart of Accounts dengan kondisi K5
272. Klik switch baris `6-1001`
273. Klik `[Activate]` pada dialog `Activate Account`
274. Verifikasi toast `No changes to save.` tampil
275. Verifikasi dialog `Activate Account` tidak tampil

### Deactivate atas akun yang sudah berstatus target
276. Tampilkan Tab Chart of Accounts dengan kondisi K5
277. Klik switch baris `5-1001`
278. Klik `[Deactivate]` pada dialog `Deactivate Account`
279. Verifikasi toast `No changes to save.` tampil
280. Verifikasi dialog `Deactivate Account` tidak tampil

### Bulk Deactivate atas akun yang seluruhnya sudah berstatus target
281. Tampilkan Tab Chart of Accounts dengan kondisi K5
282. Centang baris `5-1001`
283. Centang baris `5-1002`
284. Klik `Bulk Action`
285. Klik `Deactivate`
286. Klik `[Deactivate]` pada dialog `Deactivate Accounts`
287. Verifikasi toast `No changes to save.` tampil sebagai satu-satunya toast
288. Verifikasi Bulk Action Bar tidak tampil
