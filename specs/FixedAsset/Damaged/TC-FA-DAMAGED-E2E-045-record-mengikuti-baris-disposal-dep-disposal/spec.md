---
id: TC-FA-DAMAGED-E2E-045-record-mengikuti-baris-disposal-dep-disposal
title: "Record mengikuti baris Disposal: Submit Request menjadi In Disposal Process, Reject/Cancel/Remove kembali Damaged, dan Execute menjadi Disposed di History dengan Resolved By System"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r20", "§Aturan Logika Modul#r22", "§8.1#p2", "§8.1#r16", "§8.3#r4", "§8.3#r5", "§9.7#r12", "§9.7#r13", "§9.7#r14", "§9.4.4#r30", EC-DMG-17, S-DMG-05, S-DMG-06, T-DMG-02, "§Aturan Logika Modul#r19", "§Aturan Logika Modul#r65"]
smoke: []
dependsOn:
  - "Disposal: Dispose, Request, Reject, Cancel, Remove, Execute"
trace:
  "§Aturan Logika Modul#r19": 24
  "§Aturan Logika Modul#r20": [7, 39]
  "§Aturan Logika Modul#r65": 7
  "§9.7#r12": [7, 39]
  S-DMG-05: [9, 10]
  S-DMG-06: 11
  "§8.1#p2": [14, 48, 62, 76]
  "§9.7#r13": [21, 24]
  "§9.4.4#r30": [24, 28]
  T-DMG-02: [24, 25, 26]
  "§8.1#r16": [28, 29]
  "§8.3#r4": 28
  "§Aturan Logika Modul#r22": [45, 59, 73]
  "§9.7#r14": [45, 46, 59, 60, 73, 74]
  EC-DMG-17: [45, 48, 59, 62, 73, 76]
  "§8.3#r5": [48, 62, 76]
anchor: []
coverage:
  web: automated
---

# Record mengikuti baris Disposal: Submit Request menjadi In Disposal Process, Reject/Cancel/Remove kembali Damaged, dan Execute menjadi Disposed di History dengan Resolved By System

## Prerequisites
- Aktor: Total Control.
- Layar awal: Transactions > Disposal > Reported.
- Data:
  - DU-045-1: Damage record `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-045-2: Damage record `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-045-3: Damage record `Printer HP LaserJet M404 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-045-4: Damage record `Tablet Samsung Tab A8 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Basic`.
  - Baris Disposal hasil Submit Request atas `Laptop Dell Latitude 5420 {runId}` berstatus Waiting for Execution, tanpa menunggu approval.
  - Baris Disposal hasil Submit Request atas `Monitor Dell P2422H {runId}` berstatus Waiting for Approval, menunggu keputusan approver.

## Test Steps

### Submit Request mengubah record menjadi In Disposal Process
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

### Execute mengubah record menjadi Disposed di History
16. Buka Transactions > Disposal, daftar baris Disposal
17. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
18. Execute baris Disposal aset `Laptop Dell Latitude 5420 {runId}`
19. Buka Assets > Damaged > Active
20. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
21. Verifikasi hasil Search `Laptop Dell Latitude 5420 {runId}` di sub-tab Active menampilkan `No results found`
22. Buka sub-tab History
23. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
24. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Disposed`
25. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memuat Resolved By `System`
26. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memuat Resolved Date
27. Klik nama aset `Laptop Dell Latitude 5420 {runId}` di kolom Name
28. Verifikasi dialog Damage Log memuat node `Disposed` dengan pelaku `System`
29. Verifikasi baris detail node `Disposed` memuat `Disposal No.`
30. Tutup dialog Damage Log

### Reject baris Disposal mengembalikan record ke Damaged
31. Catat jumlah pada badge tab Damaged
32. Buka Transactions > Disposal, tab Reported
33. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
34. Buka menu ⋯ pada Disposal Report aset `Monitor Dell P2422H {runId}` di tab Reported
35. Klik `Dispose`
36. Submit Request pada form Request aset `Monitor Dell P2422H {runId}`
37. Buka Assets > Damaged > Active
38. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
39. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `In Disposal Process` selagi baris Disposalnya Waiting for Approval
40. Buka Transactions > Disposal, daftar baris Disposal
41. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
42. Reject baris Disposal aset `Monitor Dell P2422H {runId}`
43. Buka Assets > Damaged > Active
44. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
45. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `Damaged`
46. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
47. Klik nama aset `Monitor Dell P2422H {runId}` di kolom Name
48. Verifikasi dialog Damage Log memuat node `Rejected by`
49. Tutup dialog Damage Log

### Cancel baris Disposal mengembalikan record ke Damaged
50. Catat jumlah pada badge tab Damaged
51. Buka Transactions > Disposal, tab Reported
52. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
53. Buka menu ⋯ pada Disposal Report aset `Printer HP LaserJet M404 {runId}` di tab Reported
54. Klik `Dispose`
55. Submit Request pada form Request aset `Printer HP LaserJet M404 {runId}`
56. Cancel baris Disposal aset `Printer HP LaserJet M404 {runId}`
57. Buka Assets > Damaged > Active
58. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
59. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Damaged`
60. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
61. Klik nama aset `Printer HP LaserJet M404 {runId}` di kolom Name
62. Verifikasi dialog Damage Log memuat node `Canceled by`
63. Tutup dialog Damage Log

### Remove baris Disposal mengembalikan record ke Damaged
64. Catat jumlah pada badge tab Damaged
65. Buka Transactions > Disposal, tab Reported
66. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
67. Buka menu ⋯ pada Disposal Report aset `Tablet Samsung Tab A8 {runId}` di tab Reported
68. Klik `Dispose`
69. Submit Request pada form Request aset `Tablet Samsung Tab A8 {runId}`
70. Remove aset `Tablet Samsung Tab A8 {runId}` dari baris Disposal
71. Buka Assets > Damaged > Active
72. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
73. Verifikasi baris `Tablet Samsung Tab A8 {runId}` berstatus `Damaged`
74. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
75. Klik nama aset `Tablet Samsung Tab A8 {runId}` di kolom Name
76. Verifikasi dialog Damage Log memuat node `Removed from disposal by`
77. Tutup dialog Damage Log
