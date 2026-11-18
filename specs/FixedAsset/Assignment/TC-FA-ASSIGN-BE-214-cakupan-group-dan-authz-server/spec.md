---
id: TC-FA-ASSIGN-BE-214-cakupan-group-dan-authz-server
title: "Cakupan Group dan penolakan aksi tanpa hak di server"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-ASG-03", "EC-ASG-23", "F-ASSIGN-07.k1", "§9.3#r1", "§9.3#r2", "§9.3#r3", "§9.3#b1", "§9.3#b2", "EB-AKS-3@submit-assignment", "EB-AKS-3@save-draft", "EB-AKS-3@cancel-assignment", "EB-AKS-3@handover", "EB-AKS-3@unassign", "EB-AKS-3@change-pic", "EB-AKS-3@keputusan-approval", "ASSIGN-LOGIC-14a", "ASSIGN-LOGIC-14b", "ASSIGN-LOGIC-14c", "ASSIGN-LOGIC-14d", "ASSIGN-LOGIC-14e", "ASSIGN-LOGIC-14f", "ASSIGN-LOGIC-14g"]
smoke: []
dependsOn: []
owner: BE
trace:
  "V-ASG-03": [2, 4, 7]
  "EC-ASG-23": [23, 24]
  "F-ASSIGN-07.k1": [24, 78]
  "§9.3#r1": 28
  "§9.3#r2": 30
  "§9.3#r3": 31
  "§9.3#b1": [9, 31]
  "§9.3#b2": 50
  "EB-AKS-3@submit-assignment": 9
  "EB-AKS-3@save-draft": 11
  "EB-AKS-3@cancel-assignment": 15
  "EB-AKS-3@handover": 13
  "EB-AKS-3@unassign": 17
  "EB-AKS-3@change-pic": 19
  "EB-AKS-3@keputusan-approval": 21
  "ASSIGN-LOGIC-14a": [2, 7, 26]
  "ASSIGN-LOGIC-14b": [33, 35]
  "ASSIGN-LOGIC-14c": [44, 46, 54, 58, 60, 66]
  "ASSIGN-LOGIC-14d": [9, 31]
  "ASSIGN-LOGIC-14e": [4, 9, 23]
  "ASSIGN-LOGIC-14f": [37, 40, 68, 70, 72, 74, 76]
  "ASSIGN-LOGIC-14g": [46, 48, 62]
---

# Cakupan Group dan penolakan aksi tanpa hak di server

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); `Agus Pratama {runId}` (Asset Admin, cakupan Group `Branch Surabaya {runId}`); `Mila Anggraini {runId}` (Monitoring & Report, cakupan Group `Head Office {runId}`); `Nina Marlina {runId}` (Asset Admin, bukan Approver); `Oki Firmansyah {runId}` (hanya Update Manage asset & TAG); Approver `Mira Handayani {runId}`; Aktor Damaged `Dian Anggraeni {runId}`; Aktor Missing `Maya Sari {runId}`; Assignee dan PIC ber-akun login seperti di entri data.
- Data:
  - DU-214-1: User, Aktor Assignment Group asal: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-214-2: User, Aktor Assignment Group lain: Nama `Agus Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Branch Surabaya {runId}`.
  - DU-214-3: User, Pemantau tanpa hak tulis: Nama `Mila Anggraini {runId}`, Role `Monitoring & Report`, Cakupan Group `Head Office {runId}`.
  - DU-214-4: User, Asset Admin yang bukan Approver: Nama `Nina Marlina {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-214-5: User, Pemegang Update Manage asset & TAG saja: Nama `Oki Firmansyah {runId}`, Role `Update Manage asset & TAG saja, tanpa Role Transaksi Borrowing & Assignment`, Cakupan Group `Head Office {runId}`.
  - DU-214-6: Asset, Aset Available di Group Head Office untuk dipindai Aktor Group lain: Nama `Laptop HP Pavilion {runId}`, Custody `Available`, Group `Head Office {runId}`, Tag `satu tag`, Assignee `Budi Santoso {runId}`.
  - DU-214-7: Draft, Draft lintas Group dengan satu aset di luar cakupan Agus: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Laptop HP Pavilion {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Mobil Toyota Avanza {runId}`, Group aset 2 `Branch Surabaya {runId}`, Purpose `Kebutuhan kerja`.
  - DU-214-8: Asset, Aset Available untuk Submit tanpa hak: Nama `Laptop Lenovo V14 {runId}`, Custody `Available`, Group `Head Office {runId}`, Assignee `Budi Santoso {runId}`, Purpose `Kebutuhan kerja`.
  - DU-214-9: Asset, Aset Available untuk Save Draft tanpa hak: Nama `Monitor Samsung S27 {runId}`, Custody `Available`, Group `Head Office {runId}`, Assignee `Budi Santoso {runId}`, Purpose `Kebutuhan kerja`.
  - DU-214-10: Assignment, ASG dengan baris Waiting for Handover untuk Handover dan Cancel tanpa hak: Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Printer Epson L120 {runId}`, Status baris `Waiting for Handover`.
  - DU-214-11: Assignment, ASG dengan baris Assigned untuk Unassign tanpa hak: Assignee `Dedi Prasetyo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Proyektor BenQ MX {runId}`, Status baris `Assigned`.
  - DU-214-12: Assignment, ASG Division untuk Change PIC tanpa hak: Assignee `Operasional {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Perkins {runId}`, Status baris `Waiting for Handover`, PIC `Indah Permata {runId}`, PIC pengganti `Joko Susilo {runId}`.
  - DU-214-13: User, Approver Group: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-214-14: Assignment, ASG dengan baris Waiting for Approval untuk keputusan oleh bukan approver: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Speaker Bose {runId}`, Status baris `Waiting for Approval`, Approver `Mira Handayani {runId}`.
  - DU-214-15: Assignment, ASG dengan baris Assigned di Group Head Office untuk Unassign Aktor Group lain: Assignee `Fajar Nugroho {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Genset Yamaha {runId}`, Status baris `Assigned`.
  - DU-214-16: Assignment, ASG di Group Branch Surabaya yang tidak boleh dibaca Aktor Group lain: Assignee `Hadi Susanto {runId}`, Tipe Assignee `Employee`, Group `Branch Surabaya {runId}`, Baris 1 `Motor Honda Vario {runId}`, Status baris `Assigned`.
  - DU-214-17: Assignment, ASG dengan baris Assigned untuk Assignee yang tidak punya cakupan Group: Assignee `Gita Lestari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kipas Angin Cosmos {runId}`, Status baris `Assigned`, Role `tanpa Role Assignment`, Cakupan Group Assignee `tidak ada`, What happened laporan `Baling-baling patah`, Foto laporan `satu foto`.
  - DU-214-18: Assignment, ASG Division dengan baris Assigned yang dilihat PIC: Assignee `Pemasaran {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Proyektor Hitachi {runId}`, Status baris `Assigned`, PIC `Wati Susanti {runId}`, Role PIC `tanpa Role Assignment`, Cakupan Group PIC `tidak ada`.
  - DU-214-19: User, Aktor Damaged: Nama `Dian Anggraeni {runId}`, Role `pemegang hak keputusan menu Damaged`, Cakupan Group `Head Office {runId}`.
  - DU-214-20: Assignment, ASG Division dengan laporan Damaged oleh PIC lama: Assignee `Logistik {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Forklift Toyota {runId}`, Status baris `Assigned`, PIC lama `Rudi Hartono {runId}`, PIC baru `Yanti Susanti {runId}`, What happened laporan `Garpu bengkok`, Foto laporan `satu foto`.
  - DU-214-21: Assignment, ASG dengan baris Waiting for Approval yang Assignee-nya juga eligible sebagai approver: Assignee `Mira Handayani {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Fujifilm {runId}`, Status baris `Waiting for Approval`, Pengaju `Rina Wijaya {runId}`, Approver eligible `Mira Handayani {runId}`.
  - DU-214-22: Assignment, ASG Division dengan laporan Damaged oleh PIC lama yang dibatalkan pelapornya sendiri: Assignee `Keuangan {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Brankas Fireproof {runId}`, Status baris `Assigned`, PIC lama `Sigit Purnomo {runId}`, PIC baru `Tia Anggraini {runId}`, What happened laporan `Pintu macet`, Foto laporan `satu foto`.
  - DU-214-23: Assignment, ASG Division dengan laporan Missing oleh PIC lama: Assignee `Produksi {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Tablet Lenovo Tab {runId}`, Status baris `Assigned`, PIC lama `Umar Hakim {runId}`, PIC baru `Vina Oktaviani {runId}`.
  - DU-214-24: Assignment, ASG Division dengan laporan Damaged oleh PIC lama yang dinonaktifkan: Assignee `Gudang {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Mesin Fotokopi Ricoh {runId}`, Status baris `Assigned`, PIC lama `Wahyu Hidayat {runId}`, What happened laporan `Roller macet`, Foto laporan `satu foto`.
  - DU-214-25: User, Aktor Missing: Nama `Maya Sari {runId}`, Role `pemegang hak keputusan menu Missing`, Cakupan Group `Head Office {runId}`.
- Kondisi:
  - Role Transaksi sub-tab Borrowing & Assignment dipegang Aktor Assignment di atas menurut cakupan Group masing-masing.

## Test Steps

### Scan dan Save Draft atas aset di luar cakupan
1. Agus memindai tag aset `Laptop HP Pavilion {runId}` milik Group `Head Office {runId}` saat menambahkannya ke form Assignment Request pada DU-214-6
2. Verifikasi pemindaian ditolak dengan pesan `This asset belongs to [Group].` tanpa identitas atau atribut aset, dan aset tidak ditambahkan
3. Agus mengirim permintaan Save Draft langsung ke server untuk Assignee `Budi Santoso {runId}` dengan aset `Laptop HP Pavilion {runId}`
4. Verifikasi permintaan ditolak server karena aset di luar cakupan Agus dan tidak ada Draft yang tersimpan

### Submit Draft yang memuat aset di luar cakupan
5. Agus membuka Draft `Budi Santoso {runId}` pada DU-214-7 yang memuat `Laptop HP Pavilion {runId}` dari Group `Head Office {runId}` dan `Mobil Toyota Avanza {runId}` dari Group `Branch Surabaya {runId}`
6. Agus mengirim permintaan Submit atas Draft itu langsung ke server
7. Verifikasi permintaan ditolak server, baris `Laptop HP Pavilion {runId}` ditandai `Outside your groups`, dan tidak ada ASG yang terbentuk

### Aksi tulis dari aktor tanpa hak ditolak walau UI dilewati
8. Mila mengirim permintaan Submit langsung ke server untuk Assignee `Budi Santoso {runId}` dengan aset `Laptop Lenovo V14 {runId}` dan Purpose `Kebutuhan kerja` pada DU-214-8
9. Verifikasi permintaan ditolak server, tidak ada ASG terbentuk, dan aset `Laptop Lenovo V14 {runId}` tetap `Available`
10. Mila mengirim permintaan Save Draft langsung ke server untuk Assignee `Budi Santoso {runId}` dengan aset `Monitor Samsung S27 {runId}` pada DU-214-9
11. Verifikasi permintaan ditolak server dan tidak ada Draft yang tersimpan
12. Mila mengirim permintaan Handover langsung ke server untuk baris `Printer Epson L120 {runId}` pada DU-214-10
13. Verifikasi permintaan ditolak server dan baris `Printer Epson L120 {runId}` tetap `Waiting for Handover`
14. Mila mengirim permintaan Cancel langsung ke server untuk baris `Printer Epson L120 {runId}`
15. Verifikasi permintaan ditolak server dan baris `Printer Epson L120 {runId}` tetap `Waiting for Handover`
16. Mila mengirim permintaan Unassign langsung ke server untuk baris `Proyektor BenQ MX {runId}` pada DU-214-11
17. Verifikasi permintaan ditolak server dan baris `Proyektor BenQ MX {runId}` tetap `Assigned`
18. Mila mengirim permintaan Change PIC langsung ke server untuk ASG DU-214-12 dari `Indah Permata {runId}` menjadi `Joko Susilo {runId}`
19. Verifikasi permintaan ditolak server dan PIC ASG itu tetap `Indah Permata {runId}`
20. Nina mengirim keputusan Approve langsung ke server untuk baris `Speaker Bose {runId}` pada DU-214-14
21. Verifikasi permintaan ditolak server karena Nina bukan Approver dan baris `Speaker Bose {runId}` tetap `Waiting for Approval`

### Unassign oleh Aktor Group lain ditolak dan Group asal diberi tahu
22. Agus mengirim permintaan Unassign untuk baris `Genset Yamaha {runId}` pada DU-214-15 yang berada di Group asal `Head Office {runId}`
23. Verifikasi permintaan ditolak server dan baris `Genset Yamaha {runId}` tetap `Assigned`
24. Verifikasi Aktor Assignment Group asal `Rina Wijaya {runId}` menerima notifikasi `assignment_pickup_needed` karena Unassign oleh Aktor Group lain ditolak

### Cakupan baca dan Role Transaksi
25. Mila membaca daftar ASG
26. Verifikasi ASG Group `Branch Surabaya {runId}` milik `Hadi Susanto {runId}` pada DU-214-16 tidak terbaca Mila karena di luar cakupan Group
27. Oki mengirim permintaan Submit langsung ke server untuk Assignee `Budi Santoso {runId}` dengan aset `Laptop Lenovo V14 {runId}` dan Purpose `Kebutuhan kerja` pada DU-214-8
28. Verifikasi permintaan ditolak server karena Oki hanya memegang Update Manage asset & TAG tanpa Role Transaksi sub-tab Borrowing & Assignment
29. Mila mengirim permintaan Submit langsung ke server tanpa melalui UI untuk Assignee `Budi Santoso {runId}` dengan aset `Monitor Samsung S27 {runId}` dan Purpose `Kebutuhan kerja` pada DU-214-9
30. Verifikasi akses Monitoring & Report mengikuti matriks aksi per role sehingga aksi tulis ditolak
31. Verifikasi semua aksi Assignment di atas ditegakkan server dan UI Hidden atau Disabled bukan pengganti gate server

### Assignee dan PIC melihat aset tanpa cakupan Group
32. Assignee `Gita Lestari {runId}` pada DU-214-17 membuka daftar aset yang ditugaskan kepadanya
33. Verifikasi baris `Kipas Angin Cosmos {runId}` terlihat oleh Assignee walau tidak punya cakupan Group apa pun
34. PIC `Wati Susanti {runId}` pada DU-214-18 membuka daftar aset yang ditugaskan kepada `Pemasaran {runId}`
35. Verifikasi baris `Proyektor Hitachi {runId}` terlihat oleh PIC dengan penanda `On behalf of [Division]` walau PIC tidak punya cakupan Group apa pun

### Aksi Assignee dan PIC terbatas
36. Assignee `Citra Dewi {runId}` pada DU-214-10 mengirim permintaan Cancel langsung ke server untuk baris `Printer Epson L120 {runId}`
37. Verifikasi permintaan ditolak server karena aksi Assignee terbatas pada Confirm, Report Damaged, Report Missing, Cancel Damage Report, dan Cancel Missing Report, dan baris `Printer Epson L120 {runId}` tetap `Waiting for Handover`
38. Assignee `Gita Lestari {runId}` melaporkan aset `Kipas Angin Cosmos {runId}` rusak dari daftar asetnya dengan What happened `Baling-baling patah` dan satu foto
39. Assignee `Gita Lestari {runId}` membatalkan laporan miliknya yang masih `Waiting for Confirmation`
40. Verifikasi laporan milik Assignee itu berstatus dibatalkan dan baris tetap `Assigned`

### Laporan PIC lama tidak dapat dibatalkan siapa pun
41. PIC lama `Rudi Hartono {runId}` pada DU-214-20 melaporkan aset `Forklift Toyota {runId}` rusak dengan What happened `Garpu bengkok` dan satu foto
42. Rina mengganti PIC ASG DU-214-20 menjadi `Yanti Susanti {runId}`
43. PIC baru `Yanti Susanti {runId}` mengirim permintaan Cancel Damage Report atas laporan PIC lama
44. Verifikasi permintaan ditolak server karena laporan PIC lama tidak dapat dibatalkan siapa pun setelah PIC berganti
45. Rina mengirim permintaan Cancel Damage Report atas laporan PIC lama
46. Verifikasi permintaan ditolak server dan laporan tetap `Waiting for Confirmation`
47. Dian sebagai Aktor Damaged memutuskan laporan itu
48. Verifikasi laporan itu menjadi final hanya oleh keputusan Aktor Damaged

### Self-approval guard pada keputusan approval
49. Mira mengirim keputusan Approve langsung ke server untuk baris `Kamera Fujifilm {runId}` pada DU-214-21 yang Assignee-nya adalah Mira sendiri
50. Verifikasi permintaan ditolak server karena Assignee dikeluarkan dari daftar approver eligible dan baris tetap `Waiting for Approval`

### Laporan Damaged PIC lama tidak dapat dibatalkan pelapornya sendiri setelah PIC berganti
51. PIC lama `Sigit Purnomo {runId}` pada DU-214-22 melaporkan aset `Brankas Fireproof {runId}` rusak dengan What happened `Pintu macet` dan satu foto
52. Rina mengganti PIC ASG DU-214-22 menjadi `Tia Anggraini {runId}`
53. PIC lama `Sigit Purnomo {runId}` mengirim permintaan Cancel Damage Report atas laporannya sendiri
54. Verifikasi permintaan ditolak server karena laporan PIC lama tidak dapat dibatalkan siapa pun setelah PIC berganti dan laporan tetap `Waiting for Confirmation`

### Laporan Missing PIC lama tidak dapat dibatalkan dan diputuskan Aktor Missing
55. PIC lama `Umar Hakim {runId}` pada DU-214-23 melaporkan aset `Tablet Lenovo Tab {runId}` hilang
56. Rina mengganti PIC ASG DU-214-23 menjadi `Vina Oktaviani {runId}`
57. PIC baru `Vina Oktaviani {runId}` mengirim permintaan Cancel Missing Report atas laporan PIC lama
58. Verifikasi permintaan ditolak server dan laporan tetap `Waiting for Confirmation`
59. PIC lama `Umar Hakim {runId}` mengirim permintaan Cancel Missing Report atas laporannya sendiri
60. Verifikasi permintaan ditolak server dan laporan tetap `Waiting for Confirmation`
61. Maya sebagai Aktor Missing memutuskan laporan itu
62. Verifikasi laporan itu menjadi final hanya oleh keputusan Aktor Missing

### Laporan PIC lama yang dinonaktifkan tidak dapat dibatalkan siapa pun
63. PIC lama `Wahyu Hidayat {runId}` pada DU-214-24 melaporkan aset `Mesin Fotokopi Ricoh {runId}` rusak dengan What happened `Roller macet` dan satu foto
64. PIC lama `Wahyu Hidayat {runId}` dinonaktifkan
65. Rina mengirim permintaan Cancel Damage Report atas laporan PIC lama itu
66. Verifikasi permintaan ditolak server dan laporan tetap `Waiting for Confirmation`

### Aksi Assignee dan PIC di luar daftar ditolak pada state yang sah bagi Aktor Assignment
67. Assignee `Gita Lestari {runId}` pada DU-214-17 mengirim permintaan Unassign langsung ke server untuk baris `Kipas Angin Cosmos {runId}`
68. Verifikasi permintaan ditolak server karena pengirimnya Assignee dan baris `Kipas Angin Cosmos {runId}` tetap `Assigned`
69. PIC `Indah Permata {runId}` pada DU-214-12 mengirim permintaan Cancel langsung ke server untuk baris `Genset Perkins {runId}`
70. Verifikasi permintaan ditolak server karena pengirimnya PIC dan baris `Genset Perkins {runId}` tetap `Waiting for Handover`
71. PIC `Indah Permata {runId}` mengirim permintaan Handover langsung ke server untuk baris `Genset Perkins {runId}`
72. Verifikasi permintaan ditolak server karena pengirimnya PIC dan baris `Genset Perkins {runId}` tetap `Waiting for Handover`
73. PIC `Indah Permata {runId}` mengirim permintaan Change PIC langsung ke server untuk ASG DU-214-12 dari `Indah Permata {runId}` menjadi `Joko Susilo {runId}`
74. Verifikasi permintaan ditolak server karena pengirimnya PIC dan PIC ASG itu tetap `Indah Permata {runId}`
75. PIC `Wati Susanti {runId}` pada DU-214-18 mengirim permintaan Unassign langsung ke server untuk baris `Proyektor Hitachi {runId}`
76. Verifikasi permintaan ditolak server karena pengirimnya PIC dan baris `Proyektor Hitachi {runId}` tetap `Assigned`

### Penolakan Unassign lintas Group tidak mencatat log
77. Agus mengirim kembali permintaan Unassign untuk baris `Genset Yamaha {runId}` pada DU-214-15
78. Verifikasi permintaan ditolak server dan Assignment Log baris `Genset Yamaha {runId}` tidak bertambah dibanding sebelum permintaan itu
