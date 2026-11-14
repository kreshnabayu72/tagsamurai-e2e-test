---
id: TC-FA-FATR-UI-074-add-tampilan
title: "Dialog Add override: tampilan awal, Scope, Target, dan baris Field + Value"
layer: ui-client
priority: Critical
caseType: Positive
status: draft
sourceRules: [§Aturan Logika Modul#r46, §Aturan Logika Modul#r47, §Aturan Logika Modul#r48, §Aturan Logika Modul#r49, §Aturan Logika Modul#r51, §Aturan Logika Modul#r67, §Aturan Logika Modul#r100, §4.1#r8, §4.1#r283, §4.1#r284, §4.1#r285, §4.1#r286, §4.1#r287, §4.1#r288, §4.1#r289, §4.1#r290, §4.1#r291, §4.1#r292, §4.1#r294, §4.1#r295, §4.1#r296, §4.1#r297, §4.1#r298, §4.1#r299, §4.1#r300, §4.1#r301, §4.1#r302, §4.1#r303, §4.1#r304, §4.1#r305, §4.1#r306, §4.1#r307, §4.1#r308, §4.1#r309, §4.1#r319, §4.1#p60, D-02, §9.2#b84, §9.2#b86, §9.2#b87, §9.2#b150, §9.2#b155, §9.2#b197, §9.4.2#r8, §9.4.2#r25, §9.4.4#r23, §9.5#r13, §9.5#r14, §9.5#r19, §9.5#r20, §9.5#r26, §9.9#r13, §9.9#r14, §9.9#r15, §9.9#r16, §9.10.1#b5, §9.10.2#b5, §9.10.3#b5, §10#b2, EB-FRM-7@add-override, EB-TBL-5@hapus-baris-field]
smoke: []
dependsOn: []
trace:
  §Aturan Logika Modul#r46: 5
  §Aturan Logika Modul#r47: 46
  §Aturan Logika Modul#r48: 59
  §Aturan Logika Modul#r49: 69
  §Aturan Logika Modul#r51: 21
  §Aturan Logika Modul#r67: 48
  §Aturan Logika Modul#r100: [47, 48, 49]
  §4.1#r8: [4, 15, 21, 22, 175, 176]
  §4.1#r283: 28
  §4.1#r284: [15, 31, 38]
  §4.1#r285: 17
  §4.1#r286: [33, 40]
  §4.1#r287: 26
  §4.1#r288: [21, 22]
  §4.1#r289: [23, 25]
  §4.1#r290: 36
  §4.1#r291: 43
  §4.1#r292: 8
  §4.1#r294: 64
  §4.1#r295: [69, 75, 145]
  §4.1#r296: 82
  §4.1#r297: 72
  §4.1#r298: 73
  §4.1#r299: 92
  §4.1#r300: 93
  §4.1#r301: 46
  §4.1#r302: [75, 78]
  §4.1#r303: 95
  §4.1#r304: [46, 151, 155]
  §4.1#r305: [59, 61, 64, 66]
  §4.1#r306: 98
  §4.1#r307: 100
  §4.1#r308: 86
  §4.1#r309: 6
  §4.1#r319: 66
  §4.1#p60: [23, 25]
  D-02: [2, 3, 4, 80, 147]
  §9.2#b84: [46, 49, 50, 150, 151, 154, 155]
  §9.2#b86: 46
  §9.2#b87: [53, 56, 166]
  §9.2#b150: [115, 156, 157, 160, 161, 162]
  §9.2#b155: [107, 108, 111, 112]
  §9.2#b197: 47
  §9.4.2#r8: 104
  §9.4.2#r25: [115, 117, 126, 128]
  §9.4.4#r23: [115, 117]
  §9.5#r13: [7, 8]
  §9.5#r14: 10
  §9.5#r19: 12
  §9.5#r20: [46, 50, 151, 155]
  §9.5#r26: 46
  §9.9#r13: 7
  §9.9#r14: 9
  §9.9#r15: 8
  §9.9#r16: [59, 61]
  §9.10.1#b5: [115, 117]
  §9.10.2#b5: [118, 120, 121, 123]
  §9.10.3#b5: [126, 128]
  §10#b2: 12
  EB-FRM-7@add-override: [130, 131, 132, 135, 137, 140]
  EB-TBL-5@hapus-baris-field: 100
anchor: [90, 173]
coverage:
  web: automated
---

# Dialog Add override: tampilan awal, Scope, Target, dan baris Field + Value

## Prerequisites
- Aktor: Total Control. K5 memakai aktor Manage asset & TAG (Read + Update) pada Group `Proyek Karawang`. K6 memakai aktor Manage transaction settings (Read + Update).
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
  - DU-074-12: field yang ditawarkan pada transaksi Disposal: `Allow Disposal`, `Min asset age warning`, `Max deviation from book value`, `Require approval`, `Approval type`.
  - DU-074-13: sebagian field yang ditawarkan pada transaksi Transfer: `Allow Transfer`, `Destination scope`, `In-transit overdue after`.
- Kondisi:
  - K1: Dialog Add override - Borrow dibuka dari Category leaf `Vehicle > Pool car`; nilai berlaku di Category adalah DU-074-8 dan DU-074-11; plan entitas memuat Approval Workflow, Borrowing penuh, dan Assignment penuh; tree Group memuat DU-074-1 dan DU-074-2; picker Asset Name memuat DU-074-3; picker Select Asset memuat DU-074-4.
  - K2: sama dengan K1, tetapi dialog dibuka dari All categories dan nilai Company default adalah DU-074-8.
  - K3: sama dengan K1, tetapi plan entitas tidak memuat Approval Workflow dan Borrowing bukan versi penuh.
  - K4: Dialog Add override - Assign dibuka dari Category leaf `Vehicle > Pool car`; plan entitas memuat Assignment yang bukan versi penuh.
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
117. Verifikasi alasan `Requires Approval Workflow on your plan` tersampaikan pada opsi
118. Verifikasi opsi `Self service` disabled
119. Arahkan kursor ke opsi `Self service`
120. Verifikasi alasan `Available on plans with full Borrowing` tersampaikan pada opsi
121. Verifikasi opsi `Duration unit` disabled
122. Arahkan kursor ke opsi `Duration unit`
123. Verifikasi alasan `Available on plans with full Borrowing` tersampaikan pada opsi

### Opsi field bergerbang plan Assignment disabled
124. Tampilkan Dialog Add override dengan kondisi K4
125. Klik kontrol Field pada baris Field + Value pertama
126. Verifikasi opsi `Direct handover between holders` disabled
127. Arahkan kursor ke opsi `Direct handover between holders`
128. Verifikasi alasan `Available on plans with full Assignment` tersampaikan pada opsi

### Aksesibilitas form, focus trap, dan fokus kembali
129. Tampilkan Dialog Add override dengan kondisi K1
130. Verifikasi fokus berada di dalam dialog sesudah dialog tampil
131. Verifikasi kontrol Scope dan Target dinyatakan wajib bagi teknologi bantu
132. Verifikasi tombol hapus baris Field + Value memiliki label aksesibel
133. Pilih Field `Max duration` pada baris pertama
134. Klik `[Submit]`
135. Verifikasi kontrol Value pada baris pertama terhubung dengan pesan error inline-nya bagi teknologi bantu
136. Tekan `Tab` berulang kali sampai melewati kontrol terakhir dialog
137. Verifikasi fokus tetap berada di dalam dialog
138. Klik `✕` pada dialog
139. Klik `[Leave]` pada dialog Unsaved Changes
140. Verifikasi fokus kembali ke tombol `[+ Override]` yang membuka dialog

### Teks bantu nilai berlaku pada baris Field + Value kedua
141. Tampilkan Dialog Add override dengan kondisi K1
142. Pilih Field `Max duration` pada baris pertama
143. Klik `[+ Add field]`
144. Pilih Field `Max assets per borrower (concurrent)` pada baris kedua
145. Verifikasi teks bantu `Current value: 3 assets` tampil di bawah baris kedua, dari nilai berlaku DU-074-11

### Judul Dialog Add override untuk transaksi Assign
146. Tampilkan Dialog Add override dengan kondisi K4
147. Verifikasi judul dialog `Add override - Assign`

### Daftar Field pada Dialog Add override - Disposal
148. Tampilkan Dialog Add override dengan kondisi K8
149. Klik kontrol Field pada baris Field + Value pertama
150. Verifikasi opsi Field memuat `Allow Disposal`, `Min asset age warning`, `Max deviation from book value`, `Require approval`, `Approval type` (DU-074-12)
151. Verifikasi opsi Field tidak memuat `Allowed disposal types`

### Daftar Field dan field Approval bergerbang pada Dialog Add override - Transfer
152. Tampilkan Dialog Add override dengan kondisi K9
153. Klik kontrol Field pada baris Field + Value pertama
154. Verifikasi opsi Field memuat `Allow Transfer`, `Destination scope`, `In-transit overdue after` (DU-074-13)
155. Verifikasi opsi Field tidak memuat `Change Cost Center with Group`
156. Verifikasi opsi `Approval scope` disabled
157. Verifikasi opsi `Auto-approve when destination in same parent Group` disabled

### Field Approval lain pada transaksi Borrow disabled tanpa Approval Workflow
158. Tampilkan Dialog Add override dengan kondisi K3
159. Klik kontrol Field pada baris Field + Value pertama
160. Verifikasi opsi `Auto-approve` disabled
161. Verifikasi opsi `Auto-approve when duration ≤` disabled
162. Verifikasi opsi `Approval type` disabled

### Opsi Field untuk Scope Group
163. Tampilkan Dialog Add override dengan kondisi K1
164. Pilih Scope `Group`
165. Klik kontrol Field pada baris Field + Value pertama
166. Verifikasi opsi Field untuk Scope `Group` sama dengan DU-074-10, termasuk `Self service`

### Melepas target lewat tombol close pada badge
167. Tampilkan Dialog Add override dengan kondisi K1
168. Pilih Scope `Group`
169. Klik `[Select Group]`
170. Centang node `Proyek Karawang`
171. Centang node `Proyek Bekasi`
172. Klik `[Select]`
173. Verifikasi badge `Proyek Karawang` dan `Proyek Bekasi` tampil di bawah tombol `Select Group`
174. Klik tombol close pada badge `Proyek Bekasi`
175. Verifikasi badge `Proyek Karawang` tetap tampil
176. Verifikasi badge `Proyek Bekasi` tidak tampil

[^drift-1]: Drift PRD vs foundation. PRD §4.1 (FLD-35l): badge target Group berisi full path Group, bukan nama dengan hover. Foundation `prd-conventions.md` §9.14: badge Group berisi nama, hierarki lengkap `[Parent] > [Child] > [Grandchild]` pada hover. Diasersi: foundation (SB-4).
