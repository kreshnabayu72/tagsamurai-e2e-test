---
id: TC-FA-FATR-BE-091-plan
title: "Plan gating di server"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§Aturan Logika Modul#r74", "§Aturan Logika Modul#r75", "§Aturan Logika Modul#r80", "§Aturan Logika Modul#r84", "§Aturan Logika Modul#r86", "§Aturan Logika Modul#r87", "§Aturan Logika Modul#r89", "§Aturan Logika Modul#r93", "§Aturan Logika Modul#r104", "§9.2#b45", "§9.2#b46", "§9.2#b72", "§9.2#b151", "§9.2#b153", "§9.2#b329", "§9.2#b340", "§9.2#b555", "§9.2#b557", "§9.4.2#r25", "§9.4.2#r37", "§9.4.2#r38", "§9.4.2#r54", "§9.4.2#r100", "§9.4.2#r101", "§9.4.3#b2", "§9.4.3#b3", "§9.4.4#r20", "§9.4.4#r23", "§9.4.4#r54", "§9.4.4#r55", "§9.4.4#r56", "§9.4.4#r57", "§9.4.4#r58", "§9.10.1#r1", "§9.10.1#r2", "§9.10.1#r3", "§9.10.1#r4", "§9.10.1#r5", "§9.10.1#r6", "§9.10.1#r8", "§9.10.1#b3", "§9.10.1#b4", "§9.10.1#b5", "§9.10.1#b6", "§9.10.1#b9", "§9.10.1#r9", "§9.10.1#r10", "§9.10.1#p10", "§9.10.1#p11", "§9.10.1#p12", "§9.10.2#r1", "§9.10.2#r2", "§9.10.2#r3", "§9.10.2#r4", "§9.10.2#r5", "§9.10.2#r6", "§9.10.2#r7", "§9.10.2#r9", "§9.10.2#b3", "§9.10.2#b4", "§9.10.2#b5", "§9.10.2#b7", "§9.10.2#r10", "§9.10.2#r11", "§9.10.3#r1", "§9.10.3#r2", "§9.10.3#r3", "§9.10.3#r4", "§9.10.3#r5", "§9.10.3#r6", "§9.10.3#r8", "§9.10.4#b2", "§9.10.1#p7", "§9.10.3#b2", "§9.8#r15", "§9.4.4#r4", "§9.10.1#p13", "§9.10.1#r7", "§9.10.2#r8", "§9.10.3#r7"]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#r74": [5, 6, 38, 67]
  "§Aturan Logika Modul#r75": [38, 40, 41]
  "§Aturan Logika Modul#r80": [43, 44]
  "§Aturan Logika Modul#r84": [7, 8, 12]
  "§Aturan Logika Modul#r86": 73
  "§Aturan Logika Modul#r87": 74
  "§Aturan Logika Modul#r89": 76
  "§Aturan Logika Modul#r93": 80
  "§Aturan Logika Modul#r104": [9, 13]
  "§9.2#b45": 53
  "§9.2#b46": [43, 44, 76]
  "§9.2#b72": 50
  "§9.2#b151": 45
  "§9.2#b153": 39
  "§9.2#b329": 47
  "§9.2#b340": [15, 21]
  "§9.2#b555": 38
  "§9.2#b557": [73, 74]
  "§9.4.2#r25": 59
  "§9.4.2#r37": 38
  "§9.4.2#r38": 73
  "§9.4.2#r54": [37, 123, 125]
  "§9.4.2#r100": 50
  "§9.4.2#r101": 51
  "§9.4.3#b2": 50
  "§9.4.3#b3": 43
  "§9.4.4#r20": 50
  "§9.4.4#r23": [59, 60, 134, 136, 137]
  "§9.4.4#r54": 38
  "§9.4.4#r55": 66
  "§9.4.4#r56": 73
  "§9.4.4#r57": 86
  "§9.4.4#r58": 92
  "§9.10.1#r1": 14
  "§9.10.1#r2": 17
  "§9.10.1#r3": 23
  "§9.10.1#r4": 27
  "§9.10.1#r5": [38, 67]
  "§9.10.1#r6": 31
  "§9.10.1#r8": 42
  "§9.10.1#b3": [50, 143]
  "§9.10.1#b4": 56
  "§9.10.1#b5": 45
  "§9.10.1#b6": [61, 63, 108, 109, 114, 144, 148, 149]
  "§9.10.1#b9": [37, 66, 67, 68, 69, 70]
  "§9.10.1#r9": 38
  "§9.10.1#r10": [63, 119]
  "§9.10.1#p10": 38
  "§9.10.1#p11": 43
  "§9.10.1#p12": 45
  "§9.10.2#r1": 12
  "§9.10.2#r2": 18
  "§9.10.2#r3": 24
  "§9.10.2#r4": 28
  "§9.10.2#r5": [73, 74]
  "§9.10.2#r6": 75
  "§9.10.2#r7": 75
  "§9.10.2#r9": 32
  "§9.10.2#b3": [80, 81]
  "§9.10.2#b4": [84, 85]
  "§9.10.2#b5": [77, 78]
  "§9.10.2#b7": [86, 88, 89]
  "§9.10.2#r10": 73
  "§9.10.2#r11": 74
  "§9.10.3#r1": 13
  "§9.10.3#r2": 19
  "§9.10.3#r3": 25
  "§9.10.3#r4": 29
  "§9.10.3#r5": [93, 95]
  "§9.10.3#r6": [93, 95]
  "§9.10.3#r8": 33
  "§9.10.4#b2": [99, 101, 102, 103]
  "§9.10.1#p7": 113
  "§9.10.3#b2": [92, 123, 125]
  "§9.8#r15": [37, 66, 92, 123, 125]
  "§9.4.4#r4": [128, 130]
  "§9.10.1#p13": [63, 113]
  "§9.10.1#r7": [14, 17, 23, 27]
  "§9.10.2#r8": [12, 18, 24, 28]
  "§9.10.3#r7": [13, 19, 25, 29]
---
# Plan gating di server

## Prerequisites
- Aktor: Maya Pengelola (DU-091-2), Total Control dengan cakupan seluruh entitas; pengaju Budi Peminjam (DU-091-3), pengguna yang bukan Total Control dan bukan Group Manager dengan cakupan Group `Kantor Plan {runId}`, `Workshop {runId}`, dan `Gudang Plan {runId}`; dan Operator Plan (DU-091-4), operator Admin Console di luar entitas.
- Data:
  - DU-091-1: Entitas, entitas khusus spec ini, berlangganan plan Paid (rank 2): Name `Entitas Plan {runId}`; Plan `Paid (rank 2)`.
  - DU-091-2: User, pengelola Total Control: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh entitas`.
  - DU-091-3: User, pengaju peminjaman dan pemindahan yang bukan Total Control dan bukan Group Manager: Name `Budi Peminjam {runId}`; Peran `pengaju transaksi, bukan Total Control dan bukan Group Manager`; Cakupan `Group Kantor Plan {runId}, Workshop {runId}, dan Gudang Plan {runId} beserta turunannya`.
  - DU-091-4: User, operator Admin Console yang mengubah plan entitas: Name `Operator Plan {runId}`; Peran `operator Admin Console di luar entitas`.
  - DU-091-5: Category, Category leaf untuk field approval dan Need recipient confirmation: Name `Armada Plan {runId}`.
  - DU-091-6: Category, Category leaf untuk Self service dan Duration unit: Name `Peralatan Plan {runId}`.
  - DU-091-7: Group, Group tempat override penugasan: Name `Workshop {runId}`.
  - DU-091-8: Group, Group tanpa override: Name `Kantor Plan {runId}`.
  - DU-091-9: Group, Group tempat override peminjaman: Name `Gudang Plan {runId}`.
  - DU-091-10: Asset, aset di Group Workshop: Name `Truk Workshop {runId}`; Asset Name `Truk Operasional {runId}`; Category `Armada Plan {runId}`; Group `Workshop {runId}`.
  - DU-091-11: Asset, aset di Group tanpa override: Name `Mesin Kantor {runId}`; Asset Name `Mesin Operasional {runId}`; Category `Armada Plan {runId}`; Group `Kantor Plan {runId}`.
  - DU-091-12: Asset, aset di Group Gudang: Name `Truk Gudang {runId}`; Asset Name `Forklift Gudang {runId}`; Category `Peralatan Plan {runId}`; Group `Gudang Plan {runId}`.
  - DU-091-13 sampai DU-091-16 dibuat Maya Pengelola di grup Setup, dan DU-091-17 sampai DU-091-22 dan DU-091-24 adalah nilai input yang dikirim di grup masing-masing, bukan record yang sudah ada.
  - DU-091-25: Asset, aset kedua di Group Workshop untuk pengajuan saat Approval Workflow tidak tersedia: Name `Truk Workshop Dua {runId}`; Asset Name `Truk Operasional {runId}`; Category `Armada Plan {runId}`; Group `Workshop {runId}`.
  - DU-091-26: Asset, aset di Group Kantor Plan untuk pengajuan pemindahan ke Group Gudang Plan: Name `Mesin Kantor Dua {runId}`; Asset Name `Mesin Operasional {runId}`; Category `Armada Plan {runId}`; Group `Kantor Plan {runId}`.
  - DU-091-27 dan DU-091-28 dibuat Maya Pengelola di grup masing-masing, bukan record yang sudah ada.
  - DU-091-29 sampai DU-091-33 adalah nilai input yang dikirim atau disimpan di grup masing-masing, bukan record yang sudah ada.
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
1. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Require approval transaksi peminjaman nilai sendiri `ON`, Auto-approve `OFF`, Approval type `All approvers (AND)`, Need recipient confirmation `No`, Max extensions `2`, dan Max assets per assignee (concurrent) transaksi penugasan nilai sendiri `2`
2. Maya Pengelola menyimpan Category `Peralatan Plan {runId}` dengan Self service nilai sendiri `ON`, Duration unit `Hours`, dan Max extensions nilai sendiri `3`
3. Maya Pengelola menambahkan override Group `Workshop {runId}` pada Category `Armada Plan {runId}` untuk transaksi penugasan dengan Require approval `ON` dan Need recipient confirmation `No`
4. Maya Pengelola menambahkan override Group `Gudang Plan {runId}` pada Category `Peralatan Plan {runId}` untuk transaksi peminjaman dengan Self service `ON` dan Duration unit `Hours`
5. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` adalah `ON`, karena Approval Workflow tersedia
6. Verifikasi nilai efektif Require approval transaksi penugasan untuk aset `Truk Workshop {runId}` adalah `ON`, dari override Group
7. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` adalah `ON`, karena level Feature Suite Borrowing `Full`
8. Verifikasi nilai efektif Duration unit untuk aset `Truk Gudang {runId}` adalah `Hours`, karena level Feature Suite Borrowing `Full`
9. Verifikasi nilai efektif Need recipient confirmation untuk aset `Truk Workshop {runId}` adalah `No` pada level Feature Suite Assignment `Full`

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
33. Verifikasi level Feature Suite Assignment entitas pada plan kustom `Paket Kustom {runId}` adalah `Full`, karena nilai aktual level Assignment dibaca dari plan client
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
48. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
49. Maya Pengelola mengirim langsung ke server Save Category `Armada Plan {runId}` dengan Require approval transaksi peminjaman nilai sendiri `OFF`
50. Verifikasi Save ditolak server walau perubahan itu lolos dari UI, dan Changelog serta Activity Log tidak bertambah entri dari jumlah yang dicatat sebelum Save itu
51. Verifikasi Require approval Category `Armada Plan {runId}` untuk transaksi peminjaman tetap `ON`
52. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Max extensions nilai sendiri `3`, tanpa mengubah field bergerbang Require approval dan Approval type yang disabled oleh plan
53. Verifikasi Save diterima dan Max extensions tersimpan `3`, karena field Require approval dan Approval type yang disabled oleh plan tidak menghalangi Save
54. Maya Pengelola menjalankan Reset to Default pada tab peminjaman Category `Armada Plan {runId}`
55. Maya Pengelola menyimpan perubahan Reset to Default itu
56. Verifikasi Require approval, Auto-approve, dan Approval type Category `Armada Plan {runId}` tidak berubah, karena Reset to Default tidak menyentuh field bergerbang
57. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
58. Maya Pengelola mengirim langsung ke server Add override Group `Kantor Plan {runId}` pada Category `Armada Plan {runId}` untuk transaksi peminjaman dengan Require approval `ON`
59. Verifikasi Add override ditolak karena field bergerbang plan dipilih, dan tidak ada override untuk Group `Kantor Plan {runId}` terbuat
60. Verifikasi Changelog dan Activity Log tidak bertambah entri dari jumlah yang dicatat sebelum Add override itu, karena penolakan tidak menulis log
61. Verifikasi jumlah notifikasi `approver_required` tidak bertambah dari yang dicatat, walau Save Category `Armada Plan {runId}` dengan Max extensions `3` meninggalkan Require approval tersimpan `ON` tanpa Approver yang ditugaskan
62. Budi Peminjam mengajukan transaksi peminjaman atas aset `Mesin Kantor {runId}`
63. Verifikasi transaksi itu langsung lanjut ke tahap eksekusi tanpa menunggu approval dan tidak dirutekan ke Group Manager atau Total Control, walau Auto-approve Category `Armada Plan {runId}` tersimpan `OFF` dan Approval type tersimpan `All approvers (AND)`, karena Auto-approve dan Approval type tidak berpengaruh saat Approval Workflow tidak tersedia
64. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
65. Operator Plan menyalakan kembali toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`
66. Verifikasi Changelog dan Activity Log tidak bertambah entri
67. Verifikasi nilai efektif Require approval transaksi peminjaman untuk aset `Mesin Kantor {runId}` kembali `ON` langsung, dari nilai tersimpan
68. Verifikasi nilai efektif Require approval transaksi penugasan untuk aset `Truk Workshop {runId}` kembali `ON` langsung, dari override Group yang tersimpan
69. Verifikasi nilai efektif Require approval transaksi pemindahan untuk aset `Mesin Kantor {runId}` kembali `ON`, karena default Company Require approval transaksi pemindahan ON
70. Verifikasi nilai efektif Require approval transaksi pelepasan untuk aset `Mesin Kantor {runId}` kembali `ON`, karena default Company Require approval transaksi pelepasan ON

### Level Feature Suite Borrowing Basic: Self service OFF dan Duration unit Days, nilai tersimpan dipertahankan
71. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
72. Operator Plan menurunkan level Feature Suite Borrowing plan kustom `Paket Kustom {runId}` ke `Basic`
73. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` adalah `OFF`
74. Verifikasi nilai efektif Duration unit untuk aset `Truk Gudang {runId}` adalah `Days`
75. Verifikasi nilai efektif Max duration untuk aset `Truk Gudang {runId}` tetap `14`, karena yang bergerbang hanya Self service dan Duration unit
76. Verifikasi Self service Category `Peralatan Plan {runId}` tetap `ON` dan Duration unit tetap `Hours`
77. Verifikasi override Group `Gudang Plan {runId}` pada Category `Peralatan Plan {runId}` untuk transaksi peminjaman masih tersimpan
78. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` tetap `OFF`, karena override Group `Gudang Plan {runId}` bernilai `ON` tidak berlaku
79. Maya Pengelola mengirim langsung ke server Save Category `Peralatan Plan {runId}` dengan Self service nilai sendiri `OFF` dan Duration unit `Days`
80. Verifikasi Save ditolak server walau perubahan itu lolos dari UI
81. Verifikasi Self service Category `Peralatan Plan {runId}` tetap `ON` dan Duration unit tetap `Hours`
82. Maya Pengelola menjalankan Reset to Default pada tab peminjaman Category `Peralatan Plan {runId}`, yang mengembalikan Max extensions ke Inherit di draft
83. Maya Pengelola menyimpan perubahan Reset to Default itu, yang hanya memuat Max extensions kembali ke Inherit
84. Verifikasi Self service Category `Peralatan Plan {runId}` tetap `ON` dan Duration unit tetap `Hours`, karena Reset to Default tidak menyentuh field bergerbang
85. Verifikasi Max extensions Category `Peralatan Plan {runId}` kembali Inherit, hasil Reset to Default atas field yang tidak bergerbang
86. Verifikasi Changelog dan Activity Log masing-masing bertambah tepat satu entri dari yang dicatat sebelum penurunan level, yaitu untuk Max extensions pada Save perubahan Reset to Default, sehingga penurunan level tidak menambah entri apa pun
87. Operator Plan mengembalikan level Feature Suite Borrowing plan kustom `Paket Kustom {runId}` ke `Full`
88. Verifikasi nilai efektif Self service untuk aset `Truk Gudang {runId}` kembali `ON` langsung, dari nilai tersimpan
89. Verifikasi nilai efektif Duration unit untuk aset `Truk Gudang {runId}` kembali `Hours` langsung

### Level Feature Suite Assignment Basic tidak menggerbangi field tab penugasan
90. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
91. Operator Plan menurunkan level Feature Suite Assignment plan kustom `Paket Kustom {runId}` ke `Basic`
92. Verifikasi Changelog dan Activity Log tidak bertambah entri dari yang dicatat sebelum penurunan level, karena perubahan level plan bukan perubahan Settings
93. Verifikasi nilai efektif Need recipient confirmation untuk aset `Truk Workshop {runId}` tetap `No`, karena tidak ada field tab penugasan yang bergerbang plan pada level `Basic`
94. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Need recipient confirmation nilai sendiri `Yes` lewat Save Changes
95. Verifikasi Save diterima dan Need recipient confirmation Category `Armada Plan {runId}` tersimpan `Yes`, karena tidak ada field tab penugasan yang bergerbang plan pada level `Basic`
96. Operator Plan mengembalikan level Feature Suite Assignment plan kustom `Paket Kustom {runId}` ke `Full`

### Level Basic pemindahan dan pelepasan tidak menggerbangi field Settings
97. Operator Plan menurunkan level Feature Suite pemindahan dan pelepasan plan kustom `Paket Kustom {runId}` ke `Basic`
98. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Auto-approve when destination in same parent Group nilai sendiri `OFF`
99. Verifikasi Save diterima dan nilai itu tersimpan, karena tidak ada field Settings yang bergerbang pada Basic
100. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Min asset age warning nilai sendiri `6`
101. Verifikasi Save diterima dan Min asset age warning Category `Armada Plan {runId}` tersimpan `6`, karena tidak ada field Settings yang bergerbang pada Basic pelepasan
102. Verifikasi nilai efektif Auto-approve when destination in same parent Group untuk aset `Mesin Kantor {runId}` mengikuti nilai tersimpan `OFF`
103. Verifikasi nilai efektif Min asset age warning untuk aset `Mesin Kantor {runId}` mengikuti nilai tersimpan `6`
104. Operator Plan mengembalikan level Feature Suite pemindahan dan pelepasan plan kustom `Paket Kustom {runId}` ke `Full`

### Pengaju biasa menunggu approval saat Approval Workflow tersedia dan langsung lanjut saat tidak tersedia
105. Maya Pengelola menambahkan override Group `Workshop {runId}` pada Category `Armada Plan {runId}` untuk transaksi peminjaman dengan Require approval `ON`
106. Maya Pengelola mencatat jumlah notifikasi `approver_required`
107. Budi Peminjam mengajukan transaksi peminjaman atas aset `Truk Workshop {runId}`
108. Verifikasi transaksi itu menunggu approval, karena Approval Workflow tersedia dan nilai efektif Require approval `ON` dari override Group `Workshop {runId}`
109. Verifikasi jumlah notifikasi `approver_required` bertambah tepat satu dari yang dicatat, karena tidak ada Approver yang ditugaskan dan Approval Workflow tersedia
110. Operator Plan mematikan toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`
111. Maya Pengelola mencatat jumlah notifikasi `approver_required`
112. Budi Peminjam mengajukan transaksi peminjaman atas aset `Truk Workshop Dua {runId}`
113. Verifikasi transaksi itu langsung lanjut ke tahap eksekusi tanpa menunggu approval dan tidak dirutekan ke Group Manager atau Total Control, walau override Group `Workshop {runId}` tersimpan Require approval `ON`
114. Verifikasi jumlah notifikasi `approver_required` tidak bertambah dari yang dicatat, berbeda dengan pengajuan saat Approval Workflow tersedia
115. Operator Plan menyalakan kembali toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`

### Approval scope tidak berpengaruh saat Approval Workflow tidak tersedia
116. Maya Pengelola menyimpan Category `Armada Plan {runId}` dengan Require approval transaksi pemindahan nilai sendiri `ON` dan Approval scope nilai sendiri `Origin only`
117. Operator Plan mematikan toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`
118. Budi Peminjam mengajukan pemindahan aset `Mesin Kantor Dua {runId}` dari Group `Kantor Plan {runId}` ke Group `Gudang Plan {runId}`
119. Verifikasi pemindahan itu langsung lanjut ke tahap eksekusi tanpa menunggu approval di Group asal maupun Group tujuan, walau Approval scope tersimpan `Origin only` dan Require approval transaksi pemindahan tersimpan `ON`
120. Operator Plan menyalakan kembali toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`

### Perubahan level Feature Suite pemindahan dan pelepasan tidak masuk Changelog
121. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
122. Operator Plan menurunkan level Feature Suite pemindahan dan pelepasan plan kustom `Paket Kustom {runId}` ke `Basic`
123. Verifikasi Changelog dan Activity Log tidak bertambah entri dari jumlah yang dicatat, karena perubahan level plan bukan perubahan Settings
124. Operator Plan mengembalikan level Feature Suite pemindahan dan pelepasan plan kustom `Paket Kustom {runId}` ke `Full`
125. Verifikasi Changelog dan Activity Log tetap tidak bertambah entri dari jumlah yang dicatat

### Reset to Default tidak dicatat dan Save sesudahnya dicatat
126. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
127. Maya Pengelola menjalankan Reset to Default pada tab peminjaman Category `Peralatan Plan {runId}`
128. Verifikasi Changelog dan Activity Log tidak bertambah entri sesudah Reset to Default dan sebelum Save, karena Reset to Default hanya mengubah draft
129. Maya Pengelola menyimpan perubahan Reset to Default itu
130. Verifikasi Changelog dan Activity Log masing-masing bertambah tepat dua entri dari yang dicatat, untuk Self service dan Duration unit yang kembali Inherit, karena perubahan dicatat saat Save

### Add override field Borrowing bergerbang ditolak server saat level Feature Suite Borrowing Basic
131. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
132. Operator Plan menurunkan level Feature Suite Borrowing plan kustom `Paket Kustom {runId}` ke `Basic`
133. Maya Pengelola mengirim langsung ke server Add override Group `Kantor Plan {runId}` pada Category `Peralatan Plan {runId}` untuk transaksi peminjaman dengan Self service `ON`
134. Verifikasi Add override ditolak karena Self service bergerbang level Feature Suite Borrowing dan levelnya `Basic`, dan tidak ada override untuk Group `Kantor Plan {runId}` pada Category `Peralatan Plan {runId}` terbuat
135. Maya Pengelola mengirim langsung ke server Add override Group `Kantor Plan {runId}` pada Category `Peralatan Plan {runId}` untuk transaksi peminjaman dengan Duration unit `Hours`
136. Verifikasi Add override ditolak karena Duration unit bergerbang level Feature Suite Borrowing dan levelnya `Basic`, dan tidak ada override untuk Group `Kantor Plan {runId}` pada Category `Peralatan Plan {runId}` terbuat
137. Verifikasi Changelog dan Activity Log tidak bertambah entri dari yang dicatat sebelum penurunan level, karena penolakan tidak menulis log
138. Operator Plan mengembalikan level Feature Suite Borrowing plan kustom `Paket Kustom {runId}` ke `Full`

### Guard konfigurasi tanpa Approver aktif saat Approval Workflow tersedia dan tidak aktif saat tidak tersedia
139. Maya Pengelola menyimpan Category `Peralatan Plan {runId}` dengan Require approval transaksi peminjaman nilai sendiri `OFF`
140. Operator Plan mematikan toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`
141. Maya Pengelola mencatat jumlah notifikasi `approver_required`
142. Maya Pengelola mengirim langsung ke server Save Category `Peralatan Plan {runId}` dengan Require approval transaksi peminjaman nilai sendiri `ON`, aksi yang pada Approval Workflow tersedia menimbulkan kondisi tidak ada Approver karena tidak ada Role Transaksi Approver yang ditugaskan untuk transaksi peminjaman
143. Verifikasi Save ditolak server karena Require approval bergerbang plan, dan Require approval Category `Peralatan Plan {runId}` tetap `OFF`
144. Verifikasi jumlah notifikasi `approver_required` tidak bertambah dari yang dicatat, karena guard konfigurasi untuk kondisi tidak ada Approver tidak aktif saat Approval Workflow tidak tersedia
145. Operator Plan menyalakan kembali toggle Approval Workflow pada plan kustom `Paket Kustom {runId}`
146. Maya Pengelola mencatat jumlah notifikasi `approver_required`
147. Maya Pengelola menyimpan Category `Peralatan Plan {runId}` dengan Require approval transaksi peminjaman nilai sendiri `ON`
148. Verifikasi Save diterima dan Require approval Category `Peralatan Plan {runId}` tersimpan `ON`
149. Verifikasi jumlah notifikasi `approver_required` bertambah tepat satu dari yang dicatat, karena guard konfigurasi aktif saat Approval Workflow tersedia dan tidak ada Role Transaksi Approver yang ditugaskan untuk transaksi peminjaman

[^drift-1]: Drift PRD vs foundation. PRD §9.10.1, §9.10.2, dan §9.10.3 (tabel level per plan): plan bernama `starter`, `growth`, `professional`, dan `enterprise`. foundation `plans.md` §2.2 dan §3.4: kolom plan adalah slot `Free (rank 0)`, `Paid (rank 1)`, `Paid (rank 2)`, dan `Paid (rank 3)` yang namanya bebas diedit Principal, dengan nilai default plan awal per slot (Approval Workflow: No, No, Yes, Yes; Borrowing dan Assignment: None, Basic, Full, Full). Diasersi: foundation, karena nama plan adalah label bebas dan plan adalah pola bersama platform; `starter`, `growth`, `professional`, dan `enterprise` dibaca sebagai slot rank 0 sampai 3 (SB-4).
