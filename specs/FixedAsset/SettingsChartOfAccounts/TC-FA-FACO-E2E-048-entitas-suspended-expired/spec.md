---
id: TC-FA-FACO-E2E-048-entitas-suspended-expired
title: "Aksi tulis Chart of Accounts ditolak saat entitas Suspended atau Expired"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["T-11", "§[F-FACO-01] Create Account#p1", "§[F-FACO-02] Edit Account#p1", "§9.4.2#r28", "EB-AKS-7"]
smoke: []
dependsOn: []
trace:
  "T-11": [20, 34, 42, 48, 55, 64, 73, 82, 96, 110, 118, 124, 131, 140, 149, 158]
  "§[F-FACO-01] Create Account#p1": [20, 96]
  "§[F-FACO-02] Edit Account#p1": [34, 110]
  "§9.4.2#r28": [20, 27, 34, 39, 42, 45, 48, 51, 55, 58, 64, 67, 73, 76, 82, 85, 96, 103, 110, 115, 118, 121, 124, 127, 131, 134, 140, 143, 149, 152, 158, 161]
  "EB-AKS-7": [20, 34, 42, 48, 55, 64, 73, 82, 96, 110, 118, 124, 131, 140, 149, 158]
anchor: [9, 14, 25, 90, 101]
coverage:
  web: automated
---

# Aksi tulis Chart of Accounts ditolak saat entitas Suspended atau Expired

## Prerequisites
- Aktor: Default User (Total Control permanen) pada tiap entitas; spec ini memakai tiga entitas khusus yang tidak dipakai spec lain.
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-048-1: Entitas `Client Aktif {runId}` berstatus Active.
  - DU-048-2: Entitas `Client Suspended {runId}` berstatus Suspended.
  - DU-048-3: Entitas `Client Expired {runId}` berstatus Expired.
  - DU-048-4: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor, pada entitas `Client Suspended {runId}`.
  - DU-048-5: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor, pada entitas `Client Expired {runId}`.
  - DU-048-11: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor, pada entitas `Client Suspended {runId}`.
  - DU-048-12: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor, pada entitas `Client Expired {runId}`.

## Test Steps

### Pembanding di entitas Active: Create Account berhasil
1. Masuk sebagai Default User entitas `Client Aktif {runId}`
2. Buka halaman Settings > Accounting
3. Klik tab `Chart of Accounts`
4. Klik `+ Account`
5. Isi Account Code `7-2001-{runId}`
6. Isi Account Name `Office Equipment Cost {runId}`
7. Pilih Account Function `Asset Cost`
8. Klik `[Submit]`
9. Verifikasi toast `Success, account has been created.` tampil

### Create Account ditolak di entitas Suspended
10. Masuk sebagai Default User entitas `Client Suspended {runId}`
11. Buka halaman Settings > Accounting
12. Klik tab `Chart of Accounts`
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi baris Account Code `5-6001-{runId}` tampil di tabel
15. Klik `+ Account`
16. Isi Account Code `8-1001-{runId}`
17. Isi Account Name `Land Improvement Cost {runId}`
18. Pilih Account Function `Asset Cost`
19. Klik `[Submit]`
20. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
21. Masuk sebagai Default User entitas `Client Suspended {runId}`
22. Buka halaman Settings > Accounting
23. Klik tab `Chart of Accounts`
24. Ketik Search `{runId}`, tekan Enter
25. Verifikasi baris Account Code `5-6001-{runId}` tampil di tabel
26. Ganti isi kotak search dengan `8-1001-{runId}`, tekan Enter
27. Verifikasi empty state `No results found` tampil karena akun `8-1001-{runId}` tidak tercipta
28. Klik `(←)` pada kotak Search
29. Ketik Search `{runId}`, tekan Enter

### Edit Account ditolak di entitas Suspended
30. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
31. Klik `Edit`
32. Ganti Account Name dengan `Depreciation Expense – Admin Revisi S {runId}`
33. Klik `[Save]`
34. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
35. Masuk sebagai Default User entitas `Client Suspended {runId}`
36. Buka halaman Settings > Accounting
37. Klik tab `Chart of Accounts`
38. Ketik Search `{runId}`, tekan Enter
39. Verifikasi baris Account Code `5-6001-{runId}` tetap memuat Account Name `Depreciation Expense – Admin {runId}`

### Activate single ditolak di entitas Suspended
40. Klik Switch Status pada baris Account Code `4-7001-{runId}`
41. Klik `[Activate]` pada dialog konfirmasi
42. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
43. Muat ulang halaman
44. Ketik Search `{runId}`, tekan Enter
45. Verifikasi Switch Status pada baris Account Code `4-7001-{runId}` Inactive

### Deactivate single ditolak di entitas Suspended
46. Klik Switch Status pada baris Account Code `5-6001-{runId}`
47. Klik `[Deactivate]` pada dialog konfirmasi
48. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
49. Muat ulang halaman
50. Ketik Search `{runId}`, tekan Enter
51. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Active

### Delete single ditolak di entitas Suspended
52. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
53. Klik `Delete`
54. Klik `[Delete]` pada dialog konfirmasi
55. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
56. Muat ulang halaman
57. Ketik Search `{runId}`, tekan Enter
58. Verifikasi baris Account Code `5-6001-{runId}` tetap tampil di tabel

### Bulk Activate ditolak di entitas Suspended
59. Centang baris Account Code `5-6001-{runId}`
60. Centang baris Account Code `4-7001-{runId}`
61. Klik `Bulk Action`
62. Klik `Activate`
63. Klik `[Activate]` pada dialog konfirmasi
64. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
65. Muat ulang halaman
66. Ketik Search `{runId}`, tekan Enter
67. Verifikasi Switch Status pada baris Account Code `4-7001-{runId}` Inactive

### Bulk Deactivate ditolak di entitas Suspended
68. Centang baris Account Code `5-6001-{runId}`
69. Centang baris Account Code `4-7001-{runId}`
70. Klik `Bulk Action`
71. Klik `Deactivate`
72. Klik `[Deactivate]` pada dialog konfirmasi
73. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
74. Muat ulang halaman
75. Ketik Search `{runId}`, tekan Enter
76. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Active

### Bulk Delete ditolak di entitas Suspended
77. Centang baris Account Code `5-6001-{runId}`
78. Centang baris Account Code `4-7001-{runId}`
79. Klik `Bulk Action`
80. Klik `Delete`
81. Klik `[Delete]` pada dialog konfirmasi
82. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
83. Muat ulang halaman
84. Ketik Search `{runId}`, tekan Enter
85. Verifikasi baris Account Code `5-6001-{runId}` dan `4-7001-{runId}` tetap tampil di tabel

### Create Account ditolak di entitas Expired
86. Masuk sebagai Default User entitas `Client Expired {runId}`
87. Buka halaman Settings > Accounting
88. Klik tab `Chart of Accounts`
89. Ketik Search `{runId}`, tekan Enter
90. Verifikasi baris Account Code `5-6001-{runId}` tampil di tabel
91. Klik `+ Account`
92. Isi Account Code `8-1002-{runId}`
93. Isi Account Name `Building Improvement Cost {runId}`
94. Pilih Account Function `Asset Cost`
95. Klik `[Submit]`
96. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
97. Masuk sebagai Default User entitas `Client Expired {runId}`
98. Buka halaman Settings > Accounting
99. Klik tab `Chart of Accounts`
100. Ketik Search `{runId}`, tekan Enter
101. Verifikasi baris Account Code `5-6001-{runId}` tampil di tabel
102. Ganti isi kotak search dengan `8-1002-{runId}`, tekan Enter
103. Verifikasi empty state `No results found` tampil karena akun `8-1002-{runId}` tidak tercipta
104. Klik `(←)` pada kotak Search
105. Ketik Search `{runId}`, tekan Enter

### Edit Account ditolak di entitas Expired
106. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
107. Klik `Edit`
108. Ganti Account Name dengan `Depreciation Expense – Admin Revisi E {runId}`
109. Klik `[Save]`
110. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
111. Masuk sebagai Default User entitas `Client Expired {runId}`
112. Buka halaman Settings > Accounting
113. Klik tab `Chart of Accounts`
114. Ketik Search `{runId}`, tekan Enter
115. Verifikasi baris Account Code `5-6001-{runId}` tetap memuat Account Name `Depreciation Expense – Admin {runId}`

### Activate single ditolak di entitas Expired
116. Klik Switch Status pada baris Account Code `4-7001-{runId}`
117. Klik `[Activate]` pada dialog konfirmasi
118. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
119. Muat ulang halaman
120. Ketik Search `{runId}`, tekan Enter
121. Verifikasi Switch Status pada baris Account Code `4-7001-{runId}` Inactive

### Deactivate single ditolak di entitas Expired
122. Klik Switch Status pada baris Account Code `5-6001-{runId}`
123. Klik `[Deactivate]` pada dialog konfirmasi
124. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
125. Muat ulang halaman
126. Ketik Search `{runId}`, tekan Enter
127. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Active

### Delete single ditolak di entitas Expired
128. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
129. Klik `Delete`
130. Klik `[Delete]` pada dialog konfirmasi
131. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
132. Muat ulang halaman
133. Ketik Search `{runId}`, tekan Enter
134. Verifikasi baris Account Code `5-6001-{runId}` tetap tampil di tabel

### Bulk Activate ditolak di entitas Expired
135. Centang baris Account Code `5-6001-{runId}`
136. Centang baris Account Code `4-7001-{runId}`
137. Klik `Bulk Action`
138. Klik `Activate`
139. Klik `[Activate]` pada dialog konfirmasi
140. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
141. Muat ulang halaman
142. Ketik Search `{runId}`, tekan Enter
143. Verifikasi Switch Status pada baris Account Code `4-7001-{runId}` Inactive

### Bulk Deactivate ditolak di entitas Expired
144. Centang baris Account Code `5-6001-{runId}`
145. Centang baris Account Code `4-7001-{runId}`
146. Klik `Bulk Action`
147. Klik `Deactivate`
148. Klik `[Deactivate]` pada dialog konfirmasi
149. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
150. Muat ulang halaman
151. Ketik Search `{runId}`, tekan Enter
152. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Active

### Bulk Delete ditolak di entitas Expired
153. Centang baris Account Code `5-6001-{runId}`
154. Centang baris Account Code `4-7001-{runId}`
155. Klik `Bulk Action`
156. Klik `Delete`
157. Klik `[Delete]` pada dialog konfirmasi
158. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
159. Muat ulang halaman
160. Ketik Search `{runId}`, tekan Enter
161. Verifikasi baris Account Code `5-6001-{runId}` dan `4-7001-{runId}` tetap tampil di tabel
