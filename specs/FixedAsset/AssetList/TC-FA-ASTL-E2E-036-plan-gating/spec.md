---
id: TC-FA-ASTL-E2E-036-plan-gating
title: "Perilaku modul pada tiap tier plan dan level Feature Suite"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-18", "§9.10#r1", "§9.10#r2", "§9.10#r3", "§9.10#r4", "§9.10#p1", "§9.10#p2", "EB-AKS-8"]
smoke: []
dependsOn: []
trace:
  "EC-18": [8, 9]
  "§9.10#r1": [18, 23]
  "§9.10#r2": [31, 36]
  "§9.10#r3": [44, 49]
  "§9.10#r4": [57, 62]
  "§9.10#p1": [8, 9]
  "§9.10#p2": [67, 68, 69, 70, 73, 74, 77, 78, 82, 83, 88, 93, 100, 101, 102, 103, 104, 107, 108, 111, 112, 116, 117, 118, 123, 128, 135, 136, 137, 138, 139, 142, 143, 146, 147, 151, 152, 153, 158, 163]
  "EB-AKS-8": [18, 23, 31, 36, 44, 49, 57, 62]
anchor: [3]
coverage:
  web: automated
---

# Perilaku modul pada tiap tier plan dan level Feature Suite

## Prerequisites
- Aktor: `Agus Setiawan {runId}`, pemegang role Total Control; operator Admin Console yang mengubah plan entitas adalah `Operator Platform`.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - Memakai entitas khusus yang tidak dipakai spec lain.
  - DU-036-1: Entitas, Name `PT Nusa Teknik {runId}`, Plan `enterprise`
  - DU-036-2: User, Name `Agus Setiawan {runId}`, Role `Total Control`, Cakupan `Seluruh client`
  - DU-036-3: Group, Name `IT {runId}`
  - DU-036-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, Asset Class `Peralatan IT {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`
  - DU-036-5: Custom Field, Name `Kode Anggaran {runId}`, Group `Accounting`
  - DU-036-6: Asset, Name `Switch Jaringan Starter {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-036-7: Asset, Name `Switch Jaringan Growth {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-036-8: Asset, Name `Switch Jaringan Professional {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-036-9: Asset, Name `Switch Jaringan Enterprise {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-036-14: Asset, Name `Proyektor Pinjam {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-036-15: Asset, Name `Laptop Tugas {runId}`, Group `IT {runId}`, Status `Assigned`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Switch Jaringan Starter {runId}` adalah `Switch Jaringan Starter {runId} - 1`, dari Asset Name `Switch Jaringan Starter {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Switch Jaringan Growth {runId}` adalah `Switch Jaringan Growth {runId} - 1`, dari Asset Name `Switch Jaringan Growth {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Switch Jaringan Professional {runId}` adalah `Switch Jaringan Professional {runId} - 1`, dari Asset Name `Switch Jaringan Professional {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Switch Jaringan Enterprise {runId}` adalah `Switch Jaringan Enterprise {runId} - 1`, dari Asset Name `Switch Jaringan Enterprise {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Proyektor Pinjam {runId}` adalah `Proyektor Pinjam {runId} - 1`, dari Asset Name `Proyektor Pinjam {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Laptop Tugas {runId}` adalah `Laptop Tugas {runId} - 1`, dari Asset Name `Laptop Tugas {runId}`.
  - `Proyektor Pinjam {runId}` sedang dipinjam (Custody `Borrowed`) dan `Laptop Tugas {runId}` sedang ditugaskan (Custody `Assigned`).
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Lisensi `FA-7` aktif pada entitas.
  - Entitas berada pada plan `enterprise` dan lisensi `FA-7` aktif.
  - Feature Suite Borrow, Assignment, dan Transfer berada di level `Full` pada awal spec.

## Test Steps

### Plan kehilangan FA-7 saat halaman terbuka
1. Ketik Search `{runId}`, tekan Enter
2. Buka Setup Column
3. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tersedia di Setup Column
4. Tutup Setup Column
5. Operator Platform mencabut lisensi `FA-7` dari plan entitas
6. Muat ulang halaman
7. Buka Setup Column
8. Verifikasi kolom `Asset Value (Commercial)` dan `Asset Class` tetap tersedia di Setup Column
9. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tidak tersedia di Setup Column
10. Tutup Setup Column

### Edit dan Delete berperilaku sama pada plan starter
11. Operator Platform mengubah plan entitas menjadi `starter`
12. Muat ulang halaman
13. Ketik Search `{runId}`, tekan Enter
14. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
15. Klik `Edit Purchase`
16. Ganti isi Purchase Cost dengan `19000001`
17. Klik `[Save]`
18. Verifikasi toast `Success, purchase data has been saved.` tampil pada plan `starter`
19. Klik `⋯` pada baris `Switch Jaringan Starter {runId} - 1`
20. Klik `Delete Asset Data`
21. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
22. Klik `[Delete]`
23. Verifikasi toast `Success, asset data has been deleted.` tampil pada plan `starter`

### Edit dan Delete berperilaku sama pada plan growth
24. Operator Platform mengubah plan entitas menjadi `growth`
25. Muat ulang halaman
26. Ketik Search `{runId}`, tekan Enter
27. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
28. Klik `Edit Purchase`
29. Ganti isi Purchase Cost dengan `19000002`
30. Klik `[Save]`
31. Verifikasi toast `Success, purchase data has been saved.` tampil pada plan `growth`
32. Klik `⋯` pada baris `Switch Jaringan Growth {runId} - 1`
33. Klik `Delete Asset Data`
34. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
35. Klik `[Delete]`
36. Verifikasi toast `Success, asset data has been deleted.` tampil pada plan `growth`

### Edit dan Delete berperilaku sama pada plan professional
37. Operator Platform mengubah plan entitas menjadi `professional`
38. Muat ulang halaman
39. Ketik Search `{runId}`, tekan Enter
40. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
41. Klik `Edit Purchase`
42. Ganti isi Purchase Cost dengan `19000003`
43. Klik `[Save]`
44. Verifikasi toast `Success, purchase data has been saved.` tampil pada plan `professional`
45. Klik `⋯` pada baris `Switch Jaringan Professional {runId} - 1`
46. Klik `Delete Asset Data`
47. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
48. Klik `[Delete]`
49. Verifikasi toast `Success, asset data has been deleted.` tampil pada plan `professional`

### Edit dan Delete berperilaku sama pada plan enterprise
50. Operator Platform mengubah plan entitas menjadi `enterprise`
51. Muat ulang halaman
52. Ketik Search `{runId}`, tekan Enter
53. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
54. Klik `Edit Purchase`
55. Ganti isi Purchase Cost dengan `19000004`
56. Klik `[Save]`
57. Verifikasi toast `Success, purchase data has been saved.` tampil pada plan `enterprise`
58. Klik `⋯` pada baris `Switch Jaringan Enterprise {runId} - 1`
59. Klik `Delete Asset Data`
60. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
61. Klik `[Delete]`
62. Verifikasi toast `Success, asset data has been deleted.` tampil pada plan `enterprise`

### Level Feature Suite None
63. Operator Platform mengubah level ketiga Feature Suite transaksi (sebagaimana di Kondisi) menjadi `None`
64. Muat ulang halaman
65. Ketik Search `{runId}`, tekan Enter
66. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
67. Verifikasi aksi `Borrow` dan `Assign` tidak dirender (Hidden) pada level `None`
68. Verifikasi aksi `Add to Borrow Draft`, `Add to Assignment Draft`, dan `Add to Transfer Draft` tidak dirender (Hidden) pada level `None`
69. Verifikasi aksi `Mark as Returned` dan `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Available`
70. Verifikasi aksi `Report Disposal`, `Report Damage`, dan `Report Missing` tampil pada level `None`
71. Tekan Esc
72. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
73. Verifikasi aksi `Mark as Returned` tampil pada aset berstatus `Borrowed` pada level `None`
74. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
75. Tekan Esc
76. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
77. Verifikasi aksi `Mark as Unassigned` tampil pada aset berstatus `Assigned` pada level `None`
78. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
79. Tekan Esc
80. Centang baris `Laptop Pro 16 {runId} - 1`
81. Klik tombol Bulk Action
82. Verifikasi aksi Bulk `Borrow` dan `Assign` tidak dirender (Hidden) pada level `None`
83. Verifikasi aksi Bulk `Add to Borrow Draft`, `Add to Assignment Draft`, dan `Add to Transfer Draft` tidak dirender (Hidden) pada level `None`
84. Tekan Esc
85. Klik `×` pada Bar Bulk
86. Centang baris `Proyektor Pinjam {runId} - 1`
87. Klik tombol Bulk Action
88. Verifikasi aksi Bulk `Mark as Returned` tampil untuk aset berstatus `Borrowed` pada level `None`
89. Tekan Esc
90. Klik `×` pada Bar Bulk
91. Centang baris `Laptop Tugas {runId} - 1`
92. Klik tombol Bulk Action
93. Verifikasi aksi Bulk `Mark as Unassigned` tampil untuk aset berstatus `Assigned` pada level `None`
94. Tekan Esc
95. Klik `×` pada Bar Bulk

### Level Feature Suite Basic
96. Operator Platform mengubah level ketiga Feature Suite transaksi (sebagaimana di Kondisi) menjadi `Basic`
97. Muat ulang halaman
98. Ketik Search `{runId}`, tekan Enter
99. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
100. Verifikasi aksi `Borrow` dan `Assign` tampil pada level `Basic`
101. Verifikasi aksi `Transfer` tampil pada level `Basic`
102. Verifikasi aksi `Add to Borrow Draft`, `Add to Assignment Draft`, dan `Add to Transfer Draft` tidak dirender (Hidden) pada level `Basic`
103. Verifikasi aksi `Mark as Returned` dan `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Available`
104. Verifikasi aksi `Report Disposal`, `Report Damage`, dan `Report Missing` tampil pada level `Basic`
105. Tekan Esc
106. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
107. Verifikasi aksi `Mark as Returned` tampil pada aset berstatus `Borrowed` pada level `Basic`
108. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
109. Tekan Esc
110. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
111. Verifikasi aksi `Mark as Unassigned` tampil pada aset berstatus `Assigned` pada level `Basic`
112. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
113. Tekan Esc
114. Centang baris `Laptop Pro 16 {runId} - 1`
115. Klik tombol Bulk Action
116. Verifikasi aksi Bulk `Borrow` dan `Assign` tampil pada level `Basic`
117. Verifikasi aksi Bulk `Transfer` tampil pada level `Basic`
118. Verifikasi aksi Bulk `Add to Borrow Draft`, `Add to Assignment Draft`, dan `Add to Transfer Draft` tidak dirender (Hidden) pada level `Basic`
119. Tekan Esc
120. Klik `×` pada Bar Bulk
121. Centang baris `Proyektor Pinjam {runId} - 1`
122. Klik tombol Bulk Action
123. Verifikasi aksi Bulk `Mark as Returned` tampil untuk aset berstatus `Borrowed` pada level `Basic`
124. Tekan Esc
125. Klik `×` pada Bar Bulk
126. Centang baris `Laptop Tugas {runId} - 1`
127. Klik tombol Bulk Action
128. Verifikasi aksi Bulk `Mark as Unassigned` tampil untuk aset berstatus `Assigned` pada level `Basic`
129. Tekan Esc
130. Klik `×` pada Bar Bulk

### Level Feature Suite Full
131. Operator Platform mengubah level ketiga Feature Suite transaksi (sebagaimana di Kondisi) menjadi `Full`
132. Muat ulang halaman
133. Ketik Search `{runId}`, tekan Enter
134. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
135. Verifikasi aksi `Borrow` dan `Assign` tampil pada level `Full`
136. Verifikasi aksi `Transfer` tampil pada level `Full`
137. Verifikasi aksi `Add to Borrow Draft`, `Add to Assignment Draft`, dan `Add to Transfer Draft` tampil pada level `Full`
138. Verifikasi aksi `Mark as Returned` dan `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Available`
139. Verifikasi aksi `Report Disposal`, `Report Damage`, dan `Report Missing` tampil pada level `Full`
140. Tekan Esc
141. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
142. Verifikasi aksi `Mark as Returned` tampil pada aset berstatus `Borrowed` pada level `Full`
143. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
144. Tekan Esc
145. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
146. Verifikasi aksi `Mark as Unassigned` tampil pada aset berstatus `Assigned` pada level `Full`
147. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
148. Tekan Esc
149. Centang baris `Laptop Pro 16 {runId} - 1`
150. Klik tombol Bulk Action
151. Verifikasi aksi Bulk `Borrow` dan `Assign` tampil pada level `Full`
152. Verifikasi aksi Bulk `Transfer` tampil pada level `Full`
153. Verifikasi aksi Bulk `Add to Borrow Draft`, `Add to Assignment Draft`, dan `Add to Transfer Draft` tampil pada level `Full`
154. Tekan Esc
155. Klik `×` pada Bar Bulk
156. Centang baris `Proyektor Pinjam {runId} - 1`
157. Klik tombol Bulk Action
158. Verifikasi aksi Bulk `Mark as Returned` tampil untuk aset berstatus `Borrowed` pada level `Full`
159. Tekan Esc
160. Klik `×` pada Bar Bulk
161. Centang baris `Laptop Tugas {runId} - 1`
162. Klik tombol Bulk Action
163. Verifikasi aksi Bulk `Mark as Unassigned` tampil untuk aset berstatus `Assigned` pada level `Full`
164. Tekan Esc
165. Klik `×` pada Bar Bulk
