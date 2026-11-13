---
id: TC-FA-FAREG-E2E-104-kuota-tenant-habis-dep-license
title: "Kuota tenant habis: Activate diblok"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§9.4.2#r8, D-REG-08]
smoke: [D-REG-08]
dependsOn: ["License: kuota tenant"]
trace:
  §9.4.2#r8: [12, 16]
  D-REG-08: [11, 12]
anchor: []
coverage:
  web: automated
---

# Kuota tenant habis: Activate diblok

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Tenant {runId}`.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-104-1: entitas khusus `Entitas Kuota Habis {runId}`, tidak dipakai spec lain.
  - DU-104-2: Group `Gudang Tenant {runId}` di entitas `Entitas Kuota Habis {runId}`, dengan sisa kuota Group `50`.
  - DU-104-3: Asset Name `Kursi Tenant {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-104-4: Quantity `1` pada Item `Kursi Tenant {runId}`, melebihi sisa kuota tenant `0`.
- Kondisi:
  - approval registrasi pada Group `Gudang Tenant {runId}` bernilai OFF.
  - sisa kuota tenant `0`.

## Test Steps

### Activate ditolak karena kuota tenant habis
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Tenant {runId}`
3. Klik `[+ Asset Name]`
4. Pilih Asset Name `Kursi Tenant {runId}`
5. Pilih Brand `Ergotec`
6. Pilih Model `No Model`
7. Isi Quantity `1`
8. Klik `[Save draft]`
9. Klik `[Submit]`
10. Klik `[Activate]`
11. Verifikasi judul dialog `Cannot Activate` dan tombol `[OK]` tampil
12. Verifikasi dialog memuat `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
13. Klik `[OK]`
14. Klik `[Cancel]`
15. Ketik Search `Gudang Tenant {runId}`, tekan Enter
16. Verifikasi batch `Gudang Tenant {runId}` tetap di sub tab Draft dengan Total Asset `1`
