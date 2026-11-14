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
  "§2.1#r4": [3, 6]
  "§2.2#r4": [3, 6]
  "§2.2#r5": [3, 6]
  "§9.4.2#r31": [3, 5, 6]
  "EB-AKS-1": 3
  "EB-AKS-2": [5, 6, 7]
anchor: [2]
coverage:
  web: automated
---

# Aktor tanpa capability tidak melihat menu dan ditolak lewat alamat langsung

## Prerequisites
- Aktor: User `Yoga Pratama {runId}` (Group Manager, tanpa capability Manage accounting).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-046-1: User `Yoga Pratama {runId}` dengan access level Group Manager tanpa Manage accounting, scope seluruh client.

## Test Steps

### Menu tidak tampil di sidebar
1. Buka sidebar
2. Verifikasi sidebar memuat item menu lain yang boleh diakses aktor
3. Verifikasi menu `Chart of Accounts` tidak tampil di sidebar

### Alamat langsung ditolak
4. Buka halaman Chart of Accounts lewat alamat langsung
5. Verifikasi toast `You don't have permission to do this.` tampil
6. Verifikasi tabel Account List tidak tampil
7. Verifikasi aktor tidak dialihkan ke halaman lain
