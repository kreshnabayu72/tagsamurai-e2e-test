---
id: TC-FA-ASSIGN-E2E-029-approve-all-approvers
title: "Approve per aset dengan Approval type All approvers"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.4#r8", "FI-ASG-119", "FI-ASG-120", "FI-ASG-121", "FI-ASG-122"]
smoke: []
dependsOn: []
trace:
  "§4.4#r8": [3, 4, 14, 15]
  "FI-ASG-119": [14, 15, 16]
  "FI-ASG-120": 5
  "FI-ASG-121": 17
  "FI-ASG-122": 20
anchor: []
coverage:
  web: automated
---

# Approve per aset dengan Approval type All approvers

## Prerequisites
- Aktor: Approver `Rina Wulandari {runId}` (DU-029-1).
- Layar awal: Approvals > Assignment > Active.
- Data:
  - DU-029-1: User `Rina Wulandari {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`. Daftar Active-nya hanya berisi DU-029-4.
  - DU-029-2: User `Tono Wibowo {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`, approver kedua hanya pada `Genset Cummins C100 {runId}` di DU-029-4 dan sudah menyetujuinya.
  - DU-029-3: User `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office`, pengaju DU-029-4.
  - DU-029-4: Pengajuan, Group `Head Office`, Assignee `Sari Dewi {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 2 hari, pukul 09:00`, Approval type `All approvers`; aset `Excavator PC200 {runId}` (Purpose `Site work`) dan `Forklift Toyota 8FD {runId}` (Purpose `Site work`) dengan approver `Rina Wulandari {runId}` dan `Wawan Hartono {runId}`, belum diputuskan siapa pun; aset `Genset Cummins C100 {runId}` (Purpose `Field visits`) dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`, sudah disetujui `Tono Wibowo {runId}`.
  - DU-029-5: Approval Note `Site work postponed`, diisi pada `Forklift Toyota 8FD {runId}`.
  - DU-029-6: User `Wawan Hartono {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`, approver kedua pada `Excavator PC200 {runId}` dan `Forklift Toyota 8FD {runId}` di DU-029-4; belum memutuskan apa pun.

## Test Steps

### Approval Rule menampilkan progres persetujuan per aset All approvers
1. Ketik Search `Sari Dewi {runId}`, tekan Enter
2. Klik `Transaction ID` pada baris `Sari Dewi {runId}`
3. Verifikasi `Approval Rule` pada baris `Excavator PC200 {runId}` bernilai `All approvers · 0 of 2 approved`
4. Verifikasi `Approval Rule` pada baris `Genset Cummins C100 {runId}` bernilai `All approvers · 1 of 2 approved`
5. Verifikasi tidak ada kontrol untuk mengganti aset pada baris `Excavator PC200 {runId}`

### Satu Submit menyetujui, melengkapi persetujuan, dan menolak aset; hasil tercatat per aset dan pengajuan berakhir campuran
6. Ubah toggle `Approval` pada baris `Forklift Toyota 8FD {runId}` menjadi `Reject`
7. Isi `Approval Note` pada baris `Forklift Toyota 8FD {runId}` dengan `Site work postponed`
8. Klik `[Submit]` pada halaman Review
9. Klik `[Submit]` pada dialog `Submit Approval`
10. Klik tab `History`
11. Ganti isi kotak search dengan `Sari Dewi {runId}`, tekan Enter
12. Klik `⋯` pada baris `Sari Dewi {runId}`
13. Klik `Detail`
14. Verifikasi `Approval Rule` pada baris `Excavator PC200 {runId}` bernilai `All approvers · 1 of 2 approved` karena persetujuan kedua approver belum lengkap
15. Verifikasi `Approval Rule` pada baris `Genset Cummins C100 {runId}` bernilai `Approved` karena semua approver aset itu menyetujui
16. Verifikasi `Approval Rule` pada baris `Forklift Toyota 8FD {runId}` bernilai `Rejected` karena satu penolakan menolak aset itu
17. Verifikasi pengajuan memuat aset `Genset Cummins C100 {runId}` yang `Approved` dan aset `Forklift Toyota 8FD {runId}` yang `Rejected` sekaligus
18. Klik `History` pada breadcrumb
19. Arahkan kursor ke badge `Status` pada baris `Sari Dewi {runId}`
20. Verifikasi hover pada badge `Status` baris `Sari Dewi {runId}` berisi `2 approved · 1 rejected`, jumlah aset yang diputuskan `Rina Wulandari {runId}`
