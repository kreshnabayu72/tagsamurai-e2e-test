---
id: TC-FA-FAREG-E2E-081-approval-semua-reject
title: "Keputusan approval: tidak ada aset Approve"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§9.4.2#r22", "§9.7#r12", FAREG-LOGIC-06h]
smoke: [FAREG-LOGIC-06h]
dependsOn: []
trace:
  "§9.4.2#r22": [18, 23, 25]
  "§9.7#r12": [23, 25]
  FAREG-LOGIC-06h: 16
anchor: [22]
coverage:
  web: automated
---
# Keputusan approval: tidak ada aset Approve

## Prerequisites
- Aktor: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Tolak {runId}`, approver). Rina W (Manage asset & TAG) adalah pengaju pengajuan.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-081-1: Group `Gudang Tolak {runId}` dengan batas kuota aset `50`, ada di entitas aktor.
  - DU-081-2: pengajuan Waiting for Approval di Group `Gudang Tolak {runId}`, diajukan Rina W.
  - DU-081-3: satu Item pada pengajuan itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `2`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `2`.
  - DU-081-4: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Tolak {runId}`).
  - DU-081-5: batch Draft pembanding milik Rina W di Group `Gudang Tolak {runId}`, Total Asset `1`.
  - DU-081-6: keputusan yang diisi langkah: Reject dengan Reason `Duplicate entry`.
- Kondisi:
  - Group `Gudang Tolak {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Reject seluruh aset: pengajuan Rejected, alasan tercatat, dan tidak ada Draft baru
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Edit` pada baris Group `Gudang Tolak {runId}`
3. Catat nilai `Remaining Quota` pada form
4. Klik `[Cancel]` pada form; form belum diubah sehingga tidak ada dialog Unsaved Changes
5. Buka menu Approvals > Registration, tab `Active`
6. Ketik Search `{runId}`, tekan Enter
7. Klik ikon `Review` pada baris Group `Gudang Tolak {runId}`
8. Centang seluruh aset pada grup `Office Desk`
9. Pilih `Reject` pada Bulk Action
10. Isi Reason `Duplicate entry`
11. Klik `[Apply]`
12. Klik `[Submit]`
13. Klik `[Submit]` pada dialog `Submit Approval`
14. Klik tab `History`
15. Ketik Search `{runId}`, tekan Enter
16. Verifikasi baris Group `Gudang Tolak {runId}` tampil dengan Total Asset `2`, Status `Rejected`, dan Approver `Budi S`
17. Klik ikon `Registration Log` pada baris Group `Gudang Tolak {runId}`
18. Verifikasi node timeline berjudul `Rejected by Budi S` memuat Reason `Duplicate entry` sebagai alasan penolakan
19. Klik ikon `✕` pada dialog Registration Log
20. Buka Fixed Asset > Assets > Registration, sub tab `Draft`
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi baris batch Draft pembanding Group `Gudang Tolak {runId}` dengan Total Asset `1` tampil
23. Verifikasi hanya satu baris yang tampil sehingga tidak ada batch Draft baru dari aset yang ditolak
24. Klik ikon `Edit` pada baris Group `Gudang Tolak {runId}`
25. Verifikasi `Remaining Quota` pada form bertambah `2` dari nilai yang dicatat sebelum keputusan
26. Klik `[Cancel]` pada form; form belum diubah sehingga tidak ada dialog Unsaved Changes
