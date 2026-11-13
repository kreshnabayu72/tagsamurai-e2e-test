---
id: TC-FA-FAREG-E2E-072-auto-approve-kondisi-b
title: "Submit dengan approver independen tidak di-approve otomatis"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-06l, "§8.3#r7"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-06l: [5, 8]
  "§8.3#r7": 11
anchor: [10]
coverage:
  web: automated
---

# Submit dengan approver independen tidak di-approve otomatis

## Prerequisites
- Aktor: Rina W (Manage asset & TAG dengan capability Update pada Group `Gudang Mandiri {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-072-1: Group `Gudang Mandiri {runId}`, ada di entitas aktor.
  - DU-072-2: batch Draft milik Rina W di Group `Gudang Mandiri {runId}`.
  - DU-072-3: satu Item pada batch itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `2`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `2`; seluruh aset memenuhi Tingkat 2.
  - Node Registration Log yang diharapkan `Submitted by Rina W.`, dari pengaju Rina W; nama singkat Rina W tampil `Rina W.`.
- Kondisi:
  - Group `Gudang Mandiri {runId}` ber-toggle `Require Approval for Registration` ON.
  - Client aktor memiliki pengguna Total Control: Total Control eligible di setiap node Group dan dihitung sebagai approver independen, sehingga pengaju bukan satu-satunya anggota himpunan approver eligible dan Kondisi B tidak terpenuhi.

## Test Steps

### Submit dengan approver independen masuk Waiting for Approval
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Edit` pada baris Group `Gudang Mandiri {runId}`
3. Klik `[Submit]`
4. Klik `[Submit for Approval]`
5. Verifikasi toast `Success, registration has been submitted.` tampil pada pengajuan yang tidak di-approve otomatis
6. Klik sub tab `Waiting for Approval`
7. Ketik Search `{runId}`, tekan Enter
8. Verifikasi baris pengajuan Group `Gudang Mandiri {runId}` tampil di sub tab `Waiting for Approval` dengan Total Asset `2`

### Registration Log tidak mencatat Auto-approved Kondisi B
9. Klik ikon `Registration Log` pada baris Group `Gudang Mandiri {runId}`
10. Verifikasi timeline pengajuan Group `Gudang Mandiri {runId}` memuat node `Submitted by Rina W.`[^drift-1]
11. Verifikasi timeline tidak memuat node berjudul `Approved by system (no independent approver)`

[^drift-1]: Drift PRD vs override. PRD §8.3 node log `Submitted by [User]` memakai nama singkat pengguna; `prd-conventions.md` §9.13: `[First Name] [Last Initial]` (contoh tanpa titik: `John L`). Baris O-4: nama singkat mengakhiri inisial dengan titik (`John L.`). Diasersi: override O-4 (SB-6), sehingga nama singkat `Rina W.`.
