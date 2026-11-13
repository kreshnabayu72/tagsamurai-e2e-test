---
id: TC-FA-FAREG-E2E-113-notifikasi-registrasi-dep-notification
title: "Notifikasi registrasi bagi approver dan pengaju"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-06j, FAREG-LOGIC-21c, §9.8#p1, §9.8#r1, §9.8#r2, EB-NTF-1, EB-XM-2@notification]
smoke: []
dependsOn: ["Notification: notifikasi in-app"]
trace:
  FAREG-LOGIC-06j: [10, 28]
  FAREG-LOGIC-21c: [17, 26, 34, 49, 62, 77, 88, 43, 56, 71, 82, 91]
  §9.8#p1: [7, 15, 19, 41, 69]
  §9.8#r1: [7, 98]
  §9.8#r2: [15, 19, 41, 69, 101]
  EB-NTF-1: [7, 19]
  EB-XM-2@notification: [7, 8]
anchor: [97, 100]
coverage:
  web: automated
---

# Notifikasi registrasi bagi approver dan pengaju

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Notif {runId}`, `Gudang Notif Sebagian {runId}`, `Gudang Notif Kembali {runId}`, `Gudang Notif Tolak {runId}`, `Gudang Notif Batal {runId}`, dan `Gudang Notif Kedaluwarsa {runId}`, pengaju pengajuan.
  - Budi, role Manage asset & TAG dengan capability Update pada node Group `Gudang Notif {runId}`, `Gudang Notif Sebagian {runId}`, `Gudang Notif Kembali {runId}`, `Gudang Notif Tolak {runId}`, `Gudang Notif Batal {runId}`, `Gudang Notif Kedaluwarsa {runId}`, dan `Gudang Notif Otomatis {runId}`, serta Group terkelola `Gudang Notif Sendiri {runId}` dengan capability Update pada node itu, approver.
  - Dewi, role Group Manager dengan Group binaan `Gudang Notif {runId}`, `Gudang Notif Sendiri {runId}`, `Gudang Notif Sebagian {runId}`, `Gudang Notif Kembali {runId}`, `Gudang Notif Tolak {runId}`, `Gudang Notif Batal {runId}`, `Gudang Notif Kedaluwarsa {runId}`, dan `Gudang Notif Otomatis {runId}`, approver lain dan pengaju pengajuan auto-approve.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-113-1: Group `Gudang Notif {runId}`, ada di entitas aktor.
  - DU-113-2: Asset Name `Meja Notif {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-113-3: batch Draft `Gudang Notif {runId}` milik Rina berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `2`.
  - DU-113-4: Group `Gudang Notif Sendiri {runId}`, ada di entitas aktor.
  - DU-113-5: Group `Gudang Notif Sebagian {runId}`, ada di entitas aktor.
  - DU-113-6: Group `Gudang Notif Kembali {runId}`, ada di entitas aktor.
  - DU-113-7: Group `Gudang Notif Tolak {runId}`, ada di entitas aktor.
  - DU-113-8: Group `Gudang Notif Batal {runId}`, ada di entitas aktor.
  - DU-113-9: Group `Gudang Notif Kedaluwarsa {runId}`, ada di entitas aktor.
  - DU-113-10: Group `Gudang Notif Otomatis {runId}`, ada di entitas aktor.
  - DU-113-11: batch Draft `Gudang Notif Sendiri {runId}` milik Budi berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `1`.
  - DU-113-12: batch Draft `Gudang Notif Sebagian {runId}` milik Rina berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `2`.
  - DU-113-13: batch Draft `Gudang Notif Kembali {runId}` milik Rina berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `1`.
  - DU-113-14: batch Draft `Gudang Notif Tolak {runId}` milik Rina berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `1`.
  - DU-113-15: batch Draft `Gudang Notif Batal {runId}` milik Rina berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `1`.
  - DU-113-16: batch Draft `Gudang Notif Kedaluwarsa {runId}` milik Rina berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `1`.
  - DU-113-17: batch Draft `Gudang Notif Otomatis {runId}` milik Dewi berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `1`.
  - DU-113-18: Reason keputusan Budi: `Foto aset buram` untuk aset kedua pengajuan `Gudang Notif Sebagian {runId}`, `Label aset belum terpasang` untuk pengajuan `Gudang Notif Kembali {runId}`, dan `Aset ganda dengan pengajuan lain` untuk pengajuan `Gudang Notif Tolak {runId}`.
- Kondisi:
  - approval registrasi pada Group `Gudang Notif {runId}`, `Gudang Notif Sendiri {runId}`, `Gudang Notif Sebagian {runId}`, `Gudang Notif Kembali {runId}`, `Gudang Notif Tolak {runId}`, `Gudang Notif Batal {runId}`, `Gudang Notif Kedaluwarsa {runId}`, dan `Gudang Notif Otomatis {runId}` bernilai ON.
  - sisa kuota Group dan tenant mencukupi untuk seluruh aset pengajuan.

## Test Steps

### Submit memicu notifikasi actionable bagi approver dan tidak bagi pengaju
1. Rina mencatat jumlah notifikasi actionable di panel notifikasinya
2. Rina mengetik Search `Gudang Notif {runId}`, menekan Enter
3. Rina klik row action `Edit` pada baris batch `Gudang Notif {runId}`
4. Rina klik `[Submit]`
5. Rina klik `[Submit for Approval]`
6. Budi membuka panel notifikasi
7. Verifikasi notifikasi actionable dari pengajuan `Gudang Notif {runId}` tampil bagi Budi dengan tombol `[Detail]`
8. Verifikasi notifikasi actionable yang sama tampil bagi Dewi
9. Rina membuka panel notifikasinya
10. Verifikasi jumlah notifikasi actionable Rina sama dengan jumlah yang dicatat

### Keputusan approver menandai notifikasi approver lain sebagai Read
11. Budi klik `[Detail]` pada notifikasi pengajuan `Gudang Notif {runId}`
12. Budi klik `[Submit]` pada halaman Approval
13. Budi klik `[Submit]` pada dialog `Submit Approval`
14. Rina membuka panel notifikasinya
15. Verifikasi notifikasi hasil keputusan pengajuan `Gudang Notif {runId}` tampil bagi Rina
16. Dewi membuka panel notifikasi
17. Verifikasi notifikasi actionable pengajuan `Gudang Notif {runId}` milik Dewi berstatus Read
18. Rina membuka notifikasi hasil keputusan
19. Verifikasi notifikasi hasil keputusan Rina hanya memiliki tombol `[Mark as Read]`

### Pengaju pemegang hak putus tidak menerima notifikasi actionable atas pengajuannya sendiri
20. Budi mencatat jumlah notifikasi actionable di panel notifikasinya
21. Budi mengetik Search `Gudang Notif Sendiri {runId}`, menekan Enter
22. Budi klik row action `Edit` pada baris batch `Gudang Notif Sendiri {runId}`
23. Budi klik `[Submit]`
24. Budi klik `[Submit for Approval]`
25. Dewi membuka panel notifikasi
26. Verifikasi notifikasi actionable dari pengajuan `Gudang Notif Sendiri {runId}` milik Dewi berstatus Unread
27. Budi membuka panel notifikasinya
28. Verifikasi jumlah notifikasi actionable Budi sama dengan jumlah yang dicatat

### Partially Approved menandai notifikasi approver lain sebagai Read
29. Rina mengetik Search `Gudang Notif Sebagian {runId}`, menekan Enter
30. Rina klik row action `Edit` pada baris batch `Gudang Notif Sebagian {runId}`
31. Rina klik `[Submit]`
32. Rina klik `[Submit for Approval]`
33. Dewi membuka panel notifikasi
34. Verifikasi notifikasi actionable dari pengajuan `Gudang Notif Sebagian {runId}` milik Dewi berstatus Unread
35. Budi klik `[Detail]` pada notifikasi pengajuan `Gudang Notif Sebagian {runId}`
36. Budi mengubah Decision aset kedua menjadi `Reject`
37. Budi mengisi Reason aset kedua dengan `Foto aset buram`
38. Budi klik `[Submit]` pada halaman Approval
39. Budi klik `[Submit]` pada dialog `Submit Approval`
40. Rina membuka panel notifikasinya
41. Verifikasi notifikasi hasil keputusan pengajuan `Gudang Notif Sebagian {runId}` dengan status `Partially Approved` tampil bagi Rina
42. Dewi membuka panel notifikasi
43. Verifikasi notifikasi actionable pengajuan `Gudang Notif Sebagian {runId}` milik Dewi berstatus Read

### Return to Draft menandai notifikasi approver lain sebagai Read
44. Rina mengetik Search `Gudang Notif Kembali {runId}`, menekan Enter
45. Rina klik row action `Edit` pada baris batch `Gudang Notif Kembali {runId}`
46. Rina klik `[Submit]`
47. Rina klik `[Submit for Approval]`
48. Dewi membuka panel notifikasi
49. Verifikasi notifikasi actionable dari pengajuan `Gudang Notif Kembali {runId}` milik Dewi berstatus Unread
50. Budi klik `[Detail]` pada notifikasi pengajuan `Gudang Notif Kembali {runId}`
51. Budi mengubah Decision aset menjadi `Return to Draft`
52. Budi mengisi Reason aset dengan `Label aset belum terpasang`
53. Budi klik `[Submit]` pada halaman Approval
54. Budi klik `[Submit]` pada dialog `Submit Approval`
55. Dewi membuka panel notifikasi
56. Verifikasi notifikasi actionable pengajuan `Gudang Notif Kembali {runId}` milik Dewi berstatus Read

### Reject menandai notifikasi approver lain sebagai Read
57. Rina mengetik Search `Gudang Notif Tolak {runId}`, menekan Enter
58. Rina klik row action `Edit` pada baris batch `Gudang Notif Tolak {runId}`
59. Rina klik `[Submit]`
60. Rina klik `[Submit for Approval]`
61. Dewi membuka panel notifikasi
62. Verifikasi notifikasi actionable dari pengajuan `Gudang Notif Tolak {runId}` milik Dewi berstatus Unread
63. Budi klik `[Detail]` pada notifikasi pengajuan `Gudang Notif Tolak {runId}`
64. Budi mengubah Decision aset menjadi `Reject`
65. Budi mengisi Reason aset dengan `Aset ganda dengan pengajuan lain`
66. Budi klik `[Submit]` pada halaman Approval
67. Budi klik `[Submit]` pada dialog `Submit Approval`
68. Rina membuka panel notifikasinya
69. Verifikasi notifikasi hasil keputusan pengajuan `Gudang Notif Tolak {runId}` dengan status `Rejected` tampil bagi Rina
70. Dewi membuka panel notifikasi
71. Verifikasi notifikasi actionable pengajuan `Gudang Notif Tolak {runId}` milik Dewi berstatus Read

### Cancel oleh pengaju menandai notifikasi approver lain sebagai Read
72. Rina mengetik Search `Gudang Notif Batal {runId}`, menekan Enter
73. Rina klik row action `Edit` pada baris batch `Gudang Notif Batal {runId}`
74. Rina klik `[Submit]`
75. Rina klik `[Submit for Approval]`
76. Dewi membuka panel notifikasi
77. Verifikasi notifikasi actionable dari pengajuan `Gudang Notif Batal {runId}` milik Dewi berstatus Unread
78. Rina membuka Fixed Asset > Assets > Registration > Waiting for Approval
79. Rina klik row action `Cancel registration` pada baris pengajuan `Gudang Notif Batal {runId}`
80. Rina klik `[Cancel Registration]` pada dialog `Cancel Registration`
81. Dewi membuka panel notifikasi
82. Verifikasi notifikasi actionable pengajuan `Gudang Notif Batal {runId}` milik Dewi berstatus Read

### Auto-cancel sistem menandai notifikasi approver lain sebagai Read
83. Rina mengetik Search `Gudang Notif Kedaluwarsa {runId}`, menekan Enter
84. Rina klik row action `Edit` pada baris batch `Gudang Notif Kedaluwarsa {runId}`
85. Rina klik `[Submit]`
86. Rina klik `[Submit for Approval]`
87. Dewi membuka panel notifikasi
88. Verifikasi notifikasi actionable dari pengajuan `Gudang Notif Kedaluwarsa {runId}` milik Dewi berstatus Unread
89. Waktu berlalu melewati Approval Timeout platform tanpa keputusan atas pengajuan `Gudang Notif Kedaluwarsa {runId}`, sehingga sistem membatalkannya otomatis
90. Dewi membuka panel notifikasi
91. Verifikasi notifikasi actionable pengajuan `Gudang Notif Kedaluwarsa {runId}` milik Dewi berstatus Read

### Pengajuan auto-approve tidak memicu notifikasi approver maupun hasil keputusan
92. Dewi mengetik Search `Gudang Notif Otomatis {runId}`, menekan Enter
93. Dewi klik row action `Edit` pada baris batch `Gudang Notif Otomatis {runId}`
94. Dewi klik `[Submit]`
95. Dewi klik `[Submit for Approval]`
96. Budi membuka panel notifikasinya
97. Verifikasi notifikasi dari pengajuan `Gudang Notif {runId}` tampil di panel notifikasi Budi
98. Verifikasi tidak ada notifikasi `registration_waiting_approval` dari pengajuan `Gudang Notif Otomatis {runId}` di panel notifikasi Budi
99. Dewi membuka panel notifikasinya
100. Verifikasi notifikasi dari pengajuan `Gudang Notif {runId}` tampil di panel notifikasi Dewi
101. Verifikasi tidak ada notifikasi `registration_resolved` dari pengajuan `Gudang Notif Otomatis {runId}` di panel notifikasi Dewi
