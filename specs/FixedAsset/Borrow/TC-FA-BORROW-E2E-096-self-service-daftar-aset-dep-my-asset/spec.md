---
id: TC-FA-BORROW-E2E-096-self-service-daftar-aset-dep-my-asset
title: "Daftar aset self-service di mobile hanya memuat aset Non TAG yang terjangkau Borrower dan menolak TAG aset yang tidak tampil"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1d#b3", "§4.1d#b4", "§4.1d#b7"]
smoke: []
dependsOn: ["My Asset: Borrow an Asset"]
trace:
  "§4.1d#b3": 9
  "§4.1d#b4": [4, 5, 6, 7, 8]
  "§4.1d#b7": [12, 17]
anchor: []
coverage:
  android: manual
---

# Daftar aset self-service di mobile hanya memuat aset Non TAG yang terjangkau Borrower dan menolak TAG aset yang tidak tampil

## Prerequisites
- Aktor: Borrower, karyawan ber-akun login yang Group-nya `Head Office`.
- Layar awal: My Asset > Borrowed.
- Data:
  - DU-096-1: aset `Kursi A {runId}`, Category TAG `Non TAG`, Group asal `Head Office`, Self service efektif ON, Allow Borrow efektif Allow, Allowed borrower `Same Group only`, Max Duration `3 days`.
  - DU-096-2: aset `Monitor D {runId}`, Category TAG `Non TAG`, Group asal `Branch Surabaya`, Self service efektif ON, Allow Borrow efektif Allow, Allowed borrower `Employee in any Group`, Max Duration `7 days`.
  - DU-096-3: aset `Kursi B {runId}`, Category TAG `Non TAG`, Group asal `Branch Surabaya`, Self service efektif ON, Allow Borrow efektif Allow, Allowed borrower `Same Group only`, Max Duration `3 days`.
  - DU-096-4: aset `Proyektor E {runId}`, Category TAG `Non TAG`, Group asal `Head Office`, Self service efektif ON, Allow Borrow efektif Deny (override pada aset), Allowed borrower `Employee in any Group`, Max Duration `3 days`.
  - DU-096-5: aset `Printer F {runId}`, Category TAG `Non TAG`, Group asal `Head Office`, Self service efektif OFF, Allow Borrow efektif Allow, Allowed borrower `Employee in any Group`, Max Duration `3 days`.
  - DU-096-6: aset `Laptop G {runId}`, Category TAG `RFID`, Group asal `Head Office`, Self service efektif ON, Allow Borrow efektif Allow, Allowed borrower `Employee in any Group`, Max Duration `3 days`; TAG-nya terpasang pada aset.
  - DU-096-7: aset `Laptop H {runId}`, Category TAG `QR`, Group asal `Branch Surabaya`, Self service efektif ON, Allow Borrow efektif Allow, Allowed borrower `Same Group only`, Max Duration `3 days`; TAG-nya terpasang pada aset.
  - Semua aset DU-096-1 sampai DU-096-7 berstatus Custody `Available` dan Condition `Normal`, tanpa transaksi berjalan.

## Test Steps

### Aset Non TAG yang terjangkau Borrower tampil di daftar
1. Klik `[Borrow an Asset]`
2. Klik `[+ Add Assets]`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi aset `Kursi A {runId}` tampil di daftar karena Group asalnya sama dengan Group Borrower
5. Verifikasi aset `Monitor D {runId}` tampil di daftar walau Group asalnya `Branch Surabaya`, karena aturan Allowed borrower-nya `Employee in any Group`

### Aset di luar jangkauan Borrower tidak tampil sama sekali
6. Verifikasi aset `Kursi B {runId}` tidak tampil di daftar karena aturan Allowed borrower-nya `Same Group only` tidak dipenuhi
7. Verifikasi aset `Proyektor E {runId}` tidak tampil di daftar karena Allow Borrow efektifnya Deny
8. Verifikasi aset `Printer F {runId}` tidak tampil di daftar karena Self service efektifnya OFF

### Aset ber-tag tidak tampil di daftar
9. Verifikasi aset `Laptop G {runId}` tidak tampil di daftar karena Category TAG-nya bukan `Non TAG`

### TAG aset ber-tag yang tidak tampil ditolak lewat Search by Scan
10. Klik `Search by Scan`
11. Pindai TAG milik `Laptop G {runId}`
12. Verifikasi toast `Error, this asset can't be borrowed on your own.` tampil

### TAG aset di luar jangkauan Borrower ditolak lewat Search by Scan
13. Klik `[Cancel]` pada dialog Select Asset
14. Klik `[+ Add Assets]`
15. Klik `Search by Scan`
16. Pindai TAG milik `Laptop H {runId}`
17. Verifikasi toast `Error, this asset can't be borrowed on your own.` tampil
