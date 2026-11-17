---
id: TC-FA-MYASSET-E2E-003-plan-tanpa-borrowing-dan-assignment
title: "Item My Asset disembunyikan dan URL ditolak saat plan tanpa Borrowing dan Assignment"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.10#p1"]
smoke: []
dependsOn: []
trace:
  "§9.10#p1": [3, 6]
anchor: [2, 5]
coverage:
  web: automated
---

# Item My Asset disembunyikan dan URL ditolak saat plan tanpa Borrowing dan Assignment

## Prerequisites
- Aktor: Borrower di entitas khusus ber-plan `Starter`; entitas ini tidak dipakai spec lain.
- Layar awal: halaman FAMS yang memuat navbar.
- Data:
  - DU-003-1: Entitas `Entitas Starter {runId}` dengan Plan `Starter`; Borrowing dan Assignment tidak tersedia pada plan itu.
  - DU-003-2: User `Hendra Saputra {runId}`, Borrower aktif di entitas DU-003-1.

## Test Steps

### Item My Asset disembunyikan di menu profil
1. Klik avatar di navbar
2. Verifikasi menu profil memuat item akun lain
3. Verifikasi tidak ada item `My Asset` di menu profil

### Akses langsung ke URL My Asset ditolak
4. Buka halaman My Asset lewat alamat langsung
5. Verifikasi navbar tampil
6. Verifikasi akses ke halaman My Asset ditolak, tidak ada tab `Task`, `Borrowed`, `Assigned`, dan `History`
