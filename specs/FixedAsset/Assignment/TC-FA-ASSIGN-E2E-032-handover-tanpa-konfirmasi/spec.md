---
id: TC-FA-ASSIGN-E2E-032-handover-tanpa-konfirmasi
title: "Handover dengan Need recipient confirmation = No (Complete Handover)"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§3#p9", TS-ASG-07, EC-ASG-13, FI-ASG-41]
smoke: []
dependsOn: []
trace:
  "§3#p9": [4, 5, 11]
  TS-ASG-07: 7
  EC-ASG-13: [3, 11, 12]
  FI-ASG-41: [7, 11]
anchor: []
coverage:
  web: automated
---

# Handover dengan Need recipient confirmation = No (Complete Handover)

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-032-1: User `Budi Santoso {runId}`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-032-2: Aset `Meja Kerja Staf {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`).
  - DU-032-3: Aset `Kursi Ergonomis {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`).
  - DU-032-4: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Head Office`, memuat DU-032-2 dan DU-032-3, keduanya berstatus `Waiting for Handover` dengan Approval `Not required` dan Purpose `Pemakaian harian staf {runId}`.
- Kondisi:
  - Need recipient confirmation efektif bernilai `No` untuk DU-032-2 dan DU-032-3.
  - Photo at start bernilai `OFF`.

## Test Steps

### Hand Over pada ASG dengan Confirmation No
1. Ketik Search `{runId}`, tekan Enter
2. Klik `Hand Over` pada menu ⋯ baris ASG DU-032-4
3. Verifikasi kolom Confirmation kedua aset menampilkan `No`
4. Verifikasi tombol `[Complete Handover]` tampil
5. Verifikasi tombol `[Request Confirmation]` tidak tampil
6. Klik `[Complete Handover]`
7. Verifikasi toast `Success, 2 assets have been assigned to Budi S.` tampil

### ASG tercatat Assigned dengan Confirmation Not required
8. Buka halaman Transactions > Assignment, tab Transactions
9. Ketik Search `{runId}`, tekan Enter
10. Klik Transaction ID pada baris hasil pencarian
11. Verifikasi kolom Status kedua aset menampilkan `Assigned`
12. Verifikasi kolom Confirmation kedua aset menampilkan `Not required`
