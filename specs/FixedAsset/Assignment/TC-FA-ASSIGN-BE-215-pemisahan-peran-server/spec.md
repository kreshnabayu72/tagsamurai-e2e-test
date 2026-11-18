---
id: TC-FA-ASSIGN-BE-215-pemisahan-peran-server
title: "Pemisahan peran: Aktor yang menjadi Assignee atau PIC"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.4.3#b6", "ASSIGN-LOGIC-15a", "ASSIGN-LOGIC-15c", "ASSIGN-LOGIC-15d", "ASSIGN-LOGIC-15e", "ASSIGN-LOGIC-15f", "ASSIGN-LOGIC-15g", "ASSIGN-LOGIC-15h"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.4.3#b6": [2, 4, 9]
  "ASSIGN-LOGIC-15a": [2, 4, 9]
  "ASSIGN-LOGIC-15c": 14
  "ASSIGN-LOGIC-15d": 16
  "ASSIGN-LOGIC-15e": [18, 20]
  "ASSIGN-LOGIC-15f": [2, 4, 9]
  "ASSIGN-LOGIC-15g": [7, 12]
  "ASSIGN-LOGIC-15h": 20
---

# Pemisahan peran: Aktor yang menjadi Assignee atau PIC

## Prerequisites
- Aktor: Aktor Assignment `Hendra Kusuma {runId}` (Asset Admin, cakupan Group `Head Office {runId}`, juga karyawan ber-akun login dan PIC Division `Finance {runId}`); Aktor Assignment lain `Lina Marlina {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); `Tono Wibowo {runId}` (Group Manager, cakupan Group `Head Office {runId}`); `Mira Handayani {runId}` (Approver, cakupan Group `Head Office {runId}`).
- Data:
  - DU-215-1: User, Aktor Assignment yang juga Assignee Employee dan PIC Division: Nama `Hendra Kusuma {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`, PIC Division `Finance {runId}`.
  - DU-215-2: User, Aktor Assignment lain: Nama `Lina Marlina {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-215-3: User, Group Manager yang juga pengaju dan eligible sebagai approver: Nama `Tono Wibowo {runId}`, Role `Group Manager`, Cakupan Group `Head Office {runId}`.
  - DU-215-4: User, Approver Group yang juga Assignee: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-215-5: Assignment, ASG dengan baris Waiting for Handover untuk Aktor sebagai Assignee Employee: Assignee `Hendra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Dell XPS {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`.
  - DU-215-6: Assignment, ASG Division dengan Aktor sebagai PIC dan baris Waiting for Handover: Assignee `Finance {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Honda EU {runId}`, Status baris `Waiting for Handover`, PIC `Hendra Kusuma {runId}`, Need recipient confirmation `No`.
  - DU-215-7: Assignment, ASG dengan baris Assigned untuk Aktor sebagai Assignee Employee: Assignee `Hendra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Monitor LG UltraWide {runId}`, Status baris `Assigned`.
  - DU-215-8: Assignment, ASG dengan baris Assigned pada entitas terpisah level None untuk Aktor sebagai PIC: Entitas `entitas terpisah dengan Feature Suite Assignment level None`, Assignee `Finance {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Kohler {runId}`, Status baris `Assigned`, PIC `Hendra Kusuma {runId}`.
  - DU-215-9: Asset, Aset Available yang diajukan Aktor untuk dirinya sendiri: Nama `Tablet Samsung Galaxy Tab {runId}`, Custody `Available`, Calon Assignee `Hendra Kusuma {runId}`, Tipe Assignee `Employee`, Require approval `OFF`.
  - DU-215-10: Assignment, ASG dengan baris Waiting for Approval yang pengajunya eligible sebagai approver: Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Canon EOS {runId}`, Status baris `Waiting for Approval`, Pengaju `Tono Wibowo {runId}`.
  - DU-215-11: Assignment, ASG dengan baris Waiting for Approval yang Assignee-nya eligible sebagai approver: Assignee `Mira Handayani {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Proyektor Optoma {runId}`, Status baris `Waiting for Approval`, Pengaju `Lina Marlina {runId}`.
- Kondisi:
  - Need recipient confirmation seperti di entri data.
  - ASG DU-215-8 berada di entitas terpisah dengan Feature Suite Assignment level `None`, bukan di entitas level `Full` yang dipakai langkah lain spec ini; `Hendra Kusuma {runId}` adalah PIC Division di entitas itu.

## Test Steps

### Aktor yang menjadi Assignee tidak boleh menjadi pemberi saat Handover
1. Hendra mengirim permintaan Handover langsung ke server untuk baris `Laptop Dell XPS {runId}` pada DU-215-5 yang Assignee-nya adalah Hendra sendiri
2. Verifikasi Handover oleh Hendra sebagai Assignee ditolak server dan baris `Laptop Dell XPS {runId}` tetap `Waiting for Handover`

### Aktor yang menjadi PIC Division tidak boleh menjadi pemberi dan Aktor lain memprosesnya
3. Hendra mengirim permintaan Handover langsung ke server untuk baris `Genset Honda EU {runId}` pada DU-215-6 yang Assignee-nya Division `Finance {runId}` dengan PIC `Hendra Kusuma {runId}`
4. Verifikasi Handover oleh Hendra sebagai PIC ditolak server dan baris `Genset Honda EU {runId}` tetap `Waiting for Handover`
5. Lina memverifikasi tag baris `Genset Honda EU {runId}`
6. Lina menekan `[Complete Handover]` untuk baris `Genset Honda EU {runId}`
7. Verifikasi baris `Genset Honda EU {runId}` berstatus `Assigned` karena Aktor Assignment lain yang memproses

### Aktor yang menjadi Assignee tidak boleh menjadi penerima saat Unassign
8. Hendra mengirim permintaan Unassign langsung ke server untuk baris `Monitor LG UltraWide {runId}` pada DU-215-7 yang Assignee-nya adalah Hendra sendiri
9. Verifikasi Unassign oleh Hendra sebagai Assignee ditolak server dan baris `Monitor LG UltraWide {runId}` tetap `Assigned`
10. Lina memverifikasi tag baris `Monitor LG UltraWide {runId}`
11. Lina menekan `[Submit]` pada halaman Unassign untuk Assignee `Hendra Kusuma {runId}` atas baris `Monitor LG UltraWide {runId}`
12. Verifikasi baris `Monitor LG UltraWide {runId}` berstatus `Unassigned` karena Aktor Assignment lain yang menerima

### Pemisahan peran berlaku juga untuk Mark as Unassigned
13. Hendra mengirim `Mark as Unassigned` langsung ke server untuk baris `Genset Kohler {runId}` pada DU-215-8 pada entitas ber-Feature Suite Assignment level `None`
14. Verifikasi permintaan ditolak server karena Hendra adalah PIC Division aset itu dan baris tetap `Assigned`

### Aktor Assignment boleh mengajukan ASG untuk dirinya sendiri
15. Hendra mengajukan Assignment atas aset `Tablet Samsung Galaxy Tab {runId}` pada DU-215-9 dengan dirinya sendiri sebagai Assignee Employee
16. Verifikasi pemisahan peran tidak menolak pengajuan karena pengajuan untuk diri sendiri diperbolehkan

### Pengaju dan Assignee tidak memutuskan aset atas transaksinya sendiri
17. Tono mengirim keputusan Approve langsung ke server untuk baris `Kamera Canon EOS {runId}` pada DU-215-10 yang diajukan Tono sendiri
18. Verifikasi keputusan ditolak server karena pengaju dikeluarkan dari daftar approver aset itu dan baris tetap `Waiting for Approval`
19. Mira mengirim keputusan Approve langsung ke server untuk baris `Proyektor Optoma {runId}` pada DU-215-11 yang Assignee-nya adalah Mira sendiri
20. Verifikasi keputusan ditolak server karena self-approval guard tetap berlaku dan baris tetap `Waiting for Approval`
