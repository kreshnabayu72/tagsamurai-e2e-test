---
id: TC-FA-ASSIGN-UI-124-breadcrumb-halaman-assignment
title: "Breadcrumb semua halaman Assignment"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-TBL-11", "§4.2#p2", "§4.2#p3", "§4.2#r1", "§4.2#r2", "§4.2#r3", "§4.2#r4", "§4.2#r5", "§4.2#r6", "§4.2#r7", "§4.2#r8", "§4.2#r9", "§4.2#r10", "§4.2#r11", "§4.2.1#p1", "§4.2.10#p2", "§4.2.14#p1"]
smoke: []
dependsOn: []
trace:
  "EB-TBL-11": [6, 7, 8, 15, 16, 17, 23, 24, 25, 32, 33, 34, 37, 38, 39, 43, 44, 45, 48, 49, 50, 54, 55, 56, 60, 61, 62, 66, 67, 68, 72, 73, 74, 78, 79, 80, 84, 85, 86, 90, 91, 92, 96, 97, 98, 102, 103, 104, 108, 109, 110, 118, 119, 120, 128, 129, 130, 136, 137, 138, 141, 142, 143, 146, 147, 148, 151, 154, 157]
  "§4.2#p2": [8, 9, 17, 25, 34, 39, 40, 45, 50, 51, 56, 62, 68, 74, 80, 86, 92, 98, 104, 110, 120, 130, 138, 143, 148]
  "§4.2#p3": [57, 63, 69, 75, 81, 87, 93, 99, 105, 121]
  "§4.2#r1": [2, 11, 19, 27]
  "§4.2#r2": [36, 42]
  "§4.2#r3": 47
  "§4.2#r4": [53, 59, 65, 71, 77, 83, 89, 95]
  "§4.2#r5": 101
  "§4.2#r6": 107
  "§4.2#r7": 112
  "§4.2#r8": [123, 132]
  "§4.2#r9": 140
  "§4.2#r10": 145
  "§4.2#r11": [150, 153, 156]
  "§4.2.1#p1": [2, 3, 4, 5, 11, 12, 13, 14, 19, 20, 21, 22, 27, 28, 29, 30, 31]
  "§4.2.10#p2": [123, 124, 125, 126, 127, 132, 133, 134, 135]
  "§4.2.14#p1": [112, 113, 114, 115, 116, 117, 161]
anchor: [160]
coverage:
  web: automated
---

# Breadcrumb semua halaman Assignment

## Prerequisites
- Aktor: Aktor Assignment; Approver untuk K19 sampai K22 (halaman Approvals > Assignment, Review, dan Detail dari tab History); Assignee atau PIC untuk K23 sampai K25 (halaman My Asset).
- Layar awal: halaman sesuai kondisi.
- Komponen: Breadcrumb Assignment
- Data:
  - DU-124-1: Assignee `Budi S`, Assignee Type `Employee`, Group `Head Office`, Total Asset `6`.
- Kondisi:
  - K1: halaman Transactions > Assignment dengan tab Transactions aktif.
  - K2: halaman Transactions > Assignment dengan tab Drafts aktif.
  - K3: halaman Transactions > Assignment dengan tab Assigned Assets aktif.
  - K4: halaman Transactions > Assignment dengan tab History aktif.
  - K5: halaman Assignment Request baru dibuka pada level Full.
  - K6: halaman Assignment Request baru dibuka pada level Basic.
  - K7: halaman Assignment Request dibuka dari Edit draft.
  - K8: halaman Assignment Detail dibuka untuk ASG berstatus header Draft.
  - K9: halaman Assignment Detail dibuka untuk ASG berstatus header Waiting for Approval.
  - K10: halaman Assignment Detail dibuka untuk ASG berstatus header Waiting for Handover.
  - K11: halaman Assignment Detail dibuka untuk ASG berstatus header Assigned.
  - K12: halaman Assignment Detail dibuka untuk ASG berstatus header Assigned dengan penanda No PIC.
  - K13: halaman Assignment Detail dibuka untuk ASG berstatus header Unassigned.
  - K14: halaman Assignment Detail dibuka untuk ASG berstatus header Rejected.
  - K15: halaman Assignment Detail dibuka untuk ASG berstatus header Canceled.
  - K16: halaman Handover dibuka untuk ASG berstatus header Waiting for Handover.
  - K17: halaman Unassign dibuka.
  - K18: halaman Assigned Asset untuk Assignee DU-124-1 dibuka dari tab Assigned Assets.
  - K19: halaman Approvals > Assignment dengan tab Active aktif.
  - K20: halaman Approvals > Assignment dengan tab History aktif.
  - K21: halaman Review dibuka dari Approvals > Assignment tab Active.
  - K22: halaman Detail dibuka dari Approvals > Assignment tab History.
  - K23: halaman My Asset dengan tab Task aktif.
  - K24: halaman My Asset dengan tab Assigned aktif.
  - K25: halaman My Asset dengan tab History aktif.

## Test Steps

### Breadcrumb tab Transactions
1. Tampilkan Breadcrumb Assignment dengan kondisi K1
2. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Transactions`
3. Verifikasi tab `Transactions` tersimpan pada parameter `?tab=transactions`
4. Verifikasi tab navigasi memuat `Transactions`, `Drafts`, `Assigned Assets`, dan `History`
5. Verifikasi toolbar memuat `Search by Scan`, `Search`, `Filter`, `Download`, dan `[+ Assign]`
6. Verifikasi segmen pertama `Transactions` tidak bisa diklik
7. Verifikasi segmen tengah `Assignment` bisa diklik
8. Verifikasi segmen terakhir `Transactions` tidak bisa diklik
9. Verifikasi segmen `Assignment` mengarah ke `?tab=transactions`

### Breadcrumb tab Drafts
10. Tampilkan Breadcrumb Assignment dengan kondisi K2
11. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Drafts`
12. Verifikasi tab `Drafts` tersimpan pada parameter `?tab=drafts`
13. Verifikasi toolbar memuat `Search by Scan`, `Search`, `Filter`, dan `[+ Assign]`
14. Verifikasi toolbar tidak memuat `Download`
15. Verifikasi segmen pertama `Transactions` tidak bisa diklik
16. Verifikasi segmen tengah `Assignment` bisa diklik
17. Verifikasi segmen terakhir `Drafts` tidak bisa diklik

### Breadcrumb tab Assigned Assets
18. Tampilkan Breadcrumb Assignment dengan kondisi K3
19. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Assigned Assets`
20. Verifikasi tab `Assigned Assets` tersimpan pada parameter `?tab=assigned`
21. Verifikasi sub-tab memuat `By Asset` dan `By Assignee`
22. Verifikasi toolbar memuat `Search by Scan`, `Search`, `Filter`, dan `Download`
23. Verifikasi segmen pertama `Transactions` tidak bisa diklik
24. Verifikasi segmen tengah `Assignment` bisa diklik
25. Verifikasi segmen terakhir `Assigned Assets` tidak bisa diklik

### Breadcrumb tab History
26. Tampilkan Breadcrumb Assignment dengan kondisi K4
27. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `History`
28. Verifikasi tab `History` tersimpan pada parameter `?tab=history`
29. Verifikasi sub-tab memuat `By Transaction` dan `By Asset`
30. Verifikasi toolbar memuat `Search`, `Filter`, dan `Download`
31. Verifikasi toolbar tidak memuat `Search by Scan`
32. Verifikasi segmen pertama `Transactions` tidak bisa diklik
33. Verifikasi segmen tengah `Assignment` bisa diklik
34. Verifikasi segmen terakhir `History` tidak bisa diklik

### Breadcrumb Assignment Request baru pada level Full
35. Tampilkan Breadcrumb Assignment dengan kondisi K5
36. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Draft`, `Assignment Request`
37. Verifikasi segmen pertama `Transactions` tidak bisa diklik
38. Verifikasi segmen tengah `Assignment`, `Draft` bisa diklik
39. Verifikasi segmen terakhir `Assignment Request` tidak bisa diklik
40. Verifikasi segmen `Draft` mengarah ke `?tab=drafts`

### Breadcrumb Assignment Request baru pada level Basic
41. Tampilkan Breadcrumb Assignment dengan kondisi K6
42. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Transactions`, `Assignment Request`
43. Verifikasi segmen pertama `Transactions` tidak bisa diklik
44. Verifikasi segmen tengah `Assignment`, `Transactions` bisa diklik
45. Verifikasi segmen terakhir `Assignment Request` tidak bisa diklik

### Breadcrumb Assignment Request untuk Edit draft
46. Tampilkan Breadcrumb Assignment dengan kondisi K7
47. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Draft`, `Assignment Request`
48. Verifikasi segmen pertama `Transactions` tidak bisa diklik
49. Verifikasi segmen tengah `Assignment`, `Draft` bisa diklik
50. Verifikasi segmen terakhir `Assignment Request` tidak bisa diklik
51. Verifikasi segmen `Draft` mengarah ke `?tab=drafts`

### Breadcrumb Assignment Detail untuk ASG berstatus Draft
52. Tampilkan Breadcrumb Assignment dengan kondisi K8
53. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Drafts`, `Detail`
54. Verifikasi segmen pertama `Transactions` tidak bisa diklik
55. Verifikasi segmen tengah `Assignment`, `Drafts` bisa diklik
56. Verifikasi segmen terakhir `Detail` tidak bisa diklik
57. Verifikasi segmen `Drafts` sebagai tab asal bisa diklik

### Breadcrumb Assignment Detail untuk ASG berstatus Waiting for Approval
58. Tampilkan Breadcrumb Assignment dengan kondisi K9
59. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Transactions`, `Detail`
60. Verifikasi segmen pertama `Transactions` tidak bisa diklik
61. Verifikasi segmen tengah `Assignment`, `Transactions` bisa diklik
62. Verifikasi segmen terakhir `Detail` tidak bisa diklik
63. Verifikasi segmen `Transactions` sebagai tab asal bisa diklik

### Breadcrumb Assignment Detail untuk ASG berstatus Waiting for Handover
64. Tampilkan Breadcrumb Assignment dengan kondisi K10
65. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Transactions`, `Detail`
66. Verifikasi segmen pertama `Transactions` tidak bisa diklik
67. Verifikasi segmen tengah `Assignment`, `Transactions` bisa diklik
68. Verifikasi segmen terakhir `Detail` tidak bisa diklik
69. Verifikasi segmen `Transactions` sebagai tab asal bisa diklik

### Breadcrumb Assignment Detail untuk ASG berstatus Assigned
70. Tampilkan Breadcrumb Assignment dengan kondisi K11
71. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Transactions`, `Detail`
72. Verifikasi segmen pertama `Transactions` tidak bisa diklik
73. Verifikasi segmen tengah `Assignment`, `Transactions` bisa diklik
74. Verifikasi segmen terakhir `Detail` tidak bisa diklik
75. Verifikasi segmen `Transactions` sebagai tab asal bisa diklik

### Breadcrumb Assignment Detail untuk ASG berstatus Assigned dengan penanda No PIC
76. Tampilkan Breadcrumb Assignment dengan kondisi K12
77. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Transactions`, `Detail`
78. Verifikasi segmen pertama `Transactions` tidak bisa diklik
79. Verifikasi segmen tengah `Assignment`, `Transactions` bisa diklik
80. Verifikasi segmen terakhir `Detail` tidak bisa diklik
81. Verifikasi segmen `Transactions` sebagai tab asal bisa diklik

### Breadcrumb Assignment Detail untuk ASG berstatus Unassigned
82. Tampilkan Breadcrumb Assignment dengan kondisi K13
83. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `History`, `Detail`
84. Verifikasi segmen pertama `Transactions` tidak bisa diklik
85. Verifikasi segmen tengah `Assignment`, `History` bisa diklik
86. Verifikasi segmen terakhir `Detail` tidak bisa diklik
87. Verifikasi segmen `History` sebagai tab asal bisa diklik

### Breadcrumb Assignment Detail untuk ASG berstatus Rejected
88. Tampilkan Breadcrumb Assignment dengan kondisi K14
89. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `History`, `Detail`
90. Verifikasi segmen pertama `Transactions` tidak bisa diklik
91. Verifikasi segmen tengah `Assignment`, `History` bisa diklik
92. Verifikasi segmen terakhir `Detail` tidak bisa diklik
93. Verifikasi segmen `History` sebagai tab asal bisa diklik

### Breadcrumb Assignment Detail untuk ASG berstatus Canceled
94. Tampilkan Breadcrumb Assignment dengan kondisi K15
95. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `History`, `Detail`
96. Verifikasi segmen pertama `Transactions` tidak bisa diklik
97. Verifikasi segmen tengah `Assignment`, `History` bisa diklik
98. Verifikasi segmen terakhir `Detail` tidak bisa diklik
99. Verifikasi segmen `History` sebagai tab asal bisa diklik

### Breadcrumb halaman Handover
100. Tampilkan Breadcrumb Assignment dengan kondisi K16
101. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Transactions`, `Handover`
102. Verifikasi segmen pertama `Transactions` tidak bisa diklik
103. Verifikasi segmen tengah `Assignment`, `Transactions` bisa diklik
104. Verifikasi segmen terakhir `Handover` tidak bisa diklik
105. Verifikasi segmen `Transactions` sebagai tab asal bisa diklik

### Breadcrumb halaman Unassign
106. Tampilkan Breadcrumb Assignment dengan kondisi K17
107. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Assigned Assets`, `Unassign`
108. Verifikasi segmen pertama `Transactions` tidak bisa diklik
109. Verifikasi segmen tengah `Assignment`, `Assigned Assets` bisa diklik
110. Verifikasi segmen terakhir `Unassign` tidak bisa diklik

### Breadcrumb halaman Assigned Asset
111. Tampilkan Breadcrumb Assignment dengan kondisi K18
112. Verifikasi breadcrumb menampilkan segmen berurutan `Transactions`, `Assignment`, `Assigned Assets`, `Detail`
113. Verifikasi info `Assignee` menampilkan `Budi S`
114. Verifikasi kotak Search memakai placeholder `Search asset name, asset ID, or transaction ID...`
115. Verifikasi toolbar tidak memuat `Search by Scan`
116. Verifikasi tabel aset tidak memuat kolom `Assignee`
117. Verifikasi sub-tab `By Asset` dan `By Assignee` tidak tampil
118. Verifikasi segmen pertama `Transactions` tidak bisa diklik
119. Verifikasi segmen tengah `Assignment`, `Assigned Assets` bisa diklik
120. Verifikasi segmen terakhir `Detail` tidak bisa diklik
121. Verifikasi segmen `Assigned Assets` sebagai tab asal bisa diklik

### Breadcrumb Approvals > Assignment tab Active
122. Tampilkan Breadcrumb Assignment dengan kondisi K19
123. Verifikasi breadcrumb menampilkan segmen berurutan `Approvals`, `Assignment`, `Active`
124. Verifikasi tab `Active` tersimpan pada parameter `?tab=active`
125. Verifikasi tab memuat `Active` dan `History`
126. Verifikasi toolbar memuat `Search` dan `Filter`
127. Verifikasi toolbar tidak memuat `Download`
128. Verifikasi segmen pertama `Approvals` tidak bisa diklik
129. Verifikasi segmen tengah `Assignment` bisa diklik
130. Verifikasi segmen terakhir `Active` tidak bisa diklik

### Breadcrumb Approvals > Assignment tab History
131. Tampilkan Breadcrumb Assignment dengan kondisi K20
132. Verifikasi breadcrumb menampilkan segmen berurutan `Approvals`, `Assignment`, `History`
133. Verifikasi tab `History` tersimpan pada parameter `?tab=history`
134. Verifikasi tab memuat `Active` dan `History`
135. Verifikasi toolbar memuat `Search`, `Filter`, dan `Download`
136. Verifikasi segmen pertama `Approvals` tidak bisa diklik
137. Verifikasi segmen tengah `Assignment` bisa diklik
138. Verifikasi segmen terakhir `History` tidak bisa diklik

### Breadcrumb halaman Review
139. Tampilkan Breadcrumb Assignment dengan kondisi K21
140. Verifikasi breadcrumb menampilkan segmen berurutan `Approvals`, `Assignment`, `Active`, `Review`
141. Verifikasi segmen pertama `Approvals` tidak bisa diklik
142. Verifikasi segmen tengah `Assignment`, `Active` bisa diklik
143. Verifikasi segmen terakhir `Review` tidak bisa diklik

### Breadcrumb Detail dari tab History Approvals
144. Tampilkan Breadcrumb Assignment dengan kondisi K22
145. Verifikasi breadcrumb menampilkan segmen berurutan `Approvals`, `Assignment`, `History`, `Detail`
146. Verifikasi segmen pertama `Approvals` tidak bisa diklik
147. Verifikasi segmen tengah `Assignment`, `History` bisa diklik
148. Verifikasi segmen terakhir `Detail` tidak bisa diklik

### Breadcrumb My Asset tab Task
149. Tampilkan Breadcrumb Assignment dengan kondisi K23
150. Verifikasi breadcrumb menampilkan segmen berurutan `My Asset`, `Task`
151. Verifikasi tidak ada segmen breadcrumb yang bisa diklik

### Breadcrumb My Asset tab Assigned
152. Tampilkan Breadcrumb Assignment dengan kondisi K24
153. Verifikasi breadcrumb menampilkan segmen berurutan `My Asset`, `Assigned`
154. Verifikasi tidak ada segmen breadcrumb yang bisa diklik

### Breadcrumb My Asset tab History
155. Tampilkan Breadcrumb Assignment dengan kondisi K25
156. Verifikasi breadcrumb menampilkan segmen berurutan `My Asset`, `History`
157. Verifikasi tidak ada segmen breadcrumb yang bisa diklik

### Filter Panel halaman Assigned Asset tanpa filter Assignee
158. Tampilkan Breadcrumb Assignment dengan kondisi K18
159. Klik ikon Filter
160. Verifikasi Filter Panel memuat field `Status`
161. Verifikasi field `Assignee` tidak tampil pada Filter Panel


