---
id: TC-FA-FAREG-E2E-079-approval-semua-approve
title: "Keputusan approval: semua aset Approve"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-20h, "§9.7#r10", FAREG-LOGIC-06h, D-REG-10, T-REG-08]
smoke: [FAREG-LOGIC-06h, D-REG-10, T-REG-08]
dependsOn: []
trace:
  FAREG-LOGIC-20h: 10
  "§9.7#r10": [13, 16]
  FAREG-LOGIC-06h: 13
  D-REG-10: [5, 6, 7]
  T-REG-08: 9
anchor: []
coverage:
  web: automated
---
# Keputusan approval: semua aset Approve

## Prerequisites
- Aktor: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Setuju {runId}`, approver). Rina W (Manage asset & TAG) adalah pengaju pengajuan.
- Layar awal: Approvals > Registration > Active.
- Data:
  - DU-079-1: Group `Gudang Setuju {runId}`, ada di entitas aktor.
  - DU-079-2: pengajuan Waiting for Approval di Group `Gudang Setuju {runId}`, diajukan Rina W.
  - DU-079-3: satu Item pada pengajuan itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `3`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `3`.
  - DU-079-4: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Setuju {runId}`).
- Kondisi:
  - Group `Gudang Setuju {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Semua aset Approve: Submit keputusan dan kembali ke antrean Active
1. Buka menu Approvals > Registration, tab `Active`
2. Ketik Search `{runId}`, tekan Enter
3. Klik ikon `Review` pada baris Group `Gudang Setuju {runId}`
4. Klik `[Submit]`
5. Verifikasi dialog `Submit Approval` terbuka
6. Verifikasi dialog memuat ringkasan jumlah `Approve` `3`, `Return to Draft` `0`, dan `Reject` `0`
7. Verifikasi dialog memuat pertanyaan `Are you sure you want to submit it?`
8. Klik `[Submit]` pada dialog `Submit Approval`
9. Verifikasi toast `Success, registration request has been decided.` tampil
10. Verifikasi halaman kembali ke antrean `Approvals > Registration > Active`

### Pengajuan menjadi Approved dan seluruh aset Approved
11. Klik tab `History`
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi baris Group `Gudang Setuju {runId}` tampil dengan Total Asset `3`, Status `Approved`, dan Approver `Budi S`
14. Klik ikon `Detail` pada baris Group `Gudang Setuju {runId}`
15. Klik tab `Asset`
16. Verifikasi kolom Result bernilai `Approved` pada ketiga aset
