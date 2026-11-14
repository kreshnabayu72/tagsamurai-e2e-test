---
id: TC-FA-FATR-E2E-052-efek-role-permission-dep-role-permission
title: "Alert Approver mengikuti penugasan Role Transaksi Approver"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§Aturan Logika Modul#r80", "§7#r21", "§9.2#r11", "§11#r1"]
smoke: ["§11#r1"]
dependsOn:
  - "Role Permission: penugasan Role Transaksi Approver dan perubahan role"
trace:
  "§Aturan Logika Modul#r80": 11
  "§7#r21": [9, 13]
  "§9.2#r11": [4, 9, 13]
  "§11#r1": 11
anchor: [3]
coverage:
  web: automated
---

# Alert Approver mengikuti penugasan Role Transaksi Approver

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update) dan dapat menugaskan Role Transaksi.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-052-1: Group Name `Fleet Team {runId}`; Group tanpa Division dan tanpa Approver Assign.
  - DU-052-2: Category Name `Fleet Vehicles {runId}`; Category leaf dengan Require approval Assign mengikuti Company default.
  - DU-052-3: User Name `Mira Lestari {runId}`, Role `Employee`, Group `Fleet Team {runId}`; akun aktif calon Approver untuk transaksi Assign.
- Kondisi:
  - Role Transaksi `Approver` untuk transaksi `Assign` belum ditugaskan ke user mana pun di Group mana pun, dan akun `Mira Lestari {runId}` aktif.

## Test Steps
### Alert Approver tampil selama belum ada Approver untuk transaksi itu
1. Masuk sebagai Default User
2. Buka tab `Assign` pada node Category `Fleet Vehicles {runId}` di Fixed Asset > Settings > Transaction Settings
3. Verifikasi Require approval pada bagian Approval tab `Assign` bernilai `OFF`
4. Verifikasi Alert Approver tidak tampil di bagian Approval tab `Assign`
5. Klik `[Set own value]` pada field Require approval
6. Pilih nilai `ON` pada field Require approval
7. Klik `[Save]`
8. Klik `[Save]` pada dialog Save Changes
9. Verifikasi Alert severity warning `No one is assigned as Approver for this transaction in any Group. Approval goes to the Group Manager or Total Control.` tampil di bagian Approval tab `Assign`

### Penugasan Role Transaksi Approver menghilangkan Alert
10. Tetapkan Role Transaksi `Approver` untuk transaksi `Assign` kepada user `Mira Lestari {runId}` pada Group `Fleet Team {runId}`
11. Verifikasi penugasan Role Transaksi `Approver` untuk transaksi `Assign` pada user `Mira Lestari {runId}` tersimpan
12. Buka tab `Assign` pada node Category `Fleet Vehicles {runId}` di Fixed Asset > Settings > Transaction Settings
13. Verifikasi Alert Approver tidak tampil lagi di bagian Approval tab `Assign`
