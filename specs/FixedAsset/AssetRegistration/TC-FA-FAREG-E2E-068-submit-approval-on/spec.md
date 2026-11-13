---
id: TC-FA-FAREG-E2E-068-submit-approval-on
title: "Submit pada Group approval ON: pengajuan Waiting for Approval"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06c, FAREG-LOGIC-20h, "§9.7#r7", EB-FRM-1@dialog-activate, FAREG-LOGIC-06a, D-REG-03, T-REG-03]
smoke: [FAREG-LOGIC-06a, D-REG-03, T-REG-03]
dependsOn: []
trace:
  FAREG-LOGIC-06c: 11
  FAREG-LOGIC-20h: 9
  "§9.7#r7": 11
  EB-FRM-1@dialog-activate: 13
  FAREG-LOGIC-06a: 12
  D-REG-03: [4, 5, 6]
  T-REG-03: 8
anchor: []
coverage:
  web: automated
---

# Submit pada Group approval ON: pengajuan Waiting for Approval

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang Pengajuan {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-068-1: Group `Gudang Pengajuan {runId}`, ada di entitas aktor.
  - DU-068-2: batch Draft milik Rina W di Group `Gudang Pengajuan {runId}`.
  - DU-068-3: satu Item pada batch itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `2`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `2`; seluruh aset memenuhi Tingkat 2.
  - DU-068-4: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Pengajuan {runId}`), approver eligible lain selain Rina W.
  - Bullet dialog yang diharapkan `Gudang Pengajuan {runId} · 2 assets`, dari Group `Gudang Pengajuan {runId}` dan Total Asset `2`.
- Kondisi:
  - Group `Gudang Pengajuan {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Submit for Approval menghasilkan satu pengajuan Waiting for Approval
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Edit` pada baris Group `Gudang Pengajuan {runId}`
3. Klik `[Submit]`
4. Verifikasi dialog konfirmasi memuat bullet `Gudang Pengajuan {runId} · 2 assets`
5. Verifikasi dialog konfirmasi memuat pertanyaan `Are you sure you want to submit it for approval?`
6. Verifikasi tombol `[Submit for Approval]` tampil di dialog konfirmasi
7. Klik `[Submit for Approval]` dua kali berturut-turut
8. Verifikasi toast `Success, registration has been submitted.` tampil
9. Verifikasi halaman kembali ke Registration dengan sub tab `Waiting for Approval` aktif
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris pengajuan Group `Gudang Pengajuan {runId}` tampil dengan Total Asset `2` di sub tab `Waiting for Approval`
12. Verifikasi Registration ID pada baris itu berformat `REG-YYYYMMDD-NNNNN`
13. Verifikasi hanya satu baris pengajuan Group `Gudang Pengajuan {runId}` tampil
