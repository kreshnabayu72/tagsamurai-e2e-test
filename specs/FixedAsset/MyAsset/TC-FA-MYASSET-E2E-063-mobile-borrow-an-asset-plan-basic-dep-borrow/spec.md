---
id: TC-FA-MYASSET-E2E-063-mobile-borrow-an-asset-plan-basic-dep-borrow
title: "Mobile plan Basic: tombol Borrow an Asset tidak tampil"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.4.2#r82", "§9.10#p1"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§9.4.2#r82": 4
  "§9.10#p1": 4
anchor: [3]
coverage:
  android: automated
---
# Mobile plan Basic: tombol Borrow an Asset tidak tampil

## Prerequisites
- Aktor: Borrower, karyawan aktif ber-akun login di entitas khusus.
- Layar awal: halaman `My Asset` tab Task di aplikasi Android.
- Data:
  - DU-063-1: entitas khusus `Basic Borrowing {runId}` dengan plan `Basic`, yang tidak dipakai spec lain.
  - DU-063-2: aset self-service `Laptop Dell Latitude 5420 {runId}` di entitas DU-063-1, Status `Available`, Self service efektif ON, Allowed borrower mencakup aktor.
  - DU-063-3: pinjaman Admin milik aktor di entitas DU-063-1 berstatus `Borrowed` dengan aset `Projector Epson EB-X06 {runId}`, Duration `3 days`.

## Test Steps

### Tombol Borrow an Asset tidak tampil pada plan Basic
1. Klik tab `Borrowed`
2. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
3. Verifikasi kartu aset milik DU-063-3 tampil di tab Borrowed
4. Verifikasi tombol `Borrow an Asset` tidak tampil (Hidden) di tab Borrowed
