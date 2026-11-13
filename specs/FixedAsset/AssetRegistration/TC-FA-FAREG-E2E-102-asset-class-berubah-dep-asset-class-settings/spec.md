---
id: TC-FA-FAREG-E2E-102-asset-class-berubah-dep-asset-class-settings
title: "Asset Class berubah selama pengajuan menunggu"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-09c, §9.4.2#r14]
smoke: []
dependsOn: ["Asset Class Settings: Asset Class milik Asset Name"]
trace:
  FAREG-LOGIC-09c: [5, 6]
  §9.4.2#r14: [5, 6, 10]
anchor: [4]
coverage:
  web: automated
---

# Asset Class berubah selama pengajuan menunggu

## Prerequisites
- Aktor:
  - Budi, role Manage asset & TAG dengan capability Update pada node Group `Gudang Kelas {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang memicu perubahan Asset Class.
- Layar awal: Approvals > Registration > Active.
- Data:
  - DU-102-1: Group `Gudang Kelas {runId}`, ada di entitas aktor.
  - DU-102-2: Asset Name `Meja Kelas {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`, dan Asset Class `Furniture Kelas A {runId}`.
  - DU-102-3: Asset Class `Furniture Kelas B {runId}`, ada di master Asset Class.
  - DU-102-4: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Kelas {runId}`, berisi 1 aset Asset Name `Meja Kelas {runId}`.
- Kondisi: approval registrasi pada Group `Gudang Kelas {runId}` bernilai ON.

## Test Steps

### Asset Class berubah tidak memunculkan penanda di halaman Approval
1. Ketik Search `Gudang Kelas {runId}`, tekan Enter
2. Klik row action `Review` pada baris pengajuan `Gudang Kelas {runId}`
3. Admin mengubah Asset Class Asset Name `Meja Kelas {runId}` menjadi `Furniture Kelas B {runId}`
4. Verifikasi baris aset dengan Brand `Ergotec` tetap tampil pada halaman Approval
5. Verifikasi tidak ada `Alert` Warning di atas tabel aset
6. Verifikasi baris aset dengan Brand `Ergotec` tidak ditandai `Unavailable`

### Aset mengikuti Asset Class milik Asset Name sesudah Approve
7. Klik `[Submit]` pada halaman Approval
8. Klik `[Submit]` pada dialog `Submit Approval`
9. Buka Detail aset `Meja Kelas {runId}`
10. Verifikasi Asset Class aset `Furniture Kelas B {runId}`
