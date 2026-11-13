---
id: TC-FA-FAREG-E2E-075-cancel-registration-sudah-diputuskan
title: "Cancel Registration atas pengajuan yang sudah diputuskan"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [FAREG-LOGIC-20k, D-REG-17]
smoke: [D-REG-17]
dependsOn: []
trace:
  FAREG-LOGIC-20k: [8, 9]
  D-REG-17: 6
anchor: []
coverage:
  web: automated
---

# Cancel Registration atas pengajuan yang sudah diputuskan

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, pengaju pengajuan; Group terkelola `Gudang Diputus {runId}`). Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Diputus {runId}`) memutuskan pengajuan sebagai pemicu.
- Layar awal: Fixed Asset > Assets > Registration > Waiting for Approval.
- Data:
  - DU-075-1: Group `Gudang Diputus {runId}`, ada di entitas aktor.
  - DU-075-2: pengajuan Waiting for Approval di Group `Gudang Diputus {runId}`, diajukan Rina W.
  - DU-075-3: satu Item pada pengajuan itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `2`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `2`.
  - DU-075-4: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Diputus {runId}`).
- Kondisi:
  - Group `Gudang Diputus {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Cancel atas pengajuan yang sudah diputuskan membuka dialog blok
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Detail` pada baris Group `Gudang Diputus {runId}`
3. Budi S memutuskan pengajuan Group `Gudang Diputus {runId}` dengan seluruh aset `Approve`
4. Klik `[Cancel Registration]` pada footer halaman Detail
5. Klik `[Cancel Registration]` pada dialog `Cancel Registration`
6. Verifikasi dialog `Cannot Cancel` tampil dengan pesan `This request was already decided by Budi S.`
7. Klik `[OK]`
8. Verifikasi halaman Detail pengajuan dimuat ulang dan menampilkan Badge status `Approved`
9. Verifikasi dialog `Cannot Cancel` tidak tampil
