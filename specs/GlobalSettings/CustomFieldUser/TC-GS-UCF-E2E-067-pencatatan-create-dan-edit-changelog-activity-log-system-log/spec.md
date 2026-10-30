---
id: TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log
title: "Pencatatan Create dan Edit Custom Field (Field Name, Data Type, Value Setting, Placeholder, Required, Decimal Places, Dua Properti, Rename Bersama Properti Lain) pada Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-274
  - TC-GS-UCF-275
  - TC-GS-UCF-276
  - TC-GS-UCF-277
  - TC-GS-UCF-278
  - TC-GS-UCF-279
  - TC-GS-UCF-280
  - TC-GS-UCF-281
  - TC-GS-UCF-282
  - TC-GS-UCF-283
  - TC-GS-UCF-380
  - TC-GS-UCF-338
coverage:
  web: automated
---

# Pencatatan Create dan Edit Custom Field (Field Name, Data Type, Value Setting, Placeholder, Required, Decimal Places, Dua Properti, Rename Bersama Properti Lain) pada Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Seluruh aksi dan seeding spec ini dilakukan oleh Sari Dewi, sehingga entri System Log berada di Detail Sari Dewi. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field. Langkah yang membuka ulang halaman itu berfungsi sebagai pemulihan state sesudah Activity Log atau System Log.
- Data Pre-setup: tidak ada yang dipakai (seluruh target aksi tulis adalah data milik spec). Pemilik nilai User: Rahmat Hidayat dan Intan Permata (Pre-setup TC, tidak diubah selain nilai Custom Field milik spec).
- Data Dinamis (nama bersuffix `{runId}-067`; fixture baru `Fixture.customFieldUser.logCreateEdit067`):
  - Di-seed lewat API oleh Sari Dewi di hook `before` (Create menghasilkan satu entri Create per field di Changelog, System Log, dan Activity Log; entri ini bukan objek asersi, kecuali TC-GS-UCF-380 dan 338 yang hasil Search-nya memuatnya): `Log Rename Probe {runId}-067` (Text, Placeholder kosong, Required No; TC-GS-UCF-275), `Log Type Probe {runId}-067` (Dropdown `One`, `Two`; nilai User Rahmat Hidayat = `One`; TC-GS-UCF-276), `Log Value Probe {runId}-067` (Dropdown `Red`, `Green`, `Blue`; TC-GS-UCF-277), `Log Rename Value Probe {runId}-067` (Dropdown `Red`, `Green`, `Blue`; nilai User Rahmat Hidayat dan Intan Permata = `Green`; TC-GS-UCF-278), `Log Remove Value Probe {runId}-067` (Dropdown `Low`, `Mid`, `High`; nilai User Rahmat Hidayat dan Intan Permata = `Mid`; TC-GS-UCF-279), `Log Placeholder Probe {runId}-067` (Text, Placeholder kosong; TC-GS-UCF-280), `Log Required Probe {runId}-067` (Text, Required No; TC-GS-UCF-281), `Log Decimal Probe {runId}-067` (Numeric, Decimal Places 2, belum pernah memiliki nilai User; TC-GS-UCF-282), `Multi Log {runId}-067` (Text, Required No, Placeholder kosong; TC-GS-UCF-283), `Log Num Probe {runId}-067` (Text, bebas nilai User; TC-GS-UCF-380), `Rename Plus {runId}-067` (Text, Placeholder kosong, Required No; TC-GS-UCF-338). Mekanisme seeding nilai User (Rahmat Hidayat, Intan Permata) disediakan tim FE/BE.
  - Dibuat lewat UI oleh spec: `Log Create Probe {runId}-067` (TC-GS-UCF-274).
  - Diubah lewat UI oleh spec: `Log Rename Probe` menjadi `Log Rename Probe Two`, `Log Type Probe` berganti Data Type menjadi `Text`, `Log Value Probe` mendapat value `Yellow`, `Log Rename Value Probe` mengubah `Green` menjadi `Emerald`, `Log Remove Value Probe` menghapus `Mid`, `Log Placeholder Probe` mendapat Placeholder `Type here`, `Log Required Probe` menjadi Required `Yes`, `Log Decimal Probe` Decimal Places menjadi `0`, `Multi Log` Required `Yes` dan Placeholder `Fill`, `Log Num Probe` Text ke Numeric ke Text, `Rename Plus` menjadi `Rename Plus Two` dengan Required `Yes` (seluruhnya bersuffix `{runId}-067`).
  - Entri Changelog, System Log, dan Activity Log bersifat audit trail permanen dan tidak dibersihkan. Asersi "tepat N entri" memakai nama bersuffix unik per run (baseline nol untuk Action yang diasersi, S-12), dengan Search memakai nama lengkap bersuffix.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh Custom Field bersuffix `{runId}-067` yang masih ada.
- Setup Column Modal Changelog: konfigurasi default; hook `beforeEach` membersihkan cache browser.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: seeding Custom Field dan nilai User lewat API; Search pada Modal Changelog, tab System Log di Detail User, dan Activity Log tab User Action (kolom pencarian Activity Log dan System Log tidak dijelaskan di TC; lihat Temuan untuk QA).
- State global: tidak ada yang diubah selain flag Guided Tooltip.

## Test Steps

### TC-GS-UCF-274: Log Create Custom Field di Changelog, System Log, dan Activity Log

1. Klik `[+ Custom Field]`
2. Isi Field Name `Log Create Probe {runId}-067`
3. Pilih Data Type `Text`
4. Klik `[Submit]`
5. Tunggu aksi selesai (modal tertutup)
6. Klik icon Changelog
7. Ketik Search `Log Create Probe {runId}-067`, tekan Enter
8. Verifikasi Changelog: tepat 1 entri untuk `Log Create Probe {runId}-067`
9. Verifikasi entri: Action `Create`, Field `Log Create Probe {runId}-067`, Old Value `-`, New Value `Log Create Probe {runId}-067`, Modified By `Sari D`
10. Klik `[✕]`
11. Buka Global Settings > User > Detail Sari Dewi > tab System Log
12. Ketik Search `Log Create Probe {runId}-067`, tekan Enter
13. Verifikasi System Log Sari Dewi: tepat 1 entri dengan Object `Custom Field`, Name `Log Create Probe {runId}-067`
14. Buka Global Settings > Activity Log > tab User Action
15. Ketik Search `Log Create Probe {runId}-067`, tekan Enter
16. Verifikasi Activity Log: tepat 1 entri dengan Modified By `Sari D`
17. Buka Global Settings > User > Custom Field

### TC-GS-UCF-275: Log Edit Field Name mencatat nama lama dan baru dengan prefiks nama baru

18. Ketik Search `Log Rename Probe {runId}-067` pada tabel utama, tekan Enter
19. Klik `⋯` pada baris `Log Rename Probe {runId}-067`, pilih `Edit`
20. Ubah Field Name menjadi `Log Rename Probe Two {runId}-067`
21. Klik `[Save]`
22. Tunggu aksi selesai (modal tertutup)
23. Klik icon Changelog
24. Ketik Search `Log Rename Probe Two {runId}-067`, tekan Enter
25. Verifikasi Changelog: tepat 1 entri Edit
26. Verifikasi entri: Action `Edit`, Field `Log Rename Probe Two {runId}-067 — Field Name`, Old Value `Log Rename Probe {runId}-067`, New Value `Log Rename Probe Two {runId}-067`, Modified By `Sari D`
27. Klik `[✕]`
28. Buka Global Settings > User > Detail Sari Dewi > tab System Log
29. Ketik Search `Log Rename Probe Two {runId}-067`, tekan Enter
30. Verifikasi System Log Sari Dewi: tepat 1 entri Edit dengan Object `Custom Field`
31. Buka Global Settings > Activity Log > tab User Action
32. Ketik Search `Log Rename Probe Two {runId}-067`, tekan Enter
33. Verifikasi Activity Log: tepat 1 entri Edit dengan Modified By `Sari D`
34. Buka Global Settings > User > Custom Field

### TC-GS-UCF-276: Log Edit Data Type mencatat label tipe lama dan baru serta value yang dibuang

35. Ketik Search `Log Type Probe {runId}-067` pada tabel utama, tekan Enter
36. Klik `⋯` pada baris `Log Type Probe {runId}-067`, pilih `Edit`
37. Ubah Data Type menjadi `Text`
38. Klik `[Save]`
39. Klik `[Change Data Type]`
40. Tunggu aksi selesai (modal tertutup)
41. Klik icon Changelog
42. Ketik Search `Log Type Probe {runId}-067`, tekan Enter
43. Verifikasi Changelog: entri Edit `Log Type Probe {runId}-067 — Data Type` tampil tepat 1 kali dengan Old Value `Dropdown` dan New Value `Text`
44. Verifikasi Changelog: entri Edit `Log Type Probe {runId}-067 — Value Setting` tampil tepat 1 kali dengan Old Value `One, Two` dan New Value `-`
45. Verifikasi kedua entri Changelog bermodifikasi `Sari D`
46. Klik `[✕]`
47. Buka Global Settings > User > Detail Sari Dewi > tab System Log
48. Ketik Search `Log Type Probe {runId}-067`, tekan Enter
49. Verifikasi System Log Sari Dewi: entri Edit Data Type dan entri Edit Value Setting masing-masing tampil tepat 1 kali dengan Object `Custom Field`, Name `Log Type Probe {runId}-067`
50. Buka Global Settings > Activity Log > tab User Action
51. Ketik Search `Log Type Probe {runId}-067`, tekan Enter
52. Verifikasi Activity Log: entri Edit Data Type dan entri Edit Value Setting masing-masing tampil tepat 1 kali dengan Modified By `Sari D`
53. Buka Global Settings > User > Custom Field

### TC-GS-UCF-277: Log Edit Value Setting saat value ditambah

54. Ketik Search `Log Value Probe {runId}-067` pada tabel utama, tekan Enter
55. Klik `⋯` pada baris `Log Value Probe {runId}-067`, pilih `Edit`
56. Ketik `Yellow` di Dropdown Values, tekan Enter
57. Klik `[Save]`
58. Tunggu aksi selesai (modal tertutup)
59. Klik icon Changelog
60. Ketik Search `Log Value Probe {runId}-067`, tekan Enter
61. Verifikasi Changelog: tepat 1 entri Edit (satu entri level field)
62. Verifikasi entri: Action `Edit`, Field `Log Value Probe {runId}-067 — Value Setting`, Old Value `Red, Green, Blue`, New Value `Red, Green, Blue, Yellow`
63. Verifikasi Changelog: Modified By `Sari D`
64. Klik `[✕]`
65. Buka Global Settings > User > Detail Sari Dewi > tab System Log
66. Ketik Search `Log Value Probe {runId}-067`, tekan Enter
67. Verifikasi System Log Sari Dewi: tepat 1 entri Edit dengan Object `Custom Field`, Name `Log Value Probe {runId}-067`
68. Buka Global Settings > Activity Log > tab User Action
69. Ketik Search `Log Value Probe {runId}-067`, tekan Enter
70. Verifikasi Activity Log: tepat 1 entri Edit dengan Modified By `Sari D`
71. Buka Global Settings > User > Custom Field

### TC-GS-UCF-278: Log rename value yang dipakai user: satu entri level field tanpa entri per user

72. Ketik Search `Log Rename Value Probe {runId}-067` pada tabel utama, tekan Enter
73. Klik `⋯` pada baris `Log Rename Value Probe {runId}-067`, pilih `Edit`
74. Klik teks badge `Green`, ubah menjadi `Emerald`, tekan Enter
75. Klik `[Save]`
76. Tunggu aksi selesai (modal tertutup)
77. Klik icon Changelog
78. Ketik Search `Log Rename Value Probe {runId}-067`, tekan Enter
79. Verifikasi Changelog: tepat 1 entri Edit
80. Verifikasi entri Edit: Field `Log Rename Value Probe {runId}-067 — Value Setting`, Old Value `Red, Green, Blue`, New Value `Red, Emerald, Blue`
81. Verifikasi entri Edit: Modified By `Sari D`
82. Klik `[✕]`
83. Buka Global Settings > User > Detail Sari Dewi > tab System Log
84. Ketik Search `Log Rename Value Probe {runId}-067`, tekan Enter
85. Verifikasi System Log Sari Dewi: tepat 1 entri Edit dengan Object `Custom Field`, Name `Log Rename Value Probe {runId}-067` dan tidak ada entri Edit kedua untuk nama itu (tidak ada entri per user terdampak)
86. Buka Global Settings > Activity Log > tab User Action
87. Ketik Search `Log Rename Value Probe {runId}-067`, tekan Enter
88. Verifikasi Activity Log: tepat 1 entri Edit dengan Modified By `Sari D` dan tidak ada entri Edit kedua untuk nama itu (tidak ada entri per user terdampak)
89. Buka Global Settings > User > Custom Field

### TC-GS-UCF-279: Log remove value yang dipakai user: satu entri level field

90. Ketik Search `Log Remove Value Probe {runId}-067` pada tabel utama, tekan Enter
91. Klik `⋯` pada baris `Log Remove Value Probe {runId}-067`, pilih `Edit`
92. Klik `×` pada badge `Mid`
93. Klik `[Remove]`
94. Klik `[Save]`
95. Tunggu aksi selesai (modal tertutup)
96. Klik icon Changelog
97. Ketik Search `Log Remove Value Probe {runId}-067`, tekan Enter
98. Verifikasi Changelog: tepat 1 entri Edit
99. Verifikasi entri Edit: Field `Log Remove Value Probe {runId}-067 — Value Setting` (format `<Nama Field> — Value Setting`), Old Value `Low, Mid, High`, New Value `Low, High`
100. Klik `[✕]`
101. Buka Global Settings > User > Detail Sari Dewi > tab System Log
102. Ketik Search `Log Remove Value Probe {runId}-067`, tekan Enter
103. Verifikasi System Log Sari Dewi: tepat 1 entri Edit dengan Object `Custom Field`, Name `Log Remove Value Probe {runId}-067` dan tidak ada entri Edit kedua untuk nama itu (tidak ada entri per user terdampak)
104. Buka Global Settings > Activity Log > tab User Action
105. Ketik Search `Log Remove Value Probe {runId}-067`, tekan Enter
106. Verifikasi Activity Log: tepat 1 entri Edit dengan Modified By `Sari D` dan tidak ada entri Edit kedua untuk nama itu (tidak ada entri per user terdampak)
107. Buka Global Settings > User > Custom Field

### TC-GS-UCF-280: Log Edit Placeholder: nilai tersimpan, strip bila kosong, bukan default List

108. Ketik Search `Log Placeholder Probe {runId}-067` pada tabel utama, tekan Enter
109. Klik `⋯` pada baris `Log Placeholder Probe {runId}-067`, pilih `Edit`
110. Isi Placeholder `Type here`
111. Klik `[Save]`
112. Tunggu aksi selesai (modal tertutup)
113. Klik icon Changelog
114. Ketik Search `Log Placeholder Probe {runId}-067`, tekan Enter
115. Verifikasi Changelog: tepat 1 entri Edit dengan Field `Log Placeholder Probe {runId}-067 — Placeholder`
116. Verifikasi entri: Old Value `-` (bukan teks default `Enter log placeholder probe {runId}-067`)
117. Verifikasi entri: New Value `Type here`
118. Klik `[✕]`
119. Buka Global Settings > User > Detail Sari Dewi > tab System Log
120. Ketik Search `Log Placeholder Probe {runId}-067`, tekan Enter
121. Verifikasi System Log Sari Dewi: memuat entri Edit yang sama (Object `Custom Field`, Name `Log Placeholder Probe {runId}-067`)
122. Buka Global Settings > Activity Log > tab User Action
123. Ketik Search `Log Placeholder Probe {runId}-067`, tekan Enter
124. Verifikasi Activity Log (Modified By `Sari D`): memuat entri Edit yang sama
125. Buka Global Settings > User > Custom Field

### TC-GS-UCF-281: Log Edit Required mencatat Yes dan No

126. Ketik Search `Log Required Probe {runId}-067` pada tabel utama, tekan Enter
127. Klik `⋯` pada baris `Log Required Probe {runId}-067`, pilih `Edit`
128. Ubah Required menjadi `Yes`
129. Klik `[Save]`
130. Tunggu aksi selesai (modal tertutup)
131. Klik icon Changelog
132. Ketik Search `Log Required Probe {runId}-067`, tekan Enter
133. Verifikasi Changelog: tepat 1 entri Edit dengan Field `Log Required Probe {runId}-067 — Required`
134. Verifikasi entri: Old Value `No`, New Value `Yes`
135. Klik `[✕]`
136. Buka Global Settings > User > Detail Sari Dewi > tab System Log
137. Ketik Search `Log Required Probe {runId}-067`, tekan Enter
138. Verifikasi System Log Sari Dewi: memuat entri Edit yang sama (Object `Custom Field`, Name `Log Required Probe {runId}-067`)
139. Buka Global Settings > Activity Log > tab User Action
140. Ketik Search `Log Required Probe {runId}-067`, tekan Enter
141. Verifikasi Activity Log (Modified By `Sari D`): memuat entri Edit yang sama
142. Buka Global Settings > User > Custom Field

### TC-GS-UCF-282: Log perubahan Decimal Places dicatat sebagai Value Setting

143. Ketik Search `Log Decimal Probe {runId}-067` pada tabel utama, tekan Enter
144. Klik `⋯` pada baris `Log Decimal Probe {runId}-067`, pilih `Edit`
145. Ubah Decimal Places menjadi `0`
146. Klik `[Save]`
147. Tunggu aksi selesai (modal tertutup)
148. Klik icon Changelog
149. Ketik Search `Log Decimal Probe {runId}-067`, tekan Enter
150. Verifikasi Changelog: tepat 1 entri Edit
151. Verifikasi entri: Action `Edit`, Field `Log Decimal Probe {runId}-067 — Value Setting`, Old Value `2 Decimal Places`, New Value `0 Decimal Places`
152. Verifikasi Changelog: tidak ada entri dengan Field `Log Decimal Probe {runId}-067 — Decimal Places`
153. Klik `[✕]`
154. Buka Global Settings > User > Detail Sari Dewi > tab System Log
155. Ketik Search `Log Decimal Probe {runId}-067`, tekan Enter
156. Verifikasi System Log Sari Dewi: memuat entri Edit yang sama (Name `Log Decimal Probe {runId}-067`)
157. Buka Global Settings > Activity Log > tab User Action
158. Ketik Search `Log Decimal Probe {runId}-067`, tekan Enter
159. Verifikasi Activity Log: memuat entri Edit yang sama (Name `Log Decimal Probe {runId}-067`)
160. Buka Global Settings > User > Custom Field

### TC-GS-UCF-283: Edit yang mengubah dua properti mencatat tepat dua entri

161. Ketik Search `Multi Log {runId}-067` pada tabel utama, tekan Enter
162. Klik `⋯` pada baris `Multi Log {runId}-067`, pilih `Edit`
163. Ubah Required menjadi `Yes`
164. Ubah Placeholder menjadi `Fill`
165. Klik `[Save]`
166. Tunggu aksi selesai (modal tertutup)
167. Klik icon Changelog
168. Ketik Search `Multi Log {runId}-067`, tekan Enter
169. Verifikasi Changelog: tepat 2 entri Edit
170. Verifikasi entri Edit `Multi Log {runId}-067 — Required`: Old Value `No`, New Value `Yes`
171. Verifikasi entri Edit `Multi Log {runId}-067 — Placeholder`: Old Value `—`, New Value `Fill`
172. Klik `[✕]`
173. Buka Global Settings > User > Detail Sari Dewi > tab System Log
174. Ketik Search `Multi Log {runId}-067`, tekan Enter
175. Verifikasi System Log Sari Dewi: tepat 2 entri Edit (`Multi Log {runId}-067 — Required` dan `Multi Log {runId}-067 — Placeholder`)
176. Buka Global Settings > Activity Log > tab User Action
177. Ketik Search `Multi Log {runId}-067`, tekan Enter
178. Verifikasi Activity Log: tepat 2 entri Edit (`Multi Log {runId}-067 — Required` dan `Multi Log {runId}-067 — Placeholder`)
179. Buka Global Settings > User > Custom Field

### TC-GS-UCF-380: Log perubahan Data Type dari dan ke Numeric mencatat entri Data Type dan Value Setting

180. Ketik Search `Log Num Probe {runId}-067` pada tabel utama, tekan Enter
181. Klik `⋯` pada baris `Log Num Probe {runId}-067`, pilih `Edit`
182. Ubah Data Type menjadi `Numeric`
183. Klik `[Save]`
184. Klik `⋯` pada baris `Log Num Probe {runId}-067`, pilih `Edit`
185. Ubah Data Type menjadi `Text`
186. Klik `[Save]`
187. Tunggu aksi selesai (modal tertutup)
188. Klik icon Changelog
189. Ketik Search `Log Num Probe {runId}-067`, tekan Enter
190. Verifikasi Changelog: tepat 4 entri Edit
191. Verifikasi entri Text ke Numeric: Edit `Log Num Probe {runId}-067 — Data Type` (Old Value `Text`, New Value `Numeric`)
192. Verifikasi entri Text ke Numeric: Edit `Log Num Probe {runId}-067 — Value Setting` (Old Value `—`, New Value `0 Decimal Places`)
193. Verifikasi entri Numeric ke Text: Edit `Log Num Probe {runId}-067 — Data Type` (Old Value `Numeric`, New Value `Text`)
194. Verifikasi entri Numeric ke Text tampil: Edit `Log Num Probe {runId}-067 — Value Setting` (Old Value `0 Decimal Places`, New Value `—`)
195. Verifikasi tidak ada entri dengan Field `Decimal Places`
196. Klik `[✕]`

### TC-GS-UCF-338: Rename Field Name bersama perubahan properti lain: prefiks nama baru pada entri Changelog

197. Ketik Search `Rename Plus {runId}-067` pada tabel utama, tekan Enter
198. Klik `⋯` pada baris `Rename Plus {runId}-067`, pilih `Edit`
199. Ubah Field Name menjadi `Rename Plus Two {runId}-067`
200. Ubah Required menjadi `Yes`
201. Klik `[Save]`
202. Verifikasi toast sukses: "Success, custom field has been updated."
203. Klik icon Changelog
204. Ketik Search `Rename Plus Two {runId}-067`, tekan Enter
205. Verifikasi dua entri Edit tampil
206. Verifikasi entri Edit: Field `Rename Plus Two {runId}-067 — Field Name`, Old Value `Rename Plus {runId}-067`, New Value `Rename Plus Two {runId}-067`
207. Verifikasi entri Edit: Field `Rename Plus Two {runId}-067 — Required`, Old Value `No`, New Value `Yes`
208. Verifikasi prefiks nama pada kedua entri memakai nama baru `Rename Plus Two {runId}-067`
209. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 380, 338. TC-GS-UCF-380 dan 338 hanya memakai Changelog (sesuai TC) dan ditaruh di akhir supaya pola tiga surface tidak terputus. Pola tiga surface (Changelog, System Log Detail Sari Dewi, Activity Log tab User Action) dari TC-GS-UCF-274 sampai 283 identik; langkah pembukanya diulang per TC karena nama yang dicari berbeda. Penyimpangan dari urutan TC sumber: tidak ada selain penempatan ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengisian Search tabel utama untuk mempersempit ke field milik spec, Search pada Changelog, System Log, dan Activity Log, penutupan Modal Changelog lewat `[✕]` (tanpa dialog karena tidak ada form), pembukaan ulang halaman Global Settings > User > Custom Field sesudah System Log dan Activity Log (pemulihan state), dan langkah "Tunggu aksi selesai (modal tertutup)" sesudah `[Submit]` atau `[Save]` yang hasilnya tidak diasersi langsung dan langkah berikutnya berpindah surface (bagian 8b butir 8). Pada TC-GS-UCF-338 toast sukses diasersi (Expected a) sehingga tidak ada langkah tunggu.
- Asersi "tepat N entri" memakai nama bersuffix unik per run sebagai baseline nol (S-12); Search memakai nama lengkap sehingga entri Create hasil seeding tidak ikut terhitung pada Action Edit. Asersi Expected "tidak ada entri properti yang tidak berubah" TC-GS-UCF-283 dan "tidak ada entri per user terdampak" TC-GS-UCF-278 dan 279 dan "tidak ada entri Decimal Places" TC-GS-UCF-282 dan 380 diasersi lewat hitungan tepat N entri Edit dengan daftar entri yang diharapkan di surface yang sama; asersi absence log murni ada di spec 070. Klausa itu dirujuk ke S-05 sebagai asersi jumlah, bukan absence.
- Spec melewati sekitar 35 langkah (209 langkah). Sebagian besar blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log), yang tidak dihitung ke ambang (bagian 3 smell). Seluruhnya satu kelas (pencatatan Create dan Edit, satu akun aktor) dan tiap blok TC memakai Custom Field bersuffix sendiri sehingga tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - Mekanisme pencarian di tab System Log Detail User dan Activity Log tab User Action ("buka ... tab System Log" tanpa langkah Search) tidak dijelaskan di TC; spec memakai Search atas nama field bersuffix pada kedua surface dan membaca kolom Object, Name, Modified By dari baris hasil. Kolom yang ada di System Log dan Activity Log tidak dijelaskan TC.
  - Token nilai kosong tidak konsisten di TC: TC-GS-UCF-274 dan 276 menulis `-` untuk Old Value atau New Value kosong, TC-GS-UCF-283 dan 380 menulis `—`, dan TC-GS-UCF-280 menulis `-`. Spec mengikuti masing-masing TC; mohon QA menetapkan satu token.
  - TC-GS-UCF-278 dan 279 Expected b "tidak ada entri per user terdampak di surface mana pun" tidak menyatakan wujud entri per user (Name, Object); spec mengasersi hanya satu entri Edit untuk nama field di tiap surface.
  - TC-GS-UCF-276 langkah 3 menyebut `[Change Data Type]` tanpa menyatakan dialog yang memuatnya (dialog D-01 Data Type berubah); dialog tidak diasersi karena tidak ada Expected-nya.
  - TC-GS-UCF-280 Expected a mengacu "teks default `Enter log placeholder probe`"; karena nama field bersuffix, spec mengasersi teks default `Enter log placeholder probe {runId}-067` sesuai asumsi bahwa default List diturunkan dari nama field. Aturan penurunan default tidak dijelaskan di TC.
  - TC-GS-UCF-277 sampai 279 menyebut Pre-setup nilai User (Rahmat Hidayat, Intan Permata) tanpa menyatakan cara men-seed nilai Dropdown pada Detail User; mekanisme seeding disediakan tim FE/BE.
  - Post Condition TC-GS-UCF-274 (Log Create Probe) dan TC-GS-UCF-338 (Rename Plus Two Required Yes) tidak punya langkah observasi di TC, dan tidak diasersi.
  - Nilai Date entri log tidak diasersi di spec ini (TC-GS-UCF-274 sampai 338 tidak memuat Expected Date).
