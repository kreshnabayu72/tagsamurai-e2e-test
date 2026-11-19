---
id: TC-FA-ASSIGN-E2E-037-change-pic
title: "Change PIC pada ASG Division yang berjalan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [TS-ASG-12, ASSIGN-LOGIC-06k, ASSIGN-LOGIC-06u]
smoke: []
dependsOn: []
trace:
  TS-ASG-12: 5
  ASSIGN-LOGIC-06k: [5, 7]
  ASSIGN-LOGIC-06u: [9, 12]
anchor: []
coverage:
  web: automated
---

# Change PIC pada ASG Division yang berjalan

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-037-1: Division `Finance`.
  - DU-037-2: User `Nadia Pratama`, anggota aktif Division `Finance` dengan akun login, PIC saat ini pada ASG di bawah.
  - DU-037-3: User `Nadia Putri`, anggota aktif Division `Finance` dengan akun login, belum menjadi PIC ASG di bawah.
  - DU-037-4: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Waiting for Handover`.
  - DU-037-5: Aset `Monitor LG 24 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-037-6: ASG dengan Assignee Division `Finance`, PIC `Nadia Pratama`, Group `Head Office`, memuat DU-037-4 dan DU-037-5 dengan Approval `Not required` dan Purpose `Perangkat tim keuangan {runId}`.
- Kondisi:
  - Feature Suite Assignment pada level `Full`.

## Test Steps

### Change PIC dari tab Transactions
1. Ketik Search `{runId}`, tekan Enter
2. Klik `Change PIC` pada menu ⋯ baris ASG DU-037-6
3. Pilih baris `Nadia Putri` pada dialog `Select User`
4. Klik `[Select]`
5. Verifikasi toast `Success, PIC has been changed to Nadia Putri.` tampil

### PIC baru berlaku untuk semua baris aktif ASG
6. Klik Transaction ID pada baris hasil pencarian
7. Verifikasi PIC pada header menampilkan `Nadia Putri`
8. Klik `Assignment Log` pada menu ⋯ baris DU-037-4
9. Verifikasi node `PIC changed by [Actor]` memuat PIC lama `Nadia Pratama` dan PIC baru `Nadia Putri`
10. Tutup dialog Assignment Log
11. Klik `Assignment Log` pada menu ⋯ baris DU-037-5
12. Verifikasi node `PIC changed by [Actor]` memuat PIC lama `Nadia Pratama` dan PIC baru `Nadia Putri`
