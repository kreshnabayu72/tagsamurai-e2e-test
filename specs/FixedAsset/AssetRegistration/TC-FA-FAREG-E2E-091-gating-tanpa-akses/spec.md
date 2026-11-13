---
id: TC-FA-FAREG-E2E-091-gating-tanpa-akses
title: "Aktor tanpa akses: titik masuk Registration dan Approvals"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["EB-AKS-1", "EB-AKS-2"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-1": [2, 3]
  "EB-AKS-2": [5, 6, 8, 9]
anchor: [1]
coverage:
  web: automated
---

# Aktor tanpa akses: titik masuk Registration dan Approvals

## Prerequisites
- Aktor: Dian P (pengguna aktif tanpa capability Read pada Assets dan Approvals, hanya memegang capability Read pada Damaged).
- Layar awal: Fixed Asset > Damaged.
- Data:
  - DU-091-1: Dian P (capability Read pada Damaged saja, tanpa capability pada Assets dan Approvals, seluruh client).

## Test Steps

### Item sidebar modul tidak tampil bagi aktor tanpa capability read
1. Verifikasi item sidebar `Damaged` tampil bagi Dian P
2. Verifikasi item sidebar `Assets` tidak tampil bagi Dian P
3. Verifikasi item sidebar `Approvals` tidak tampil bagi Dian P

### Halaman Registration lewat alamat langsung ditolak
4. Buka halaman `Registration` pada Fixed Asset > Assets lewat alamat langsung (URL)
5. Verifikasi toast `You don't have permission to do this.` tampil tanpa pengalihan halaman untuk halaman `Registration`
6. Verifikasi isi halaman `Registration` tidak tampil

### Halaman Approvals > Registration lewat alamat langsung ditolak
7. Buka halaman `Approvals` > `Registration` lewat alamat langsung (URL)
8. Verifikasi toast `You don't have permission to do this.` tampil tanpa pengalihan halaman untuk halaman `Approvals` > `Registration`
9. Verifikasi isi halaman `Approvals` > `Registration` tidak tampil
