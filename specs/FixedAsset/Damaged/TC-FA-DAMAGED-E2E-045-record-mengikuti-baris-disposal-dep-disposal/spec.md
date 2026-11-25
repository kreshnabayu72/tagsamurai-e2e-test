---
id: TC-FA-DAMAGED-E2E-045-record-mengikuti-baris-disposal-dep-disposal
title: "Record mengikuti baris Disposal: Submit Request menjadi In Disposal Process, Reject/Cancel/Remove atas baris dari Report kembali Reported Disposal (Report kembali Reported), dan Execute menjadi Disposed di History dengan Resolved By System"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r20", "§Aturan Logika Modul#r22", "§8.1#p2", "§8.1#r16", "§8.3#r4", "§8.3#r5", "§9.7#r12", "§9.7#r13", "§9.7#r14", "§9.4.4#r30", EC-DMG-17, S-DMG-05, S-DMG-06, T-DMG-02, "§Aturan Logika Modul#r19", "§Aturan Logika Modul#r65", "§3#p7", "§9.2#r3"]
smoke: []
dependsOn:
  - "Disposal: Dispose, Request, Reject, Cancel, Remove, Execute"
trace:
  "§Aturan Logika Modul#r19": 27
  "§Aturan Logika Modul#r20": [7, 18, 42, 97, 100]
  "§Aturan Logika Modul#r65": 7
  "§9.7#r12": [7, 42]
  S-DMG-05: [9, 10]
  S-DMG-06: 11
  "§8.1#p2": [14, 48, 51, 55, 65, 68, 72, 82, 85, 89]
  "§9.7#r13": [24, 27]
  "§9.4.4#r30": [27, 31]
  T-DMG-02: [27, 28, 29]
  "§8.1#r16": [31, 32]
  "§8.3#r4": 31
  "§Aturan Logika Modul#r22": [48, 55, 65, 72, 82, 89]
  "§9.7#r14": [48, 49, 55, 65, 66, 72, 82, 83, 89]
  EC-DMG-17: [48, 51, 55, 65, 68, 72, 85]
  "§3#p7": [7, 27, 48, 65, 82]
  "§9.2#r3": [7, 48, 55, 65, 72, 82, 89]
  "§8.3#r5": [51, 68, 85]
anchor: []
coverage:
  web: automated
---

# Record mengikuti baris Disposal: Submit Request menjadi In Disposal Process, Reject/Cancel/Remove atas baris dari Report kembali Reported Disposal (Report kembali Reported), dan Execute menjadi Disposed di History dengan Resolved By System

## Prerequisites
- Aktor: Total Control.
- Layar awal: Transactions > Disposal > Reported.
- Data:
  - DU-045-1: Damage record `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-045-2: Damage record `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-045-3: Damage record `Printer HP LaserJet M404 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-045-4: Damage record `Tablet Samsung Tab A8 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-045-5: Damage record `Headset Jabra Evolve2 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Full`.
  - Baris Disposal hasil Submit Request atas `Laptop Dell Latitude 5420 {runId}` berstatus Waiting for Execution, tanpa menunggu approval.
  - Baris Disposal hasil Submit Request atas `Monitor Dell P2422H {runId}` berstatus Waiting for Approval, menunggu keputusan approver.

## Test Steps

### Submit Request mengubah record menjadi In Disposal Process dan Report tetap di tab Reported
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Buka menu ⋯ pada Disposal Report aset `Laptop Dell Latitude 5420 {runId}` di tab Reported
3. Klik `Dispose`
4. Submit Request pada form Request aset `Laptop Dell Latitude 5420 {runId}`
5. Buka Assets > Damaged > Active
6. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
7. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `In Disposal Process`
8. Buka menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId}`
9. Verifikasi menu baris `Laptop Dell Latitude 5420 {runId}` memuat aksi `Damage Log`
10. Verifikasi aksi `Mark as Repaired` Hidden pada menu baris `Laptop Dell Latitude 5420 {runId}`
11. Verifikasi aksi `Cancel Disposal Report` Hidden pada menu baris `Laptop Dell Latitude 5420 {runId}`
12. Tutup menu ⋯
13. Klik nama aset `Laptop Dell Latitude 5420 {runId}` di kolom Name
14. Verifikasi dialog Damage Log memuat node `Disposal requested by`
15. Tutup dialog Damage Log
16. Buka Transactions > Disposal, tab Reported
17. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
18. Verifikasi Disposal Report atas aset `Laptop Dell Latitude 5420 {runId}` tetap tampil di tab Reported dengan status `In Disposal Process`

### Execute mengubah record menjadi Disposed di History
19. Buka Transactions > Disposal, daftar baris Disposal
20. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
21. Execute baris Disposal aset `Laptop Dell Latitude 5420 {runId}`
22. Buka Assets > Damaged > Active
23. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
24. Verifikasi hasil Search `Laptop Dell Latitude 5420 {runId}` di sub-tab Active menampilkan `No results found`
25. Buka sub-tab History
26. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
27. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Disposed`
28. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memuat Resolved By `System`
29. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memuat Resolved Date
30. Klik nama aset `Laptop Dell Latitude 5420 {runId}` di kolom Name
31. Verifikasi dialog Damage Log memuat node `Disposed` dengan pelaku `System`
32. Verifikasi baris detail node `Disposed` memuat `Disposal No.`
33. Tutup dialog Damage Log

### Reject baris Disposal mengembalikan record ke Reported Disposal dan Report kembali Reported
34. Catat jumlah pada badge tab Damaged
35. Buka Transactions > Disposal, tab Reported
36. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
37. Buka menu ⋯ pada Disposal Report aset `Monitor Dell P2422H {runId}` di tab Reported
38. Klik `Dispose`
39. Submit Request pada form Request aset `Monitor Dell P2422H {runId}`
40. Buka Assets > Damaged > Active
41. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
42. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `In Disposal Process` selagi baris Disposalnya Waiting for Approval
43. Buka Transactions > Disposal, daftar baris Disposal
44. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
45. Reject baris Disposal aset `Monitor Dell P2422H {runId}`
46. Buka Assets > Damaged > Active
47. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
48. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `Reported Disposal`
49. Verifikasi jumlah pada badge tab Damaged sama dengan jumlah yang dicatat
50. Klik nama aset `Monitor Dell P2422H {runId}` di kolom Name
51. Verifikasi dialog Damage Log memuat node `Rejected by`
52. Tutup dialog Damage Log
53. Buka Transactions > Disposal, tab Reported
54. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
55. Verifikasi Disposal Report atas aset `Monitor Dell P2422H {runId}` tampil di tab Reported dengan status `Reported`

### Cancel baris Disposal mengembalikan record ke Reported Disposal dan Report kembali Reported
56. Catat jumlah pada badge tab Damaged
57. Buka Transactions > Disposal, tab Reported
58. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
59. Buka menu ⋯ pada Disposal Report aset `Printer HP LaserJet M404 {runId}` di tab Reported
60. Klik `Dispose`
61. Submit Request pada form Request aset `Printer HP LaserJet M404 {runId}`
62. Cancel baris Disposal aset `Printer HP LaserJet M404 {runId}`
63. Buka Assets > Damaged > Active
64. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
65. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Reported Disposal`
66. Verifikasi jumlah pada badge tab Damaged sama dengan jumlah yang dicatat
67. Klik nama aset `Printer HP LaserJet M404 {runId}` di kolom Name
68. Verifikasi dialog Damage Log memuat node `Canceled by`
69. Tutup dialog Damage Log
70. Buka Transactions > Disposal, tab Reported
71. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
72. Verifikasi Disposal Report atas aset `Printer HP LaserJet M404 {runId}` tampil di tab Reported dengan status `Reported`

### Remove baris Disposal mengembalikan record ke Reported Disposal dan Report kembali Reported
73. Catat jumlah pada badge tab Damaged
74. Buka Transactions > Disposal, tab Reported
75. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
76. Buka menu ⋯ pada Disposal Report aset `Tablet Samsung Tab A8 {runId}` di tab Reported
77. Klik `Dispose`
78. Submit Request pada form Request aset `Tablet Samsung Tab A8 {runId}`
79. Remove aset `Tablet Samsung Tab A8 {runId}` dari baris Disposal
80. Buka Assets > Damaged > Active
81. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
82. Verifikasi baris `Tablet Samsung Tab A8 {runId}` berstatus `Reported Disposal`
83. Verifikasi jumlah pada badge tab Damaged sama dengan jumlah yang dicatat
84. Klik nama aset `Tablet Samsung Tab A8 {runId}` di kolom Name
85. Verifikasi dialog Damage Log memuat node `Removed from disposal by`
86. Tutup dialog Damage Log
87. Buka Transactions > Disposal, tab Reported
88. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
89. Verifikasi Disposal Report atas aset `Tablet Samsung Tab A8 {runId}` tampil di tab Reported dengan status `Reported`

### Draft Disposal tidak mengubah record dan tidak memberi penanda pada Report
90. Buka Transactions > Disposal, tab Reported
91. Ketik Search `Headset Jabra Evolve2 {runId}`, tekan Enter
92. Buka menu ⋯ pada Disposal Report aset `Headset Jabra Evolve2 {runId}` di tab Reported
93. Klik `Dispose`
94. Simpan form Request aset `Headset Jabra Evolve2 {runId}` sebagai Draft
95. Buka Assets > Damaged > Active
96. Ketik Search `Headset Jabra Evolve2 {runId}`, tekan Enter
97. Verifikasi baris `Headset Jabra Evolve2 {runId}` tetap berstatus `Reported Disposal`
98. Buka Transactions > Disposal, tab Reported
99. Ketik Search `Headset Jabra Evolve2 {runId}`, tekan Enter
100. Verifikasi Disposal Report atas aset `Headset Jabra Evolve2 {runId}` tampil di tab Reported dengan status `Reported`
