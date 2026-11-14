---
id: TC-FA-FATR-E2E-046-efek-my-asset-dep-my-asset
title: "Setting transaksi berlaku di My Asset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§11#r15", "EB-XM-2@my-asset"]
smoke: []
dependsOn:
  - "My Asset: daftar aset pengguna"
trace:
  "§11#r15": [12, 20]
  "EB-XM-2@my-asset": [12, 20, 28]
anchor: [3]
coverage:
  web: automated
---

# Setting transaksi berlaku di My Asset

## Prerequisites
- Aktor: `Gita Permata {runId}` sebagai pengguna My Asset; Default User yang memegang Manage transaction settings (Update) sebagai pengubah setting.
- Layar awal: Fixed Asset > My Asset
- Data:
  - DU-046-1: Group Name `Office Pool {runId}`; Group tanpa Division.
  - DU-046-2: Category Name `Office Equipment {runId}`, Allow Borrow `Allow`, Allow Assign `Allow`; Category leaf dengan Allow Borrow dan Allow Assign nilai sendiri.
  - DU-046-3: User Name `Gita Permata {runId}`, Role `Employee`, Group `Office Pool {runId}`; akun aktif pemegang aset.
  - DU-046-4: Asset Name `Laptop Lenovo T14 {runId}`, Category `Office Equipment {runId}`, Group `Office Pool {runId}`, Status `Assigned`, Holder `Gita Permata {runId}`; aset yang dipegang Gita dan tampil di My Asset.
- Kondisi:
  - Akun `Gita Permata {runId}` aktif dan kredensialnya tersedia untuk login.

## Test Steps

### Override Allow Borrow Deny tercermin di My Asset
1. Masuk sebagai `Gita Permata {runId}`
2. Buka daftar My Asset
3. Verifikasi aksi `Borrow` pada aset `Laptop Lenovo T14 {runId}` aktif
4. Masuk sebagai Default User
5. Buka tab `Borrow` pada node Category `Office Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
6. Klik `[+ Override]` pada bagian Overrides
7. Isi Scope `Asset` dengan Target `Laptop Lenovo T14 {runId}`
8. Pilih Field `Allow Borrow` dengan Value `Deny`
9. Klik `[Submit]`
10. Masuk sebagai `Gita Permata {runId}`
11. Buka daftar My Asset
12. Verifikasi aksi `Borrow` pada aset `Laptop Lenovo T14 {runId}` disabled dengan alasan dan kontak tersampaikan

### Perubahan nilai Category untuk `Assign` tercermin di My Asset
13. Masuk sebagai Default User
14. Buka tab `Assign` pada node Category `Office Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
15. Pilih nilai `Deny` pada field Allow Assign
16. Klik `[Save]`
17. Klik `[Save]` pada dialog Save Changes
18. Masuk sebagai `Gita Permata {runId}`
19. Buka daftar My Asset
20. Verifikasi aksi `Assign` pada aset `Laptop Lenovo T14 {runId}` disabled sesuai nilai baru Category `Office Equipment {runId}`

### Penghapusan override `Borrow` tercermin di My Asset
21. Masuk sebagai Default User
22. Buka tab `Borrow` pada node Category `Office Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
23. Buka menu ⋯ pada baris override untuk `Laptop Lenovo T14 {runId}`
24. Klik `Delete`
25. Klik `[Delete]` pada dialog Delete Override
26. Masuk sebagai `Gita Permata {runId}`
27. Buka daftar My Asset
28. Verifikasi aksi `Borrow` pada aset `Laptop Lenovo T14 {runId}` aktif lagi
