---
id: TC-FA-FAREG-E2E-074-cancel-registration-dibuang
title: "Cancel Registration dengan aset dibuang"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§9.7#r12", "§9.7#r17", D-REG-14, T-REG-10]
smoke: [D-REG-14, T-REG-10]
dependsOn: []
trace:
  "§9.7#r12": 12
  "§9.7#r17": [8, 12]
  D-REG-14: 4
  T-REG-10: 6
anchor: [11]
coverage:
  web: automated
---

# Cancel Registration dengan aset dibuang

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, pengaju pengajuan; Group terkelola `Gudang Dibuang {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Waiting for Approval.
- Data:
  - DU-074-1: Group `Gudang Dibuang {runId}`, ada di entitas aktor.
  - DU-074-2: pengajuan Waiting for Approval di Group `Gudang Dibuang {runId}`, diajukan Rina W.
  - DU-074-3: satu Item pada pengajuan itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `4`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `4`.
  - DU-074-4: batch Draft pembanding milik Rina W di Group `Gudang Dibuang {runId}`, Total Asset `1`.
- Kondisi:
  - Group `Gudang Dibuang {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Cancel Registration dengan checkbox dilepas membuang aset
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Cancel registration` pada baris Group `Gudang Dibuang {runId}`
3. Klik checkbox `Save as Draft to edit` hingga tidak tercentang
4. Verifikasi teks bantu `The assets will be discarded and their reserved quota is released. This can't be undone.` tampil
5. Klik `[Cancel Registration]`
6. Verifikasi toast `Success, registration has been canceled.` tampil
7. Ketik Search `{runId}`, tekan Enter
8. Verifikasi baris pengajuan Group `Gudang Dibuang {runId}` tampil di sub tab `History` dengan Total Asset `4`, Status `Canceled`, dan Approver `—`
9. Klik sub tab `Draft`
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris batch Draft pembanding Group `Gudang Dibuang {runId}` tampil dengan Total Asset `1`
12. Verifikasi hanya baris dengan Total Asset `1` yang tampil sehingga tidak ada batch Draft hasil pengajuan yang dibatalkan
