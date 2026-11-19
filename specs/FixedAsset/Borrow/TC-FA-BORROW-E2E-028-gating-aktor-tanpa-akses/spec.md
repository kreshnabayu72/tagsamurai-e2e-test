---
id: TC-FA-BORROW-E2E-028-gating-aktor-tanpa-akses
title: "Aktor tanpa capability Borrow tidak melihat item sidebar dan halaman Borrow tidak membuka isinya"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [EB-AKS-1, EB-AKS-2]
smoke: []
dependsOn: []
trace:
  EB-AKS-1: 2
  EB-AKS-2: [4, 5, 6]
anchor: [1]
coverage:
  web: automated
---

# Aktor tanpa capability Borrow tidak melihat item sidebar dan halaman Borrow tidak membuka isinya

## Prerequisites
- Aktor: pengguna tanpa capability Borrow (bukan Total Control, Group Manager, Asset Admin, Approver, Monitoring & Report, maupun Read Only).
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-028-1: User `Tono Wijaya {runId}`, role tanpa capability Borrow, aktif, ada di entitas aktor.

## Test Steps

### Item sidebar Borrow tidak tampil
1. Verifikasi sidebar memuat item menu lain yang dapat diakses aktor
2. Verifikasi item `Borrow` di bawah `Transactions` tidak tampil di sidebar

### URL langsung ke halaman Borrow tidak membuka isinya
3. Buka URL halaman `Transactions > Borrow` secara langsung
4. Verifikasi toast `You don't have permission to do this.` tampil
5. Verifikasi aktor tidak dialihkan ke halaman lain
6. Verifikasi tabel BRW dan tombol `[+ Borrow]` tidak tampil
