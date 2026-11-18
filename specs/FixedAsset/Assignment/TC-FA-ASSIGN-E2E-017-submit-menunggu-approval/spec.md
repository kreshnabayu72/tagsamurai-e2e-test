---
id: TC-FA-ASSIGN-E2E-017-submit-menunggu-approval
title: "Submit dengan Require approval ON dan campuran ON/OFF"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["TS-ASG-04", "TS-ASG-05", "EC-ASG-09", "F-ASSIGN-03.k3"]
smoke: []
dependsOn: []
trace:
  "TS-ASG-04": [15, 63]
  "TS-ASG-05": [33, 81]
  "EC-ASG-09": [34, 35, 37]
  "F-ASSIGN-03.k3": [16, 17, 36, 38, 41, 42, 46]
anchor: []
coverage:
  web: automated
---

# Submit dengan Require approval ON dan campuran ON/OFF

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office` dan `Grup Approver Ganda {runId}`.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-017-1: Aset `Toyota Avanza {runId}`, Category `Vehicle`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-017-2: Aset `Toyota Innova {runId}`, Category `Vehicle`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-017-3: Aset `Toyota Hilux {runId}`, Category `Vehicle`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-017-4: Aset `Laptop Dell Latitude 5420 {runId}`, Category `Laptop`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-017-5: Assignee Employee `Dewi Anggraini` (email `dewi.anggraini@example.com`, Position `Staff`, Division `Finance`), karyawan aktif dengan akun login.
  - DU-017-6: Approver `Rina Wijaya`, pemegang Role Transaksi Approver pada Group `Head Office`, satu-satunya approver untuk aset Category `Vehicle`.
  - DU-017-7: Purpose baris aset `Operasional lapangan` dan `Kerja harian`.
  - DU-017-8: Group `Grup Approver Ganda {runId}` dengan dua approver, `Dimas Prakoso {runId}` dan `Wulan Sari {runId}`, Approval type `Any one`.
  - DU-017-9: Approver `Dimas Prakoso {runId}`, pemegang Role Transaksi Approver pada Group `Grup Approver Ganda {runId}`.
  - DU-017-10: Approver `Wulan Sari {runId}`, pemegang Role Transaksi Approver pada Group `Grup Approver Ganda {runId}`.
  - DU-017-11: Assignee Employee `Bayu Nugroho {runId}` (email `bayu.nugroho@example.com`, Position `Staff`, Division `Finance`), karyawan aktif dengan akun login.
  - DU-017-12: Aset `Toyota Fortuner {runId}`, Category `Vehicle`, Group `Grup Approver Ganda {runId}`, Custody `Available`, Condition `Normal`.
  - DU-017-13: Aset `Toyota Camry {runId}`, Category `Vehicle`, Group `Grup Approver Ganda {runId}`, Custody `Available`, Condition `Normal`.
  - DU-017-14: Aset `Laptop Lenovo ThinkPad T14 {runId}`, Category `Laptop`, Group `Grup Approver Ganda {runId}`, Custody `Available`, Condition `Normal`.
  - DU-017-15: Aset `Laptop Asus ExpertBook B1 {runId}`, Category `Laptop`, Group `Grup Approver Ganda {runId}`, Custody `Available`, Condition `Normal`.
  - DU-017-16: Aset `Toyota Rush {runId}`, Category `Vehicle`, Group `Grup Approver Ganda {runId}`, Custody `Available`, Condition `Normal`.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Require approval bernilai ON untuk Category `Vehicle` dengan Approval type `Any one`, dan OFF untuk Category `Laptop`.

## Test Steps

### Submit semua aset menunggu approval
1. Klik `[+ Assign]`
2. Klik pilihan `Employee`
3. Klik `[Select Assignee]`
4. Pilih baris `Dewi Anggraini` pada dialog Select Assignee
5. Klik `[Select]`
6. Klik `[+ Asset]`
7. Ketik Search `{runId}`, tekan Enter
8. Centang baris `Toyota Avanza {runId}`
9. Centang baris `Toyota Innova {runId}`
10. Klik `[Select]`
11. Isi Purpose baris `Toyota Avanza {runId}` dengan `Operasional lapangan`
12. Isi Purpose baris `Toyota Innova {runId}` dengan `Operasional lapangan`
13. Klik `[Submit]`
14. Klik `[Submit]` pada dialog `Submit Assignment`
15. Verifikasi toast `Success, assignment has been submitted for approval to Rina Wijaya.` tampil
16. Verifikasi status baris `Toyota Avanza {runId}` dan `Toyota Innova {runId}` keduanya `Waiting for Approval`
17. Verifikasi Approval kedua baris `Waiting`

### Submit campuran aset tanpa approval dan aset menunggu approval
18. Buka `Transactions > Assignment`
19. Klik `[+ Assign]`
20. Klik pilihan `Employee`
21. Klik `[Select Assignee]`
22. Pilih baris `Dewi Anggraini` pada dialog Select Assignee
23. Klik `[Select]`
24. Klik `[+ Asset]`
25. Ketik Search `{runId}`, tekan Enter
26. Centang baris `Laptop Dell Latitude 5420 {runId}`
27. Centang baris `Toyota Hilux {runId}`
28. Klik `[Select]`
29. Isi Purpose baris `Laptop Dell Latitude 5420 {runId}` dengan `Kerja harian`
30. Isi Purpose baris `Toyota Hilux {runId}` dengan `Operasional lapangan`
31. Klik `[Submit]`
32. Klik `[Submit]` pada dialog `Submit Assignment`
33. Verifikasi toast `Success, 1 of 2 assets is ready for handover. 1 submitted for approval to Rina Wijaya.` tampil
34. Verifikasi status header ASG `Waiting for Handover` walau satu baris masih menunggu approval
35. Verifikasi status baris `Laptop Dell Latitude 5420 {runId}` `Waiting for Handover`
36. Verifikasi Approval baris `Laptop Dell Latitude 5420 {runId}` `Not required`
37. Verifikasi status baris `Toyota Hilux {runId}` `Waiting for Approval`
38. Verifikasi Approval baris `Toyota Hilux {runId}` `Waiting`

### Assignment Log mencatat pengajuan per baris
39. Klik `⋯` pada baris `Toyota Hilux {runId}`
40. Klik `Assignment Log`
41. Verifikasi node `Assignment requested by [Actor]` tampil pada dialog Assignment Log
42. Verifikasi Approval pada node tersebut `Waiting 1 approver`
43. Klik `✕` pada dialog Assignment Log
44. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
45. Klik `Assignment Log`
46. Verifikasi Approval pada node `Assignment requested by [Actor]` `Not required`
47. Klik `✕` pada dialog Assignment Log

### Submit semua aset menunggu approval dengan penerima tidak tunggal
48. Buka `Transactions > Assignment`
49. Klik `[+ Assign]`
50. Klik pilihan `Employee`
51. Klik `[Select Assignee]`
52. Pilih baris `Bayu Nugroho {runId}` pada dialog Select Assignee
53. Klik `[Select]`
54. Klik `[+ Asset]`
55. Ketik Search `{runId}`, tekan Enter
56. Centang baris `Toyota Fortuner {runId}`
57. Centang baris `Toyota Camry {runId}`
58. Klik `[Select]`
59. Isi Purpose baris `Toyota Fortuner {runId}` dengan `Operasional lapangan`
60. Isi Purpose baris `Toyota Camry {runId}` dengan `Operasional lapangan`
61. Klik `[Submit]`
62. Klik `[Submit]` pada dialog `Submit Assignment`
63. Verifikasi toast `Success, assignment has been submitted for approval.` tampil, tanpa nama penerima karena aset yang menunggu approval punya dua approver, `Dimas Prakoso {runId}` dan `Wulan Sari {runId}`

### Submit campuran dengan lebih dari satu aset siap handover dan penerima tidak tunggal
64. Buka `Transactions > Assignment`
65. Klik `[+ Assign]`
66. Klik pilihan `Employee`
67. Klik `[Select Assignee]`
68. Pilih baris `Bayu Nugroho {runId}` pada dialog Select Assignee
69. Klik `[Select]`
70. Klik `[+ Asset]`
71. Ketik Search `{runId}`, tekan Enter
72. Centang baris `Laptop Lenovo ThinkPad T14 {runId}`
73. Centang baris `Laptop Asus ExpertBook B1 {runId}`
74. Centang baris `Toyota Rush {runId}`
75. Klik `[Select]`
76. Isi Purpose baris `Laptop Lenovo ThinkPad T14 {runId}` dengan `Kerja harian`
77. Isi Purpose baris `Laptop Asus ExpertBook B1 {runId}` dengan `Kerja harian`
78. Isi Purpose baris `Toyota Rush {runId}` dengan `Operasional lapangan`
79. Klik `[Submit]`
80. Klik `[Submit]` pada dialog `Submit Assignment`
81. Verifikasi toast `Success, 2 of 3 assets are ready for handover. 1 submitted for approval.` tampil, tanpa nama penerima karena aset yang menunggu approval punya dua approver
