---
id: TC-FA-ASSIGN-E2E-049-plan-level-basic
title: "Feature Suite Assignment level Basic"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.10#b1", "§9.10#b3", "§9.10#b4", "§9.10#b5", "§9.10#b6", "§9.10#r33", "§9.10#r34", "§9.10#r35", "§9.10#r36", "§9.10#p12", "EC-ASG-36", "EC-ASG-99", "EC-ASG-107", "EC-ASG-109", "EC-ASG-112", "EC-ASG-115", "EC-ASG-56", "S-ASG-06", "ASSIGN-LOGIC-06t", "ASSIGN-LOGIC-06x", "ASSIGN-LOGIC-18n"]
smoke: []
dependsOn: []
trace:
  "§9.10#b1": [10, 21, 25, 28, 32, 36, 38]
  "§9.10#b3": [53, 58, 59]
  "§9.10#b4": 34
  "§9.10#b5": [25, 28, 30, 40, 43, 45, 47]
  "§9.10#b6": [8, 11, 14, 90, 91, 94]
  "§9.10#r33": [68, 106]
  "§9.10#r34": [62, 65, 106]
  "§9.10#r35": 72
  "§9.10#r36": [75, 80, 87, 99, 101]
  "§9.10#p12": 108
  "EC-ASG-36": [68, 75, 99, 101, 106]
  "EC-ASG-99": [4, 40, 68, 106]
  "EC-ASG-107": [45, 47]
  "EC-ASG-109": 53
  "EC-ASG-112": [8, 11, 14, 90, 91, 94]
  "EC-ASG-115": [80, 81, 83, 87]
  "EC-ASG-56": [58, 59]
  "S-ASG-06": 10
  "ASSIGN-LOGIC-06t": [8, 14, 90]
  "ASSIGN-LOGIC-06x": [11, 14, 80, 87]
  "ASSIGN-LOGIC-18n": [40, 43, 68, 106]
anchor: [9, 13, 39, 42, 52, 67, 86, 93, 104]
coverage:
  web: automated
---

# Feature Suite Assignment level Basic

## Prerequisites
- Aktor: Total Control `Wulan Hartati {runId}` (DU-049-2) di entitas khusus DU-049-1 yang tidak dipakai spec lain, kecuali kelompok pertama yang dikerjakan pembuat Draft `Rina Wijaya {runId}` (DU-049-16)
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-049-1: Entitas (Entitas khusus dengan Feature Suite Assignment level Basic), Name `Entitas Basic {runId}`, Level Feature Suite Assignment `Basic`, Level sebelumnya `Full`
  - DU-049-2: User (Aktor Total Control), Name `Wulan Hartati {runId}`, Role `Total Control`, Cakupan `Seluruh client`
  - DU-049-3: User (Assignee Employee), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-049-4: User (Anggota Division pengganti PIC), Name `Sari Dewi {runId}`, Role `tanpa role Assignment`
  - DU-049-5: Group (Group utama), Name `Head Office {runId}`
  - DU-049-6: Group (Group cabang), Name `Branch Surabaya {runId}`
  - DU-049-7: Division (Division dengan PIC nonaktif), Name `Finance {runId}`, PIC `Dedi Hartono {runId}`, Status PIC `Nonaktif`, Anggota lain `Sari Dewi {runId}`
  - DU-049-8: Asset (Aset tersedia untuk form), Name `Laptop Dell Latitude 5420 {runId}`, Group `Head Office {runId}`, Status `Available`
  - DU-049-9: Asset (Aset tersedia untuk form di Group lain), Name `Monitor LG 24 {runId}`, Group `Branch Surabaya {runId}`, Status `Available`
  - DU-049-10: Assignment (ASG Waiting for Handover yang dibuat saat level Full), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-049-11: Assignment (ASG Division berjalan dengan No PIC sesudah turun ke Basic), Assignee `Finance {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Projector Epson EB-X49 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Dedi Hartono {runId}`, Penanda `No PIC`
  - DU-049-12: Assignment (ASG Assigned berjalan), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Camera Sony A7 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-049-13: Assignment (ASG Waiting for Handover yang melewati Transaction timeout), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Server Dell R740 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-049-14: Assignment (ASG Waiting for Approval yang ditutup sistem saat Approval Workflow dicabut pada T-0), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Tablet Samsung Tab S8 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Hendra Wijaya {runId}`
  - DU-049-15: Assignment (Pengajuan yang dibuat dari form), Assignee `Budi Santoso {runId}`, Aset 1 `Laptop Dell Latitude 5420 {runId}`, Aset 2 `Monitor LG 24 {runId}`, Purpose `Dipakai tim operasional lapangan`, Status `Waiting for Handover`
  - DU-049-16: User (Pembuat Draft yang tidak mengajukan ASG), Name `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`
  - DU-049-17: Draft (Draft Employee yang ada sebelum T-0), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Webcam Logitech C920 {runId}`, Origin `New`, Modified By `Rina Wijaya {runId}`
  - DU-049-18: Draft (Draft Division yang ada sebelum T-0), Assignee `Finance {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, PIC `Sari Dewi {runId}`, Aset `Whiteboard Digital Samsung {runId}`, Origin `New`, Modified By `Rina Wijaya {runId}`
  - DU-049-19: Division (Division dengan PIC aktif), Name `Operations {runId}`, PIC `Gita Permata {runId}`, Anggota lain `Bima Nugroho {runId}`
  - DU-049-20: Assignment (ASG Division Assigned berjalan), Assignee `Operations {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Assigned`, Aset `Excavator Komatsu PC200 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Gita Permata {runId}`
  - DU-049-21: User (Approver aset DU-049-14), Name `Hendra Wijaya {runId}`, Role `Approver`, Cakupan `Group penugasan Head Office {runId}`
- Kondisi:
  - Feature Suite Assignment berada pada level `Full` sebelum T-0 dan turun ke level `Basic` pada T-0
  - Draft DU-049-17 dan DU-049-18 ada sebelum T-0
  - Akun `Rina Wijaya {runId}` aktif, dan kredensialnya disediakan fase 2
  - Approval Workflow dicabut oleh plan pada T-0, sehingga pengajuan `Waiting for Approval` aset `Tablet Samsung Tab S8 {runId}` ditutup `Canceled` oleh `System`
  - Transaction timeout untuk ASG yang memuat aset `Server Dell R740 {runId}` terlampaui

## Test Steps

### Draft yang ada sebelum T-0 dihapus tanpa notifikasi
1. Masuk sebagai pembuat Draft `Rina Wijaya {runId}`
2. Catat jumlah notifikasi pada Bell icon aktor
3. Downgrade plan entitas dari level `Full` ke level `Basic` berjalan di T-0
4. Verifikasi jumlah notifikasi pada Bell icon aktor tetap sama sesudah Draft yang ada sebelum T-0 dihapus
5. Masuk sebagai Total Control `Wulan Hartati {runId}`

### Form Assignment Request level Basic tanpa Save Draft
6. Klik menu `Transactions > Assignment`
7. Klik `[+ Assign]`
8. Verifikasi form `Assignment Request` terbuka langsung dengan Assignee Type `Employee` tanpa overlay `Assign to`
9. Verifikasi tombol `[Submit]` tampil
10. Verifikasi tombol `[Save Draft]` tidak tampil
11. Verifikasi field PIC tidak tampil
12. Klik `[Select Assignee]`
13. Verifikasi dialog Select Assignee memuat daftar Employees dengan `Budi Santoso {runId}`
14. Verifikasi sub-tab `Divisions` tidak tampil pada dialog Select Assignee
15. Pilih `Budi Santoso {runId}` pada daftar Employees
16. Klik `[Select]`
17. Klik `[+ Asset]`
18. Centang aset `Laptop Dell Latitude 5420 {runId}`
19. Centang aset `Monitor LG 24 {runId}`
20. Klik `[Select]`
21. Verifikasi aset `Laptop Dell Latitude 5420 {runId}` dengan Group `Head Office {runId}` dan aset `Monitor LG 24 {runId}` dengan Group `Branch Surabaya {runId}` tampil dalam satu form
22. Isi Purpose aset `Laptop Dell Latitude 5420 {runId}` dengan `Dipakai tim operasional lapangan`
23. Isi Purpose aset `Monitor LG 24 {runId}` dengan `Dipakai tim operasional lapangan`

### Isian form yang belum dikirim dipulihkan lewat Restore Changes
24. Klik `[Cancel]` pada form
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`
27. Klik `[+ Assign]`
28. Verifikasi dialog `Restore Changes` tampil dengan teks `You have unsaved changes from your last visit. Do you want to restore them?`
29. Klik `[Restore]`
30. Verifikasi aset `Laptop Dell Latitude 5420 {runId}` dan aset `Monitor LG 24 {runId}` kembali tampil di form beserta Purpose `Dipakai tim operasional lapangan`

### Submit memecah pengajuan multi-Group
31. Klik `[Submit]`
32. Verifikasi dialog `Submit Assignment` menyebut dua assignment, satu untuk Group `Head Office {runId}` dan satu untuk Group `Branch Surabaya {runId}`
33. Klik `[Submit]` pada dialog
34. Verifikasi toast `Success, 2 assignments have been submitted.` tampil
35. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
36. Verifikasi ASG dengan Group `Head Office {runId}` memuat aset `Laptop Dell Latitude 5420 {runId}`
37. Ganti isi kotak Search dengan `Monitor LG 24 {runId}`, tekan Enter
38. Verifikasi ASG dengan Group `Branch Surabaya {runId}` memuat aset `Monitor LG 24 {runId}`

### Tab Drafts dan sub-tab By Assignee tidak ada
39. Verifikasi tab `Transactions`, `Assigned Assets`, dan `History` tampil
40. Verifikasi tab `Drafts` tidak tampil
41. Klik tab `Assigned Assets`
42. Verifikasi sub-tab `By Asset` tampil
43. Verifikasi sub-tab `By Assignee` tidak tampil
44. Buka alamat halaman Assignment dengan `?tab=drafts`
45. Verifikasi tab `Transactions` yang aktif
46. Buka alamat halaman Assignment dengan `?view=assignee`
47. Verifikasi sub-tab `By Asset` yang aktif

### Cancel Assignment tanpa Save as Draft to edit
48. Klik menu `Transactions > Assignment`
49. Ketik Search `Printer HP M404 {runId}`, tekan Enter
50. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
51. Klik `Cancel Assignment`
52. Verifikasi dialog `Cancel Assignment` tampil
53. Verifikasi checkbox `Save as Draft to edit` tidak tampil
54. Klik `[Go Back]`

### Timeout ditutup Canceled tanpa Draft baru
55. Job Transaction timeout berjalan untuk ASG yang memuat aset `Server Dell R740 {runId}`
56. Klik tab `History`
57. Ketik Search `Server Dell R740 {runId}`, tekan Enter
58. Verifikasi baris aset `Server Dell R740 {runId}` berstatus `Canceled` dengan alasan `Not handed over`
59. Verifikasi tab `Drafts` tetap tidak tampil

### ASG yang berjalan sesudah turun ke Basic
60. Klik tab `History`
61. Ketik Search `Tablet Samsung Tab S8 {runId}`, tekan Enter
62. Verifikasi baris aset `Tablet Samsung Tab S8 {runId}` berstatus `Canceled` dengan alasan `Approval Workflow removed`
63. Buka menu ⋯ pada baris aset `Tablet Samsung Tab S8 {runId}`
64. Klik `Assignment Log`
65. Verifikasi node `Canceled by System` tampil pada Assignment Log
66. Tutup dialog Assignment Log
67. Verifikasi tab `Transactions`, `Assigned Assets`, dan `History` tampil
68. Verifikasi tab `Drafts` tidak tampil sehingga Draft yang ada sebelum turun ke Basic tidak dapat dibuka
69. Klik menu `Transactions > Assignment`
70. Klik tab `Assigned Assets`
71. Ketik Search `Camera Sony A7 {runId}`, tekan Enter
72. Verifikasi aset `Camera Sony A7 {runId}` tampil dan aksi `Unassign` tersedia untuk ASG yang berjalan
73. Klik tab `Transactions`
74. Ketik Search `Projector Epson EB-X49 {runId}`, tekan Enter
75. Verifikasi ASG dengan Assignee `Finance {runId}` berstatus `Waiting for Handover` tetap tampil dengan penanda `No PIC`
76. Buka menu ⋯ pada baris ASG yang memuat aset `Projector Epson EB-X49 {runId}`
77. Klik `Change PIC`
78. Pilih `Sari Dewi {runId}` pada dialog Select User
79. Klik `[Select]`
80. Verifikasi toast sukses Change PIC tampil dengan nama PIC baru `Sari Dewi {runId}`
81. Verifikasi penanda `No PIC` tidak tampil lagi pada ASG itu
82. Buka menu ⋯ pada baris ASG yang memuat aset `Projector Epson EB-X49 {runId}`
83. Verifikasi aksi `Hand Over` tampil dan aktif
84. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
85. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
86. Verifikasi aksi `Hand Over` tampil
87. Verifikasi aksi `Change PIC` tidak tampil pada ASG Employee

### Quick Action Assign pada level Basic
88. Klik Quick Action pada navbar
89. Klik `Assign`
90. Verifikasi form `Assignment Request` terbuka dari Quick Action langsung dengan Assignee Type `Employee` tanpa overlay `Assign to`
91. Verifikasi field PIC tidak tampil pada form dari Quick Action
92. Klik `[Select Assignee]`
93. Verifikasi dialog Select Assignee dari Quick Action memuat daftar Employees dengan `Budi Santoso {runId}`
94. Verifikasi sub-tab `Divisions` tidak tampil pada dialog Select Assignee dari Quick Action
95. Klik `[Cancel]` pada dialog Select Assignee
96. Klik `[Cancel]` pada form yang belum diubah

### ASG Assignee Division yang sudah Assigned lanjut normal pada Basic
97. Klik menu `Transactions > Assignment`
98. Ketik Search `Excavator Komatsu PC200 {runId}`, tekan Enter
99. Verifikasi ASG dengan Assignee `Operations {runId}` berstatus `Assigned` tampil pada daftar
100. Buka menu ⋯ pada baris ASG yang memuat aset `Excavator Komatsu PC200 {runId}`
101. Verifikasi aksi `Unassign` tampil dan aktif untuk ASG Division yang berjalan

### Upgrade kembali ke Full tidak memulihkan Draft dan tidak membuat Draft baru
102. Upgrade plan entitas kembali ke level `Full`
103. Klik menu `Transactions > Assignment`
104. Verifikasi tab `Drafts` tampil
105. Klik tab `Drafts`
106. Verifikasi tab `Drafts` menampilkan `No drafts` sehingga Draft yang ada sebelum T-0 tidak dipulihkan dan penutupan ASG oleh sistem tidak membuat Draft baru

### Perubahan plan bukan perubahan Settings
107. Buka Changelog Transaction Settings
108. Verifikasi tidak ada entri perubahan plan pada Changelog Transaction Settings
