---
id: TC-FA-BORROW-E2E-036-entitas-suspended-expired-aksi-tulis
title: "Entitas Suspended atau Expired menolak setiap aksi tulis Borrow dan tetap membaca data"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [EB-AKS-7]
smoke: []
dependsOn: []
trace:
  EB-AKS-7: [6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 48, 49, 50, 51, 52, 54, 55, 58, 62, 64, 66, 70, 71, 72, 77, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 119, 120, 121, 122, 123, 125, 126, 129, 133, 135, 137, 141, 142, 143, 148, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 190, 191, 192, 193, 194, 196, 197, 200, 204, 206, 208, 212, 213, 214]
anchor: []
coverage:
  web: automated
---

# Entitas Suspended atau Expired menolak setiap aksi tulis Borrow dan tetap membaca data

## Prerequisites
- Aktor: Total Control, lalu Borrower pada langkah «Masuk sebagai Borrower»; operator Admin Console `Operator Admin Console {runId}` mengubah status entitas dari luar tenant.
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-036-1: Entitas `Samudra Logistik {runId}`, level Feature Suite Borrowing `Full`, status awal Active.
  - DU-036-2: User `Maya Putri {runId}`, role Total Control, cakupan seluruh client, aktif.
  - DU-036-3: User `Operator Admin Console {runId}`, operator Admin Console di luar tenant, aktif.
  - DU-036-4: User `Rudi Hartono {runId}`, karyawan tanpa role Borrow, aktif, Home Group `Head Office {runId}`.
  - DU-036-5: Group `Head Office {runId}`.
  - DU-036-6: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-036-7: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Maya Putri {runId}`.
  - DU-036-8: BRW berstatus Borrowed, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Maya Putri {runId}`.
  - DU-036-9: BRW berstatus Waiting for Approval yang approval-nya dirutekan ke `Maya Putri {runId}` (alasan `No eligible approver`), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Meeting Mic Set {runId}`, Duration `2 days`, Purpose `Rapat tahunan`, Requested By `Rina Wulandari {runId}`.
  - DU-036-10: Draft milik Borrower `Rudi Hartono {runId}`, berisi aset `Scanner Epson DS-530 {runId}` (Group `Head Office {runId}`), Total Asset `1`, Modified By `Maya Putri {runId}`.
  - DU-036-11: Percobaan Create BRW untuk Borrower `Rudi Hartono {runId}`, aset `Laptop Lenovo T14 {runId}`, Duration `2`, Purpose `Kunjungan tamu`.
  - DU-036-12: Percobaan ubah Draft DU-036-10: Duration aset `Scanner Epson DS-530 {runId}` menjadi `4`.
  - DU-036-13: Percobaan Request Extension untuk aset `Toyota Avanza {runId}`: Extend By `2 days`, Reason `Pekerjaan belum selesai`.
  - DU-036-14: User `Rina Wulandari {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-036-15: BRW berstatus Extension Approval (Extend menunggu approval), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Projector Epson EB-X06 {runId}`, Duration `4 days`, Purpose `Presentasi vendor`, Requested By `Rina Wulandari {runId}`.
  - DU-036-16: BRW berstatus Extension Request (pengajuan Extend dari My Asset menunggu review), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Printer Canon G3010 {runId}`, Duration `4 days`, Purpose `Cetak dokumen audit`, Requested By `Rina Wulandari {runId}`.
  - DU-036-17: BRW berstatus Borrowed dengan Damage Report Waiting for Confirmation yang dilaporkan `Maya Putri {runId}`, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Excavator Komatsu PC200 {runId}`, Duration `6 days`, Purpose `Pekerjaan galian`, Requested By `Rina Wulandari {runId}`.
  - DU-036-18: Draft milik Borrower `Rudi Hartono {runId}`, berisi aset `Mixer Beton Portable {runId}` (Group `Head Office {runId}`), Total Asset `1`, Modified By `Maya Putri {runId}`.
  - DU-036-19: Percobaan Add to Borrow Draft untuk Borrower `Rudi Hartono {runId}`, aset `Laptop Lenovo T14 {runId}`, ke Draft DU-036-10.
  - DU-036-20: BRW berstatus Waiting for Handover dengan serah-terima yang sedang berlangsung dan menunggu konfirmasi Borrower (Task `Confirm Handover` tersedia bagi Borrower), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Camera Sony A7 {runId}`, Duration `2 days`, Purpose `Dokumentasi acara`, Requested By `Maya Putri {runId}`.
  - DU-036-21: BRW berstatus Borrowed dengan Missing Report Waiting for Confirmation yang dilaporkan Borrower `Rudi Hartono {runId}`, Group `Head Office {runId}`, aset `Drone DJI Mavic {runId}`, Duration `5 days`, Purpose `Pemetaan lahan`, Requested By `Maya Putri {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus `Samudra Logistik {runId}` yang tidak dipakai spec lain.
  - Level Feature Suite Borrowing entitas itu bernilai `Full`.
  - Akun `Maya Putri {runId}` dan `Rudi Hartono {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Entitas Suspended: modul terbuka, data terbaca, dan setiap aksi tulis ditolak
1. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `Samudra Logistik {runId}` menjadi `Suspended`
2. Masuk sebagai Total Control `Maya Putri {runId}`
3. Muat ulang halaman
4. Klik menu `Transactions > Borrow`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi halaman Borrow terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Suspended`
7. Verifikasi BRW milik DU-036-7 tampil di tabel pada entitas `Suspended`
8. Kirim Create BRW dengan nilai dari DU-036-11
9. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
10. Kirim Save Draft pada Draft milik DU-036-10 dengan nilai dari DU-036-12
11. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
12. Kirim Delete atas Draft milik DU-036-10
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
14. Kirim Cancel Borrow atas BRW milik DU-036-7
15. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
16. Kirim Hand Over atas BRW milik DU-036-7
17. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
18. Kirim Remind Borrower atas BRW milik DU-036-7
19. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
20. Kirim Request Extension atas BRW milik DU-036-8 dengan nilai dari DU-036-13
21. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
22. Kirim Return atas BRW milik DU-036-8
23. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
24. Kirim Report Damaged atas aset `Toyota Avanza {runId}`
25. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
26. Kirim Report Missing atas aset `Toyota Avanza {runId}`
27. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
28. Kirim keputusan `Approve` atas aset `Meeting Mic Set {runId}` milik DU-036-9
29. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
30. Kirim Submit atas Draft milik DU-036-10
31. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
32. Kirim Add to Borrow Draft atas aset `Laptop Lenovo T14 {runId}` dengan nilai dari DU-036-19
33. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
34. Kirim Cancel Extension atas BRW milik DU-036-15
35. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
36. Kirim keputusan `Approve` atas pengajuan Extension Request milik DU-036-16
37. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
38. Kirim keputusan `Reject` atas pengajuan Extension Request milik DU-036-16
39. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
40. Kirim Cancel Damage Report atas aset `Excavator Komatsu PC200 {runId}` milik DU-036-17
41. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
42. Kirim keputusan `Reject` atas aset `Meeting Mic Set {runId}` milik DU-036-9
43. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
44. Kirim Bulk Delete atas Draft milik DU-036-10 dan DU-036-18
45. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
46. Ketik Search `{runId}`, tekan Enter
47. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
48. Verifikasi BRW milik DU-036-8 masih berstatus `Borrowed`
49. Verifikasi BRW milik DU-036-9 masih berstatus `Waiting for Approval`
50. Verifikasi BRW milik DU-036-15 masih berstatus `Extension Approval`
51. Verifikasi BRW milik DU-036-16 masih berstatus `Extension Request`
52. Verifikasi BRW milik DU-036-17 masih memuat Damage Report `Waiting for Confirmation`
53. Klik tab `Drafts`
54. Verifikasi Draft milik DU-036-10 masih tampil dengan Total Asset `1`
55. Verifikasi Draft milik DU-036-18 masih tampil dengan Total Asset `1`
56. Klik tab `Transactions`

### Entitas Suspended: Cancel Borrow ke Draft dan aksi tulis Borrower dari halaman pinjaman pribadi ditolak
57. Kirim Cancel Borrow dengan `Save as Draft to edit` atas BRW milik DU-036-7
58. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
59. Masuk sebagai Borrower `Rudi Hartono {runId}`
60. Buka halaman pinjaman pribadi Borrower dari menu Profile
61. Kirim Confirm Handover atas BRW milik DU-036-20 sebagai Borrower
62. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
63. Kirim Cancel Borrow atas BRW milik DU-036-7 sebagai Borrower
64. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
65. Kirim Cancel Missing Report atas aset `Drone DJI Mavic {runId}` milik DU-036-21 sebagai Borrower
66. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
67. Masuk sebagai Total Control `Maya Putri {runId}`
68. Klik menu `Transactions > Borrow`
69. Ketik Search `{runId}`, tekan Enter
70. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
71. Verifikasi BRW milik DU-036-20 masih berstatus `Waiting for Handover`
72. Verifikasi BRW milik DU-036-21 masih memuat Missing Report `Waiting for Confirmation`

### Entitas Expired: modul terbuka, data terbaca, dan setiap aksi tulis ditolak
73. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `Samudra Logistik {runId}` menjadi `Expired`
74. Muat ulang halaman
75. Klik menu `Transactions > Borrow`
76. Ketik Search `{runId}`, tekan Enter
77. Verifikasi halaman Borrow terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Expired`
78. Verifikasi BRW milik DU-036-7 tampil di tabel pada entitas `Expired`
79. Kirim Create BRW dengan nilai dari DU-036-11
80. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
81. Kirim Save Draft pada Draft milik DU-036-10 dengan nilai dari DU-036-12
82. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
83. Kirim Delete atas Draft milik DU-036-10
84. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
85. Kirim Cancel Borrow atas BRW milik DU-036-7
86. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
87. Kirim Hand Over atas BRW milik DU-036-7
88. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
89. Kirim Remind Borrower atas BRW milik DU-036-7
90. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
91. Kirim Request Extension atas BRW milik DU-036-8 dengan nilai dari DU-036-13
92. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
93. Kirim Return atas BRW milik DU-036-8
94. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
95. Kirim Report Damaged atas aset `Toyota Avanza {runId}`
96. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
97. Kirim Report Missing atas aset `Toyota Avanza {runId}`
98. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
99. Kirim keputusan `Approve` atas aset `Meeting Mic Set {runId}` milik DU-036-9
100. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
101. Kirim Submit atas Draft milik DU-036-10
102. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
103. Kirim Add to Borrow Draft atas aset `Laptop Lenovo T14 {runId}` dengan nilai dari DU-036-19
104. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
105. Kirim Cancel Extension atas BRW milik DU-036-15
106. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
107. Kirim keputusan `Approve` atas pengajuan Extension Request milik DU-036-16
108. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
109. Kirim keputusan `Reject` atas pengajuan Extension Request milik DU-036-16
110. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
111. Kirim Cancel Damage Report atas aset `Excavator Komatsu PC200 {runId}` milik DU-036-17
112. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
113. Kirim keputusan `Reject` atas aset `Meeting Mic Set {runId}` milik DU-036-9
114. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
115. Kirim Bulk Delete atas Draft milik DU-036-10 dan DU-036-18
116. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
117. Ketik Search `{runId}`, tekan Enter
118. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
119. Verifikasi BRW milik DU-036-8 masih berstatus `Borrowed`
120. Verifikasi BRW milik DU-036-9 masih berstatus `Waiting for Approval`
121. Verifikasi BRW milik DU-036-15 masih berstatus `Extension Approval`
122. Verifikasi BRW milik DU-036-16 masih berstatus `Extension Request`
123. Verifikasi BRW milik DU-036-17 masih memuat Damage Report `Waiting for Confirmation`
124. Klik tab `Drafts`
125. Verifikasi Draft milik DU-036-10 masih tampil dengan Total Asset `1`
126. Verifikasi Draft milik DU-036-18 masih tampil dengan Total Asset `1`
127. Klik tab `Transactions`

### Entitas Expired: Cancel Borrow ke Draft dan aksi tulis Borrower dari halaman pinjaman pribadi ditolak
128. Kirim Cancel Borrow dengan `Save as Draft to edit` atas BRW milik DU-036-7
129. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
130. Masuk sebagai Borrower `Rudi Hartono {runId}`
131. Buka halaman pinjaman pribadi Borrower dari menu Profile
132. Kirim Confirm Handover atas BRW milik DU-036-20 sebagai Borrower
133. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
134. Kirim Cancel Borrow atas BRW milik DU-036-7 sebagai Borrower
135. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
136. Kirim Cancel Missing Report atas aset `Drone DJI Mavic {runId}` milik DU-036-21 sebagai Borrower
137. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
138. Masuk sebagai Total Control `Maya Putri {runId}`
139. Klik menu `Transactions > Borrow`
140. Ketik Search `{runId}`, tekan Enter
141. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
142. Verifikasi BRW milik DU-036-20 masih berstatus `Waiting for Handover`
143. Verifikasi BRW milik DU-036-21 masih memuat Missing Report `Waiting for Confirmation`

### Entitas Grace: modul terbuka, data terbaca, dan setiap aksi tulis ditolak
144. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `Samudra Logistik {runId}` menjadi `Expired (Grace)`
145. Muat ulang halaman
146. Klik menu `Transactions > Borrow`
147. Ketik Search `{runId}`, tekan Enter
148. Verifikasi halaman Borrow terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Expired (Grace)`
149. Verifikasi BRW milik DU-036-7 tampil di tabel pada entitas `Expired (Grace)`
150. Kirim Create BRW dengan nilai dari DU-036-11
151. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
152. Kirim Save Draft pada Draft milik DU-036-10 dengan nilai dari DU-036-12
153. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
154. Kirim Delete atas Draft milik DU-036-10
155. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
156. Kirim Cancel Borrow atas BRW milik DU-036-7
157. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
158. Kirim Hand Over atas BRW milik DU-036-7
159. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
160. Kirim Remind Borrower atas BRW milik DU-036-7
161. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
162. Kirim Request Extension atas BRW milik DU-036-8 dengan nilai dari DU-036-13
163. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
164. Kirim Return atas BRW milik DU-036-8
165. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
166. Kirim Report Damaged atas aset `Toyota Avanza {runId}`
167. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
168. Kirim Report Missing atas aset `Toyota Avanza {runId}`
169. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
170. Kirim keputusan `Approve` atas aset `Meeting Mic Set {runId}` milik DU-036-9
171. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
172. Kirim Submit atas Draft milik DU-036-10
173. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
174. Kirim Add to Borrow Draft atas aset `Laptop Lenovo T14 {runId}` dengan nilai dari DU-036-19
175. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
176. Kirim Cancel Extension atas BRW milik DU-036-15
177. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
178. Kirim keputusan `Approve` atas pengajuan Extension Request milik DU-036-16
179. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
180. Kirim keputusan `Reject` atas pengajuan Extension Request milik DU-036-16
181. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
182. Kirim Cancel Damage Report atas aset `Excavator Komatsu PC200 {runId}` milik DU-036-17
183. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
184. Kirim keputusan `Reject` atas aset `Meeting Mic Set {runId}` milik DU-036-9
185. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
186. Kirim Bulk Delete atas Draft milik DU-036-10 dan DU-036-18
187. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
188. Ketik Search `{runId}`, tekan Enter
189. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
190. Verifikasi BRW milik DU-036-8 masih berstatus `Borrowed`
191. Verifikasi BRW milik DU-036-9 masih berstatus `Waiting for Approval`
192. Verifikasi BRW milik DU-036-15 masih berstatus `Extension Approval`
193. Verifikasi BRW milik DU-036-16 masih berstatus `Extension Request`
194. Verifikasi BRW milik DU-036-17 masih memuat Damage Report `Waiting for Confirmation`
195. Klik tab `Drafts`
196. Verifikasi Draft milik DU-036-10 masih tampil dengan Total Asset `1`
197. Verifikasi Draft milik DU-036-18 masih tampil dengan Total Asset `1`
198. Klik tab `Transactions`

### Entitas Grace: Cancel Borrow ke Draft dan aksi tulis Borrower dari halaman pinjaman pribadi ditolak
199. Kirim Cancel Borrow dengan `Save as Draft to edit` atas BRW milik DU-036-7
200. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
201. Masuk sebagai Borrower `Rudi Hartono {runId}`
202. Buka halaman pinjaman pribadi Borrower dari menu Profile
203. Kirim Confirm Handover atas BRW milik DU-036-20 sebagai Borrower
204. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
205. Kirim Cancel Borrow atas BRW milik DU-036-7 sebagai Borrower
206. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
207. Kirim Cancel Missing Report atas aset `Drone DJI Mavic {runId}` milik DU-036-21 sebagai Borrower
208. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
209. Masuk sebagai Total Control `Maya Putri {runId}`
210. Klik menu `Transactions > Borrow`
211. Ketik Search `{runId}`, tekan Enter
212. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
213. Verifikasi BRW milik DU-036-20 masih berstatus `Waiting for Handover`
214. Verifikasi BRW milik DU-036-21 masih memuat Missing Report `Waiting for Confirmation`
