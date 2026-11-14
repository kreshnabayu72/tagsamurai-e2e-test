---
id: TC-FA-FATR-BE-091-plan
title: "Plan gating di server"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
owner: BE
sourceRules: ["§Aturan Logika Modul#r72", "§Aturan Logika Modul#r73", "§Aturan Logika Modul#r78", "§Aturan Logika Modul#r82", "§Aturan Logika Modul#r84", "§Aturan Logika Modul#r85", "§Aturan Logika Modul#r87", "§Aturan Logika Modul#r91", "§Aturan Logika Modul#r102", "§Aturan Logika Modul#r104", "§Aturan Logika Modul#r107", "§Aturan Logika Modul#r111", "§9.2#b45", "§9.2#b46", "§9.2#b72", "§9.2#b151", "§9.2#b153", "§9.2#b329", "§9.2#b340", "§9.2#b556", "§9.2#b558", "§9.2#b560", "§9.4.2#r25", "§9.4.2#r37", "§9.4.2#r38", "§9.4.2#r54", "§9.4.2#r92", "§9.4.2#r93", "§9.4.3#b2", "§9.4.3#b3", "§9.4.4#r20", "§9.4.4#r23", "§9.4.4#r54", "§9.4.4#r55", "§9.4.4#r56", "§9.4.4#r57", "§9.4.4#r58", "§9.4.4#r59", "§9.10.1#r1", "§9.10.1#r2", "§9.10.1#r3", "§9.10.1#r4", "§9.10.1#r5", "§9.10.1#r6", "§9.10.1#r8", "§9.10.1#b3", "§9.10.1#b4", "§9.10.1#b5", "§9.10.1#b6", "§9.10.1#b9", "§9.10.1#r9", "§9.10.1#r10", "§9.10.1#p10", "§9.10.1#p11", "§9.10.1#p12", "§9.10.2#r1", "§9.10.2#r2", "§9.10.2#r3", "§9.10.2#r4", "§9.10.2#r5", "§9.10.2#r6", "§9.10.2#r7", "§9.10.2#r9", "§9.10.2#b3", "§9.10.2#b4", "§9.10.2#b5", "§9.10.2#b7", "§9.10.2#r10", "§9.10.2#r11", "§9.10.3#r1", "§9.10.3#r2", "§9.10.3#r3", "§9.10.3#r4", "§9.10.3#r5", "§9.10.3#r6", "§9.10.3#r7", "§9.10.3#r9", "§9.10.3#b2", "§9.10.3#b3", "§9.10.3#b4", "§9.10.3#b5", "§9.10.3#b7", "§9.10.4#b2"]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#r72": [5, 6, 38, 64]
  "§Aturan Logika Modul#r73": [38, 40, 41]
  "§Aturan Logika Modul#r78": [43, 44]
  "§Aturan Logika Modul#r82": [7, 8, 12]
  "§Aturan Logika Modul#r84": 70
  "§Aturan Logika Modul#r85": 71
  "§Aturan Logika Modul#r87": 73
  "§Aturan Logika Modul#r91": 77
  "§Aturan Logika Modul#r102": [9, 13, 89]
  "§Aturan Logika Modul#r104": 89
  "§Aturan Logika Modul#r107": 91
  "§Aturan Logika Modul#r111": 95
  "§9.2#b45": 52
  "§9.2#b46": [43, 44, 73, 91]
  "§9.2#b72": 49
  "§9.2#b151": 45
  "§9.2#b153": 39
  "§9.2#b329": 47
  "§9.2#b340": [15, 21]
  "§9.2#b556": 38
  "§9.2#b558": [70, 71]
  "§9.2#b560": 89
  "§9.4.2#r25": 57
  "§9.4.2#r37": 38
  "§9.4.2#r38": [70, 89]
  "§9.4.2#r54": 37
  "§9.4.2#r92": 49
  "§9.4.2#r93": 50
  "§9.4.3#b2": 49
  "§9.4.3#b3": 43
  "§9.4.4#r20": 49
  "§9.4.4#r23": 57
  "§9.4.4#r54": 38
  "§9.4.4#r55": 63
  "§9.4.4#r56": 70
  "§9.4.4#r57": 83
  "§9.4.4#r58": 89
  "§9.4.4#r59": 101
  "§9.10.1#r1": 14
  "§9.10.1#r2": 17
  "§9.10.1#r3": 23
  "§9.10.1#r4": 27
  "§9.10.1#r5": [38, 64]
  "§9.10.1#r6": 31
  "§9.10.1#r8": 42
  "§9.10.1#b3": 49
  "§9.10.1#b4": 55
  "§9.10.1#b5": 45
  "§9.10.1#b6": [58, 60]
  "§9.10.1#b9": [37, 63, 64, 65, 66, 67]
  "§9.10.1#r9": 38
  "§9.10.1#r10": 60
  "§9.10.1#p10": 38
  "§9.10.1#p11": 43
  "§9.10.1#p12": 45
  "§9.10.2#r1": 12
  "§9.10.2#r2": 18
  "§9.10.2#r3": 24
  "§9.10.2#r4": 28
  "§9.10.2#r5": [70, 71]
  "§9.10.2#r6": 72
  "§9.10.2#r7": 72
  "§9.10.2#r9": 32
  "§9.10.2#b3": [77, 78]
  "§9.10.2#b4": [81, 82]
  "§9.10.2#b5": [74, 75]
  "§9.10.2#b7": [83, 85, 86]
  "§9.10.2#r10": 70
  "§9.10.2#r11": 71
  "§9.10.3#r1": 13
  "§9.10.3#r2": 19
  "§9.10.3#r3": 25
  "§9.10.3#r4": 29
  "§9.10.3#r5": 89
  "§9.10.3#r6": 90
  "§9.10.3#r7": 90
  "§9.10.3#r9": 33
  "§9.10.3#b2": 89
  "§9.10.3#b3": [95, 96]
  "§9.10.3#b4": [99, 100]
  "§9.10.3#b5": [92, 93]
  "§9.10.3#b7": [101, 103]
  "§9.10.4#b2": [106, 108, 109, 110]
---
# Plan gating di server

## Prerequisites
- Aktor: Maya Pengelola (DU-091-2), Total Control dengan cakupan seluruh entitas; pemanggil terotorisasi Rudi Integrasi (DU-091-3); dan Operator Plan (DU-091-4), operator Admin Console di luar entitas.
- Data:
  - DU-091-1: Entitas, entitas khusus spec ini, berlangganan plan Paid (rank 2): Name `Entitas Plan {runId}`; Plan `Paid (rank 2)`.
  - DU-091-2: User, pengelola Total Control: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh entitas`.
  - DU-091-3: User, pemanggil terotorisasi yang mengajukan transaksi dan mengirim request langsung: Name `Rudi Integrasi {runId}`; Access Level `Total Control`; Cakupan `seluruh entitas`.
  - DU-091-4: User, operator Admin Console yang mengubah plan entitas: Name `Operator Plan {runId}`; Peran `operator Admin Console di luar entitas`.
  - DU-091-5: Category, Category leaf untuk field approval dan Direct handover: Name `Armada Plan {runId}`.
  - DU-091-6: Category, Category leaf untuk Self service dan Duration unit: Name `Peralatan Plan {runId}`.
  - DU-091-7: Group, Group tempat override penugasan: Name `Workshop {runId}`.
  - DU-091-8: Group, Group tanpa override: Name `Kantor Plan {runId}`.
  - DU-091-9: Group, Group tempat override peminjaman: Name `Gudang Plan {runId}`.
  - DU-091-10: Asset, aset di Group Workshop: Name `Truk Workshop {runId}`; Asset Name `Truk Operasional {runId}`; Category `Armada Plan {runId}`; Group `Workshop {runId}`.
  - DU-091-11: Asset, aset di Group tanpa override: Name `Mesin Kantor {runId}`; Asset Name `Mesin Operasional {runId}`; Category `Armada Plan {runId}`; Group `Kantor Plan {runId}`.
  - DU-091-12: Asset, aset di Group Gudang: Name `Truk Gudang {runId}`; Asset Name `Forklift Gudang {runId}`; Category `Peralatan Plan {runId}`; Group `Gudang Plan {runId}`.
  - DU-091-13 sampai DU-091-16 dibuat Maya Pengelola di grup Setup, dan DU-091-17 sampai DU-091-22 dan DU-091-24 adalah nilai input yang dikirim di grup masing-masing, bukan record yang sudah ada.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Plan {runId}` (DU-091-1) yang tidak dipakai spec lain, karena yang diubah adalah plan dan toggle entitas; Operator Plan mengubah plan lewat Admin Console.
  - Entitas berlangganan plan `Paid (rank 2)` dengan nilai default plan awal: Approval Workflow ON serta Feature Suite Borrowing dan Assignment `Full`.
  - Perubahan toggle Approval Workflow dan level Feature Suite di spec ini dilakukan pada plan kustom `Paket Kustom {runId}` (DU-091-23), plan milik spec ini yang hanya dipakai entitas khusus spec ini, sehingga tidak memengaruhi entitas lain.
  - Allowed assignee: Division bernilai `ON` pada Company default dan Inherit pada Category `Armada Plan {runId}`.
  - Seluruh field Category `Armada Plan {runId}` dan `Peralatan Plan {runId}` bernilai Inherit, dan belum ada override pada kedua Category itu.
  - Tidak ada Role Transaksi Approver yang ditugaskan untuk transaksi peminjaman di Group mana pun pada entitas ini.
  - Jumlah entri Changelog dan Activity Log dibaca sebagai selisih terhadap nilai yang dicatat sebelum aksi.

## Test Steps

### Setup: nilai field bergerbang disimpan saat plan membuka semua field
1. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Require approval transaksi peminjaman nilai sendiri `ON`, Auto-approve `OFF`, Approval type `All approvers (AND)`, Direct handover between holders `Allow`, Max extensions `2`, dan Max assets per assignee (concurrent) transaksi penugasan nilai sendiri `2`
2. Maya Pengelola menyimpan Category `Peralatan Plan {runId}` dengan Self service nilai sendiri `ON`, Duration unit `Hours`, dan Max extensions nilai sendiri `3`
3. Maya Pengelola menambahkan override Group `Workshop {runId}` pada Category `Armada Plan {runId}` untuk transaksi penugasan dengan Require approval `ON` dan Direct handover between holders `Allow`
4. Maya Pengelola menambahkan override Group `Gudang Plan {runId}` pada Category `Peralatan Plan {runId}` untuk transaksi peminjaman dengan Self service `ON` dan Duration unit `Hours`
5. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` adalah `ON`, karena Approval Workflow tersedia
6. Verifikasi nilai efektif Require approval transaksi penugasan untuk aset `Truk Workshop {runId}` adalah `ON`, dari override Group
7. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` adalah `ON`, karena level Feature Suite Borrowing `Full`
8. Verifikasi nilai efektif Duration unit untuk aset `Truk Gudang {runId}` adalah `Hours`, karena level Feature Suite Borrowing `Full`
9. Verifikasi nilai efektif Direct handover between holders untuk aset `Truk Workshop {runId}` adalah `Allow`, karena level Feature Suite Assignment `Full`

### Level plan per tier menentukan ketersediaan Approval Workflow, Borrowing, dan Assignment
10. Operator Plan memindahkan plan entitas ke `Free (rank 0)` dengan nilai default plan awal[^drift-1]
11. Maya Pengelola menjalankan Export rules pada Category `Armada Plan {runId}`
12. Verifikasi level Feature Suite Borrowing entitas pada `Free (rank 0)` adalah `None`
13. Verifikasi level Feature Suite Assignment entitas pada `Free (rank 0)` adalah `None`
14. Verifikasi baris Approval Workflow pada sheet Info berkas Export rules adalah `Not available`, karena Approval Workflow pada `Free (rank 0)` tidak tersedia
15. Verifikasi sheet Rules pada berkas itu tidak memuat transaksi peminjaman, karena level Feature Suite-nya `None`
16. Operator Plan memindahkan plan entitas ke `Paid (rank 1)` dengan nilai default plan awal[^drift-1]
17. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` adalah `OFF`, karena Approval Workflow pada `Paid (rank 1)` tidak tersedia
18. Verifikasi level Feature Suite Borrowing entitas pada `Paid (rank 1)` adalah `Basic`
19. Verifikasi level Feature Suite Assignment entitas pada `Paid (rank 1)` adalah `Basic`
20. Maya Pengelola menjalankan Export rules pada Category `Armada Plan {runId}`
21. Verifikasi sheet Rules pada berkas itu memuat transaksi peminjaman, karena level Feature Suite-nya bukan `None`
22. Operator Plan memindahkan plan entitas ke `Paid (rank 2)` dengan nilai default plan awal[^drift-1]
23. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` adalah `ON`, karena Approval Workflow pada `Paid (rank 2)` tersedia
24. Verifikasi level Feature Suite Borrowing entitas pada `Paid (rank 2)` adalah `Full`
25. Verifikasi level Feature Suite Assignment entitas pada `Paid (rank 2)` adalah `Full`
26. Operator Plan memindahkan plan entitas ke `Paid (rank 3)` dengan nilai default plan awal[^drift-1]
27. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` adalah `ON`, karena Approval Workflow pada `Paid (rank 3)` tersedia
28. Verifikasi level Feature Suite Borrowing entitas pada `Paid (rank 3)` adalah `Full`
29. Verifikasi level Feature Suite Assignment entitas pada `Paid (rank 3)` adalah `Full`

### Plan kustom dibaca dari nilai fitur plan client, bukan dari namanya
30. Operator Plan menerapkan plan kustom `Paket Kustom {runId}` pada entitas, dengan Approval Workflow ON, Feature Suite Borrowing `Basic`, dan Feature Suite Assignment `Full`
31. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` adalah `ON`, karena nilai Approval Workflow dibaca dari plan client dan bukan dari nama plan
32. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` adalah `OFF`, karena nilai aktual level Borrowing dibaca dari plan client
33. Verifikasi nilai efektif Direct handover between holders untuk aset `Truk Workshop {runId}` adalah `Allow`, karena nilai aktual level Assignment dibaca dari plan client
34. Operator Plan mengubah plan kustom `Paket Kustom {runId}` menjadi Approval Workflow ON serta Feature Suite Borrowing, Assignment, pemindahan, dan pelepasan `Full`

### Approval Workflow tidak tersedia di plan: nilai efektif Require approval OFF dan nilai tersimpan dipertahankan
35. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log serta jumlah notifikasi `approver_required`
36. Operator Plan mematikan toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`
37. Verifikasi Changelog dan Activity Log tidak bertambah entri, karena perubahan toggle plan bukan perubahan Settings
38. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` adalah `OFF`, walau nilai tersimpan Category `Armada Plan {runId}` `ON`
39. Verifikasi nilai efektif Require approval transaksi penugasan untuk aset `Truk Workshop {runId}` adalah `OFF`, karena override Group `Workshop {runId}` bernilai `ON` tidak berlaku
40. Verifikasi nilai efektif Require approval transaksi pemindahan untuk aset `Mesin Kantor {runId}` adalah `OFF`
41. Verifikasi nilai efektif Require approval transaksi pelepasan untuk aset `Mesin Kantor {runId}` adalah `OFF`
42. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` tetap `ON`, karena yang bergerbang hanya field approval
43. Verifikasi Require approval Category `Armada Plan {runId}` untuk transaksi peminjaman tetap `ON`
44. Verifikasi Auto-approve Category `Armada Plan {runId}` tetap `OFF` dan Approval type tetap `All approvers (AND)`
45. Verifikasi override Group `Workshop {runId}` pada Category `Armada Plan {runId}` masih tersimpan
46. Maya Pengelola menjalankan Export rules pada Category `Armada Plan {runId}`
47. Verifikasi sheet Rules pada berkas itu memuat baris Transaction `Borrow`, Field `Require approval` dengan Value `Active`, nilai tersimpan pada baris field bergerbang
48. Maya Pengelola mengirim langsung ke server Save Category `Armada Plan {runId}` dengan Require approval transaksi peminjaman nilai sendiri `OFF`
49. Verifikasi Save ditolak server walau perubahan itu lolos dari UI, dan tidak ada entri log
50. Verifikasi Require approval Category `Armada Plan {runId}` untuk transaksi peminjaman tetap `ON`
51. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Max extensions nilai sendiri `3`, tanpa mengubah field bergerbang
52. Verifikasi Save diterima, karena field yang disabled oleh plan dilewati validasi Save
53. Maya Pengelola menjalankan Reset to Default pada tab peminjaman Category `Armada Plan {runId}`
54. Maya Pengelola menyimpan perubahan Reset to Default itu
55. Verifikasi Require approval, Auto-approve, dan Approval type Category `Armada Plan {runId}` tidak berubah, karena Reset to Default tidak menyentuh field bergerbang
56. Maya Pengelola mengirim langsung ke server Add override Group `Kantor Plan {runId}` pada Category `Armada Plan {runId}` untuk transaksi peminjaman dengan Require approval `ON`
57. Verifikasi Add override ditolak karena field bergerbang plan dipilih, dan tidak ada override untuk Group `Kantor Plan {runId}` terbuat
58. Verifikasi jumlah notifikasi `approver_required` tidak bertambah dari yang dicatat, walau Save Category `Armada Plan {runId}` pada langkah 51 meninggalkan Require approval tersimpan `ON` tanpa Approver yang ditugaskan, karena guard konfigurasi tidak aktif saat Approval Workflow tidak tersedia
59. Rudi Integrasi mengajukan transaksi peminjaman atas aset `Mesin Kantor {runId}`
60. Verifikasi transaksi itu langsung lanjut ke tahap eksekusi tanpa menunggu approval dan tidak dirutekan ke Group Manager atau Total Control, walau Auto-approve Category `Armada Plan {runId}` tersimpan `OFF` dan Approval type tersimpan `All approvers (AND)`, karena Auto-approve dan Approval type tidak berpengaruh saat Approval Workflow tidak tersedia
61. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
62. Operator Plan menyalakan kembali toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`
63. Verifikasi Changelog dan Activity Log tidak bertambah entri
64. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` kembali `ON` langsung, dari nilai tersimpan
65. Verifikasi nilai efektif Require approval transaksi penugasan untuk aset `Truk Workshop {runId}` kembali `ON` langsung, dari override Group yang tersimpan
66. Verifikasi nilai efektif Require approval transaksi pemindahan untuk aset `Mesin Kantor {runId}` kembali `ON`, karena default Company Require approval transaksi pemindahan ON
67. Verifikasi nilai efektif Require approval transaksi pelepasan untuk aset `Mesin Kantor {runId}` kembali `ON`, karena default Company Require approval transaksi pelepasan ON

### Level Feature Suite Borrowing Basic: Self service OFF dan Duration unit Days, nilai tersimpan dipertahankan
68. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
69. Operator Plan menurunkan level Feature Suite Borrowing plan kustom `Paket Kustom {runId}` ke `Basic`
70. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` adalah `OFF`
71. Verifikasi nilai efektif Duration unit untuk aset `Truk Gudang {runId}` adalah `Days`
72. Verifikasi nilai efektif Max duration untuk aset `Truk Gudang {runId}` tetap `14`, karena yang bergerbang hanya Self service dan Duration unit
73. Verifikasi Self service Category `Peralatan Plan {runId}` tetap `ON` dan Duration unit tetap `Hours`
74. Verifikasi override Group `Gudang Plan {runId}` pada Category `Peralatan Plan {runId}` untuk transaksi peminjaman masih tersimpan
75. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` tetap `OFF`, karena override Group `Gudang Plan {runId}` bernilai `ON` tidak berlaku
76. Maya Pengelola mengirim langsung ke server Save Category `Peralatan Plan {runId}` dengan Self service nilai sendiri `OFF` dan Duration unit `Days`
77. Verifikasi Save ditolak server walau perubahan itu lolos dari UI
78. Verifikasi Self service Category `Peralatan Plan {runId}` tetap `ON` dan Duration unit tetap `Hours`
79. Maya Pengelola menjalankan Reset to Default pada tab peminjaman Category `Peralatan Plan {runId}`, yang mengembalikan Max extensions ke Inherit di draft
80. Maya Pengelola menyimpan perubahan Reset to Default itu, yang hanya memuat Max extensions kembali ke Inherit
81. Verifikasi Self service Category `Peralatan Plan {runId}` tetap `ON` dan Duration unit tetap `Hours`, karena Reset to Default tidak menyentuh field bergerbang
82. Verifikasi Max extensions Category `Peralatan Plan {runId}` kembali Inherit, hasil Reset to Default atas field yang tidak bergerbang
83. Verifikasi Changelog dan Activity Log masing-masing bertambah tepat satu entri dari yang dicatat pada langkah 68, yaitu untuk Max extensions pada Save langkah 80, sehingga penurunan level tidak menambah entri apa pun
84. Operator Plan mengembalikan level Feature Suite Borrowing plan kustom `Paket Kustom {runId}` ke `Full`
85. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` kembali `ON` langsung, dari nilai tersimpan
86. Verifikasi nilai efektif Duration unit untuk aset `Truk Gudang {runId}` kembali `Hours` langsung

### Level Feature Suite Assignment Basic: Direct handover Deny, nilai tersimpan dipertahankan
87. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
88. Operator Plan menurunkan level Feature Suite Assignment plan kustom `Paket Kustom {runId}` ke `Basic`
89. Verifikasi nilai efektif Direct handover between holders untuk aset `Truk Workshop {runId}` adalah `Deny`, apa pun nilai tersimpannya
90. Verifikasi nilai efektif Allowed assignee: Division untuk aset `Truk Workshop {runId}` tetap `ON`, karena yang bergerbang hanya Direct handover between holders
91. Verifikasi Direct handover between holders Category `Armada Plan {runId}` tetap `Allow`
92. Verifikasi override Group `Workshop {runId}` pada Category `Armada Plan {runId}` untuk transaksi penugasan masih tersimpan
93. Verifikasi nilai efektif Direct handover between holders untuk aset `Truk Workshop {runId}` tetap `Deny`, karena override Group `Workshop {runId}` bernilai `Allow` tidak berlaku
94. Maya Pengelola mengirim langsung ke server Save Category `Armada Plan {runId}` dengan Direct handover between holders nilai sendiri `Deny`
95. Verifikasi Save ditolak server walau perubahan itu lolos dari UI
96. Verifikasi Direct handover between holders Category `Armada Plan {runId}` tetap `Allow`
97. Maya Pengelola menjalankan Reset to Default pada tab penugasan Category `Armada Plan {runId}`, yang mengembalikan Max assets per assignee (concurrent) ke Inherit di draft
98. Maya Pengelola menyimpan perubahan Reset to Default itu, yang hanya memuat Max assets per assignee (concurrent) kembali ke Inherit
99. Verifikasi Direct handover between holders Category `Armada Plan {runId}` tetap `Allow`, karena Reset to Default tidak menyentuh field bergerbang
100. Verifikasi Max assets per assignee (concurrent) Category `Armada Plan {runId}` kembali Inherit, hasil Reset to Default atas field yang tidak bergerbang
101. Verifikasi Changelog dan Activity Log masing-masing bertambah tepat satu entri dari yang dicatat pada langkah 87, yaitu untuk Max assets per assignee (concurrent) pada Save langkah 98, sehingga penurunan level tidak menambah entri apa pun
102. Operator Plan mengembalikan level Feature Suite Assignment plan kustom `Paket Kustom {runId}` ke `Full`
103. Verifikasi nilai efektif Direct handover between holders untuk aset `Truk Workshop {runId}` kembali `Allow` langsung, dari nilai tersimpan

### Level Basic pemindahan dan pelepasan tidak menggerbangi field Settings
104. Operator Plan menurunkan level Feature Suite pemindahan dan pelepasan plan kustom `Paket Kustom {runId}` ke `Basic`
105. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Auto-approve when destination in same parent Group nilai sendiri `OFF`
106. Verifikasi Save diterima dan nilai itu tersimpan, karena tidak ada field Settings yang bergerbang pada Basic
107. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Min asset age warning nilai sendiri `6`
108. Verifikasi Save diterima dan Min asset age warning Category `Armada Plan {runId}` tersimpan `6`, karena tidak ada field Settings yang bergerbang pada Basic pelepasan
109. Verifikasi nilai efektif Auto-approve when destination in same parent Group untuk aset `Mesin Kantor {runId}` mengikuti nilai tersimpan `OFF`
110. Verifikasi nilai efektif Min asset age warning untuk aset `Mesin Kantor {runId}` mengikuti nilai tersimpan `6`
111. Operator Plan mengembalikan level Feature Suite pemindahan dan pelepasan plan kustom `Paket Kustom {runId}` ke `Full`

[^drift-1]: Drift PRD vs foundation. PRD §9.10.1, §9.10.2, dan §9.10.3 (tabel level per plan): plan bernama `starter`, `growth`, `professional`, dan `enterprise`. foundation `plans.md` §2.2 dan §3.4: kolom plan adalah slot `Free (rank 0)`, `Paid (rank 1)`, `Paid (rank 2)`, dan `Paid (rank 3)` yang namanya bebas diedit Principal, dengan nilai default plan awal per slot (Approval Workflow: No, No, Yes, Yes; Borrowing dan Assignment: None, Basic, Full, Full). Diasersi: foundation, karena nama plan adalah label bebas dan plan adalah pola bersama platform; `starter`, `growth`, `professional`, dan `enterprise` dibaca sebagai slot rank 0 sampai 3 (SB-4).
