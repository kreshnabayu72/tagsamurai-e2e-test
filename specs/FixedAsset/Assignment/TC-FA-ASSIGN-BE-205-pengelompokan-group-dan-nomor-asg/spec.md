---
id: TC-FA-ASSIGN-BE-205-pengelompokan-group-dan-nomor-asg
title: "Pengelompokan per Group asal dan penomoran ASG"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.2#b17", "§9.2#b18", "§9.2#b19", "§9.2#b20", "§9.2#b21", "§9.2#p36", "§9.2#p38", "§9.2#p40", "§9.2#p41", "§9.2#p42", "§9.2#p43", "§9.5#r12", "§9.5#r13", "§10#r2", "ASSIGN-LOGIC-05a", "ASSIGN-LOGIC-05b", "ASSIGN-LOGIC-05c", "ASSIGN-LOGIC-05d", "ASSIGN-LOGIC-05e", "ASSIGN-LOGIC-05g", "ASSIGN-LOGIC-05h", "ASSIGN-LOGIC-05i"]
smoke: []
dependsOn: []
trace:
  "§9.2#b17": [6, 12, 13, 24, 35, 36]
  "§9.2#b18": [7, 9]
  "§9.2#b19": [2, 3]
  "§9.2#b20": [15, 22]
  "§9.2#b21": [17, 18, 19]
  "§9.2#p36": 5
  "§9.2#p38": 5
  "§9.2#p40": 5
  "§9.2#p41": 7
  "§9.2#p42": 8
  "§9.2#p43": 10
  "§9.5#r12": [11, 12, 29]
  "§9.5#r13": [2, 29]
  "§10#r2": 6
  "ASSIGN-LOGIC-05a": [6, 32]
  "ASSIGN-LOGIC-05b": 6
  "ASSIGN-LOGIC-05c": [13, 24]
  "ASSIGN-LOGIC-05d": 11
  "ASSIGN-LOGIC-05e": 26
  "ASSIGN-LOGIC-05g": [2, 32]
  "ASSIGN-LOGIC-05h": [7, 10]
  "ASSIGN-LOGIC-05i": 14
owner: BE
---

# Pengelompokan per Group asal dan penomoran ASG

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Grup Asal A {runId}` dan `Grup Asal B {runId}`, sebagai pengaju. Approver `Rina Wijaya {runId}` pada kedua Group. Pengelola plan pada langkah yang menyebutnya.
- Data:
  - DU-205-1: Category KP beserta Asset Name, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Require approval `OFF`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`.
  - DU-205-2: Category KA beserta Asset Name, Category `Kategori Pecah Approval {runId}`, Asset Name `Nama Pecah Approval {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Require approval `ON`, Override Category Approval type `Any one`, Override Category Allowed assignee Employee `ON`.
  - DU-205-3: Group asal A beserta approver, Group `Grup Asal A {runId}`, Approver `Rina Wijaya {runId}`.
  - DU-205-4: Group asal B beserta approver, Group `Grup Asal B {runId}`, Approver `Rina Wijaya {runId}`.
  - DU-205-5: Assignee Employee dengan akun login, Name `Budi Santoso {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-205-6: Approver pada Group asal A dan B, Name `Rina Wijaya {runId}`, Role Transaksi `Approver`, Status `Aktif`.
  - DU-205-7: PIC Division ber-akun login, Name `Joko Prasetyo {runId}`, Division `Gudang {runId}`, Status `Aktif`, Akun login `Ada`.
  - DU-205-8: Division Assignee dengan PIC, Division `Gudang {runId}`, PIC `Joko Prasetyo {runId}`.
  - DU-205-9: Aset Laptop Dell Latitude, Name `Laptop Dell Latitude {runId}`, Group `Grup Asal A {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-10: Aset Projector Epson EB-X49, Name `Projector Epson EB-X49 {runId}`, Group `Grup Asal A {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-11: Aset Camera Sony A7, Name `Camera Sony A7 {runId}`, Group `Grup Asal A {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-12: Aset Toyota Innova, Name `Toyota Innova {runId}`, Group `Grup Asal B {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-13: Aset Aset Approval Grup A, Name `Aset Approval Grup A {runId}`, Group `Grup Asal A {runId}`, Category `Kategori Pecah Approval {runId}`, Asset Name `Nama Pecah Approval {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-14: Aset Aset Approval Grup B, Name `Aset Approval Grup B {runId}`, Group `Grup Asal B {runId}`, Category `Kategori Pecah Approval {runId}`, Asset Name `Nama Pecah Approval {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-15: Aset Aset Division Grup A, Name `Aset Division Grup A {runId}`, Group `Grup Asal A {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-16: Aset Aset Division Grup B, Name `Aset Division Grup B {runId}`, Group `Grup Asal B {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-17: Aset Aset Baru Grup A, Name `Aset Baru Grup A {runId}`, Group `Grup Asal A {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-18: Aset Aset Rusak Grup B, Name `Aset Rusak Grup B {runId}`, Group `Grup Asal B {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Damaged`.
  - DU-205-19: Aset Aset Basic Grup A, Name `Aset Basic Grup A {runId}`, Group `Grup Asal A {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-20: Aset Aset Basic Grup B, Name `Aset Basic Grup B {runId}`, Group `Grup Asal B {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-21: Input form untuk Assignee Budi dengan Purpose per aset, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Note `Penugasan multi Group {runId}`, Purpose Laptop `Daily work`, Purpose Projector `Training`, Purpose Camera `Training`, Purpose Toyota Innova `Field visits`.
  - DU-205-22: Input form untuk Assignee Division, Assignee `Gudang {runId}`, Tipe Assignee `Division`, PIC `Joko Prasetyo {runId}`, Note `Penugasan Division multi Group {runId}`, Purpose `Daily work`.
  - DU-205-23: Input form umum untuk Assignee Budi, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Note `Penugasan uji nomor {runId}`, Purpose `Daily work`.
  - DU-205-24: Aset Aset Urutan Grup B, Name `Aset Urutan Grup B {runId}`, Group `Grup Asal B {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-205-25: Aset Aset Urutan Grup A, Name `Aset Urutan Grup A {runId}`, Group `Grup Asal A {runId}`, Category `Kategori Pecah {runId}`, Asset Name `Nama Pecah {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
- Kondisi:
  - Level Feature Suite Assignment pada plan adalah `Full` pada awal spec.
  - Setiap aset berada di Custody `Available` dan tidak berada di ASG aktif maupun Draft mana pun.

## Test Steps

### Draft tetap satu form dan belum dipecah
1. Aktor Assignment menyimpan Draft untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan multi Group {runId}`, memuat aset `Laptop Dell Latitude {runId}` dengan Purpose `Daily work`, aset `Projector Epson EB-X49 {runId}` dan `Camera Sony A7 {runId}` dengan Purpose `Training`, dan aset `Toyota Innova {runId}` dari Group `Grup Asal B {runId}` dengan Purpose `Field visits`
2. Verifikasi Draft tetap satu dokumen dengan empat baris dari dua Group, dan belum bernomor
3. Verifikasi belum ada ASG hasil pecahan sebelum Submit, karena pemecahan terjadi saat Submit

### Submit memecah Draft menjadi satu ASG per Group asal
4. Aktor Assignment mengajukan Submit atas Draft tersebut
5. Verifikasi Submit atas empat aset Assignee `Budi Santoso {runId}` menghasilkan hasil berikut: aset Group `Grup Asal A {runId}` menjadi satu ASG dan aset Group `Grup Asal B {runId}` menjadi ASG lain
6. Verifikasi satu Submit menghasilkan dua ASG, karena satu header hanya untuk satu Group dan kunci pengelompokan adalah Group asal aset
7. Verifikasi ASG yang memuat Group `Grup Asal A {runId}` berisi baris `Laptop Dell Latitude {runId}`, `Projector Epson EB-X49 {runId}`, dan `Camera Sony A7 {runId}` walau Purpose-nya berbeda, sehingga Purpose tidak memecah ASG
8. Verifikasi ASG lain memuat hanya baris `Toyota Innova {runId}` dari Group `Grup Asal B {runId}`
9. Verifikasi satu ASG memuat baris dengan Purpose `Daily work` dan baris dengan Purpose `Training`
10. Verifikasi tidak ada ASG yang dipecah berdasarkan Purpose
11. Verifikasi setiap ASG hasil pecahan mendapat Transaction ID `ASG-YYYY-NNNN` sendiri yang berbeda
12. Verifikasi Transaction ID ASG Group `Grup Asal A {runId}` lebih kecil daripada Transaction ID ASG Group `Grup Asal B {runId}`, mengikuti urutan kelompok di form
13. Verifikasi kedua ASG memiliki Assignee `Budi Santoso {runId}` yang sama dan Note `Penugasan multi Group {runId}` yang disalin ke setiap ASG
14. Verifikasi hasil baca kedua ASG tidak memuat penanda atau rujukan yang mengikat keduanya sebagai hasil satu Submit
15. Verifikasi Assignee `Budi Santoso {runId}` menerima satu notifikasi `assignment_ready_handover` gabungan untuk kedua ASG yang siap diserahkan pada hari yang sama

### Remind Assignee dikirim terpisah
16. Aktor Assignment menjalankan `Remind Assignee` untuk baris `Laptop Dell Latitude {runId}` yang `Waiting for Handover`
17. Verifikasi notifikasi `assignment_ready_handover` dikirim ulang untuk baris `Laptop Dell Latitude {runId}` sebagai notifikasi tersendiri, tidak digabung dengan notifikasi lain
18. Verifikasi status baris `Laptop Dell Latitude {runId}` tetap `Waiting for Handover` dan batas serah terima tidak berubah
19. Verifikasi Assignment Log baris `Laptop Dell Latitude {runId}` tidak memuat node baru akibat Remind Assignee

### Notifikasi hasil approval digabung per Assignee
20. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan uji nomor {runId}`, memuat aset `Aset Approval Grup A {runId}` dari Group `Grup Asal A {runId}` dan aset `Aset Approval Grup B {runId}` dari Group `Grup Asal B {runId}` dengan Purpose `Daily work`
21. Approver `Rina Wijaya {runId}` menyetujui kedua pengajuan pada hari yang sama
22. Verifikasi Assignee `Budi Santoso {runId}` menerima satu notifikasi `assignment_resolved` gabungan dan satu notifikasi `assignment_ready_handover` gabungan untuk kedua ASG yang diputuskan pada hari yang sama

### PIC dan Note sama untuk semua ASG hasil pecahan
23. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}`, Note `Penugasan Division multi Group {runId}`, dan aset `Aset Division Grup A {runId}` dan `Aset Division Grup B {runId}` dengan Purpose `Daily work`
24. Verifikasi kedua ASG hasil pecahan memiliki PIC `Joko Prasetyo {runId}` yang sama dan Note `Penugasan Division multi Group {runId}` yang disalin ke setiap ASG

### Satu baris gagal menggagalkan seluruh Submit
25. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Baru Grup A {runId}` dari Group `Grup Asal A {runId}` dan aset `Aset Rusak Grup B {runId}` dari Group `Grup Asal B {runId}` yang Condition-nya `Damaged`
26. Verifikasi Submit ditolak dengan pesan `This asset is Damaged and can't be assigned.` dan tidak ada ASG yang dibuat, termasuk untuk aset `Aset Baru Grup A {runId}` yang layak

### Nomor ASG tidak dipakai ulang walau ASG dibatalkan
27. Pengaju melakukan Cancel Assignment atas seluruh ASG yang memuat aset `Laptop Dell Latitude {runId}`
28. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan uji nomor {runId}`, memuat aset `Laptop Dell Latitude {runId}`, `Projector Epson EB-X49 {runId}`, dan `Camera Sony A7 {runId}` dengan Purpose `Daily work`
29. Verifikasi ASG baru mendapat Transaction ID `ASG-YYYY-NNNN` yang berbeda dan lebih besar daripada Transaction ID ASG yang dibatalkan, karena nomor diberikan saat Submit dan tidak dipakai ulang walau ASG dibatalkan

### Form multi-Group tetap dipecah pada level Basic
30. Pengelola plan menurunkan Feature Suite Assignment ke level `Basic`
31. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan uji nomor {runId}`, memuat aset `Aset Basic Grup A {runId}` dari Group `Grup Asal A {runId}` dan aset `Aset Basic Grup B {runId}` dari Group `Grup Asal B {runId}` dengan Purpose `Daily work`
32. Verifikasi form multi-Group diterima pada level `Basic` dan dipecah menjadi satu ASG per Group asal
33. Pengelola plan menaikkan kembali Feature Suite Assignment ke level `Full`

### Nomor ASG mengikuti urutan kelompok di form, bukan urutan abjad Group
34. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan uji nomor {runId}`, memuat aset `Aset Urutan Grup B {runId}` dari Group `Grup Asal B {runId}` pada urutan pertama di form dan aset `Aset Urutan Grup A {runId}` dari Group `Grup Asal A {runId}` pada urutan kedua, dengan Purpose `Daily work`
35. Verifikasi Submit menghasilkan satu ASG untuk Group `Grup Asal B {runId}` dan satu ASG untuk Group `Grup Asal A {runId}`
36. Verifikasi Transaction ID ASG Group `Grup Asal B {runId}` lebih kecil daripada Transaction ID ASG Group `Grup Asal A {runId}`, karena nomor mengikuti urutan kelompok di form dan bukan urutan abjad nama Group atau urutan pembuatan Group
