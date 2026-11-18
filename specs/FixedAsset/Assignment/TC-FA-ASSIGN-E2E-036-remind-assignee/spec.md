---
id: TC-FA-ASSIGN-E2E-036-remind-assignee
title: "Remind Assignee pada baris Waiting for Handover"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [TS-ASG-30]
smoke: []
dependsOn: []
trace:
  TS-ASG-30: [3, 6, 9]
anchor: []
coverage:
  web: automated
---

# Remind Assignee pada baris Waiting for Handover

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-036-1: User `Budi Santoso {runId}`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-036-2: Aset `Laptop Lenovo ThinkPad {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`).
  - DU-036-3: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Head Office`, memuat DU-036-2 berstatus `Waiting for Handover` dengan Approval `Not required` dan Purpose `Pengganti laptop lama {runId}`.
  - DU-036-4: Division `Finance {runId}`.
  - DU-036-5: User `Nadia Putri {runId}`, anggota aktif Division `Finance {runId}` dengan akun login, menjadi PIC pada ASG di bawah.
  - DU-036-6: Aset `Printer Epson L3250 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`).
  - DU-036-7: ASG dengan Assignee Division `Finance {runId}`, PIC `Nadia Putri {runId}` aktif, Group `Head Office`, memuat DU-036-6 berstatus `Waiting for Handover` dengan Approval `Not required` dan Purpose `Perlengkapan cetak divisi keuangan {runId}`.
- Kondisi:
  - Feature Suite Assignment pada level `Full`.

## Test Steps

### Remind Assignee mengirim pengingat
1. Ketik Search `{runId}`, tekan Enter
2. Klik `Remind Assignee` pada menu ⋯ baris ASG DU-036-3
3. Verifikasi toast `Success, reminder has been sent to Budi S.` tampil

### Remind Assignee pada ASG Division mengirim pengingat ke PIC
4. Ganti isi kotak search dengan `{runId}`, tekan Enter
5. Klik `Remind Assignee` pada menu ⋯ baris ASG DU-036-7
6. Verifikasi toast berawalan `Success, reminder has been sent to` tampil

### Remind Assignee tidak memperbarui Last Updated
7. Catat nilai kolom Last Updated baris ASG DU-036-3
8. Klik `Remind Assignee` pada menu ⋯ baris ASG DU-036-3
9. Verifikasi nilai kolom Last Updated baris ASG DU-036-3 sama dengan nilai yang dicatat
