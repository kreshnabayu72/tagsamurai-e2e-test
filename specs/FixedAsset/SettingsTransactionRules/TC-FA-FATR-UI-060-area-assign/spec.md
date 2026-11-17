---
id: TC-FA-FATR-UI-060-area-assign
title: "Area utama: field tab Assign"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r66
  - §4.1#r110
  - §4.1#r111
  - §4.1#r112
  - §4.1#r113
  - §4.1#r171
  - §4.1#r173
  - §4.1#r187
  - §4.1#r192
  - §4.1#r209
  - §4.1#r221
  - §9.2#b423
  - §4.1#r189
smoke: []
dependsOn: []
trace:
  §4.1#r66: [2, 4, 59]
  §4.1#r110: [6, 8, 61]
  §4.1#r111: [9, 11, 32, 37, 63]
  §4.1#r112: [12, 51, 65]
  §4.1#r113: [13, 15, 33, 38, 67]
  §4.1#r171: [18, 42, 46, 69]
  §4.1#r173: [19, 43, 47, 71]
  §4.1#r187: [21, 23, 34, 39, 73]
  §4.1#r192: [24, 26, 44, 49, 75]
  §4.1#r209: [29, 52, 77]
  §4.1#r221: [30, 35, 40, 79]
  §9.2#b423: [18, 19]
  §4.1#r189: 56
anchor: [54, 55]
coverage:
  web: automated
---

# Area utama: field tab Assign

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-060-1: Pengaturan Company default tab Assign pada All categories: Allow Assign `Allow`, Allowed assignee: Employee `ON`, Allowed assignee: Division `ON`, Max assets per assignee (concurrent) `0`, Need recipient confirmation `Yes`, Photo at start `ON`, Photo at end `ON`, Require approval `OFF`, Approval type `Any one approver`, Transaction timeout `7`, Send email notifications `OFF`.
  - DU-060-2: Pengaturan Company default tab Assign pada All categories yang berbeda dari nilai awal: Allowed assignee: Employee `ON`, Allowed assignee: Division `OFF`, Need recipient confirmation `No`, Photo at start `OFF`, Photo at end `OFF`, Require approval `ON`, Approval type `All approvers (AND)`, Send email notifications `ON`.
- Kondisi:
  - K1: node All categories terpilih, tab Assign aktif, Approval Workflow tersedia di plan, nilai Company default memakai DU-060-1.
  - K2: node All categories terpilih, tab Assign aktif, Approval Workflow tersedia di plan, nilai Company default memakai DU-060-2.

## Test Steps

### Eligibility dan Limits Assign
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi `Allow Assign` bernilai `Allow`
3. Buka daftar pilihan `Allow Assign`
4. Verifikasi pilihan `Allow Assign` adalah `Allow` dan `Deny`
5. Tutup daftar pilihan dengan Escape
6. Verifikasi `Allowed assignee: Employee` bernilai `ON`
7. Matikan `Allowed assignee: Employee`
8. Verifikasi `Allowed assignee: Employee` bernilai `OFF`
9. Verifikasi `Allowed assignee: Division` bernilai `ON`
10. Matikan `Allowed assignee: Division`
11. Verifikasi `Allowed assignee: Division` bernilai `OFF`
12. Verifikasi `Max assets per assignee (concurrent)` bernilai `0`
13. Verifikasi `Need recipient confirmation` bernilai `Yes`
14. Buka daftar pilihan `Need recipient confirmation`
15. Verifikasi pilihan `Need recipient confirmation` adalah `Yes` dan `No`
16. Tutup daftar pilihan dengan Escape

### Evidence Assign
17. Tampilkan Area utama dengan kondisi K1
18. Verifikasi `Photo at start` bernilai `ON` pada bagian `Evidence`
19. Verifikasi `Photo at end` bernilai `ON` pada bagian `Evidence`

### Approval Assign
20. Tampilkan Area utama dengan kondisi K1
21. Verifikasi `Require approval` bernilai `OFF`
22. Nyalakan `Require approval`
23. Verifikasi `Require approval` bernilai `ON`
24. Verifikasi `Approval type` bernilai `Any one approver`
25. Buka daftar pilihan `Approval type`
26. Verifikasi pilihan `Approval type` adalah `Any one approver` dan `All approvers (AND)`
27. Tutup daftar pilihan dengan Escape

### Reminders dan Notifications Assign
28. Tampilkan Area utama dengan kondisi K1
29. Verifikasi `Transaction timeout` bernilai `7`
30. Verifikasi `Send email notifications` bernilai `OFF`

### Reset to Default mengembalikan field tab Assign ke nilai awal
31. Tampilkan Area utama dengan kondisi K2
32. Verifikasi `Allowed assignee: Division` bernilai `OFF`
33. Verifikasi `Need recipient confirmation` bernilai `No`
34. Verifikasi `Require approval` bernilai `ON`
35. Verifikasi `Send email notifications` bernilai `ON`
36. Klik `Reset to Default`
37. Verifikasi `Allowed assignee: Division` kembali ke nilai awal `ON`
38. Verifikasi `Need recipient confirmation` kembali ke nilai awal `Yes`
39. Verifikasi `Require approval` kembali ke nilai awal `OFF`
40. Verifikasi `Send email notifications` kembali ke nilai awal `OFF`

### Reset to Default mengembalikan Evidence dan Approval type Assign ke nilai awal
41. Tampilkan Area utama dengan kondisi K2
42. Verifikasi `Photo at start` bernilai `OFF` pada bagian `Evidence`
43. Verifikasi `Photo at end` bernilai `OFF` pada bagian `Evidence`
44. Verifikasi `Approval type` bernilai `All approvers (AND)`
45. Klik `Reset to Default`
46. Verifikasi `Photo at start` kembali ke nilai awal `ON` pada bagian `Evidence`
47. Verifikasi `Photo at end` kembali ke nilai awal `ON` pada bagian `Evidence`
48. Nyalakan `Require approval`
49. Verifikasi `Approval type` kembali ke nilai awal `Any one approver`

### Satuan field angka tab Assign
50. Tampilkan Area utama dengan kondisi K1
51. Verifikasi addon `Max assets per assignee (concurrent)` menunjukkan satuan `assets`
52. Verifikasi addon `Transaction timeout` menunjukkan satuan `days`

### Auto-approve tidak dirender di tab Assign saat Require approval ON
53. Tampilkan Area utama dengan kondisi K2
54. Verifikasi `Require approval` bernilai `ON`
55. Verifikasi field `Approval type` tampil pada tab `Assign`
56. Verifikasi field `Auto-approve` tidak ada pada tab `Assign` karena tidak dirender

### Teks bantuan label field tab Assign
57. Tampilkan Area utama dengan kondisi K2
58. Pindahkan fokus keyboard ke bantuan label `Allow Assign`
59. Verifikasi teks bantuan label `Allow Assign` tersampaikan berbunyi `Whether this transaction can be made for assets in this category.`
60. Pindahkan fokus keyboard ke bantuan label `Allowed assignee: Employee`
61. Verifikasi teks bantuan label `Allowed assignee: Employee` tersampaikan berbunyi `Allows assets to be assigned to individual employees.`
62. Pindahkan fokus keyboard ke bantuan label `Allowed assignee: Division`
63. Verifikasi teks bantuan label `Allowed assignee: Division` tersampaikan berbunyi `Allows assets to be assigned to a division, with a PIC chosen per transaction.`
64. Pindahkan fokus keyboard ke bantuan label `Max assets per assignee (concurrent)`
65. Verifikasi teks bantuan label `Max assets per assignee (concurrent)` tersampaikan berbunyi `Maximum number of assets one assignee can hold at the same time; 0 means unlimited.`
66. Pindahkan fokus keyboard ke bantuan label `Need recipient confirmation`
67. Verifikasi teks bantuan label `Need recipient confirmation` tersampaikan berbunyi `Requires the assignee to accept responsibility at handover.`
68. Pindahkan fokus keyboard ke bantuan label `Photo at start`
69. Verifikasi teks bantuan label `Photo at start` tersampaikan berbunyi `Requires a camera photo at the first step of the transaction.`
70. Pindahkan fokus keyboard ke bantuan label `Photo at end`
71. Verifikasi teks bantuan label `Photo at end` tersampaikan berbunyi `Requires a camera photo at the last step of the transaction.`
72. Pindahkan fokus keyboard ke bantuan label `Require approval`
73. Verifikasi teks bantuan label `Require approval` tersampaikan berbunyi `Requires approval before the transaction proceeds.`
74. Pindahkan fokus keyboard ke bantuan label `Approval type`
75. Verifikasi teks bantuan label `Approval type` tersampaikan berbunyi `Whether one approver or all approvers must approve.`
76. Pindahkan fokus keyboard ke bantuan label `Transaction timeout`
77. Verifikasi teks bantuan label `Transaction timeout` tersampaikan berbunyi `Days a transaction can wait at a step before it is closed automatically.`
78. Pindahkan fokus keyboard ke bantuan label `Send email notifications`
79. Verifikasi teks bantuan label `Send email notifications` tersampaikan berbunyi `Also sends this transaction's notifications by email.`
