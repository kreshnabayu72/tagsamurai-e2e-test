---
id: TC-FA-FACO-E2E-046-gating-tanpa-akses
title: "Aktor tanpa capability ditolak lewat alamat langsung"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§2.1#r4", "§2.2#r4", "§2.2#r5", "§9.4.2#r31", "EB-AKS-2"]
smoke: []
dependsOn: []
trace:
  "§2.1#r4": [3, 8]
  "§2.2#r4": [3]
  "§2.2#r5": [8]
  "§9.4.2#r31": [2, 3, 7, 8]
  "EB-AKS-2": [2, 3, 4, 7, 8, 9]
anchor: []
coverage:
  web: automated
---

# Aktor tanpa capability ditolak lewat alamat langsung

## Prerequisites
- Aktor: User `Yoga Pratama {runId}` (Group Manager, tanpa capability Manage accounting) dan User `Dewi Anggraini {runId}` (role lain, bukan Group Manager, tanpa capability Manage accounting).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-046-1: User `Yoga Pratama {runId}` dengan access level Group Manager tanpa Manage accounting, scope seluruh client.
  - DU-046-2: User `Dewi Anggraini {runId}` dengan role lain (bukan Group Manager) tanpa Manage accounting, scope seluruh client.

## Test Steps

### Alamat langsung ditolak
1. Buka halaman Chart of Accounts lewat alamat langsung
2. Verifikasi toast `You don't have permission to do this.` tampil
3. Verifikasi isi tab Chart of Accounts, yaitu tabel Account List, tidak tampil
4. Verifikasi aktor tidak dialihkan ke halaman lain

### Alamat langsung ditolak bagi aktor role lain
5. Masuk sebagai `Dewi Anggraini {runId}`
6. Buka halaman Chart of Accounts lewat alamat langsung
7. Verifikasi toast `You don't have permission to do this.` tampil
8. Verifikasi isi tab Chart of Accounts, yaitu tabel Account List, tidak tampil
9. Verifikasi aktor tidak dialihkan ke halaman lain
