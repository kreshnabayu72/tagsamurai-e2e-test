---
id: TC-FA-FATR-E2E-057-efek-accounting-dep-accounting
title: "Setting Transfer dan Disposal berlaku di Accounting"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.4.2#r138"]
smoke: []
dependsOn:
  - "Accounting: Post dan review Cost Center"
trace:
  "§9.4.2#r138": 6
anchor: [3]
coverage:
  web: automated
---

# Setting Transfer dan Disposal berlaku di Accounting

## Prerequisites
- Aktor: `Rina Hartono {runId}` sebagai pengguna Accounting yang dapat melakukan Post.
- Layar awal: Accounting > Post dan review Cost Center
- Data:
  - DU-057-1: Group Name `Finance Team {runId}`; Group tanpa Division.
  - DU-057-2: User Name `Rina Hartono {runId}`, Role `Employee`, Group `Finance Team {runId}`; akun aktif Accounting yang melakukan Post.
  - DU-057-3: Asset Name `Office Printer OP70 {runId}`, Group `Finance Team {runId}`, Status `Disposed`; aset yang Disposal-nya berstatus Executed dan menunggu Post.
  - DU-057-4: Disposal Asset `Office Printer OP70 {runId}`, Require approval `OFF`, Status `Executed`; Disposal dengan nilai efektif Require approval OFF yang berstatus Executed dan muncul di tab Waiting to Post.
- Kondisi:
  - Accounting & Depreciation (FA-7) aktif pada plan entitas, sehingga tahap Post dan tab `Waiting to Post` tersedia.
  - Disposal aset `Office Printer OP70 {runId}` berstatus `Executed` dengan nilai efektif Require approval `OFF`, dan akun `Rina Hartono {runId}` aktif.

## Test Steps

### Accounting tetap melakukan Post pada Disposal dengan Require approval OFF
1. Masuk sebagai `Rina Hartono {runId}`
2. Buka tab `Waiting to Post` pada halaman Post dan review Cost Center
3. Verifikasi baris untuk aset `Office Printer OP70 {runId}` tampil di tab `Waiting to Post`
4. Klik `[Post]` pada baris aset `Office Printer OP70 {runId}`
5. Klik `[Post]` pada dialog konfirmasi
6. Verifikasi baris untuk aset `Office Printer OP70 {runId}` tidak lagi tampil di tab `Waiting to Post`
