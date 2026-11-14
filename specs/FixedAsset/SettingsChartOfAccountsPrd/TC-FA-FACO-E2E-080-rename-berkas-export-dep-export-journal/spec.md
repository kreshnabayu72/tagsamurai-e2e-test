---
id: TC-FA-FACO-E2E-080-rename-berkas-export-dep-export-journal
title: "Perubahan Account Name berlaku untuk export berikutnya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FACO-LOGIC-04d, "§9.7#r19", "§11.2#r1", "EB-XM-2@export-journal"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  FACO-LOGIC-04d: [14, 16]
  "§9.7#r19": [14, 16]
  "§11.2#r1": [2, 14, 16]
  "EB-XM-2@export-journal": [14, 15]
coverage:
  web: automated
---

# Perubahan Account Name berlaku untuk export berikutnya

## Prerequisites
- Aktor: Admin dengan role Total Control, yang juga menjalankan Export Journal.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan.
  - DU-080-1: Account Code `RNX1-{runId}`, Account Name `Plant Machinery Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - DU-080-2: akun baru yang dibuat Admin: Account Code `RNX2-{runId}`, Account Name `Conveyor Cost {runId}`, Account Function `Capitalization Offset`.
  - DU-080-3: Account Name baru untuk DU-080-1: `Plant Machinery Cost Revised {runId}`.
- Kondisi:
  - Akun DU-080-1 dan akun DU-080-2 ikut dalam berkas Export Journal yang dijalankan sesudah akun itu ada.
  - Export Journal pertama memakai periode jurnal `M0 − 2 bulan` dan yang kedua `M0 − 1 bulan`.

## Test Steps

### Export berikutnya memuat akun baru dan Account Name yang diubah, berkas lama tidak berubah
1. Export Journal untuk periode `M0 − 2 bulan` selesai dan menghasilkan berkas pertama yang memuat akun `RNX1-{runId}`
2. Verifikasi berkas pertama memuat akun dengan Account Code `RNX1-{runId}` dan Account Name `Plant Machinery Cost {runId}`
3. Klik `[+ Account]`
4. Isi Account Code `RNX2-{runId}`
5. Isi Account Name `Conveyor Cost {runId}`
6. Pilih Account Function `Capitalization Offset`
7. Klik `[Submit]`
8. Ketik Search `RNX1-{runId}`, tekan Enter
9. Klik `⋯` pada baris `RNX1-{runId}`
10. Klik `Edit`
11. Ganti isi Account Name dengan `Plant Machinery Cost Revised {runId}`
12. Klik `[Save]`
13. Export Journal untuk periode `M0 − 1 bulan` selesai dan menghasilkan berkas kedua yang memuat akun `RNX1-{runId}` dan akun `RNX2-{runId}`
14. Verifikasi berkas kedua memuat akun dengan Account Code `RNX1-{runId}` dan Account Name `Plant Machinery Cost Revised {runId}`
15. Verifikasi berkas kedua memuat akun dengan Account Code `RNX2-{runId}` dan Account Name `Conveyor Cost {runId}`
16. Verifikasi berkas pertama masih memuat akun dengan Account Code `RNX1-{runId}` dan Account Name `Plant Machinery Cost {runId}`
