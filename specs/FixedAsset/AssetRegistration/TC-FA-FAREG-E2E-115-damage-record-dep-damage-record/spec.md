---
id: TC-FA-FAREG-E2E-115-damage-record-dep-damage-record
title: "Aset Active ber-Condition Damaged mendapat Damage record"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-05l, §9.4.2#r52, EB-XM-2@damaged]
smoke: []
dependsOn: ["Damage Record: Damage record"]
trace:
  FAREG-LOGIC-05l: [7, 8, 10, 18, 19, 29]
  §9.4.2#r52: [7, 8, 10, 18, 19, 29]
  EB-XM-2@damaged: [7, 8]
anchor: []
coverage:
  web: automated
---

# Aset Active ber-Condition Damaged mendapat Damage record

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Rusak OFF {runId}`, serta capability Update pada node Group `Gudang Rusak ON {runId}` dan `Gudang Rusak Tolak {runId}`.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-115-1: Group `Gudang Rusak OFF {runId}`, ada di entitas aktor.
  - DU-115-2: Group `Gudang Rusak ON {runId}`, ada di entitas aktor.
  - DU-115-3: Group `Gudang Rusak Tolak {runId}`, ada di entitas aktor.
  - DU-115-4: Asset Name `Genset Rusak {runId}` dengan TAG Type `Non-TAG`, Brand `Cummins`, Model `C150D5`.
  - DU-115-5: batch Draft `Gudang Rusak OFF {runId}` milik Rina berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Panel kontrol retak {runId}`.
  - DU-115-6: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Rusak ON {runId}`, berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Radiator bocor {runId}`.
  - DU-115-7: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Rusak Tolak {runId}`, berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Aki soak {runId}`.
  - DU-115-8: Reason `Aset duplikat` yang diketik Rina untuk keputusan `Reject`.
- Kondisi:
  - approval registrasi bernilai OFF pada Group `Gudang Rusak OFF {runId}`, dan ON pada Group `Gudang Rusak ON {runId}` dan `Gudang Rusak Tolak {runId}`.
  - sisa kuota Group dan tenant mencukupi.

## Test Steps

### Approval OFF: Damage record dibuat saat Activate
1. Ketik Search `Gudang Rusak OFF {runId}`, tekan Enter
2. Klik row action `Edit` pada baris batch `Gudang Rusak OFF {runId}`
3. Klik `[Submit]`
4. Klik `[Activate]`
5. Buka Damage Record
6. Ketik Search `Panel kontrol retak {runId}`, tekan Enter
7. Verifikasi Damage record dengan deskripsi `Panel kontrol retak {runId}` tampil
8. Verifikasi Damage record itu ber-Source `Registration` dan berstatus `Damaged`

### Approval ON: Damage record dibuat saat Approve
9. Ganti isi kotak search dengan `Radiator bocor {runId}`, tekan Enter
10. Verifikasi tidak ada Damage record dengan deskripsi `Radiator bocor {runId}`, empty state `No results found` tampil
11. Buka Approvals > Registration > Active
12. Ketik Search `Gudang Rusak ON {runId}`, tekan Enter
13. Klik row action `Review` pada baris pengajuan `Gudang Rusak ON {runId}`
14. Klik `[Submit]`
15. Klik `[Submit]` pada dialog `Submit Approval`
16. Buka Damage Record
17. Ketik Search `Radiator bocor {runId}`, tekan Enter
18. Verifikasi Damage record dengan deskripsi `Radiator bocor {runId}` tampil
19. Verifikasi Damage record itu ber-Source `Registration` dan berstatus `Damaged`

### Reject tidak membuat Damage record
20. Buka Approvals > Registration > Active
21. Ketik Search `Gudang Rusak Tolak {runId}`, tekan Enter
22. Klik row action `Review` pada baris pengajuan `Gudang Rusak Tolak {runId}`
23. Ubah Decision aset `Genset Rusak {runId}` menjadi `Reject`
24. Isi Reason `Aset duplikat`
25. Klik `[Submit]`
26. Klik `[Submit]` pada dialog `Submit Approval`
27. Buka Damage Record
28. Ketik Search `Aki soak {runId}`, tekan Enter
29. Verifikasi tidak ada Damage record dengan deskripsi `Aki soak {runId}`, empty state `No results found` tampil
