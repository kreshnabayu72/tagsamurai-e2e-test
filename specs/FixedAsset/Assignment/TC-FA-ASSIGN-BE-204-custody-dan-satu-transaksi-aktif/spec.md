---
id: TC-FA-ASSIGN-BE-204-custody-dan-satu-transaksi-aktif
title: "Custody aset dan satu transaksi aktif per aset"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["V-ASG-02", "§9.2#p33", "§9.4.3#b4", "§10#r1", "§9.7#r1", "§9.7#r2", "§9.7#r3", "§9.7#r4", "§9.7#r5", "§9.7#r6", "§9.7#r7", "§9.7#r8", "§9.7#r9", "§9.7#r10", "§9.7#r11", "§9.7#r12", "ASSIGN-LOGIC-04a", "ASSIGN-LOGIC-04b", "ASSIGN-LOGIC-04c", "ASSIGN-LOGIC-04d", "ASSIGN-LOGIC-04e", "ASSIGN-LOGIC-04f", "ASSIGN-LOGIC-04g"]
smoke: []
dependsOn: []
trace:
  "V-ASG-02": [9, 20, 23]
  "§9.2#p33": [11, 14, 16, 18, 23, 24, 26, 29, 91, 94, 96, 97, 99]
  "§9.4.3#b4": [20, 21, 23]
  "§10#r1": [11, 21]
  "§9.7#r1": [11, 14, 16, 18]
  "§9.7#r2": 32
  "§9.7#r3": [30, 35, 37, 40, 43, 85]
  "§9.7#r4": [82, 83, 87]
  "§9.7#r5": [2, 3, 4, 5]
  "§9.7#r6": [53, 54, 55, 59, 60]
  "§9.7#r7": [49, 50, 51]
  "§9.7#r8": [44, 45, 46, 47]
  "§9.7#r9": [74, 75, 76, 77]
  "§9.7#r10": [66, 67]
  "§9.7#r11": [63, 64]
  "§9.7#r12": [70, 71, 72]
  "ASSIGN-LOGIC-04a": [3, 7, 50]
  "ASSIGN-LOGIC-04b": 12
  "ASSIGN-LOGIC-04c": [7, 11, 37]
  "ASSIGN-LOGIC-04d": [14, 16, 18, 33]
  "ASSIGN-LOGIC-04e": 9
  "ASSIGN-LOGIC-04f": [32, 66]
  "ASSIGN-LOGIC-04g": [30, 35, 40, 43, 82, 85, 99]
owner: BE
---

# Custody aset dan satu transaksi aktif per aset

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Grup Custody {runId}` sebagai pengaju dan pemberi handover; Aktor Assignment kedua `Lina Marlina {runId}` dengan cakupan yang sama pada langkah yang menyebutnya. Approver `Rina Wijaya {runId}`. Pengelola plan dan pengelola status entitas pada langkah yang menyebutnya.
- Data:
  - DU-204-1: Category KC beserta Asset Name, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Photo at end `OFF`, Override Category Require approval `OFF`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`.
  - DU-204-2: Category KA beserta Asset Name, Category `Kategori Approval {runId}`, Asset Name `Nama Approval {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Photo at end `OFF`, Override Category Require approval `ON`, Override Category Approval type `Any one`, Override Category Allowed assignee Employee `ON`.
  - DU-204-3: Category KK beserta Asset Name, Category `Kategori Konfirmasi {runId}`, Asset Name `Nama Konfirmasi {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `Yes`, Override Category Photo at start `OFF`, Override Category Photo at end `OFF`, Override Category Require approval `OFF`, Override Category Allowed assignee Employee `ON`.
  - DU-204-4: Group aset beserta approver, Group `Grup Custody {runId}`, Approver `Rina Wijaya {runId}`.
  - DU-204-5: Assignee Employee dengan akun login, Name `Budi Santoso {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-204-6: Assignee Employee kedua dengan akun login, Name `Tono Hartono {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-204-7: Aktor Assignment kedua, Name `Lina Marlina {runId}`, Role `Asset Admin`, Group `Grup Custody {runId}`, Status `Aktif`, berhak mengajukan transaksi `Borrow`, `Transfer`, dan `Disposal` atas aset pada Group `Grup Custody {runId}`.
  - DU-204-8: Approver aset, Name `Rina Wijaya {runId}`, Role Transaksi `Approver`, Status `Aktif`.
  - DU-204-9: PIC lama yang sudah dinonaktifkan, Name `Joko Prasetyo {runId}`, Division `Gudang {runId}`, Status `Nonaktif`.
  - DU-204-10: PIC pengganti ber-akun login, Name `Wati Susanti {runId}`, Division `Gudang {runId}`, Status `Aktif`, Akun login `Ada`.
  - DU-204-11: Division Assignee, Division `Gudang {runId}`.
  - DU-204-12: Aset Aset Draft Kunci, Name `Aset Draft Kunci {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-13: Aset Aset Submit, Name `Aset Submit {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-14: Aset Aset Serentak, Name `Aset Serentak {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-15: Aset Aset Hilang, Name `Aset Hilang {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-16: Aset Aset Cancel, Name `Aset Cancel {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-17: Aset Aset Reject, Name `Aset Reject {runId}`, Group `Grup Custody {runId}`, Category `Kategori Approval {runId}`, Asset Name `Nama Approval {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-18: Aset Aset Approve, Name `Aset Approve {runId}`, Group `Grup Custody {runId}`, Category `Kategori Approval {runId}`, Asset Name `Nama Approval {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-19: Aset Aset Draft Tambah, Name `Aset Draft Tambah {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-20: Aset Aset Konfirmasi Satu, Name `Aset Konfirmasi Satu {runId}`, Group `Grup Custody {runId}`, Category `Kategori Konfirmasi {runId}`, Asset Name `Nama Konfirmasi {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-21: Aset Aset Konfirmasi Dua, Name `Aset Konfirmasi Dua {runId}`, Group `Grup Custody {runId}`, Category `Kategori Konfirmasi {runId}`, Asset Name `Nama Konfirmasi {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-22: Aset Aset Tanpa PIC, Name `Aset Tanpa PIC {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `In Assignment Process`, Condition `Normal`.
  - DU-204-23: Aset Aset Wind Down, Name `Aset Wind Down {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-24: Aset Aset Plan Menunggu, Name `Aset Plan Menunggu {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-25: Aset Aset Plan Draft, Name `Aset Plan Draft {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-26: Aset Aset Suspended, Name `Aset Suspended {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-27: ASG Division tanpa PIC aktif, Assignee `Gudang {runId}`, Tipe Assignee `Division`, PIC `Joko Prasetyo {runId}`, Status PIC `Nonaktif`, Aset `Aset Tanpa PIC {runId}`, Status baris `Waiting for Handover`.
  - DU-204-28: Input pengajuan untuk Assignee Employee, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Note `Penugasan uji custody {runId}`, Purpose `Daily work`.
  - DU-204-29: Input pengajuan untuk Assignee Tono, Assignee `Tono Hartono {runId}`, Tipe Assignee `Employee`, Purpose `Daily work`.
  - DU-204-30: Input PIC pengganti, PIC `Wati Susanti {runId}`.
  - DU-204-31: Aset Aset Jendela Konfirmasi, Name `Aset Jendela Konfirmasi {runId}`, Group `Grup Custody {runId}`, Category `Kategori Konfirmasi {runId}`, Asset Name `Nama Konfirmasi {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-32: Aset Aset Draft Massal Satu, Name `Aset Draft Massal Satu {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-204-33: Aset Aset Draft Massal Dua, Name `Aset Draft Massal Dua {runId}`, Group `Grup Custody {runId}`, Category `Kategori Custody {runId}`, Asset Name `Nama Custody {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
- Kondisi:
  - Level Feature Suite Assignment pada plan adalah `Full` pada awal spec.
  - Status entitas aktor adalah aktif pada awal spec.
  - Setiap aset berada di Custody `Available` kecuali yang disebut lain di Data, dan tidak berada di ASG aktif maupun Draft mana pun.
  - Transaction timeout berlaku menurut Transaction Settings tab Assign.
  - Jendela konfirmasi Handover bernilai `15 menit`.

## Test Steps

### Draft tidak mengunci aset
1. Aktor Assignment menyimpan Draft untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan uji custody {runId}` dan aset `Aset Draft Kunci {runId}` dengan Purpose `Daily work`
2. Verifikasi Draft tersimpan dengan header dan baris tanpa nomor ASG
3. Verifikasi Custody aset `Aset Draft Kunci {runId}` tetap `Available` setelah Draft disimpan
4. Verifikasi penyimpanan Draft tercatat di Transaction admin log
5. Verifikasi penyimpanan Draft tidak memicu notifikasi
6. Aktor Assignment kedua `Lina Marlina {runId}` mengajukan Submit untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Draft Kunci {runId}`
7. Verifikasi Submit berhasil walau aset `Aset Draft Kunci {runId}` ada di Draft, karena Draft tidak mengunci aset, dan Custody aset berubah menjadi `In Assignment Process`

### Kelayakan Draft dievaluasi ulang saat Submit
8. Aktor Assignment mengajukan Submit atas Draft yang memuat aset `Aset Draft Kunci {runId}`
9. Verifikasi Submit ditolak dengan pesan `This asset is already in [Transaction ID].` dengan Transaction ID ASG yang diajukan `Lina Marlina {runId}`, karena kelayakan dievaluasi ulang saat Submit

### Submit mengunci aset secara atomik bersama status baris
10. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Submit {runId}`
11. Verifikasi baris aset `Aset Submit {runId}` berstatus `Waiting for Handover` dan Custody aset adalah `In Assignment Process`, selalu berpasangan setelah Submit selesai
12. Verifikasi Custody aset `Aset Submit {runId}` terbaca sebagai bagian status global aset, terpisah dari status baris yang merupakan status transaksi
13. Aktor Assignment kedua `Lina Marlina {runId}` mengajukan transaksi `Borrow` atas aset `Aset Submit {runId}`
14. Verifikasi transaksi `Borrow` atas aset `Aset Submit {runId}` ditolak dan Custody tetap `In Assignment Process`, karena aset tidak boleh masuk transaksi lain selama `In Assignment Process`
15. Aktor Assignment kedua `Lina Marlina {runId}` mengajukan transaksi `Transfer` atas aset `Aset Submit {runId}`
16. Verifikasi transaksi `Transfer` atas aset `Aset Submit {runId}` ditolak dan Custody tetap `In Assignment Process`, karena aset tidak boleh masuk transaksi lain selama `In Assignment Process`
17. Aktor Assignment kedua `Lina Marlina {runId}` mengajukan transaksi `Disposal` atas aset `Aset Submit {runId}`
18. Verifikasi transaksi `Disposal` atas aset `Aset Submit {runId}` ditolak dan Custody tetap `In Assignment Process`, karena aset tidak boleh masuk transaksi lain selama `In Assignment Process`
19. Aktor Assignment kedua `Lina Marlina {runId}` mengajukan Submit untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Submit {runId}`
20. Verifikasi Submit ditolak dengan pesan `This asset is already in [Transaction ID].` dengan Transaction ID ASG milik aset `Aset Submit {runId}`
21. Verifikasi hanya satu ASG aktif yang memuat aset `Aset Submit {runId}` dan Custody tetap `In Assignment Process`

### Dua Submit bersamaan atas aset yang sama
22. Aktor Assignment dan Aktor Assignment kedua `Lina Marlina {runId}` mengajukan Submit secara bersamaan atas aset `Aset Serentak {runId}`, masing-masing untuk Assignee `Budi Santoso {runId}` dan `Tono Hartono {runId}`
23. Verifikasi jumlah ASG aktif yang memuat aset `Aset Serentak {runId}` tepat satu, dan Submit yang lain ditolak dengan pesan `This asset is already in [Transaction ID].`
24. Verifikasi Custody aset `Aset Serentak {runId}` adalah `In Assignment Process`

### Report Damaged sebelum Handover ditolak dan Report Missing membatalkan baris
25. Aktor Assignment melakukan `Report Damaged` atas aset `Aset Submit {runId}` yang Custody-nya `In Assignment Process`
26. Verifikasi laporan ditolak, Condition aset `Aset Submit {runId}` tetap `Normal`, dan baris tetap `Waiting for Handover`
27. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Hilang {runId}`
28. Aktor Assignment melakukan `Report Missing` atas aset `Aset Hilang {runId}` yang barisnya belum diserahkan
29. Verifikasi baris aset `Aset Hilang {runId}` berstatus `Canceled` oleh `System` dengan alasan `Asset reported missing`, dan Condition aset `Missing`
30. Verifikasi Custody aset `Aset Hilang {runId}` kembali `Available` setelah baris ditutup otomatis

### Handover mengubah Custody menjadi Assigned
31. Aktor Assignment menyelesaikan handover aset `Aset Submit {runId}` tanpa konfirmasi Assignee
32. Verifikasi baris aset `Aset Submit {runId}` berstatus `Assigned`, Custody `Assigned`, dan Held by adalah Assignee `Budi Santoso {runId}`
33. Verifikasi aset `Aset Submit {runId}` yang `Assigned` tidak ditawarkan untuk Submit ASG lain: Submit atas aset itu ditolak dan Custody tetap `Assigned`

### Unassign mengembalikan Custody ke Available dan aset kembali ke pool
34. Aktor Assignment melakukan Unassign atas aset `Aset Submit {runId}`
35. Verifikasi Custody aset `Aset Submit {runId}` kembali `Available`
36. Aktor Assignment mengajukan Submit untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Submit {runId}`
37. Verifikasi Submit atas aset `Aset Submit {runId}` berhasil karena aset sudah kembali ke pool, dan Custody berubah menjadi `In Assignment Process`

### Cancel mengembalikan Custody ke Available
38. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Cancel {runId}`
39. Pengaju melakukan Cancel Assignment pada baris aset `Aset Cancel {runId}`
40. Verifikasi baris aset `Aset Cancel {runId}` berstatus `Canceled` dan Custody `Available`

### Approve dan Reject memengaruhi Custody sesuai keputusan
41. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Reject {runId}` dan `Aset Approve {runId}`
42. Approver `Rina Wijaya {runId}` memutuskan dalam satu pengajuan: Reject aset `Aset Reject {runId}` dan Approve aset `Aset Approve {runId}`
43. Verifikasi baris aset `Aset Reject {runId}` berstatus `Rejected` dan Custody `Available`
44. Verifikasi baris aset `Aset Approve {runId}` berubah dari `Waiting for Approval` menjadi `Waiting for Handover`
45. Verifikasi Custody aset `Aset Approve {runId}` tetap `In Assignment Process` setelah Approve
46. Verifikasi batas serah terima baris aset `Aset Approve {runId}` mulai dihitung sejak keputusan Approve
47. Verifikasi Assignment Log memuat node `Approved by [Approver]` dan keputusan tercatat di Transaction admin log

### Add to Assignment Draft dan Delete Draft tidak mengubah Custody
48. Aktor Assignment menambahkan aset `Aset Draft Tambah {runId}` ke Draft baru untuk Assignee `Budi Santoso {runId}` lewat `Add to Assignment Draft`
49. Verifikasi Draft bertambah satu baris untuk aset `Aset Draft Tambah {runId}`
50. Verifikasi Custody aset `Aset Draft Tambah {runId}` tetap `Available` setelah ditambahkan ke Draft
51. Verifikasi penambahan baris Draft tercatat di Transaction admin log
52. Aktor Assignment menghapus Draft tersebut
53. Verifikasi Draft dihapus tanpa status akhir
54. Verifikasi Custody aset `Aset Draft Tambah {runId}` tetap `Available` setelah Draft dihapus
55. Verifikasi penghapusan Draft tercatat di Transaction admin log
56. Aktor Assignment menyimpan Draft untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Draft Massal Satu {runId}` dan Purpose `Daily work`
57. Aktor Assignment menyimpan Draft untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Draft Massal Dua {runId}` dan Purpose `Daily work`
58. Aktor Assignment menghapus kedua Draft tersebut sekaligus lewat Delete bulk
59. Verifikasi kedua Draft dihapus tanpa status akhir
60. Verifikasi Custody aset `Aset Draft Massal Satu {runId}` dan `Aset Draft Massal Dua {runId}` tetap `Available` setelah Delete bulk

### Konfirmasi handover: sesi, konfirmasi sebagian, dan pembatalan sesi
61. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Konfirmasi Satu {runId}` dan `Aset Konfirmasi Dua {runId}`
62. Aktor Assignment menekan `Request Confirmation` untuk kedua aset
63. Verifikasi terbentuk satu sesi konfirmasi aktif untuk ASG tersebut, dan status baris serta Custody kedua aset belum berubah
64. Verifikasi notifikasi `assignment_confirmation_required` dikirim ke Assignee
65. Assignee `Budi Santoso {runId}` mengonfirmasi penerimaan hanya aset `Aset Konfirmasi Satu {runId}` dengan aset `Aset Konfirmasi Dua {runId}` tidak dicentang
66. Verifikasi baris aset `Aset Konfirmasi Satu {runId}` berstatus `Assigned` dan Custody `Assigned`
67. Verifikasi baris aset `Aset Konfirmasi Dua {runId}` tetap `Waiting for Handover` dan Custody tetap `In Assignment Process`, dan Assignment Log memuat node `Handed over` serta `Confirmation not received`
68. Aktor Assignment menekan `Request Confirmation` untuk aset `Aset Konfirmasi Dua {runId}`
69. Aktor Assignment menekan `Cancel Request` pada sesi konfirmasi tersebut
70. Verifikasi sesi konfirmasi batal
71. Verifikasi baris aset `Aset Konfirmasi Dua {runId}` tetap `Waiting for Handover`
72. Verifikasi Assignment Log memuat node `Confirmation not received`

### Change PIC menghapus penanda No PIC
73. Aktor Assignment melakukan `Change PIC` pada ASG Division milik DU-204-27 dengan PIC baru `Wati Susanti {runId}`
74. Verifikasi PIC pada header ASG tersebut adalah `Wati Susanti {runId}` dan penanda `No PIC` hilang
75. Verifikasi notifikasi `assignment_pic_assigned` dikirim ke PIC baru `Wati Susanti {runId}` atas baris aktif ASG tersebut
76. Verifikasi Task `assignment_pic_required` untuk ASG tersebut selesai karena Change PIC
77. Verifikasi Assignment Log memuat node `PIC changed` dan perubahan tercatat di Transaction admin log

### Downgrade ke level None di T-0
78. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Wind Down {runId}` dan `Aset Plan Menunggu {runId}`
79. Aktor Assignment menyelesaikan handover aset `Aset Wind Down {runId}` tanpa konfirmasi Assignee
80. Aktor Assignment menyimpan Draft untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Plan Draft {runId}` dan Purpose `Daily work`
81. Pengelola plan menurunkan Feature Suite Assignment ke level `None` dan T-0 tercapai
82. Verifikasi baris aset `Aset Plan Menunggu {runId}` berstatus `Canceled` oleh `System` dengan alasan `Assignment not available on plan`, Custody `Available`, dan tidak ada Draft baru
83. Verifikasi Draft yang memuat aset `Aset Plan Draft {runId}` dihapus
84. Aktor Assignment melakukan `Mark as Unassigned` atas aset `Aset Wind Down {runId}`
85. Verifikasi baris aset `Aset Wind Down {runId}` berstatus `Unassigned` dan Custody `Available`
86. Pengelola plan menaikkan kembali Feature Suite Assignment ke level `Full`
87. Verifikasi baris aset `Aset Plan Menunggu {runId}` tetap `Canceled` dan Draft yang memuat aset `Aset Plan Draft {runId}` tidak dipulihkan

### Entitas Suspended menolak aksi tulis dan job sistem tetap berjalan
88. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Suspended {runId}`
89. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Jendela Konfirmasi {runId}`
90. Aktor Assignment menekan `Request Confirmation` untuk aset `Aset Jendela Konfirmasi {runId}`
91. Verifikasi terbentuk satu sesi konfirmasi aktif untuk aset `Aset Jendela Konfirmasi {runId}`
92. Pengelola status entitas mengubah status entitas aktor menjadi `Suspended`
93. Aktor Assignment melakukan Cancel Assignment pada baris aset `Aset Suspended {runId}` dan mengajukan Submit untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Plan Draft {runId}`
94. Verifikasi kedua aksi tulis ditolak server, baris aset `Aset Suspended {runId}` tetap `Waiting for Handover`, Custody tetap `In Assignment Process`, dan tidak ada entri log baru
95. Waktu berlalu melewati jendela konfirmasi `15 menit` sejak sesi konfirmasi aset `Aset Jendela Konfirmasi {runId}` dimulai
96. Verifikasi sesi konfirmasi aset `Aset Jendela Konfirmasi {runId}` batal oleh `System` dan baris tetap `Waiting for Handover`, karena job sistem jendela konfirmasi tetap berjalan pada entitas `Suspended`
97. Verifikasi Assignment Log aset `Aset Jendela Konfirmasi {runId}` memuat node `Confirmation not received` oleh `System`
98. Waktu berlalu melewati Transaction timeout sejak baris aset `Aset Suspended {runId}` masuk `Waiting for Handover`
99. Verifikasi baris aset `Aset Suspended {runId}` ditutup `Canceled` oleh `System` dengan alasan `Not handed over`, karena job sistem tetap berjalan pada entitas `Suspended`
100. Pengelola status entitas mengembalikan status entitas aktor menjadi aktif
