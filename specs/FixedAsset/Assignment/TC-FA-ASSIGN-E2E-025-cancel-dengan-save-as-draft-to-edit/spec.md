---
id: TC-FA-ASSIGN-E2E-025-cancel-dengan-save-as-draft-to-edit
title: "Cancel dengan Save as Draft to edit lalu Submit ulang"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.2#p69", "§9.2#p70", "§9.2#p71", "§9.2#b47", "§9.2#b48", "§9.2#b49", "§9.2#b50", "§9.2#b51", "§9.2#b52", "§9.2#b53", "§9.2#b54", "§9.2#b55", "§9.2#r21", "§9.2#r22", "§9.2#r23", "§9.2#r24", "TS-ASG-22", "EC-ASG-53", "EC-ASG-54", "F-ASSIGN-09.k3"]
smoke: []
dependsOn: []
trace:
  "§9.2#p69": [22, 29]
  "§9.2#p70": 13
  "§9.2#p71": [74, 87]
  "§9.2#b47": [4, 70]
  "§9.2#b48": 7
  "§9.2#b49": 13
  "§9.2#b50": 28
  "§9.2#b51": [22, 25, 114]
  "§9.2#b52": 23
  "§9.2#b53": 92
  "§9.2#b54": [9, 10]
  "§9.2#b55": 17
  "§9.2#r21": 5
  "§9.2#r22": 80
  "§9.2#r23": [99, 104]
  "§9.2#r24": [87, 92]
  "TS-ASG-22": 9
  "EC-ASG-53": [52, 54]
  "EC-ASG-54": [61, 70]
  "F-ASSIGN-09.k3": [4, 17]
anchor: [69, 73]
coverage:
  web: automated
---

# Cancel dengan Save as Draft to edit lalu Submit ulang

## Prerequisites
- Aktor:
  - Aktor A: Asset Admin (Aktor Assignment) `Bagas Santoso {runId}` dengan cakupan Group `Head Office`, pembatal ASG.
  - Aktor C: Total Control tanpa penugasan Group, hanya memproses lewat fallback Total Control.
  - Aktor P: Approver pada Group `Head Office`, hanya memicu penolakan aset.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-025-1: ASG Assignee Employee `Sari Dewi`, Group `Head Office`, Note `Untuk proyek Q4`, diajukan oleh `Yuni Astuti {runId}` (bukan Aktor A), berstatus Waiting for Handover, berisi `Laptop Dell Latitude 5420 {runId}` (Purpose `Kerja harian`) dan `Monitor LG 24 {runId}` (Purpose `Presentasi`).
  - DU-025-2: ASG Assignee Employee `Sari Dewi`, Group `Head Office`, berstatus Waiting for Handover, berisi `Printer HP M404 {runId}` (Purpose `Kerja harian`).
  - DU-025-3: ASG Assignee Employee `Sari Dewi`, Group `Head Office`, berstatus Waiting for Handover, berisi `Projector Epson EB-X49 {runId}` (Purpose `Kerja harian`).
  - DU-025-4: ASG Assignee Employee `Sari Dewi`, Group `Head Office`, berisi `Scanner Epson DS-530 {runId}` berstatus Assigned dan `Camera Sony A7 {runId}` berstatus Waiting for Handover.
  - DU-025-5: ASG Assignee Employee `Sari Dewi`, Group `Head Office`, berstatus Waiting for Approval, berisi `Toyota Avanza {runId}`, approver Aktor P `Maya Putri {runId}`.
  - DU-025-6: ASG Assignee Employee `Sari Dewi`, Group `Head Office`, berstatus Waiting for Handover, berisi `Generator Honda EU70 {runId}`, dengan batas serah terima yang akan terlampaui.
  - DU-025-7: ASG Assignee Employee `Sari Dewi`, Group `Head Office`, berstatus Waiting for Approval, berisi `Excavator PC200 {runId}`, dengan batas persetujuan yang akan terlampaui.
  - DU-025-8: Aktor C `Rudi Hermawan {runId}`, Total Control, tanpa penugasan Group.
  - DU-025-9: Assignee Employee `Sari Dewi`, karyawan aktif dengan akun login.
  - DU-025-10: Assignee Employee `Nadia Putri`, karyawan aktif dengan akun login.
  - DU-025-11: Purpose baris aset baru `Operasional kantor`.
  - DU-025-12: Approval Note penolakan `Aset dipakai proyek lain`.
  - DU-025-13: Aktor A `Bagas Santoso {runId}`, Asset Admin dengan cakupan Group `Head Office`, yang membatalkan ASG pada langkah Cancel.
  - DU-025-14: Pengaju ASG asal `Yuni Astuti {runId}`, Asset Admin dengan cakupan Group `Head Office`, berbeda dari Aktor A.
  - DU-025-15: ASG Assignee Division `Finance`, PIC `Nadia Putri`, Group `Head Office`, berstatus Waiting for Handover, berisi aset `Forklift Toyota 8FD {runId}` (Purpose `Kerja harian`).
  - Draft hasil Cancel DU-025-1 berisi `2` aset.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Akun Aktor C dan Aktor P aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Cancel per ASG dengan Save as Draft to edit
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Klik `⋯` pada baris ASG
3. Klik `Cancel Assignment`
4. Verifikasi checkbox `Save as Draft to edit` tampil pada dialog `Cancel Assignment` dan belum tercentang
5. Verifikasi dialog `Cancel Assignment` tidak memiliki field Reason
6. Centang `Save as Draft to edit`
7. Verifikasi teks bantu `The assets become available again and a new draft with the same details is created so you can fix and resubmit it.` tampil
8. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
9. Verifikasi toast `Success, assignment has been canceled and saved as a draft.` tampil
10. Verifikasi toast tersebut tidak memuat tautan ke Draft baru
11. Klik tab `History`
12. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
13. Verifikasi ASG dengan aset `Laptop Dell Latitude 5420 {runId}` tampil di tab History berstatus `Canceled`
14. Klik Transaction ID pada baris ASG hasil
15. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
16. Klik `Assignment Log`
17. Verifikasi node `Canceled by [Actor]` memuat baris detail `Saved as draft` berupa tautan ke Draft
18. Klik `✕` pada dialog Assignment Log

### Draft baru memuat isi ASG asal
19. Buka `Transactions > Assignment`
20. Klik tab `Drafts`
21. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
22. Verifikasi Draft Assignee `Sari Dewi` dengan Total Asset `2` dan Origin `Restored` tampil beserta keterangan `Restored from [Transaction ID]`
23. Verifikasi Modified By pada Draft baru berisi `Bagas Santoso {runId}`, nama Aktor A yang membatalkan, dan bukan `Yuni Astuti {runId}` yang mengajukan ASG asal
24. Klik Assignee `Sari Dewi` pada baris Draft
25. Verifikasi Draft memuat Assignee `Sari Dewi`, Note `Untuk proyek Q4`, baris `Laptop Dell Latitude 5420 {runId}` dengan Purpose `Kerja harian`, dan baris `Monitor LG 24 {runId}` dengan Purpose `Presentasi`

### Submit ulang Draft hasil Cancel
26. Klik `[Submit]`
27. Klik `[Submit]` pada dialog `Submit Assignment`
28. Verifikasi toast `Success, assignment [Transaction ID] is ready for handover.` tampil sehingga aset yang dilepas dapat diajukan ulang
29. Verifikasi Transaction ID ASG baru berbeda dari Transaction ID ASG asal yang berstatus Canceled

### Aset Draft hasil Cancel diambil transaksi lain sebelum Submit ulang
30. Buka `Transactions > Assignment`
31. Ketik Search `Printer HP M404 {runId}`, tekan Enter
32. Klik `⋯` pada baris ASG
33. Klik `Cancel Assignment`
34. Centang `Save as Draft to edit`
35. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
36. Klik `[+ Assign]`
37. Klik pilihan `Employee`
38. Klik `[Select Assignee]`
39. Pilih baris `Nadia Putri` pada dialog Select Assignee
40. Klik `[Select]`
41. Klik `[+ Asset]`
42. Ketik Search `Printer HP M404 {runId}`, tekan Enter
43. Centang baris `Printer HP M404 {runId}`
44. Klik `[Select]`
45. Isi Purpose baris `Printer HP M404 {runId}` dengan `Operasional kantor`
46. Klik `[Submit]`
47. Klik `[Submit]` pada dialog `Submit Assignment`
48. Buka `Transactions > Assignment`
49. Klik tab `Drafts`
50. Ganti isi kotak search dengan `Printer HP M404 {runId}`, tekan Enter
51. Klik Assignee `Sari Dewi` pada baris Draft
52. Verifikasi baris `Printer HP M404 {runId}` ditandai ikon ⚠ dengan caption `This asset can no longer be assigned.`
53. Klik `[Submit]`
54. Verifikasi caption `Remove the unavailable assets to continue.` tampil dan Submit diblokir
55. Klik `[Cancel]` pada form (form belum diubah, tanpa dialog Unsaved Changes)

### Aktor tanpa cakupan Group ASG tidak bisa Save as Draft to edit
56. Masuk sebagai Aktor C
57. Buka `Transactions > Assignment`
58. Ketik Search `Projector Epson EB-X49 {runId}`, tekan Enter
59. Klik `⋯` pada baris ASG
60. Klik `Cancel Assignment`
61. Verifikasi checkbox `Save as Draft to edit` disabled dengan alasan `You don't manage Head Office, so this assignment can't be saved as a draft.` tersampaikan pada checkbox
62. Klik `[Go Back]`

### ASG yang memiliki baris Assigned
63. Masuk sebagai Aktor A
64. Buka `Transactions > Assignment`
65. Ketik Search `Camera Sony A7 {runId}`, tekan Enter
66. Klik Transaction ID pada baris ASG hasil
67. Klik `⋯` pada baris `Camera Sony A7 {runId}`
68. Klik `Cancel Assignment`
69. Verifikasi dialog `Cancel Assignment` tampil dengan pertanyaan `Are you sure you want to cancel it?`
70. Verifikasi checkbox `Save as Draft to edit` tidak tampil karena ASG sudah memiliki baris Assigned
71. Klik `[Go Back]`
72. Klik `⋯` pada baris `Scanner Epson DS-530 {runId}`
73. Verifikasi aksi `Assignment Log` tersedia pada baris `Scanner Epson DS-530 {runId}`
74. Verifikasi aksi `Cancel Assignment` tidak tersedia pada baris `Scanner Epson DS-530 {runId}` yang berstatus Assigned
75. Tekan Esc untuk menutup menu baris

### Approver menolak aset: baris Rejected tanpa Draft baru
76. Aktor P menolak aset `Toyota Avanza {runId}` pada ASG yang menunggu approval dengan Approval Note `Aset dipakai proyek lain`
77. Buka `Transactions > Assignment`
78. Klik tab `History`
79. Ganti isi kotak search dengan `Toyota Avanza {runId}`, tekan Enter
80. Verifikasi ASG dengan aset `Toyota Avanza {runId}` tampil di tab History berstatus `Rejected`

### Penutupan otomatis karena batas serah terima terlampaui
81. Job Transaction timeout berjalan setelah batas serah terima ASG dengan aset `Generator Honda EU70 {runId}` terlampaui
82. Klik tab `History`
83. Ganti isi kotak search dengan `Generator Honda EU70 {runId}`, tekan Enter
84. Klik Transaction ID pada baris ASG hasil
85. Klik `⋯` pada baris `Generator Honda EU70 {runId}`
86. Klik `Assignment Log`
87. Verifikasi node `Canceled by System` memuat Reason `Not handed over`
88. Klik `✕` pada dialog Assignment Log
89. Buka `Transactions > Assignment`
90. Klik tab `Drafts`
91. Ganti isi kotak search dengan `Generator Honda EU70 {runId}`, tekan Enter
92. Verifikasi Draft baru dengan Origin `Restored by system` dan keterangan `Restored from [Transaction ID]` tampil

### Penutupan otomatis karena timeout menunggu approval
93. Job Transaction timeout berjalan setelah batas persetujuan ASG dengan aset `Excavator PC200 {runId}` terlampaui
94. Klik tab `History`
95. Ganti isi kotak search dengan `Excavator PC200 {runId}`, tekan Enter
96. Klik Transaction ID pada baris ASG hasil
97. Klik `⋯` pada baris `Excavator PC200 {runId}`
98. Klik `Assignment Log`
99. Verifikasi node `Canceled by System` memuat Reason `Timed out (Waiting for Approval)`
100. Klik `✕` pada dialog Assignment Log
101. Buka `Transactions > Assignment`
102. Klik tab `Drafts`
103. Ganti isi kotak search dengan `Excavator PC200 {runId}`, tekan Enter
104. Verifikasi Draft baru dengan Origin `Restored by system` tampil untuk aset `Excavator PC200 {runId}`

### Draft hasil Cancel memuat Assignee Division dan PIC
105. Buka `Transactions > Assignment`
106. Ketik Search `Forklift Toyota 8FD {runId}`, tekan Enter
107. Klik `⋯` pada baris ASG
108. Klik `Cancel Assignment`
109. Centang `Save as Draft to edit`
110. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
111. Klik tab `Drafts`
112. Ganti isi kotak search dengan `Forklift Toyota 8FD {runId}`, tekan Enter
113. Klik Assignee `Finance` pada baris Draft
114. Verifikasi Draft memuat Assignee Division `Finance`, PIC `Nadia Putri`, dan baris `Forklift Toyota 8FD {runId}` dengan Purpose `Kerja harian`
115. Klik `[Cancel]` pada form (form belum diubah, tanpa dialog Unsaved Changes)
