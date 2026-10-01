---
id: TC-GS-USER-E2E-146-responsibilities-distributor-pending-approvals
title: Tab Responsibilities entity Distributor hanya menampilkan Pending Approvals
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-605
coverage:
  web: automated
---

# Tab Responsibilities entity Distributor hanya menampilkan Pending Approvals

## Prerequisites

- Login sebagai Role: Total Control, entity Distributor
- User "Dewi Distributor" punya satu approval Admin Console yang menunggu
- Spec ini tidak mengubah data

## Test Steps

1. Buka User Detail "Dewi Distributor" > Tab Responsibilities
2. Verifikasi hanya sub-tab Pending Approvals (Admin Console) yang ada dan switcher disembunyikan
3. Verifikasi keempat sub-tab FAMS tidak ada
4. Verifikasi kolom tabel: Transaction ID, Transaction, Requester, Submission Date

## Notes

- Pasangan `TC-GS-USER-E2E-059` bagian Entity Principal. Aturan sama untuk ketiga entity non-Client (`user.md` §4.2).
- Empty state entity Distributor tidak dicakup karena tertahan `GAP-282`.
