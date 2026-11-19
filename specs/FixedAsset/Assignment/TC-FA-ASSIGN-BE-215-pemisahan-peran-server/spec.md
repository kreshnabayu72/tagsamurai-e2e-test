---
id: TC-FA-ASSIGN-BE-215-pemisahan-peran-server
title: "Pemrosesan sendiri: Aktor yang menjadi Assignee atau PIC"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASSIGN-LOGIC-15a", "ASSIGN-LOGIC-15b", "ASSIGN-LOGIC-15c", "ASSIGN-LOGIC-15d", "ASSIGN-LOGIC-15e", "ASSIGN-LOGIC-15f", "ASSIGN-LOGIC-15g", "ASSIGN-LOGIC-15h", "ASSIGN-LOGIC-15i", "ASSIGN-LOGIC-15j", "FI-ASG-67"]
smoke: []
dependsOn: []
owner: BE
trace:
  "ASSIGN-LOGIC-15a": [1, 2, 5, 6, 12, 13]
  "ASSIGN-LOGIC-15b": [9, 10]
  "ASSIGN-LOGIC-15c": [3, 7]
  "ASSIGN-LOGIC-15d": [17, 18]
  "ASSIGN-LOGIC-15e": [19, 20, 21, 22]
  "ASSIGN-LOGIC-15f": [10, 16]
  "ASSIGN-LOGIC-15g": [1, 5, 9, 10, 11]
  "ASSIGN-LOGIC-15h": 22
  "ASSIGN-LOGIC-15i": [4, 8, 14]
  "ASSIGN-LOGIC-15j": [15, 16]
  "FI-ASG-67": [9, 10]
---

# Pemrosesan sendiri: Aktor yang menjadi Assignee atau PIC

## Prerequisites
- Aktor: Aktor Assignment `Hendra Kusuma {runId}` (Asset Admin, cakupan Group `Head Office {runId}`, juga karyawan ber-akun login dan PIC Division `Finance {runId}`); Aktor Assignment lain `Lina Marlina {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); `Tono Wibowo {runId}` (Group Manager, cakupan Group `Head Office {runId}`); `Mira Handayani {runId}` (Approver, cakupan Group `Head Office {runId}`).
- Data:
  - DU-215-1: User, Aktor Assignment yang juga Assignee Employee dan PIC Division: Nama `Hendra Kusuma {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`, PIC Division `Finance {runId}`.
  - DU-215-2: User, Aktor Assignment lain: Nama `Lina Marlina {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-215-3: User, Group Manager yang juga pengaju dan eligible sebagai approver: Nama `Tono Wibowo {runId}`, Role `Group Manager`, Cakupan Group `Head Office {runId}`.
  - DU-215-4: User, Approver Group yang juga Assignee: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-215-5: Assignment, ASG dengan baris Waiting for Handover untuk Aktor sebagai Assignee Employee: Assignee `Hendra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Dell XPS {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`.
  - DU-215-6: Assignment, ASG Division dengan Aktor sebagai PIC dan baris Waiting for Handover: Assignee `Finance {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Honda EU {runId}`, Status baris `Waiting for Handover`, PIC `Hendra Kusuma {runId}`, Need recipient confirmation `Yes`.
  - DU-215-7: Assignment, ASG dengan baris Assigned untuk Aktor sebagai Assignee Employee: Assignee `Hendra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Monitor LG UltraWide {runId}`, Status baris `Assigned`.
  - DU-215-8: Assignment, ASG dengan baris Assigned pada entitas terpisah level None untuk Aktor sebagai PIC: Entitas `entitas terpisah dengan Feature Suite Assignment level None`, Assignee `Finance {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Kohler {runId}`, Status baris `Assigned`, PIC `Hendra Kusuma {runId}`.
  - DU-215-9: Asset, Aset Available yang diajukan Aktor untuk dirinya sendiri: Nama `Tablet Samsung Galaxy Tab {runId}`, Custody `Available`, Calon Assignee `Hendra Kusuma {runId}`, Tipe Assignee `Employee`, Require approval `OFF`.
  - DU-215-10: Assignment, ASG dengan baris Waiting for Approval yang pengajunya eligible sebagai approver: Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Canon EOS {runId}`, Status baris `Waiting for Approval`, Pengaju `Tono Wibowo {runId}`.
  - DU-215-11: Assignment, ASG dengan baris Waiting for Approval yang Assignee-nya eligible sebagai approver: Assignee `Mira Handayani {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Proyektor Optoma {runId}`, Status baris `Waiting for Approval`, Pengaju `Lina Marlina {runId}`.
- Kondisi:
  - Need recipient confirmation seperti di entri data.
  - ASG DU-215-8 berada di entitas terpisah dengan Feature Suite Assignment level `None`, bukan di entitas level `Full` yang dipakai langkah lain spec ini; `Hendra Kusuma {runId}` adalah PIC Division di entitas itu.

## Test Steps

### Aktor yang menjadi Assignee dapat menjadi pemberi saat Handover dengan scan TAG
1. Hendra memverifikasi tag baris `Laptop Dell XPS {runId}` pada DU-215-5 yang Assignee-nya adalah Hendra sendiri
2. Hendra menekan `[Complete Handover]` untuk baris `Laptop Dell XPS {runId}`
3. Verifikasi baris `Laptop Dell XPS {runId}` berstatus `Assigned` dengan Confirmation `Confirmed (self)` tanpa permintaan konfirmasi ke penerima
4. Verifikasi node `Handed over` di Assignment Log baris `Laptop Dell XPS {runId}` menampilkan `Self-processed`

### Aktor yang menjadi PIC Division dapat menjadi pemberi saat Handover dengan scan TAG
5. Hendra memverifikasi tag baris `Genset Honda EU {runId}` pada DU-215-6 yang Assignee-nya Division `Finance {runId}` dengan PIC `Hendra Kusuma {runId}`
6. Hendra menekan `[Complete Handover]` untuk baris `Genset Honda EU {runId}`
7. Verifikasi baris `Genset Honda EU {runId}` berstatus `Assigned` dengan Confirmation `Confirmed (self)` tanpa permintaan konfirmasi ke penerima
8. Verifikasi node `Handed over` di Assignment Log baris `Genset Honda EU {runId}` menampilkan `Self-processed`

### Aktor yang menjadi Assignee dapat menjadi penerima saat Unassign dengan scan TAG
9. Hendra mengirim permintaan Unassign langsung ke server untuk baris `Monitor LG UltraWide {runId}` pada DU-215-7 yang Assignee-nya adalah Hendra sendiri, dengan aset itu diverifikasi tanpa scan TAG
10. Verifikasi permintaan ditolak server dan baris `Monitor LG UltraWide {runId}` tetap `Assigned`
11. Hendra memverifikasi tag baris `Monitor LG UltraWide {runId}`
12. Hendra menekan `[Submit]` pada halaman Unassign untuk Assignee `Hendra Kusuma {runId}` atas baris `Monitor LG UltraWide {runId}`
13. Verifikasi baris `Monitor LG UltraWide {runId}` berstatus `Unassigned` dengan Custody `Available`
14. Verifikasi node `Unassigned` di Assignment Log baris `Monitor LG UltraWide {runId}` menampilkan `Self-processed`

### Mark as Unassigned atas aset sendiri tetap ditolak
15. Hendra mengirim `Mark as Unassigned` langsung ke server untuk baris `Genset Kohler {runId}` pada DU-215-8 pada entitas ber-Feature Suite Assignment level `None`
16. Verifikasi permintaan ditolak server karena Hendra adalah PIC Division aset itu dan baris tetap `Assigned`

### Aktor Assignment boleh mengajukan ASG untuk dirinya sendiri
17. Hendra mengajukan Assignment atas aset `Tablet Samsung Galaxy Tab {runId}` pada DU-215-9 dengan dirinya sendiri sebagai Assignee Employee
18. Verifikasi pengajuan diterima server karena pengajuan untuk diri sendiri diperbolehkan

### Pengaju dan Assignee tidak memutuskan aset atas transaksinya sendiri
19. Tono mengirim keputusan Approve langsung ke server untuk baris `Kamera Canon EOS {runId}` pada DU-215-10 yang diajukan Tono sendiri
20. Verifikasi keputusan ditolak server karena pengaju dikeluarkan dari daftar approver aset itu dan baris tetap `Waiting for Approval`
21. Mira mengirim keputusan Approve langsung ke server untuk baris `Proyektor Optoma {runId}` pada DU-215-11 yang Assignee-nya adalah Mira sendiri
22. Verifikasi keputusan ditolak server karena self-approval guard tetap berlaku dan baris tetap `Waiting for Approval`
