---
id: TC-FA-ASSIGN-E2E-068-asset-detail-level-none-dep-asset-detail
title: "Asset Detail pada level None: Transaction log Assignment terbaca dan Mark as Unassigned di header"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.10#r19", "ASSIGN-LOGIC-18f", "EC-ASG-98"]
smoke: []
dependsOn: ["Asset Detail: Transaction log Assignment, aksi Mark as Unassigned di header, dan tab History"]
trace:
  "§9.10#r19": [4, 5, 6, 9, 11]
  "ASSIGN-LOGIC-18f": [6, 9]
  "EC-ASG-98": [8, 14, 15]
anchor: []
coverage:
  web: automated
---

# Asset Detail pada level None: Transaction log Assignment terbaca dan Mark as Unassigned di header

## Prerequisites
- Aktor: Total Control `Maya Kusuma {runId}` (DU-068-2) di entitas khusus DU-068-1 yang tidak dipakai spec lain
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-068-1: Entitas (Entitas khusus dengan Feature Suite Assignment level Full yang akan turun ke None), Name `Entitas None Asset Detail {runId}`, Level Feature Suite Assignment `Full`, Level setelah downgrade `None`
  - DU-068-2: User (Aktor Total Control), Name `Maya Kusuma {runId}`, Role `Total Control`, Cakupan `Seluruh client`
  - DU-068-3: User (Assignee Employee), Name `Doni Saputra {runId}`, Role `tanpa role Assignment`
  - DU-068-4: User (Pengaju pengajuan), Name `Bima Pratama {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`
  - DU-068-5: Group (Group aset), Name `Head Office {runId}`
  - DU-068-6: Assignment (ASG Assigned yang tetap berjalan sesudah downgrade), Assignee `Doni Saputra {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Kamera Canon EOS R6 {runId}`, Requested By `Bima Pratama {runId}`, Approval `Not required`
  - DU-068-7: Assignment (ASG Waiting for Handover yang ditutup saat downgrade), Assignee `Doni Saputra {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer Brother HL-L5100 {runId}`, Requested By `Bima Pratama {runId}`, Approval `Not required`
- Kondisi:
  - Feature Suite Assignment pada entitas berada pada level `Full` sebelum downgrade

## Test Steps

### Transaction log dan Mark as Unassigned di header aset Assigned
1. Downgrade plan entitas ke level `None` berjalan di T-0
2. Buka Asset Detail aset `Kamera Canon EOS R6 {runId}`
3. Buka tab `Transaction log`
4. Verifikasi kolom Assignment `Date`, `Transaction ID`, `Status`, `Reader name`, `Group`, `PIC`, dan `Assignee` tampil pada Transaction log
5. Verifikasi baris berstatus `Assigned` tampil dengan Group `Head Office {runId}` dan Assignee `Doni Saputra {runId}`
6. Verifikasi tombol `Mark as Unassigned` tampil dan aktif di header Asset Detail aset yang Assigned

### Aset yang menunggu kembali Available dan header tanpa Mark as Unassigned
7. Buka Asset Detail aset `Printer Brother HL-L5100 {runId}`
8. Verifikasi Custody aset `Printer Brother HL-L5100 {runId}` adalah `Available`
9. Verifikasi tombol `Mark as Unassigned` tidak tampil di header Asset Detail aset yang Available

### Transaction log dan Assignment Log mencatat penutupan oleh System
10. Buka tab `Transaction log`
11. Verifikasi baris berstatus `Canceled` tampil dengan Assignee `Doni Saputra {runId}`
12. Klik Transaction ID pada baris berstatus `Canceled`
13. Klik aksi `Assignment Log` pada baris aset `Printer Brother HL-L5100 {runId}`
14. Verifikasi node `Canceled by System` tampil pada dialog `Assignment Log`
15. Verifikasi Reason `Assignment not available on plan` tampil pada node `Canceled by System`
