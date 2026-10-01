---
id: TC-GS-USER-E2E-147-responsibilities-partner-pending-approvals
title: Tab Responsibilities entity Partner hanya menampilkan Pending Approvals
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-606
coverage:
  web: automated
---

# Tab Responsibilities entity Partner hanya menampilkan Pending Approvals

## Prerequisites

- Login sebagai Role: Total Control, entity Partner
- User "Pandu Partner" punya satu approval Admin Console yang menunggu
- Spec ini tidak mengubah data

## Test Steps

1. Buka User Detail "Pandu Partner" > Tab Responsibilities
2. Verifikasi hanya sub-tab Pending Approvals (Admin Console) yang ada dan switcher disembunyikan
3. Verifikasi keempat sub-tab FAMS tidak ada
4. Verifikasi kolom tabel: Transaction ID, Transaction, Requester, Submission Date

## Notes

- Pasangan `TC-GS-USER-E2E-059` bagian Entity Principal. Aturan sama untuk ketiga entity non-Client (`user.md` §4.2).
- Empty state entity Partner tidak dicakup karena tertahan `GAP-282`.
