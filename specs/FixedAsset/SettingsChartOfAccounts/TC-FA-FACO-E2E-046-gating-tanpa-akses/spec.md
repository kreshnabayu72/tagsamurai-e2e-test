---
id: TC-FA-FACO-E2E-046-gating-tanpa-akses
title: "Aktor tanpa capability tidak melihat menu dan ditolak lewat alamat langsung"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§2.1#r4", "§2.2#r4", "§2.2#r5", "§9.4.2#r31", "EB-AKS-1", "EB-AKS-2"]
smoke: []
dependsOn: []
trace:
  "§2.1#r4": [3, 6, 11, 14]
  "§2.2#r4": [3, 6]
  "§2.2#r5": [11, 14]
  "§9.4.2#r31": [3, 5, 6, 11, 13, 14]
  "EB-AKS-1": [3, 11]
  "EB-AKS-2": [5, 6, 7, 13, 14, 15]
anchor: [2, 10]
coverage:
  web: automated
---

# Aktor tanpa capability tidak melihat menu dan ditolak lewat alamat langsung

## Prerequisites
- Aktor: User `Yoga Pratama {runId}` (Group Manager, tanpa capability Manage accounting) dan User `Dewi Anggraini {runId}` (role lain, bukan Group Manager, tanpa capability Manage accounting).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-046-1: User `Yoga Pratama {runId}` dengan access level Group Manager tanpa Manage accounting, scope seluruh client.
  - DU-046-2: User `Dewi Anggraini {runId}` dengan role lain (bukan Group Manager) tanpa Manage accounting, scope seluruh client.

## Test Steps

### Menu tidak tampil di sidebar
1. Buka sidebar
2. Verifikasi sidebar memuat item menu lain yang boleh diakses aktor
3. Verifikasi menu `Accounting` tidak tampil di sidebar, termasuk di bawah menu `Settings`

### Alamat langsung ditolak
4. Buka halaman Chart of Accounts lewat alamat langsung
5. Verifikasi toast `You don't have permission to do this.` tampil
6. Verifikasi tabel Account List tidak tampil
7. Verifikasi aktor tidak dialihkan ke halaman lain

### Menu tidak tampil di sidebar bagi aktor role lain
8. Masuk sebagai `Dewi Anggraini {runId}`
9. Buka sidebar
10. Verifikasi sidebar memuat item menu lain yang boleh diakses aktor
11. Verifikasi menu `Accounting` tidak tampil di sidebar, termasuk di bawah menu `Settings`

### Alamat langsung ditolak bagi aktor role lain
12. Buka halaman Chart of Accounts lewat alamat langsung
13. Verifikasi toast `You don't have permission to do this.` tampil
14. Verifikasi tabel Account List tidak tampil
15. Verifikasi aktor tidak dialihkan ke halaman lain
