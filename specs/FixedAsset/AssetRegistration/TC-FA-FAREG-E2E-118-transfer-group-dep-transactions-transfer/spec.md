---
id: TC-FA-FAREG-E2E-118-transfer-group-dep-transactions-transfer
title: "Group aset Active berubah lewat Transfer"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-03j, EB-XM-2@transactions-transfer]
smoke: []
dependsOn: ["Transactions Transfer: perpindahan Group"]
trace:
  FAREG-LOGIC-03j: 5
  EB-XM-2@transactions-transfer: 4
anchor: []
coverage:
  web: automated
---

# Group aset Active berubah lewat Transfer

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Transfer A {runId}` dan `Gudang Transfer B {runId}`.
- Layar awal: Fixed Asset > Transactions > Transfer.
- Data:
  - DU-118-1: Group `Gudang Transfer A {runId}` dengan Group Code `GTA`, ada di entitas aktor.
  - DU-118-2: Group `Gudang Transfer B {runId}` dengan Group Code `GTB`, ada di entitas aktor.
  - DU-118-3: aset Active `Laptop Transfer {runId}` di Group `Gudang Transfer A {runId}` dengan Asset Code `LPT-GTA-0118`, segmen Group `GTA`.
- Kondisi: pola Asset Code memuat segmen Group.

## Test Steps

### Transfer mengubah Group tanpa mengubah Asset Code
1. Pindahkan aset `Laptop Transfer {runId}` dari Group `Gudang Transfer A {runId}` ke Group `Gudang Transfer B {runId}` lewat Transfer
2. Buka Fixed Asset > Assets > Assets
3. Ketik Search `Laptop Transfer {runId}`, tekan Enter
4. Verifikasi Group aset `Laptop Transfer {runId}` adalah `Gudang Transfer B {runId}`
5. Verifikasi Asset Code aset tetap `LPT-GTA-0118` dengan segmen Group `GTA`
