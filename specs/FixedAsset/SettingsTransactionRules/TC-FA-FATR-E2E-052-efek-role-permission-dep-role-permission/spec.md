---
id: TC-FA-FATR-E2E-052-efek-role-permission-dep-role-permission
title: "Alert Approver mengikuti penugasan Role Transaksi Approver"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§Aturan Logika Modul#r82, §7#r21, §9.2#r11, §9.4.2#r19, §11#r1]
smoke: [§11#r1]
dependsOn:
  - "Role Permission: penugasan Role Transaksi Approver dan perubahan role"
trace:
  §Aturan Logika Modul#r82: [11, 16]
  §7#r21: [9, 13]
  §9.2#r11: [4, 9, 13]
  §9.4.2#r19: 9
  §11#r1: 11
anchor: [3]
coverage:
  web: automated
---

# Alert Approver mengikuti penugasan Role Transaksi Approver

## Prerequisites
- Aktor: Default User `Dian Permata {runId}` (DU-052-8) yang memegang Manage transaction settings (Update) dan dapat menugaskan Role Transaksi. Operator Admin Console mengubah plan entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-052-5: Entitas `Nusa Fleet {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan transaksi Assign dan Approval Workflow ON.
  - DU-052-1: Group Name `Fleet Team {runId}`, ada di entitas DU-052-5; Group tanpa Division dan tanpa Approver Assign.
  - DU-052-2: Category Name `Fleet Vehicles {runId}`, ada di entitas DU-052-5; Category leaf dengan Require approval Assign mengikuti Company default.
  - DU-052-3: User Name `Mira Lestari {runId}`, Role `Employee`, Group `Fleet Team {runId}`, ada di entitas DU-052-5; akun aktif calon Approver untuk transaksi Assign.
  - DU-052-6: User Name `Joko Santoso {runId}`, Role `Employee`, Group `Fleet Team {runId}`, ada di entitas DU-052-5; akun aktif calon Approver untuk transaksi Assign.
  - DU-052-8: User `Dian Permata {runId}`, Default User dengan Global Role Manage transaction settings (Update) dan Group Role Manage asset & TAG (Read, Update) pada Group `Fleet Team {runId}` beserta turunannya, ada di entitas DU-052-5.
- Kondisi:
  - Role Transaksi `Approver` untuk transaksi `Assign` belum ditugaskan ke user mana pun di Group mana pun di entitas DU-052-5, dan akun `Mira Lestari {runId}`, `Joko Santoso {runId}`, dan `Dian Permata {runId}` aktif.
  - Approval Workflow plan entitas DU-052-5 bernilai ON saat spec dimulai.

## Test Steps
### Alert Approver tampil selama belum ada Approver untuk transaksi itu
1. Masuk sebagai `Dian Permata {runId}`
2. Buka tab `Assign` pada node Category `Fleet Vehicles {runId}` di Fixed Asset > Settings > Transaction Settings
3. Verifikasi Require approval pada bagian Approval tab `Assign` bernilai `OFF`
4. Verifikasi Alert Approver tidak tampil di bagian Approval tab `Assign`
5. Klik `[Set own value]` pada field Require approval
6. Pilih nilai `ON` pada field Require approval
7. Klik `[Save]`
8. Klik `[Save]` pada dialog Save Changes
9. Verifikasi Alert severity `warning` dengan pesan `No one is assigned as Approver for this transaction in any Group. Approval goes to the Group Manager or Total Control.` tampil di bagian Approval tab `Assign`

### Penugasan Role Transaksi Approver menghilangkan Alert
10. Tetapkan Role Transaksi `Approver` untuk transaksi `Assign` kepada user `Mira Lestari {runId}` pada Group `Fleet Team {runId}`
11. Verifikasi penugasan Role Transaksi `Approver` untuk transaksi `Assign` pada user `Mira Lestari {runId}` tersimpan
12. Buka tab `Assign` pada node Category `Fleet Vehicles {runId}` di Fixed Asset > Settings > Transaction Settings
13. Verifikasi Alert Approver tidak tampil lagi di bagian Approval tab `Assign`

### Penugasan Role Transaksi Approver tetap bisa diisi saat Approval Workflow plan OFF
14. Operator mengubah toggle Approval Workflow plan entitas `Nusa Fleet {runId}` menjadi OFF
15. Tetapkan Role Transaksi `Approver` untuk transaksi `Assign` kepada user `Joko Santoso {runId}` pada Group `Fleet Team {runId}`
16. Verifikasi penugasan Role Transaksi `Approver` untuk transaksi `Assign` pada user `Joko Santoso {runId}` tersimpan
