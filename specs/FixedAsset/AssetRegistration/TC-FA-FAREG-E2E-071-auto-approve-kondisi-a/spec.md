---
id: TC-FA-FAREG-E2E-071-auto-approve-kondisi-a
title: "Auto-approve Kondisi A: pengaju Group Manager Group aset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06l, "§8.3#r7", "§9.2#p41", "§9.2#p43", "§9.2#p45", "§9.2#p46", "§9.2#p47", "§9.7#r8"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-06l: [6, 8, 14]
  "§8.3#r7": [8, 9]
  "§9.2#p41": 6
  "§9.2#p43": 6
  "§9.2#p45": 6
  "§9.2#p46": [6, 8]
  "§9.2#p47": 14
  "§9.7#r8": [6, 8, 14]
anchor: [13]
coverage:
  web: automated
---

# Auto-approve Kondisi A: pengaju Group Manager Group aset

## Prerequisites
- Aktor: Agus P (Group Manager Group `Gudang Manajer {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-071-1: Group `Gudang Manajer {runId}`, ada di entitas aktor.
  - DU-071-2: batch Draft milik Agus P di Group `Gudang Manajer {runId}`.
  - DU-071-3: satu Item pada batch itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `30`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `30`; seluruh aset memenuhi Tingkat 2.
  - DU-071-4: pengajuan berstatus Waiting for Approval di Group `Gudang Manajer {runId}`, diajukan Rina W (Manage asset & TAG), Total Asset `5`.
  - Node Registration Log yang diharapkan `Approved by Agus P (Group Manager — requester)`, dari pengaju Agus P.
- Kondisi:
  - Group `Gudang Manajer {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Submit oleh Group Manager langsung Approved dan masuk History
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Edit` pada baris Group `Gudang Manajer {runId}`
3. Klik `[Submit]`
4. Klik `[Submit for Approval]`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris pengajuan Group `Gudang Manajer {runId}` tampil di sub tab `History` dengan Total Asset `30`, Status `Approved`, dan Approver `Agus P`

### Registration Log mencatat Auto-approved Kondisi A
7. Klik ikon `Registration Log` pada baris Group `Gudang Manajer {runId}`
8. Verifikasi node timeline berjudul `Approved by Agus P (Group Manager — requester)`
9. Verifikasi node itu memuat Jumlah Approved `30`
10. Klik ikon `✕` pada dialog Registration Log

### Pengajuan auto-approve tidak masuk antrean Approvals
11. Buka menu Approvals > Registration, tab `Active`
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi baris pengajuan Group `Gudang Manajer {runId}` dengan Total Asset `5` tampil di tab `Active`
14. Verifikasi hanya baris dengan Total Asset `5` yang tampil sehingga pengajuan dengan Total Asset `30` tidak ada di antrean
