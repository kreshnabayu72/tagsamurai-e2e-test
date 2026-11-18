---
id: TC-FA-ASTL-BE-085-manage-race-kuota-terakhir
title: "Dua aksi Manage berebut kuota terakhir"
layer: be-e2e
priority: High
caseType: Edge
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-20i, EC-36, F-ASTL-16.k2]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-20i: [3, 4]
  EC-36: [3, 4, 5]
  F-ASTL-16.k2: [5, 6]
anchor: []
---

# Dua aksi Manage berebut kuota terakhir

## Prerequisites
- Aktor: Total Control (Rina), Total Control (Budi).
- Data:
  - DU-085-1: User `Rina Maharani {runId}`, role Total Control, cakupan seluruh client.
  - DU-085-2: User `Budi Santoso {runId}`, role Total Control, cakupan seluruh client.
  - DU-085-3: Group `Cabang Makassar {runId}` dengan Available license `1`.
  - DU-085-4: Aset `Printer Laser - R1 {runId}` berstatus `Unmanaged` di `Cabang Makassar {runId}`.
  - DU-085-5: Aset `Server Rack - R2 {runId}` berstatus `Unmanaged` di `Cabang Makassar {runId}`.

## Test Steps

### Dua Manage serentak atas kuota terakhir
1. Catat jumlah entri Changelog aset `Printer Laser - R1 {runId}` dan `Server Rack - R2 {runId}`
2. Rina meng-Manage aset `Printer Laser - R1 {runId}` dan Budi meng-Manage aset `Server Rack - R2 {runId}` secara serentak, keduanya dengan sumber `Available quota`
3. Verifikasi tepat satu permintaan berhasil dan satu permintaan ditolak dengan `QUOTA_EXCEEDED`
4. Verifikasi Available group `Cabang Makassar {runId}` bernilai `0` dan tidak pernah negatif
5. Verifikasi tepat satu dari kedua aset berstatus `Pending Activation` dan aset lainnya tetap `Unmanaged`
6. Verifikasi jumlah entri Changelog kedua aset bertambah sebanyak permintaan yang berhasil, yaitu satu entri
