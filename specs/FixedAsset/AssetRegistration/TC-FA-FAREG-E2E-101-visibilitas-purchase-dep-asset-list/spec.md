---
id: TC-FA-FAREG-E2E-101-visibilitas-purchase-dep-asset-list
title: "Kelompok Purchase dihilangkan bagi Manage asset & TAG"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [FAREG-LOGIC-02c]
smoke: [FAREG-LOGIC-02c]
dependsOn: ["Asset List: kolom kelompok Purchase"]
trace:
  FAREG-LOGIC-02c: [3, 6]
anchor: [2, 5]
coverage:
  web: automated
---

# Kelompok Purchase dihilangkan bagi Manage asset & TAG

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Purchase {runId}`, tanpa Manage purchase, Group Manager, Total Control, atau Read Only.
- Layar awal: Fixed Asset > Assets > Assets.
- Data:
  - DU-101-1: Group `Gudang Purchase {runId}`, ada di entitas aktor.
  - DU-101-2: aset Active `Monitor Purchase {runId}` di Group `Gudang Purchase {runId}`, dengan `Cost` `8500000` pada kelompok Purchase.

## Test Steps

### Kelompok Purchase dihilangkan dari daftar aset
1. Ketik Search `Monitor Purchase {runId}`, tekan Enter
2. Verifikasi baris aset `Monitor Purchase {runId}` tampil dengan Group `Gudang Purchase {runId}`
3. Verifikasi kolom `Cost` tidak tampil (Hidden) pada daftar aset

### Kelompok Purchase dihilangkan dari Asset Detail
4. Klik row action `Detail` pada baris aset `Monitor Purchase {runId}`
5. Verifikasi kelompok General tampil dengan Asset Name `Monitor Purchase {runId}`
6. Verifikasi kelompok Purchase tidak tampil (Hidden) pada Asset Detail
