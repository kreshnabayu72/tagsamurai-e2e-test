---
id: TC-FA-FAREG-E2E-069-submit-aset-belum-lengkap
title: "Submit dengan aset belum memenuhi Tingkat 2: tidak ada yang diproses"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§9.4.2#r7", FAREG-LOGIC-01i, V-REG-02]
smoke: [FAREG-LOGIC-01i, V-REG-02]
dependsOn: []
trace:
  "§9.4.2#r7": [5, 8, 11]
  FAREG-LOGIC-01i: 11
  V-REG-02: 4
anchor: []
coverage:
  web: automated
---

# Submit dengan aset belum memenuhi Tingkat 2: tidak ada yang diproses

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang Kekurangan {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-069-1: Group `Gudang Kekurangan {runId}`, ada di entitas aktor.
  - DU-069-2: batch Draft milik Rina W di Group `Gudang Kekurangan {runId}`.
  - DU-069-3: satu Item pada batch itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `2`, TAG Type `Non-TAG`; Total Asset `2`. Aset ke-1 Condition `Normal` dan memenuhi Tingkat 2. Aset ke-2 Condition `Damaged` dengan Damage note belum diisi, sehingga belum memenuhi Tingkat 2.

## Test Steps

### Submit ditolak dan seluruh aset tetap Draft
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Edit` pada baris Group `Gudang Kekurangan {runId}`
3. Klik `[Submit]`
4. Verifikasi `Alert` Danger tampil di atas footer dengan pesan `Please complete the data for 1 asset to continue.`
5. Verifikasi dialog konfirmasi Submit tidak terbuka
6. Klik tab `Asset`
7. Klik kolom Name aset ke-2 pada Item `Office Desk`
8. Verifikasi field Damage note ditandai danger dengan pesan inline `Damage note must not be empty`
9. Klik `[Cancel]` pada form; form belum diubah sehingga tidak ada dialog Unsaved Changes
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris Group `Gudang Kekurangan {runId}` masih tampil di sub tab `Draft` dengan Total Asset `2`
