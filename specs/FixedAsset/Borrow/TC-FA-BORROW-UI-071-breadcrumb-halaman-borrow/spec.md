---
id: TC-FA-BORROW-UI-071-breadcrumb-halaman-borrow
title: "Breadcrumb tiap halaman Borrow"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2#p2", "§4.2#p3", "§4.2#r1", "§4.2#r2", "§4.2#r3", "§4.2#r4", "§4.2#r5", "§4.2#r6", "§4.2#r7", "§4.2#r8", "§4.2#r9", "§4.2#r10", "§4.2#r11", "§4.2#r12", "§4.2#r13", "§4.2.1#p1", "§4.2.3#p1", "§4.2.9#p2", "§4.2.10#p2", "§4.2.10#r1", "§4.2.10#r2", "§4.2.10#r3", "§4.2.10#r4", "EB-TBL-11"]
smoke: []
dependsOn: []
trace:
  "§4.2#p2": [22, 45, 47, 53, 57]
  "§4.2#p3": [24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 46]
  "§4.2#r1": [2, 6, 9, 14]
  "§4.2#r2": [17, 20]
  "§4.2#r3": [24, 26, 28, 30, 32, 34, 36, 38, 40, 42]
  "§4.2#r4": 49
  "§4.2#r5": [51, 53]
  "§4.2#r6": [55, 57]
  "§4.2#r7": 59
  "§4.2#r8": 61
  "§4.2#r9": 63
  "§4.2#r10": [65, 69]
  "§4.2#r11": 72
  "§4.2#r12": 74
  "§4.2#r13": [76, 78, 80]
  "§4.2.1#p1": [2, 3, 4, 6, 7, 9, 10, 12, 14, 15]
  "§4.2.3#p1": [17, 18, 20, 22, 88, 89, 90]
  "§4.2.9#p2": 72
  "§4.2.10#p2": [65, 66, 67, 69, 70]
  "§4.2.10#r1": 65
  "§4.2.10#r2": 69
  "§4.2.10#r3": 72
  "§4.2.10#r4": 74
  "EB-TBL-11": [44, 45, 47, 82, 84, 85, 86]
anchor: []
coverage:
  web: automated
---

# Breadcrumb tiap halaman Borrow

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`.
- Layar awal: Halaman yang menampilkan breadcrumb
- Komponen: Breadcrumb Borrow
- Data:
  - DU-071-1: breadcrumb yang diharapkan `Transactions > Borrow > Transactions`.
  - DU-071-2: breadcrumb yang diharapkan `Transactions > Borrow > Drafts`.
  - DU-071-3: breadcrumb yang diharapkan `Transactions > Borrow > Borrowed Assets`.
  - DU-071-4: breadcrumb yang diharapkan `Transactions > Borrow > History`.
  - DU-071-5: breadcrumb yang diharapkan `Transactions > Borrow > Draft > Borrow Request`.
  - DU-071-6: breadcrumb yang diharapkan `Transactions > Borrow > Borrow Request`.
  - DU-071-7: breadcrumb yang diharapkan `Transactions > Borrow > Drafts > Detail`.
  - DU-071-8: breadcrumb yang diharapkan `Transactions > Borrow > Transactions > Detail`.
  - DU-071-9: breadcrumb yang diharapkan `Transactions > Borrow > History > Detail`.
  - DU-071-10: breadcrumb yang diharapkan `Transactions > Borrow > Transactions > Handover`.
  - DU-071-11: breadcrumb yang diharapkan `Transactions > Borrow > Transactions > Return`.
  - DU-071-12: breadcrumb yang diharapkan `Transactions > Borrow > Borrowed Assets > Return`.
  - DU-071-13: breadcrumb yang diharapkan `Transactions > Borrow > Transactions > Extension Request`.
  - DU-071-14: breadcrumb yang diharapkan `Transactions > Borrow > Borrowed Assets > Extension Request`.
  - DU-071-15: breadcrumb yang diharapkan `Transactions > Borrow > Transactions > Review`.
  - DU-071-16: breadcrumb yang diharapkan `My Asset > Borrowed > Extension Request`.
  - DU-071-17: breadcrumb yang diharapkan `Transactions > Borrow > Borrowed Assets > Detail`.
  - DU-071-18: breadcrumb yang diharapkan `Approvals > Borrow > Active`.
  - DU-071-19: breadcrumb yang diharapkan `Approvals > Borrow > History`.
  - DU-071-20: breadcrumb yang diharapkan `Approvals > Borrow > Active > Review`.
  - DU-071-21: breadcrumb yang diharapkan `Approvals > Borrow > History > Detail`.
  - DU-071-22: breadcrumb yang diharapkan `My Asset > Task`.
  - DU-071-23: breadcrumb yang diharapkan `My Asset > Borrowed`.
  - DU-071-24: breadcrumb yang diharapkan `My Asset > History`.
- Kondisi:
  - K1: tab Transactions pada Halaman Borrow.
  - K2: tab Drafts pada Halaman Borrow.
  - K3: tab Borrowed Assets pada Halaman Borrow, sub-tab By Asset.
  - K4: tab Borrowed Assets pada Halaman Borrow, sub-tab By Borrower.
  - K5: tab History pada Halaman Borrow.
  - K6: halaman Borrow Request baru dan pengguna memiliki tab Drafts.
  - K7: halaman Borrow Request untuk Edit draft dan pengguna memiliki tab Drafts.
  - K8: halaman Borrow Request dan pengguna tidak memiliki tab Drafts (level Basic atau role tanpa Drafts).
  - K9: Borrow Detail dibuka untuk BRW berstatus header Draft.
  - K10: Borrow Detail dibuka untuk BRW berstatus header Waiting for Approval.
  - K11: Borrow Detail dibuka untuk BRW berstatus header Waiting for Handover.
  - K12: Borrow Detail dibuka untuk BRW berstatus header Extension Request.
  - K13: Borrow Detail dibuka untuk BRW berstatus header Extension Approval.
  - K14: Borrow Detail dibuka untuk BRW berstatus header Borrowed.
  - K15: Borrow Detail dibuka untuk BRW berstatus header Borrowed dengan penanda Overdue.
  - K16: Borrow Detail dibuka untuk BRW berstatus header Returned.
  - K17: Borrow Detail dibuka untuk BRW berstatus header Rejected.
  - K18: Borrow Detail dibuka untuk BRW berstatus header Canceled.
  - K19: Borrow Detail dibuka untuk BRW berstatus header Waiting for Approval.
  - K20: halaman Handover dibuka dari tab Transactions.
  - K21: halaman Return dibuka dari tab Transactions.
  - K22: halaman Return dibuka dari tab Borrowed Assets untuk aset dari beberapa BRW.
  - K23: halaman Extend dibuka dari tab Transactions.
  - K24: halaman Extend dibuka dari tab Borrowed Assets.
  - K25: halaman Review Extension Request dibuka dari tab Transactions.
  - K26: halaman Extend dibuka dari My Asset.
  - K27: detail Borrowed Asset dibuka dari tab Borrowed Assets.
  - K28: halaman Approvals > Borrow tab Active.
  - K29: halaman Approvals > Borrow tab History.
  - K30: halaman Review Approval dibuka dari tab Active.
  - K31: Borrow Detail dibuka dari tab History Approvals.
  - K32: halaman My Asset tab Task.
  - K33: halaman My Asset tab Borrowed.
  - K34: halaman My Asset tab History.
  - K35: halaman My Asset tab Task.
  - K36: halaman Approvals > Borrow tab Active.

## Test Steps

### Breadcrumb dan toolbar tab Transactions
1. Tampilkan Breadcrumb Borrow dengan kondisi K1
2. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions`
3. Verifikasi Tabs menampilkan `Transactions`, `Drafts`, `Borrowed Assets`, dan `History`
4. Verifikasi toolbar tab Transactions menampilkan `Search by Scan`, `Search`, `Filter`, `Download`, dan `[+ Borrow]`

### Breadcrumb dan toolbar tab Drafts
5. Tampilkan Breadcrumb Borrow dengan kondisi K2
6. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Drafts`
7. Verifikasi toolbar tab Drafts menampilkan `Search by Scan`, `Search`, `Filter`, dan `[+ Borrow]`

### Breadcrumb dan toolbar tab Borrowed Assets
8. Tampilkan Breadcrumb Borrow dengan kondisi K3
9. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Borrowed Assets`
10. Verifikasi toolbar tab Borrowed Assets menampilkan sub-tab `By Asset` dan `By Borrower`, `Search by Scan`, `Search`, `Filter`, dan `Download`

### Toolbar tab Borrowed Assets sub-tab By Borrower
11. Tampilkan Breadcrumb Borrow dengan kondisi K4
12. Verifikasi toolbar sub-tab By Borrower tidak menampilkan `Search by Scan`

### Breadcrumb dan toolbar tab History
13. Tampilkan Breadcrumb Borrow dengan kondisi K5
14. Verifikasi breadcrumb menampilkan `Transactions > Borrow > History`
15. Verifikasi toolbar tab History menampilkan sub-tab `By Transaction` dan `By Asset`, `Search`, `Filter`, dan `Download`

### Breadcrumb Borrow Request baru
16. Tampilkan Breadcrumb Borrow dengan kondisi K6
17. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Draft > Borrow Request`
18. Verifikasi judul `Borrow Request` tampil

### Breadcrumb Edit draft
19. Tampilkan Breadcrumb Borrow dengan kondisi K7
20. Verifikasi breadcrumb Edit draft sama dengan Borrow Request baru, `Transactions > Borrow > Draft > Borrow Request`

### Breadcrumb Borrow Request tanpa tab Drafts
21. Tampilkan Breadcrumb Borrow dengan kondisi K8
22. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Borrow Request`

### Origin Tab Borrow Detail untuk status Draft
23. Tampilkan Breadcrumb Borrow dengan kondisi K9
24. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Drafts > Detail`

### Origin Tab Borrow Detail untuk status Waiting for Approval
25. Tampilkan Breadcrumb Borrow dengan kondisi K10
26. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Detail`

### Origin Tab Borrow Detail untuk status Waiting for Handover
27. Tampilkan Breadcrumb Borrow dengan kondisi K11
28. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Detail`

### Origin Tab Borrow Detail untuk status Extension Request
29. Tampilkan Breadcrumb Borrow dengan kondisi K12
30. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Detail`

### Origin Tab Borrow Detail untuk status Extension Approval
31. Tampilkan Breadcrumb Borrow dengan kondisi K13
32. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Detail`

### Origin Tab Borrow Detail untuk status Borrowed
33. Tampilkan Breadcrumb Borrow dengan kondisi K14
34. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Detail`

### Origin Tab Borrow Detail untuk status Borrowed dengan penanda Overdue
35. Tampilkan Breadcrumb Borrow dengan kondisi K15
36. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Detail`

### Origin Tab Borrow Detail untuk status Returned
37. Tampilkan Breadcrumb Borrow dengan kondisi K16
38. Verifikasi breadcrumb menampilkan `Transactions > Borrow > History > Detail`

### Origin Tab Borrow Detail untuk status Rejected
39. Tampilkan Breadcrumb Borrow dengan kondisi K17
40. Verifikasi breadcrumb menampilkan `Transactions > Borrow > History > Detail`

### Origin Tab Borrow Detail untuk status Canceled
41. Tampilkan Breadcrumb Borrow dengan kondisi K18
42. Verifikasi breadcrumb menampilkan `Transactions > Borrow > History > Detail`

### Segmen breadcrumb Borrow Detail
43. Tampilkan Breadcrumb Borrow dengan kondisi K19
44. Verifikasi segmen `Transactions` pertama pada breadcrumb tidak dapat diklik
45. Verifikasi segmen `Borrow` pada breadcrumb dapat diklik dan mengarah ke tab Transactions
46. Verifikasi segmen origin `Transactions` pada breadcrumb dapat diklik
47. Verifikasi segmen `Detail` terakhir pada breadcrumb tidak dapat diklik

### Breadcrumb Handover
48. Tampilkan Breadcrumb Borrow dengan kondisi K20
49. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Handover`

### Breadcrumb Return dari Transactions
50. Tampilkan Breadcrumb Borrow dengan kondisi K21
51. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Return`

### Breadcrumb Return dari Borrowed Assets
52. Tampilkan Breadcrumb Borrow dengan kondisi K22
53. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Borrowed Assets > Return`

### Breadcrumb Extend dari Transactions
54. Tampilkan Breadcrumb Borrow dengan kondisi K23
55. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Extension Request`

### Breadcrumb Extend dari Borrowed Assets
56. Tampilkan Breadcrumb Borrow dengan kondisi K24
57. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Borrowed Assets > Extension Request`

### Breadcrumb Review Extension Request
58. Tampilkan Breadcrumb Borrow dengan kondisi K25
59. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Transactions > Review`

### Breadcrumb Extension dari My Asset
60. Tampilkan Breadcrumb Borrow dengan kondisi K26
61. Verifikasi breadcrumb menampilkan `My Asset > Borrowed > Extension Request`

### Breadcrumb detail Borrowed Asset
62. Tampilkan Breadcrumb Borrow dengan kondisi K27
63. Verifikasi breadcrumb menampilkan `Transactions > Borrow > Borrowed Assets > Detail`

### Breadcrumb Approvals tab Active
64. Tampilkan Breadcrumb Borrow dengan kondisi K28
65. Verifikasi breadcrumb menampilkan `Approvals > Borrow > Active`
66. Verifikasi Tabs menampilkan `Active` dan `History`
67. Verifikasi toolbar tab Active menampilkan `Search` dan `Filter`

### Breadcrumb Approvals tab History
68. Tampilkan Breadcrumb Borrow dengan kondisi K29
69. Verifikasi breadcrumb menampilkan `Approvals > Borrow > History`
70. Verifikasi toolbar tab History menampilkan `Search`, `Filter`, dan `Download`

### Breadcrumb halaman Review Approval
71. Tampilkan Breadcrumb Borrow dengan kondisi K30
72. Verifikasi breadcrumb menampilkan `Approvals > Borrow > Active > Review`

### Breadcrumb detail dari tab History Approvals
73. Tampilkan Breadcrumb Borrow dengan kondisi K31
74. Verifikasi breadcrumb menampilkan `Approvals > Borrow > History > Detail`

### Breadcrumb My Asset tab Task
75. Tampilkan Breadcrumb Borrow dengan kondisi K32
76. Verifikasi breadcrumb menampilkan `My Asset > Task`

### Breadcrumb My Asset tab Borrowed
77. Tampilkan Breadcrumb Borrow dengan kondisi K33
78. Verifikasi breadcrumb menampilkan `My Asset > Borrowed`

### Breadcrumb My Asset tab History
79. Tampilkan Breadcrumb Borrow dengan kondisi K34
80. Verifikasi breadcrumb menampilkan `My Asset > History`

### Breadcrumb dua segmen tanpa segmen yang bisa diklik
81. Tampilkan Breadcrumb Borrow dengan kondisi K35
82. Verifikasi segmen `My Asset` dan `Task` pada breadcrumb tidak dapat diklik karena breadcrumb hanya dua segmen

### Segmen tengah breadcrumb Approvals
83. Tampilkan Breadcrumb Borrow dengan kondisi K36
84. Verifikasi segmen `Approvals` pertama pada breadcrumb tidak dapat diklik
85. Verifikasi segmen `Borrow` pada breadcrumb dapat diklik
86. Verifikasi segmen `Active` terakhir pada breadcrumb tidak dapat diklik

### Segmen Draft pada breadcrumb Borrow Request menuju tab Drafts
87. Tampilkan Breadcrumb Borrow dengan kondisi K6
88. Verifikasi segmen `Draft` pada breadcrumb dapat diklik dan mengarah ke tab Drafts
89. Verifikasi judul `Borrow Request` tampil
90. Verifikasi form tidak menampilkan badge Draft, judul `Borrow details`, dan judul `Assets`
