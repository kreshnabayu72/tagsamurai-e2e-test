---
id: TC-FA-ASSIGN-BE-219-status-transaksi-vs-status-global-aset
title: "Status transaksi berbeda dari status global aset"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["ASSIGN-LOGIC-19a", "ASSIGN-LOGIC-19b", "ASSIGN-LOGIC-19c", "ASSIGN-LOGIC-19d", "ASSIGN-LOGIC-19e", "ASSIGN-LOGIC-19f", "ASSIGN-LOGIC-19g", "ASSIGN-LOGIC-19h", "ASSIGN-LOGIC-19i", "ASSIGN-LOGIC-19j", "ASSIGN-LOGIC-19k"]
smoke: []
dependsOn: []
owner: BE
trace:
  "ASSIGN-LOGIC-19a": 2
  "ASSIGN-LOGIC-19b": 2
  "ASSIGN-LOGIC-19c": [3, 11]
  "ASSIGN-LOGIC-19d": [6, 9]
  "ASSIGN-LOGIC-19e": [11, 12]
  "ASSIGN-LOGIC-19f": 15
  "ASSIGN-LOGIC-19g": [12, 21, 22]
  "ASSIGN-LOGIC-19h": 2
  "ASSIGN-LOGIC-19i": 3
  "ASSIGN-LOGIC-19j": [11, 17]
  "ASSIGN-LOGIC-19k": 17
---

# Status transaksi berbeda dari status global aset

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); `Dian Anggraeni {runId}` (pemegang hak keputusan menu `Damaged` pada Group `Head Office {runId}`); Assignee Employee dan PIC ber-akun login seperti di entri data.
- Data:
  - DU-219-1: User, Aktor Assignment: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-219-2: User, Pemegang hak keputusan menu Damaged: Nama `Dian Anggraeni {runId}`, Role `pemegang hak keputusan menu Damaged`, Cakupan Group `Head Office {runId}`.
  - DU-219-3: Assignment, ASG dengan dua baris Assigned: satu akan dilaporkan rusak, satu tidak: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Acer Swift {runId}`, Baris 2 `Proyektor Epson EB {runId}`, Status baris `Assigned`, Condition aset `Normal`, Description laporan `Layar bergaris`.
  - DU-219-4: Assignment, ASG Division dengan baris Assigned yang field Division asetnya berubah: Assignee `Finance {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Honda EU {runId}`, Status baris `Assigned`, PIC `Hendra Kusuma {runId}`, Division aset sebelum `IT {runId}`, Condition aset `Normal`.
  - DU-219-5: Assignment, ASG dengan baris Assigned yang dilaporkan hilang oleh Assignee: Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Tablet iPad {runId}`, Status baris `Assigned`, Condition aset `Normal`.
- Kondisi:
  - Condition awal semua aset `Normal`.

## Test Steps

### Dua status dimiliki modul berbeda
1. Rina membaca baris `Laptop Acer Swift {runId}` pada DU-219-3 dan status asetnya
2. Verifikasi status transaksi baris `Laptop Acer Swift {runId}` adalah `Assigned` yang dimiliki Assignment dan tampil di kolom `Status`
3. Verifikasi status global aset `Laptop Acer Swift {runId}` adalah Custody `Assigned` dan Condition `Normal`, dimiliki aset beserta modul pemiliknya, dan bukan nilai kolom `Status` baris

### Assignment hanya mengubah Custody dan field Division aset Assignee Division
4. Rina memverifikasi tag baris `Proyektor Epson EB {runId}`
5. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Budi Santoso {runId}` atas baris `Proyektor Epson EB {runId}`
6. Verifikasi Unassign hanya mengubah Custody aset `Proyektor Epson EB {runId}` menjadi `Available` dan Condition tetap `Normal`
7. Rina memverifikasi tag baris `Genset Honda EU {runId}` pada DU-219-4
8. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Finance {runId}`
9. Verifikasi Unassign pada ASG bertipe `Division` mengubah Custody dan mengembalikan field `Division` aset ke `IT {runId}` tanpa mengubah Condition

### Satu peristiwa dua efek yang berdiri sendiri
10. Assignee `Budi Santoso {runId}` melaporkan aset `Laptop Acer Swift {runId}` rusak dengan Description `Layar bergaris`
11. Verifikasi status global aset `Laptop Acer Swift {runId}` langsung berubah menjadi Condition `Damaged`
12. Verifikasi status baris `Laptop Acer Swift {runId}` tetap `Assigned` dengan badge `Reported Damaged` yang berubah terpisah dari status global aset
13. Rina memverifikasi tag baris `Laptop Acer Swift {runId}`
14. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Budi Santoso {runId}` atas baris `Laptop Acer Swift {runId}`
15. Verifikasi baris `Laptop Acer Swift {runId}` berstatus `Unassigned` dengan marker `Damaged` sebagai status transaksi
16. Dian menandai aset `Laptop Acer Swift {runId}` sebagai repaired
17. Verifikasi Condition aset `Laptop Acer Swift {runId}` kembali `Normal` sedangkan marker `Damaged` pada baris tetap karena marker adalah status transaksi, bukan status global aset

### Status global aset tidak diturunkan dari status baris
18. Assignee `Citra Dewi {runId}` melaporkan aset `Tablet iPad {runId}` pada DU-219-5 hilang dari tampilan Assignee
19. Rina memverifikasi tag baris `Tablet iPad {runId}`
20. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Citra Dewi {runId}`
21. Verifikasi baris `Tablet iPad {runId}` berstatus `Unassigned` dan Custody `Available` sedangkan Condition aset tetap `Missing` karena status global tidak diturunkan dari status baris
22. Verifikasi Assignment hanya menampilkan Condition aset sebagai rujukan tanpa menyalinnya ke status baris
