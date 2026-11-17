---
id: TC-FA-FATR-E2E-020-changelog
title: "Changelog mencatat perubahan setting per field"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r55", "§4.1#r57", "§4.1#r102", "§4.4#r15", "§8.1#r1", "§8.1#r3", "§8.1#r4", "§8.2#r1", "§9.2#p17", "§9.2#b376", "§9.2#b377", "§9.4.2#r53", "§9.4.2#r92", "§9.4.3#b8", "§9.4.4#r44", "§9.7#r8", "§11#r10", "EB-LOG-1", "EB-LOG-2", "§9.2#b42"]
smoke: ["§9.2#b42"]
dependsOn: []
trace:
  "§4.1#r55": 35
  "§4.1#r57": [90, 97]
  "§4.1#r102": [15, 134, 148, 149]
  "§4.4#r15": 2
  "§8.1#r1": [15, 90]
  "§8.1#r3": [15, 26]
  "§8.1#r4": 16
  "§8.2#r1": [15, 44]
  "§9.2#p17": 15
  "§9.2#b376": 4
  "§9.2#b377": 116
  "§9.4.2#r53": 4
  "§9.4.2#r92": [15, 26, 44, 53, 80]
  "§9.4.3#b8": [116, 125]
  "§9.4.4#r44": 4
  "§9.7#r8": 15
  "§11#r10": 17
  "EB-LOG-1": [68, 69, 70, 71]
  "EB-LOG-2": 81
  "§9.2#b42": 79
anchor: [113, 122]
coverage:
  web: automated
---
# Changelog mencatat perubahan setting per field

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` (DU-020-1).
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-020-1: User `Rina Wulandari {runId}`, role Total Control, cakupan seluruh Group di entitas DU-020-19, dibuat di entitas itu. Modified By yang diharapkan `Rina W`, dari Name `Rina Wulandari {runId}`.
  - DU-020-2: Category leaf `Mobil Dinas {runId}` di bawah Category induk `Kendaraan {runId}`, semua field bernilai Inherit; full path Category `Kendaraan {runId} > Mobil Dinas {runId}`; ada di entitas DU-020-19.
  - DU-020-3: Group `Proyek Karawang {runId}`, ada di entitas DU-020-19.
  - DU-020-19: Entitas `Armada Mitra Sejahtera {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan transaksi Borrow, Assign, Transfer, dan Disposal, serta Approval Workflow.
- Kondisi:
  - Company default entitas DU-020-19 bernilai bawaan: Max duration `14`, Duration unit `Days`, Allowed disposal types seluruh opsi (`Sell`, `Scrap`, `Donate`, `Trade-in`, `Write-off`), dan Long missing after `30`.
  - Level Feature Suite Borrowing, Assignment, Transfer, dan Disposal entitas DU-020-19 bernilai `Full`.

## Test Steps

### Changelog belum memuat entri ber-runId sebelum Save pertama
1. Klik ikon Changelog di header
2. Verifikasi dialog `Changelog: Transaction Settings` terbuka
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi empty state `No results found` tampil karena belum ada entri ber-runId
5. Klik `✕` pada dialog Changelog

### Edit Max duration dari Inherit ke nilai sendiri tercatat per field
6. Klik Category induk `Kendaraan {runId}` di Sidebar Category Tree untuk membuka cabangnya
7. Klik Category leaf `Mobil Dinas {runId}`
8. Klik tab `Borrow`
9. Klik `[Set own value]` pada field Max duration
10. Isi Max duration `21`
11. Klik `[Save]`
12. Klik `[Save]` pada dialog Save Changes
13. Klik ikon Changelog di header
14. Ketik Search `{runId}`, tekan Enter
15. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, dan New Value `21 days`
16. Verifikasi baris tersebut berkolom Action `Edit`
17. Verifikasi baris tersebut berkolom Modified By `Rina W`
18. Klik `✕` pada dialog Changelog

### Edit Allow Borrow dari Inherit ke Deny tercatat per field
19. Klik tab `Borrow`
20. Klik `[Set own value]` pada field Allow Borrow
21. Pilih Allow Borrow `Deny`
22. Klik `[Save]`
23. Klik `[Save]` pada dialog Save Changes
24. Klik ikon Changelog di header
25. Ketik Search `{runId}`, tekan Enter
26. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Borrow (Allow Borrow)`, Old Value `Inherit`, dan New Value `Deny`
27. Klik `✕` pada dialog Changelog

### Edit Allowed disposal types menulis nilai berderet dipisah koma
28. Klik tab `Disposal`
29. Klik `[Set own value]` pada field Allowed disposal types
30. Hapus pilihan `Donate` dari Allowed disposal types
31. Klik `[Save]`
32. Klik `[Save]` pada dialog Save Changes
33. Klik ikon Changelog di header
34. Ketik Search `{runId}`, tekan Enter
35. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Disposal (Allowed disposal types)`, Old Value `Inherit`, dan New Value `Sell, Scrap, Trade-in, Write-off`
36. Klik `✕` pada dialog Changelog

### Edit Photo at start dari Inherit ke OFF tercatat per field
37. Klik tab `Assign`
38. Klik `[Set own value]` pada field Photo at start
39. Matikan switch Photo at start
40. Klik `[Save]`
41. Klik `[Save]` pada dialog Save Changes
42. Klik ikon Changelog di header
43. Ketik Search `{runId}`, tekan Enter
44. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Assign (Photo at start)`, Old Value `Inherit`, dan New Value `OFF`
45. Klik `✕` pada dialog Changelog

### Edit Approval type dari Inherit ke All approvers (AND) tercatat per field
46. Klik tab `Transfer`
47. Klik `[Set own value]` pada field Approval type
48. Pilih Approval type `All approvers (AND)`
49. Klik `[Save]`
50. Klik `[Save]` pada dialog Save Changes
51. Klik ikon Changelog di header
52. Ketik Search `{runId}`, tekan Enter
53. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Transfer (Approval type)`, Old Value `Inherit`, dan New Value `All approvers (AND)`
54. Klik `✕` pada dialog Changelog

### Satu Save yang mengubah dua field menghasilkan dua entri
55. Klik ikon Changelog di header
56. Ketik Search `{runId}`, tekan Enter
57. Catat jumlah baris hasil Search
58. Klik `✕` pada dialog Changelog
59. Klik tab `Transfer`
60. Klik `[Set own value]` pada field Destination scope
61. Pilih Destination scope `Within same parent Group`
62. Klik `[Set own value]` pada field In-transit overdue after
63. Isi In-transit overdue after `10`
64. Klik `[Save]`
65. Klik `[Save]` pada dialog Save Changes
66. Klik ikon Changelog di header
67. Ketik Search `{runId}`, tekan Enter
68. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Transfer (Destination scope)`, Old Value `Inherit`, dan New Value `Within same parent Group`
69. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Transfer (In-transit overdue after)`, Old Value `Inherit`, dan New Value `10 days`
70. Verifikasi jumlah baris hasil Search bertambah dua dari jumlah yang dicatat
71. Verifikasi tidak ada baris dengan Field `Transfer (Approval scope)`
72. Klik `✕` pada dialog Changelog

### Reset to Default tercatat dan entri lama tetap menampilkan nilai saat itu
73. Klik tab `Borrow`
74. Klik `[Reset to Default]`
75. Klik `[Save]`
76. Klik `[Save]` pada dialog Save Changes
77. Klik ikon Changelog di header
78. Ketik Search `{runId}`, tekan Enter
79. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Borrow (Max duration)`, Old Value `21 days`, dan New Value `Inherit`
80. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Borrow (Allow Borrow)`, Old Value `Deny`, dan New Value `Inherit`
81. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, dan New Value `21 days` tanpa berubah
82. Klik `✕` pada dialog Changelog

### Edit setting All categories tercatat dengan Category All categories
83. Klik All categories di Sidebar Category Tree
84. Klik tab `Damaged & Missing`
85. Isi Long missing after `45`
86. Klik `[Save]`
87. Klik `[Save]` pada dialog Save Changes
88. Klik ikon Changelog di header
89. Ketik Search `Long missing after`, tekan Enter
90. Verifikasi baris teratas hasil Search, menurut urutan bawaan Date Newest First, memuat Category `All categories`, Field `Damaged & Missing (Long missing after)`, Old Value `30 days`, dan New Value `45 days`
91. Klik `✕` pada dialog Changelog
92. Isi Long missing after `30`
93. Klik `[Save]`
94. Klik `[Save]` pada dialog Save Changes
95. Klik ikon Changelog di header
96. Ketik Search `Long missing after`, tekan Enter
97. Verifikasi baris teratas hasil Search, menurut urutan bawaan Date Newest First, memuat Category `All categories`, Field `Damaged & Missing (Long missing after)`, Old Value `45 days`, dan New Value `30 days`
98. Klik `✕` pada dialog Changelog

### Add override dan Delete override tidak masuk Changelog
99. Klik Category leaf `Mobil Dinas {runId}`
100. Klik tab `Borrow`
101. Klik ikon Changelog di header
102. Ketik Search `{runId}`, tekan Enter
103. Catat jumlah baris hasil Search
104. Klik `✕` pada dialog Changelog
105. Klik `[+ Override]`
106. Pilih Scope `Group`
107. Klik `[Select Group]`
108. Centang Group `Proyek Karawang {runId}`
109. Klik `[Select]`
110. Pilih Field `Max duration`
111. Isi Value `30`
112. Klik `[Submit]`
113. Verifikasi toast `Success, override has been added.` tampil
114. Klik ikon Changelog di header
115. Ketik Search `{runId}`, tekan Enter
116. Verifikasi jumlah baris hasil Search sama dengan jumlah yang dicatat sebelum Add override
117. Klik `✕` pada dialog Changelog
118. Ketik Search `Proyek Karawang {runId}` pada tabel Overrides, tekan Enter
119. Klik menu `⋯` pada baris `Proyek Karawang {runId}`
120. Klik `Delete`
121. Klik `[Delete]` pada dialog Delete Override
122. Verifikasi toast `Success, override has been deleted.` tampil
123. Klik ikon Changelog di header
124. Ketik Search `{runId}`, tekan Enter
125. Verifikasi jumlah baris hasil Search tetap sama dengan jumlah yang dicatat sebelum Add override
126. Klik `✕` pada dialog Changelog

### Auto-approve when duration ≤ ditulis dengan satuan Duration unit di Changelog
127. Klik tab `Borrow`
128. Klik `[Set own value]` pada field Auto-approve when duration ≤
129. Isi Auto-approve when duration ≤ `2`
130. Klik `[Save]`
131. Klik `[Save]` pada dialog Save Changes
132. Klik ikon Changelog di header
133. Ketik Search `{runId}`, tekan Enter
134. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Borrow (Auto-approve when duration ≤)`, Old Value `Inherit`, dan New Value `2 days`
135. Klik `✕` pada dialog Changelog

### Satuan Duration unit Hours ditulis pada Old Value dan New Value di Changelog
136. Klik tab `Borrow`
137. Klik `[Set own value]` pada field Duration unit
138. Pilih Duration unit `Hours`
139. Klik `[Save]`
140. Klik `[Save]` pada dialog Save Changes
141. Klik `[Set own value]` pada field Max duration
142. Isi Max duration `3`
143. Isi Auto-approve when duration ≤ `4`
144. Klik `[Save]`
145. Klik `[Save]` pada dialog Save Changes
146. Klik ikon Changelog di header
147. Ketik Search `{runId}`, tekan Enter
148. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, dan New Value `3 hours`
149. Verifikasi ada baris dengan Category `Kendaraan {runId} > Mobil Dinas {runId}`, Field `Borrow (Auto-approve when duration ≤)`, dan New Value `4 hours`
150. Klik `✕` pada dialog Changelog
