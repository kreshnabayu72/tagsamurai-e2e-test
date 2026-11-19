---
id: TC-FA-ASSIGN-E2E-066-aksi-asset-list-level-basic-dep-asset-list
title: "Asset List pada level Basic: aksi Assign tampil dan Add to Assignment Draft tidak tampil"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.10#b2", "EC-ASG-99"]
smoke: []
dependsOn: ["Asset List: aksi Assign dan Add to Assignment Draft pada baris aset"]
trace:
  "§9.10#b2": [3, 4, 9, 10]
  "EC-ASG-99": [4, 10]
anchor: []
coverage:
  web: automated
---

# Asset List pada level Basic: aksi Assign tampil dan Add to Assignment Draft tidak tampil

## Prerequisites
- Aktor: Total Control `Dian Permata {runId}` (DU-066-2) di entitas khusus DU-066-1 yang tidak dipakai spec lain
- Layar awal: Asset List
- Data:
  - DU-066-1: Entitas (Entitas khusus dengan Feature Suite Assignment level Basic), Name `Entitas Basic Asset List {runId}`, Level Feature Suite Assignment `Basic`, Level sebelumnya `Full`
  - DU-066-2: User (Aktor Total Control), Name `Dian Permata {runId}`, Role `Total Control`, Cakupan `Seluruh client`
  - DU-066-3: Group (Group aset), Name `Head Office {runId}`
  - DU-066-4: Asset (Aset tersedia untuk aksi baris), Name `Printer Epson L3250 {runId}`, Group `Head Office {runId}`, Custody `Available`
  - DU-066-5: Asset (Aset tersedia kedua untuk aksi bulk), Name `Proyektor BenQ MW550 {runId}`, Group `Head Office {runId}`, Custody `Available`
- Kondisi:
  - Feature Suite Assignment pada entitas berada pada level `Basic` setelah turun dari `Full` pada T-0

## Test Steps

### Aksi baris aset pada level Basic
1. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
2. Buka menu ⋯ pada baris aset `Printer Epson L3250 {runId}`
3. Verifikasi aksi `Assign` tampil pada baris aset `Printer Epson L3250 {runId}`
4. Verifikasi aksi `Add to Assignment Draft` tidak tampil pada baris aset `Printer Epson L3250 {runId}`
5. Tutup menu ⋯

### Aksi bulk pada level Basic
6. Ganti isi kotak Search dengan `{runId}`, tekan Enter
7. Centang baris `Printer Epson L3250 {runId}`
8. Centang baris `Proyektor BenQ MW550 {runId}`
9. Verifikasi aksi `Assign` tampil pada menu aksi bulk
10. Verifikasi aksi `Add to Assignment Draft` tidak tampil pada menu aksi bulk
