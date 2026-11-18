---
id: TC-FA-ASSIGN-BE-208-approval-aturan-server
title: "Aturan approval per aset: Any one, All, self-approval guard, dan reroute"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.2#b22", "§9.2#b23", "§9.2#b24", "§9.2#b25", "§9.2#b26", "§9.2#b27", "§9.2#b28", "§9.2#r19", "§9.2#r20", "§9.2#p45", "§9.2#p47", "§9.2#p49", "§9.2#p51", "§9.2#p52", "§9.2#p53", "§9.2#p54", "§9.2#p55", "§9.2#p56", "§9.2#p57", "F-ASSIGN-05.k2", "F-ASSIGN-05.k3", "EC-ASG-12", "EC-ASG-42", "§9.4.3#b5", "§10#r6", "ASSIGN-LOGIC-07a", "ASSIGN-LOGIC-07b", "ASSIGN-LOGIC-07c", "ASSIGN-LOGIC-07d", "ASSIGN-LOGIC-07e", "ASSIGN-LOGIC-07f", "ASSIGN-LOGIC-07g", "ASSIGN-LOGIC-07h", "ASSIGN-LOGIC-07i", "ASSIGN-LOGIC-07j", "ASSIGN-LOGIC-07k", "ASSIGN-LOGIC-07l", "ASSIGN-LOGIC-07n", "ASSIGN-LOGIC-07o", "ASSIGN-LOGIC-07p", "ASSIGN-LOGIC-07q", "ASSIGN-LOGIC-07s", "ASSIGN-LOGIC-07t", "ASSIGN-LOGIC-07u", "ASSIGN-LOGIC-07v", "ASSIGN-LOGIC-07w"]
smoke: []
dependsOn: []
trace:
  "§9.2#b22": [10, 11, 12]
  "§9.2#b23": [7, 26, 35, 47, 59, 95, 96, 110, 111]
  "§9.2#b24": [15, 74, 79, 98]
  "§9.2#b25": [82, 83]
  "§9.2#b26": [14, 34, 99]
  "§9.2#b27": [8, 9, 10, 31, 32]
  "§9.2#b28": [28, 55, 56]
  "§9.2#r19": [22, 23, 30, 42]
  "§9.2#r20": [24, 34, 43]
  "§9.2#p45": [23, 37, 42, 48, 50, 92]
  "§9.2#p47": 2
  "§9.2#p49": 2
  "§9.2#p51": 2
  "§9.2#p52": 3
  "§9.2#p53": 4
  "§9.2#p54": 5
  "§9.2#p55": [6, 8]
  "§9.2#p56": 13
  "§9.2#p57": 40
  "F-ASSIGN-05.k2": 15
  "F-ASSIGN-05.k3": [62, 66, 107]
  "EC-ASG-12": [17, 19, 66, 68, 98, 101, 102, 104]
  "EC-ASG-42": [62, 64, 107]
  "§9.4.3#b5": [17, 19, 68, 74, 79, 101, 104]
  "§10#r6": 23
  "ASSIGN-LOGIC-07a": [4, 82]
  "ASSIGN-LOGIC-07b": 17
  "ASSIGN-LOGIC-07c": [11, 86, 87, 88, 89]
  "ASSIGN-LOGIC-07d": [11, 87]
  "ASSIGN-LOGIC-07e": 25
  "ASSIGN-LOGIC-07f": [27, 36]
  "ASSIGN-LOGIC-07g": [4, 5]
  "ASSIGN-LOGIC-07h": 3
  "ASSIGN-LOGIC-07i": [28, 30, 56]
  "ASSIGN-LOGIC-07j": [55, 56]
  "ASSIGN-LOGIC-07k": [14, 66]
  "ASSIGN-LOGIC-07l": [23, 42, 45]
  "ASSIGN-LOGIC-07n": [24, 34]
  "ASSIGN-LOGIC-07o": [15, 72, 98, 99]
  "ASSIGN-LOGIC-07p": [72, 74, 76, 77, 79]
  "ASSIGN-LOGIC-07q": [62, 64, 66, 77, 102, 107]
  "ASSIGN-LOGIC-07s": 13
  "ASSIGN-LOGIC-07t": 25
  "ASSIGN-LOGIC-07u": [30, 32]
  "ASSIGN-LOGIC-07v": [31, 46]
  "ASSIGN-LOGIC-07w": 43
owner: BE
---

# Aturan approval per aset: Any one, All, self-approval guard, dan reroute

## Prerequisites
- Aktor: Aktor Assignment `Hendra Kusuma {runId}` (Asset Admin) dengan cakupan Group `Grup Approval {runId}`, `Grup Reroute {runId}`, `Grup Tunggal {runId}`, `Grup Division Approval {runId}`, `Grup Division Tunggal {runId}`, `Grup Satu Approver {runId}`, dan `Grup Cabut {runId}`, sebagai pengaju. Approver: `Rina Wijaya {runId}` dan `Agus Pratama {runId}`; approver `Bagas Reroute {runId}` pada Group `Grup Reroute {runId}`; approver `Wati Susanti {runId}` pada Group `Grup Division Approval {runId}` dan `Grup Division Tunggal {runId}`; Group Manager `Gita Manajer {runId}`. approver `Bayu Cabut {runId}` pada Group `Grup Cabut {runId}`; approver `Rina Wijaya {runId}` sebagai satu-satunya approver Group `Grup Satu Approver {runId}`. Pengelola karyawan, Pengelola Role Transaksi, dan pengelola plan pada langkah yang menyebutnya.
- Data:
  - DU-208-1: Category KL beserta Asset Name, Category `Kategori Tanpa Approval {runId}`, Asset Name `Nama Tanpa Approval {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`, Override Category Require approval `OFF`.
  - DU-208-2: Category KA beserta Asset Name, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`, Override Category Require approval `ON`, Override Category Approval type `Any one`.
  - DU-208-3: Category KX beserta Asset Name, Category `Kategori All {runId}`, Asset Name `Nama All {runId}`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`, Override Category Require approval `ON`, Override Category Approval type `All`.
  - DU-208-4: Group induk dengan approver, Group `Grup Induk Approval {runId}`, Approver `Rina Wijaya {runId}, Agus Pratama {runId}`.
  - DU-208-5: Group aset dengan approver, anak dari Group induk, Group `Grup Approval {runId}`, Parent Group `Grup Induk Approval {runId}`, Approver `Rina Wijaya {runId}, Hendra Kusuma {runId}, Sari Dewi {runId}`.
  - DU-208-6: Group dengan satu approver yang akan dinonaktifkan, Group `Grup Reroute {runId}`, Approver `Bagas Reroute {runId}`, Group Manager `Gita Manajer {runId}`.
  - DU-208-7: Group dengan satu approver yang sama dengan pengaju, Group `Grup Tunggal {runId}`, Approver `Hendra Kusuma {runId}`, Group Manager `Gita Manajer {runId}`.
  - DU-208-8: Group Assignee Division dengan dua approver, Group `Grup Division Approval {runId}`, Approver `Rina Wijaya {runId}, Wati Susanti {runId}`, Group Manager `Gita Manajer {runId}`.
  - DU-208-9: Group Assignee Division dengan satu approver, Group `Grup Division Tunggal {runId}`, Approver `Wati Susanti {runId}`, Group Manager `Gita Manajer {runId}`.
  - DU-208-10: Assignee Employee dan pemegang Role Transaksi Approver, Name `Sari Dewi {runId}`, Tipe Assignee `Employee`, Role Transaksi `Approver`, Status `Aktif`, Akun login `Ada`.
  - DU-208-11: Aktor Assignment pengaju dan pemegang Role Transaksi Approver, Name `Hendra Kusuma {runId}`, Role `Asset Admin`, Role Transaksi `Approver`, Status `Aktif`.
  - DU-208-12: Approver pertama, Name `Rina Wijaya {runId}`, Role Transaksi `Approver`, Status `Aktif`.
  - DU-208-13: Approver kedua, Name `Agus Pratama {runId}`, Role Transaksi `Approver`, Status `Aktif`.
  - DU-208-14: Approver yang akan dinonaktifkan, Name `Bagas Reroute {runId}`, Role Transaksi `Approver`, Status `Aktif`.
  - DU-208-15: PIC pengganti dan pemegang Role Transaksi Approver, Name `Wati Susanti {runId}`, Role Transaksi `Approver`, Division `Gudang {runId}`, Status `Aktif`, Akun login `Ada`.
  - DU-208-16: PIC awal ber-akun login, Name `Joko Prasetyo {runId}`, Division `Gudang {runId}`, Status `Aktif`, Akun login `Ada`.
  - DU-208-17: Group Manager yang menaungi, Name `Gita Manajer {runId}`, Role `Group Manager`, Status `Aktif`.
  - DU-208-18: Division Assignee, Division `Gudang {runId}`.
  - DU-208-19: Aset Laptop LPT, Name `Laptop LPT {runId}`, Group `Grup Approval {runId}`, Category `Kategori Tanpa Approval {runId}`, Asset Name `Nama Tanpa Approval {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-20: Aset Projector PRJ, Name `Projector PRJ {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-21: Aset Excavator EXC, Name `Excavator EXC {runId}`, Group `Grup Approval {runId}`, Category `Kategori All {runId}`, Asset Name `Nama All {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-22: Aset Projector Tolak, Name `Projector Tolak {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-23: Aset Excavator Tolak, Name `Excavator Tolak {runId}`, Group `Grup Approval {runId}`, Category `Kategori All {runId}`, Asset Name `Nama All {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-24: Aset Projector Bulk Satu, Name `Projector Bulk Satu {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-25: Aset Projector Bulk Dua, Name `Projector Bulk Dua {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-26: Aset Projector Batal, Name `Projector Batal {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-27: Aset Projector Tanpa Workflow, Name `Projector Tanpa Workflow {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-28: Aset Projector Reroute, Name `Projector Reroute {runId}`, Group `Grup Reroute {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-29: Aset Projector Approver Tunggal, Name `Projector Approver Tunggal {runId}`, Group `Grup Tunggal {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-30: Aset Excavator Division, Name `Excavator Division {runId}`, Group `Grup Division Approval {runId}`, Category `Kategori All {runId}`, Asset Name `Nama All {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-31: Aset Projector Division, Name `Projector Division {runId}`, Group `Grup Division Tunggal {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-32: Input pengajuan untuk Assignee Sari, Assignee `Sari Dewi {runId}`, Tipe Assignee `Employee`, Purpose `Daily work`.
  - DU-208-33: Input pengajuan untuk Assignee Division, Assignee `Gudang {runId}`, Tipe Assignee `Division`, PIC `Joko Prasetyo {runId}`, Purpose `Daily work`.
  - DU-208-34: Input Change PIC, PIC `Wati Susanti {runId}`.
  - DU-208-35: Approval Note Reject, Approval Note `Aset sedang dipakai tim lain {runId}`.
  - DU-208-36: Group dengan satu approver, Group `Grup Satu Approver {runId}`, Approver `Rina Wijaya {runId}`, Group Manager `Gita Manajer {runId}`.
  - DU-208-37: Group dengan satu approver yang penugasannya akan dicabut, Group `Grup Cabut {runId}`, Approver `Bayu Cabut {runId}`, Group Manager `Gita Manajer {runId}`.
  - DU-208-38: Approver yang penugasannya akan dicabut, Name `Bayu Cabut {runId}`, Role Transaksi `Approver`, Status `Aktif`.
  - DU-208-39: Aset Projector Multi A, Name `Projector Multi A {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-40: Aset Projector Multi B, Name `Projector Multi B {runId}`, Group `Grup Satu Approver {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-41: Aset Projector Campur Satu, Name `Projector Campur Satu {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-42: Aset Projector Campur Dua, Name `Projector Campur Dua {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-43: Aset Projector Timeout, Name `Projector Timeout {runId}`, Group `Grup Approval {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-44: Aset Projector Satu Approver, Name `Projector Satu Approver {runId}`, Group `Grup Satu Approver {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-45: Aset Excavator Satu Approver, Name `Excavator Satu Approver {runId}`, Group `Grup Satu Approver {runId}`, Category `Kategori All {runId}`, Asset Name `Nama All {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-46: Aset Excavator PIC Approver, Name `Excavator PIC Approver {runId}`, Group `Grup Division Approval {runId}`, Category `Kategori All {runId}`, Asset Name `Nama All {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-47: Aset Projector PIC Tunggal, Name `Projector PIC Tunggal {runId}`, Group `Grup Division Tunggal {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-208-48: Aset Projector Cabut, Name `Projector Cabut {runId}`, Group `Grup Cabut {runId}`, Category `Kategori Any One {runId}`, Asset Name `Nama Any One {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
- Kondisi:
  - Level Feature Suite Assignment pada plan adalah `Full`, dan Approval Workflow tersedia di plan pada awal spec.
  - Setiap aset berada di Custody `Available` dan tidak berada di ASG aktif maupun Draft mana pun.

## Test Steps

### Satu pengajuan memuat aturan approval berbeda per aset
1. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Laptop LPT {runId}`, `Projector PRJ {runId}`, `Excavator EXC {runId}` dan Purpose `Daily work`
2. Verifikasi Submit atas tiga aset Assignee `Sari Dewi {runId}` menghasilkan hasil berikut, dan pengajuan dibuat oleh pengaju `Hendra Kusuma {runId}`
3. Verifikasi baris `Laptop LPT {runId}` langsung `Waiting for Handover` dengan Approval `Not required`, karena Require approval efektif `OFF`
4. Verifikasi baris `Projector PRJ {runId}` berstatus `Waiting for Approval` dengan Approval `Waiting` dan approver `Rina Wijaya {runId}` dan `Agus Pratama {runId}` sama-sama belum memutuskan menurut Any one
5. Verifikasi baris `Excavator EXC {runId}` berstatus `Waiting for Approval` dengan Approval `Waiting` dan approver `Rina Wijaya {runId}` dan `Agus Pratama {runId}` belum memutuskan menurut All dengan progres 0 dari 2 menyetujui
6. Verifikasi status header ASG Assignee `Sari Dewi {runId}` adalah `Waiting for Handover`, karena baris `Waiting for Handover` mengalahkan baris `Waiting for Approval`
7. Verifikasi status pengajuan yang memuat baris `Projector PRJ {runId}` dan `Excavator EXC {runId}` adalah `Waiting`, karena kedua baris masih menunggu keputusan
8. Verifikasi approver `Rina Wijaya {runId}` dan `Agus Pratama {runId}` melihat satu pengajuan di `Approvals > Assignment` yang memuat kedua aset yang dapat mereka putuskan
9. Verifikasi seluruh aset pengajuan terbaca pada halaman Review oleh approver `Agus Pratama {runId}`
10. Verifikasi Approval Rule baris `Projector PRJ {runId}` menampilkan Approval type `Any one` dan baris `Excavator EXC {runId}` menampilkan Approval type `All` dengan progres 0 dari 2 menyetujui
11. Verifikasi baris `Projector PRJ {runId}` dan `Excavator EXC {runId}` masuk satu pengajuan approval tipe `Assignment` dengan ID sama dengan Transaction ID ASG
12. Verifikasi baris `Projector PRJ {runId}` dan `Excavator EXC {runId}` membawa approver dan Approval type efektifnya sendiri, yaitu `Any one` dan `All`, dalam satu pengajuan yang sama
13. Verifikasi tidak ada pengajuan terpisah menurut Approval type maupun himpunan approver
14. Verifikasi daftar approver baris `Excavator EXC {runId}` hanya memuat `Rina Wijaya {runId}` dan `Agus Pratama {runId}`, dan `Rina Wijaya {runId}` tercatat satu kali walau memegang penugasan di Group dan Group induknya
15. Verifikasi pengaju `Hendra Kusuma {runId}` dan Assignee `Sari Dewi {runId}` tidak masuk daftar approver eligible walau memegang Role Transaksi `Approver` pada Group aset
16. Pengaju `Hendra Kusuma {runId}` menyetujui baris `Projector PRJ {runId}` atas pengajuannya sendiri
17. Verifikasi keputusan pengaju ditolak dan baris `Projector PRJ {runId}` tetap `Waiting for Approval`, karena tidak ada Auto-approve dan pengaju tidak memutuskan aset atas transaksinya sendiri
18. Assignee `Sari Dewi {runId}` menyetujui baris `Excavator EXC {runId}` atas transaksinya sendiri
19. Verifikasi keputusan Assignee ditolak dan baris `Excavator EXC {runId}` tetap `Waiting for Approval`
20. Aktor mencatat jumlah notifikasi approver `Agus Pratama {runId}` sebelum keputusan `Rina Wijaya {runId}`

### Approve dan Reject per aset, Any one dan All
21. Approver `Rina Wijaya {runId}` memutuskan dalam satu pengiriman seluruh asetnya di pengajuan: Approve aset `Projector PRJ {runId}` dan Approve aset `Excavator EXC {runId}`
22. Verifikasi jumlah notifikasi `Agus Pratama {runId}` tidak bertambah dalam 5 detik sesudah keputusan `Rina Wijaya {runId}` atas baris `Projector PRJ {runId}`, karena aset yang sudah diputuskan pada Any one tidak memicu notifikasi ke approver lain
23. Verifikasi baris `Projector PRJ {runId}` berstatus `Waiting for Handover` karena keputusan pertama pada Any one menentukan aset itu, dan tidak ada tingkat approval berikutnya
24. Verifikasi baris `Excavator EXC {runId}` tetap `Waiting for Approval` dengan progres 1 dari 2 menyetujui, karena mode All menuntut semua approver menyetujui
25. Verifikasi kedua keputusan `Rina Wijaya {runId}` tersimpan bersama dalam satu pengiriman dan tidak ada keputusan yang tersimpan sebagian
26. Verifikasi status pengajuan adalah `Waiting`, karena aset `Excavator EXC {runId}` masih menunggu keputusan `Agus Pratama {runId}`
27. Verifikasi pengajuan tidak lagi tampil di Active `Rina Wijaya {runId}` untuk aset `Projector PRJ {runId}` dan tercatat satu entri di History `Rina Wijaya {runId}`
28. Verifikasi keputusan `Rina Wijaya {runId}` atas baris `Projector PRJ {runId}` diterapkan per aset dan tidak mengubah baris `Laptop LPT {runId}`
29. Approver `Agus Pratama {runId}` menolak baris `Projector PRJ {runId}` dengan Approval Note `Aset sedang dipakai tim lain {runId}`
30. Verifikasi keputusan `Agus Pratama {runId}` atas baris `Projector PRJ {runId}` ditolak dan baris tetap `Waiting for Handover`, karena aset yang sudah diputuskan tidak lagi menjadi tugas approver lain
31. Verifikasi pengajuan tetap tampil di Active `Agus Pratama {runId}` karena aset `Excavator EXC {runId}` belum ia putuskan, dan aset `Projector PRJ {runId}` tidak termasuk tugasnya
32. Verifikasi baris `Projector PRJ {runId}` tetap terbaca oleh `Agus Pratama {runId}` pada halaman Review pengajuan yang sama dan tidak dapat ia putuskan (`Not your approval`), karena baris itu sudah diputuskan `Rina Wijaya {runId}`
33. Approver `Agus Pratama {runId}` menyetujui baris `Excavator EXC {runId}`
34. Verifikasi baris `Excavator EXC {runId}` berstatus `Waiting for Handover` dengan progres 2 dari 2 menyetujui, tanpa suara `Hendra Kusuma {runId}` maupun `Sari Dewi {runId}` yang dikeluarkan guard
35. Verifikasi status pengajuan menjadi `Approved` dan ditutup, karena seluruh asetnya sudah diputuskan
36. Verifikasi pengajuan tercatat satu entri di History `Agus Pratama {runId}` dan tidak ada lagi di Active `Agus Pratama {runId}` maupun Active `Rina Wijaya {runId}`
37. Verifikasi Assignee `Sari Dewi {runId}` menerima notifikasi `assignment_resolved` dan `assignment_ready_handover` untuk baris yang disetujui

### Reject: keputusan pertama menolak pada Any one dan satu penolakan menolak pada All
38. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Tolak {runId}`, `Excavator Tolak {runId}` dan Purpose `Daily work`
39. Approver `Rina Wijaya {runId}` menolak baris `Projector Tolak {runId}` tanpa mengisi Approval Note
40. Verifikasi penolakan tanpa Approval Note ditolak dengan pesan `Approval note must not be empty` dan baris `Projector Tolak {runId}` tetap `Waiting for Approval`
41. Approver `Rina Wijaya {runId}` memutuskan dalam satu pengiriman: Reject aset `Projector Tolak {runId}` dan Reject aset `Excavator Tolak {runId}` dengan Approval Note `Aset sedang dipakai tim lain {runId}`
42. Verifikasi baris `Projector Tolak {runId}` berstatus `Rejected` dan Custody `Available`, karena keputusan pertama pada Any one menentukan aset itu
43. Verifikasi baris `Excavator Tolak {runId}` berstatus `Rejected` setelah satu penolakan walau `Agus Pratama {runId}` belum memutuskan, dan permintaan yang belum dijawab ditutup
44. Approver `Agus Pratama {runId}` menyetujui baris `Projector Tolak {runId}`
45. Verifikasi baris `Projector Tolak {runId}` tetap `Rejected`, karena keputusan pertama sudah menentukan aset itu
46. Verifikasi pengajuan tidak tercatat di Active maupun History `Agus Pratama {runId}` untuk aset yang sudah ditolak lebih dulu oleh approver lain
47. Verifikasi status pengajuan adalah `Rejected`
48. Verifikasi Assignee `Sari Dewi {runId}` menerima notifikasi `assignment_resolved` atas baris `Projector Tolak {runId}` dan `Excavator Tolak {runId}` yang ditolak
49. Aktor Assignment `Hendra Kusuma {runId}` mengajukan ulang Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Tolak {runId}` dan Purpose `Daily work`
50. Verifikasi baris `Projector Tolak {runId}` yang ditolak dapat diajukan ulang sebagai ASG baru dan berstatus `Waiting for Approval`

### Bulk Approve hanya mencakup aset milik approver itu
51. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Bulk Satu {runId}` dan Purpose `Daily work`
52. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Bulk Dua {runId}` dan Purpose `Daily work`, sebagai pengajuan terpisah
53. Approver `Agus Pratama {runId}` menyetujui baris `Projector Bulk Satu {runId}`, yang menjadi satu-satunya asetnya di pengajuan itu
54. Approver `Rina Wijaya {runId}` melakukan Bulk Approve dengan memilih pengajuan yang memuat `Projector Bulk Satu {runId}` dan pengajuan yang memuat `Projector Bulk Dua {runId}`
55. Verifikasi baris `Projector Bulk Dua {runId}` berstatus `Waiting for Handover` berdasarkan keputusan `Rina Wijaya {runId}`
56. Verifikasi keputusan baris `Projector Bulk Satu {runId}` tetap milik `Agus Pratama {runId}` dan Bulk Approve `Rina Wijaya {runId}` tidak diterapkan pada baris itu, karena bukan aset `Rina Wijaya {runId}` yang belum ia putuskan

### Pengajuan yang dibatalkan
57. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Batal {runId}` dan Purpose `Daily work`
58. Pengaju melakukan Cancel Assignment atas ASG tersebut
59. Verifikasi status pengajuan adalah `Canceled` dan ditutup

### Approver yang dinonaktifkan saat pengajuan menunggu dirutekan ulang
60. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Reroute {runId}` dan Purpose `Daily work`
61. Pengelola karyawan menonaktifkan approver `Bagas Reroute {runId}`
62. Verifikasi Assignment Log memuat node `Approval rerouted` oleh `System` dengan alasan `Approver removed` yang merutekan ke Group Manager `Gita Manajer {runId}`
63. Group Manager `Gita Manajer {runId}` menyetujui baris `Projector Reroute {runId}`
64. Verifikasi baris `Projector Reroute {runId}` berstatus `Waiting for Handover`, karena Group Manager `Gita Manajer {runId}` menjadi approver aktif dan keputusan pertamanya final

### Tidak ada approver eligible dirutekan ke Group Manager
65. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Approver Tunggal {runId}` dan Purpose `Daily work`
66. Verifikasi Assignment Log memuat node `Approval rerouted` dengan alasan `No eligible approver` dan `Routed to: Group Manager (no eligible approver)`, karena satu-satunya approver adalah pengaju `Hendra Kusuma {runId}`
67. Pengaju `Hendra Kusuma {runId}` menyetujui baris `Projector Approver Tunggal {runId}`
68. Verifikasi keputusan pengaju ditolak dan baris `Projector Approver Tunggal {runId}` tetap `Waiting for Approval` sampai Group Manager `Gita Manajer {runId}` memutuskan

### Change PIC menerapkan guard pada baris Waiting for Approval
69. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Excavator Division {runId}` dan Purpose `Daily work`
70. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Projector Division {runId}` dan Purpose `Daily work`
71. Aktor Assignment melakukan `Change PIC` menjadi `Wati Susanti {runId}` pada kedua ASG Assignee Division tersebut
72. Verifikasi `Wati Susanti {runId}` dikeluarkan dari snapshot approver baris `Excavator Division {runId}` dan suaranya tidak dibutuhkan pada mode All
73. Approver `Wati Susanti {runId}` yang menjadi PIC menyetujui baris `Excavator Division {runId}`
74. Verifikasi keputusan PIC `Wati Susanti {runId}` ditolak dan baris `Excavator Division {runId}` tetap `Waiting for Approval`, karena PIC tidak memutuskan aset atas transaksinya sendiri
75. Approver `Rina Wijaya {runId}` menyetujui baris `Excavator Division {runId}`
76. Verifikasi baris `Excavator Division {runId}` berstatus `Waiting for Handover` setelah persetujuan `Rina Wijaya {runId}` saja
77. Verifikasi snapshot approver baris `Projector Division {runId}` menjadi kosong sehingga baris dirutekan ulang ke Group Manager `Gita Manajer {runId}` dengan node `Approval rerouted`
78. Approver `Wati Susanti {runId}` yang menjadi PIC menyetujui baris `Projector Division {runId}`
79. Verifikasi keputusan PIC `Wati Susanti {runId}` ditolak dan baris `Projector Division {runId}` tetap `Waiting for Approval` sampai Group Manager `Gita Manajer {runId}` memutuskan

### Plan tanpa Approval Workflow melewati approval
80. Pengelola plan menonaktifkan Approval Workflow pada plan entitas
81. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Tanpa Workflow {runId}` dan Purpose `Daily work`
82. Verifikasi baris `Projector Tanpa Workflow {runId}` langsung `Waiting for Handover` dengan Approval `Not required`, karena Require approval efektif `OFF` pada plan tanpa Approval Workflow
83. Verifikasi nilai efektif Require approval baris `Projector Tanpa Workflow {runId}` adalah `OFF` walau override Category-nya `ON`
84. Pengelola plan mengaktifkan kembali Approval Workflow pada plan entitas

### Satu Submit multi-Group menghasilkan satu pengajuan per Transaction ID
85. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Multi A {runId}` dari Group `Grup Approval {runId}` dan aset `Projector Multi B {runId}` dari Group `Grup Satu Approver {runId}` dan Purpose `Daily work`
86. Verifikasi Submit menghasilkan dua ASG dengan Transaction ID berbeda, satu per Group asal
87. Verifikasi approver `Rina Wijaya {runId}` melihat dua pengajuan terpisah di `Approvals > Assignment`, satu per Transaction ID, dengan ID pengajuan sama dengan Transaction ID ASG-nya
88. Verifikasi pengajuan dari Group `Grup Approval {runId}` memuat hanya baris `Projector Multi A {runId}` dan pengajuan dari Group `Grup Satu Approver {runId}` memuat hanya baris `Projector Multi B {runId}`
89. Verifikasi approver `Agus Pratama {runId}` melihat hanya pengajuan yang memuat baris `Projector Multi A {runId}`

### Satu approver saja: Any one dan All sama
90. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Satu Approver {runId}` dan `Excavator Satu Approver {runId}` dan Purpose `Daily work`
91. Approver `Rina Wijaya {runId}` memutuskan dalam satu pengiriman seluruh asetnya di pengajuan: Approve aset `Projector Satu Approver {runId}` dan Approve aset `Excavator Satu Approver {runId}`
92. Verifikasi baris `Projector Satu Approver {runId}` pada Any one dan baris `Excavator Satu Approver {runId}` pada All sama-sama berstatus `Waiting for Handover`, karena keputusan satu-satunya approver langsung menentukan aset, dengan progres 1 dari 1 menyetujui pada mode All

### Status pengajuan Partially Approved bila sebagian disetujui dan sebagian ditolak
93. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Campur Satu {runId}` dan `Projector Campur Dua {runId}` dan Purpose `Daily work`
94. Approver `Rina Wijaya {runId}` memutuskan dalam satu pengiriman: Approve aset `Projector Campur Satu {runId}` dan Reject aset `Projector Campur Dua {runId}` dengan Approval Note `Aset sedang dipakai tim lain {runId}`
95. Verifikasi baris `Projector Campur Satu {runId}` berstatus `Waiting for Handover` dan baris `Projector Campur Dua {runId}` berstatus `Rejected`
96. Verifikasi status pengajuan adalah `Partially Approved`, karena seluruh aset sudah diputuskan dengan sebagian disetujui dan sebagian ditolak

### PIC pemegang Role Transaksi Approver dikeluarkan dari daftar approver sejak Submit
97. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Wati Susanti {runId}` dan aset `Excavator PIC Approver {runId}` dan `Projector PIC Tunggal {runId}` dan Purpose `Daily work`
98. Verifikasi daftar approver baris `Excavator PIC Approver {runId}` hanya memuat `Rina Wijaya {runId}`, dan `Wati Susanti {runId}` yang menjadi PIC tidak masuk daftar walau memegang Role Transaksi `Approver` pada Group aset
99. Verifikasi baris `Excavator PIC Approver {runId}` pada mode All hanya membutuhkan suara `Rina Wijaya {runId}` dengan progres 0 dari 1 menyetujui, karena suara PIC tidak dihitung
100. Approver `Wati Susanti {runId}` yang menjadi PIC menyetujui baris `Excavator PIC Approver {runId}`
101. Verifikasi keputusan PIC `Wati Susanti {runId}` ditolak dan baris `Excavator PIC Approver {runId}` tetap `Waiting for Approval`, karena PIC tidak memutuskan aset atas transaksinya sendiri
102. Verifikasi Assignment Log baris `Projector PIC Tunggal {runId}` memuat node `Approval rerouted` dengan alasan `No eligible approver` dan `Routed to: Group Manager (no eligible approver)`, karena satu-satunya approver adalah PIC `Wati Susanti {runId}`
103. Approver `Wati Susanti {runId}` yang menjadi PIC menyetujui baris `Projector PIC Tunggal {runId}`
104. Verifikasi keputusan PIC `Wati Susanti {runId}` ditolak dan baris `Projector PIC Tunggal {runId}` tetap `Waiting for Approval` sampai Group Manager `Gita Manajer {runId}` memutuskan

### Penugasan approver dicabut saat pengajuan menunggu dirutekan ulang
105. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Cabut {runId}` dan Purpose `Daily work`
106. Pengelola Role Transaksi mencabut Role Transaksi `Approver` dari `Bayu Cabut {runId}` pada Group `Grup Cabut {runId}`, sedangkan karyawan `Bayu Cabut {runId}` tetap aktif
107. Verifikasi Assignment Log memuat node `Approval rerouted` oleh `System` dengan alasan `Approver removed` yang merutekan ke Group Manager `Gita Manajer {runId}`, karena penugasan approver dicabut walau karyawannya tetap aktif

### Pengajuan ditutup sistem karena Transaction timeout berstatus Canceled
108. Aktor Assignment `Hendra Kusuma {runId}` mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Projector Timeout {runId}` dan Purpose `Daily work`
109. Waktu berlalu melewati Transaction timeout sejak baris `Projector Timeout {runId}` masuk `Waiting for Approval`
110. Verifikasi baris `Projector Timeout {runId}` berstatus `Canceled` oleh `System` dengan alasan `Timed out (Waiting for Approval)`
111. Verifikasi status pengajuan adalah `Canceled`, karena ditutup sistem
