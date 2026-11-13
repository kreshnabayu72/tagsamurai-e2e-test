---
id: TC-FA-FAREG-E2E-072-auto-approve-kondisi-b
title: "Auto-approve Kondisi B: tanpa approver independen"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06l, "§8.3#r7"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-06l: [6, 8]
  "§8.3#r7": [8, 9]
anchor: []
coverage:
  web: automated
---

# Auto-approve Kondisi B: tanpa approver independen

## Prerequisites
- Aktor: Rina W (Manage asset & TAG dengan capability Update pada Group `Gudang Mandiri {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-072-1: Group `Gudang Mandiri {runId}`, ada di entitas aktor.
  - DU-072-2: batch Draft milik Rina W di Group `Gudang Mandiri {runId}`.
  - DU-072-3: satu Item pada batch itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `2`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `2`; seluruh aset memenuhi Tingkat 2.
  - Node Registration Log yang diharapkan `Approved by system (no independent approver)`.
- Kondisi:
  - Group `Gudang Mandiri {runId}` ber-toggle `Require Approval for Registration` ON.
  - Rina W adalah satu-satunya anggota himpunan approver eligible pada Group `Gudang Mandiri {runId}`: tidak ada Group Manager, Total Control, maupun pemegang capability Update lain yang eligible.

## Test Steps

### Submit oleh satu-satunya approver eligible langsung Approved oleh sistem
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Edit` pada baris Group `Gudang Mandiri {runId}`
3. Klik `[Submit]`
4. Klik `[Submit for Approval]`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris pengajuan Group `Gudang Mandiri {runId}` tampil di sub tab `History` dengan Total Asset `2`, Status `Approved`, dan Approver `System`

### Registration Log mencatat Auto-approved Kondisi B
7. Klik ikon `Registration Log` pada baris Group `Gudang Mandiri {runId}`
8. Verifikasi node timeline berjudul `Approved by system (no independent approver)`
9. Verifikasi node itu memuat Jumlah Approved `2`
