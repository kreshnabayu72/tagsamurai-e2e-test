---
id: TC-GS-USER-E2E-059-responsibilities-gating-subscription
title: 'Tab Responsibilities menyesuaikan sub-tab dengan entity dan subscription'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-100
  - TC-GS-USER-101
  - TC-GS-USER-484
  - TC-GS-USER-104
  - TC-GS-USER-380
coverage:
  web: automated
---

# Tab Responsibilities menyesuaikan sub-tab dengan entity dan subscription

## Prerequisites

- Empat entity uji, masing-masing dengan Role: Total Control:
  - Entity A: Client dengan FAMS aktif. User "Ahmad Fauzi" punya satu baris di tiap sub-tab (Borrowed Assets, Assigned Assets, Pending Approvals, Pending Tasks), dan user "Dodi Kosong" punya nol baris di keempatnya
  - Entity B: Client tanpa subscription FAMS, dengan produk lain yang aktif
  - Entity C: Client tanpa subscription produktif apa pun
  - Entity P: Principal (Admin Console)
- Pengamatan permintaan jaringan ke Fixed-Asset dan Supply Asset tersedia bagi skrip
- Spec ini tidak mengubah data. Cara berpindah entity ditentukan tim FE di tahap script

## Test Steps

### Client dengan FAMS aktif

1. Di entity A, buka User Detail "Ahmad Fauzi" > Tab Responsibilities
2. Verifikasi label tab "Responsibilities (4)" dan 4 sub-tab tampil dengan badge masing-masing: "Borrowed Assets (1)", "Assigned Assets (1)", "Pending Approvals (1)", "Pending Tasks (1)"
3. Buka User Detail "Dodi Kosong" > Tab Responsibilities
4. Verifikasi empty state global "No pending responsibilities" dengan deskripsi "This user has no active custody, pending approvals, or tasks." tampil sebelum sub-tab mana pun dibuka

### Client tanpa FAMS

5. Di entity B, buka Tab Responsibilities user mana pun
6. Verifikasi keempat sub-tab FAMS tidak tampil di switcher dan tidak ada permintaan jaringan ke Fixed-Asset sama sekali

### Client tanpa subscription produktif

7. Di entity C, buka Tab Responsibilities user mana pun
8. Verifikasi empty state global "No pending responsibilities" dengan deskripsi "This user has no active custody, pending approvals, or tasks." tampil, tanpa sub-tab switcher, dan tidak ada permintaan jaringan ke Fixed-Asset atau Supply Asset

### Entity Principal

9. Di entity P, buka Tab Responsibilities user mana pun yang punya approval menunggu
10. Verifikasi hanya sub-tab Pending Approvals (Admin Console) yang ada dan switcher disembunyikan, keempat sub-tab FAMS tidak ada, dan kolomnya identik dengan versi Client: Transaction ID, Transaction, Requester, Submission Date

## Notes

- Sumber `user.md` bagian 4.1 (gating subscription), 4.2, 4.2a, dan 7.1. Untuk tenant tanpa FAMS, array FAMS bernilai `null`, sehingga sub-tab tidak dirender dan tidak ada round-trip.
- Kebutuhan empat entity dengan konfigurasi subscription berbeda ditulis di Prerequisites untuk tim FE.
