---
id: TC-FA-FATR-E2E-131-plan-transfer-approval-scope
title: "Level Feature Suite Transfer Basic mengunci Approval scope, In-transit overdue after, dan Photo at end"
layer: ui-e2e
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: [FATR-LOGIC-18b, FATR-LOGIC-18d, FATR-LOGIC-18e, FATR-LOGIC-18f, FATR-LOGIC-18l, S-23a, EC-73, FLD-30d, FLD-36r, OVR-COL-TGT-d, OVR-COL-TGT-m, AU-TOOLTIP-f, §9.10.4#b1, FLD-15, FLD-23, FATR-LOGIC-18m, FATR-LOGIC-18n, FATR-LOGIC-18o, FATR-LOGIC-18p, FATR-LOGIC-18q, FATR-LOGIC-18t, FLD-23e, S-23b]
smoke: [FATR-LOGIC-18d, S-23a, FLD-30d]
dependsOn: []
trace:
  FATR-LOGIC-18b: [11, 25]
  FATR-LOGIC-18d: [11, 33]
  FATR-LOGIC-18e: [12, 34, 36]
  FATR-LOGIC-18f: [15, 16]
  FATR-LOGIC-18l: [42, 43, 44, 45]
  S-23a: [11, 12, 13, 14, 17]
  EC-73: [11, 12, 20, 21, 22, 25, 26, 27]
  FLD-30d: [11, 13, 14]
  FLD-36r: [25, 26, 27, 67, 68, 69, 70]
  OVR-COL-TGT-d: [19, 63]
  OVR-COL-TGT-m: [20, 21, 22]
  AU-TOOLTIP-f: [14, 22, 27, 56, 60, 70]
  §9.10.4#b1: [11, 12, 14, 25, 34, 53, 57, 67, 68]
  FLD-15: [53, 54, 55, 56, 63, 64, 67, 75, 78]
  FLD-23: [57, 58, 59, 60, 63, 64, 68, 76, 78]
  FATR-LOGIC-18m: [53, 54, 55, 56]
  FATR-LOGIC-18n: [57, 58, 59, 60]
  FATR-LOGIC-18o: [54, 58, 75, 76]
  FATR-LOGIC-18p: [55, 56, 59, 60]
  FATR-LOGIC-18q: [63, 64, 67, 68, 69, 70, 78]
  FATR-LOGIC-18t: [61]
  FLD-23e: [57, 58, 59, 60]
  S-23b: [53, 55, 56, 57, 59, 60]
anchor: [3, 4]
coverage:
  web: automated
---

# Level Feature Suite Transfer Basic mengunci Approval scope, In-transit overdue after, dan Photo at end

## Prerequisites
- Aktor: Total Control (Rina Wulandari {runId}). Operator Admin Console memicu perubahan level plan dan toggle Approval Workflow entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-131-1: Entitas `Entitas Plan Transfer Scope {runId}`, entitas khusus yang tidak dipakai spec lain, level Feature Suite Transfer `Full` dan Approval Workflow `ON`. Company default tab Transfer pada All categories menyimpan Require approval `ON`, Approval scope `Both`, Destination scope `Any Group`, Destination quota check `ON`, In-transit overdue after `7`, dan Photo at end `ON`.
  - DU-131-2: Override dengan Scope `Group`, Target `Workshop {runId}`, Overridden `Approval scope (Destination only)`, `In-transit overdue after (3)`, dan `Photo at end (OFF)`, Category `All categories`, transaksi `Transfer`, Created By `Rina Wulandari {runId}`.
  - DU-131-3: Group `Workshop {runId}` ada di entitas ini.

## Test Steps

### Level Full: Approval scope dapat diubah dan override tampil
1. Klik `All categories` pada Sidebar Category Tree
2. Klik tab `Transfer`
3. Verifikasi kontrol `Approval scope` aktif
4. Verifikasi `Approval scope` bernilai `Both`
5. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
6. Verifikasi baris override dengan Target `Workshop {runId}` memuat Overridden `Approval scope (Destination only)`

### Level Basic mengunci Approval scope dan nilai tersimpan dipertahankan
7. Operator mengubah level Feature Suite Transfer entitas menjadi `Basic`
8. Muat ulang halaman
9. Klik `All categories` pada Sidebar Category Tree
10. Klik tab `Transfer`
11. Verifikasi kontrol `Approval scope` disabled
12. Verifikasi `Approval scope` tetap bernilai `Both`
13. Arahkan pointer ke kontrol `Approval scope` yang disabled
14. Verifikasi alasan `Available on plans with full Transfer.` tersampaikan pada kontrol `Approval scope` yang disabled
15. Verifikasi kontrol `Destination scope` aktif
16. Verifikasi kontrol `Destination quota check` aktif
17. Verifikasi Alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tidak ada

### Override Approval scope tidak berlaku pada Basic
18. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
19. Verifikasi baris override dengan Target `Workshop {runId}` tetap memuat Overridden `Approval scope (Destination only)`
20. Verifikasi sel Target baris `Workshop {runId}` memuat Badge `Not applied`
21. Arahkan pointer ke Badge `Not applied` pada baris `Workshop {runId}`
22. Verifikasi alasan `Available on plans with full Transfer.` tersampaikan pada Badge `Not applied`

### Opsi Approval scope di Dialog Add override disabled
23. Klik `[+ Override]`
24. Klik select Field pada baris Field + Value pertama
25. Verifikasi opsi `Approval scope` disabled
26. Arahkan pointer ke opsi `Approval scope`
27. Verifikasi alasan `Available on plans with full Transfer.` tersampaikan pada opsi `Approval scope` yang disabled
28. Verifikasi opsi `Destination scope` tidak disabled
29. Klik `✕` pada Dialog Add override, form belum diubah

### Upgrade ke Full: Approval scope aktif kembali dengan nilai tersimpan
30. Operator mengubah level Feature Suite Transfer entitas menjadi `Full`
31. Muat ulang halaman
32. Klik `All categories` pada Sidebar Category Tree, lalu klik tab `Transfer`
33. Verifikasi kontrol `Approval scope` aktif
34. Verifikasi `Approval scope` bernilai `Both`
35. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
36. Verifikasi sel Target baris `Workshop {runId}` tidak memuat Badge `Not applied`

### Approval Workflow tidak tersedia pada Transfer Basic: tooltip Approval Workflow yang tampil
37. Operator mengubah level Feature Suite Transfer entitas menjadi `Basic`
38. Operator mematikan toggle Approval Workflow pada plan entitas
39. Muat ulang halaman
40. Klik `All categories` pada Sidebar Category Tree, lalu klik tab `Transfer`
41. Verifikasi Alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil di bagian `Approval`
42. Verifikasi kontrol `Approval scope` disabled
43. Arahkan pointer ke kontrol `Approval scope` yang disabled
44. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada kontrol `Approval scope` yang disabled
45. Verifikasi alasan `Available on plans with full Transfer.` tidak tersampaikan pada kontrol `Approval scope`

### Pemulihan: Full dengan Approval Workflow ON
46. Operator menyalakan kembali toggle Approval Workflow dan mengubah level Feature Suite Transfer entitas menjadi `Full`
47. Muat ulang halaman
48. Klik `All categories` pada Sidebar Category Tree, lalu klik tab `Transfer`
49. Verifikasi kontrol `Approval scope` aktif dan bernilai `Both`

### Basic mengunci In-transit overdue after dan Photo at end sel Transfer
50. Operator mengubah level Feature Suite Transfer entitas menjadi `Basic`
51. Muat ulang halaman
52. Klik `All categories` pada Sidebar Category Tree, lalu klik tab `Transfer`
53. Verifikasi kontrol `In-transit overdue after` disabled
54. Verifikasi `In-transit overdue after` tetap bernilai `7`
55. Arahkan pointer ke kontrol `In-transit overdue after` yang disabled
56. Verifikasi alasan `Available on plans with full Transfer.` tersampaikan pada kontrol `In-transit overdue after` yang disabled
57. Verifikasi kontrol `Photo at end` disabled
58. Verifikasi `Photo at end` tetap bernilai `ON`
59. Arahkan pointer ke kontrol `Photo at end` yang disabled
60. Verifikasi alasan `Available on plans with full Transfer.` tersampaikan pada kontrol `Photo at end` yang disabled
61. Verifikasi kontrol `Destination quota check` aktif
62. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
63. Verifikasi baris override dengan Target `Workshop {runId}` tetap memuat Overridden `In-transit overdue after (3)` dan `Photo at end (OFF)`
64. Verifikasi sel Target baris `Workshop {runId}` memuat Badge `Not applied`
65. Klik `[+ Override]`
66. Klik select Field pada baris Field + Value pertama
67. Verifikasi opsi `In-transit overdue after` disabled
68. Verifikasi opsi `Photo at end` disabled
69. Arahkan pointer ke opsi `Photo at end`
70. Verifikasi alasan `Available on plans with full Transfer.` tersampaikan pada opsi `Photo at end` yang disabled
71. Klik `✕` pada Dialog Add override, form belum diubah

### Upgrade ke Full: In-transit overdue after dan Photo at end aktif kembali dengan nilai tersimpan
72. Operator mengubah level Feature Suite Transfer entitas menjadi `Full`
73. Muat ulang halaman
74. Klik `All categories` pada Sidebar Category Tree, lalu klik tab `Transfer`
75. Verifikasi kontrol `In-transit overdue after` aktif dan bernilai `7`
76. Verifikasi kontrol `Photo at end` aktif dan bernilai `ON`
77. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
78. Verifikasi sel Target baris `Workshop {runId}` tidak memuat Badge `Not applied`
