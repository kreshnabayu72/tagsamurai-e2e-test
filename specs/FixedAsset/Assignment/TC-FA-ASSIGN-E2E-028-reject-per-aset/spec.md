---
id: TC-FA-ASSIGN-E2E-028-reject-per-aset
title: "Reject per aset dengan Approval Note"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.4#r9", "F-ASSIGN-05.k1"]
smoke: []
dependsOn: []
trace:
  "§4.4#r9": [5, 6, 14, 26]
  "F-ASSIGN-05.k1": [17, 21]
anchor: []
coverage:
  web: automated
---

# Reject per aset dengan Approval Note

## Prerequisites
- Aktor: Total Control `Dewi Anggraini {runId}` (DU-028-1), approver kedua aset di DU-028-3.
- Layar awal: Approvals > Assignment > Active.
- Data:
  - DU-028-1: User `Dewi Anggraini {runId}`, Role `Total Control`, approver tunggal kedua aset di DU-028-3. Daftar Active-nya hanya berisi DU-028-3.
  - DU-028-2: User `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office`, pengaju DU-028-3.
  - DU-028-3: Pengajuan, Group `Head Office`, Assignee `Sari Dewi {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 2 hari, pukul 09:00`, Approval type `Any one approver`; aset `Excavator PC200 {runId}` (Purpose `Site work`) dan `Toyota Avanza {runId}` (Purpose `Field visits`), approver `Dewi Anggraini {runId}`, belum diputuskan.
  - DU-028-4: Approval Note `Site work postponed`, diisi pada `Excavator PC200 {runId}`.

## Test Steps

### Reject tanpa Approval Note diblokir
1. Ketik Search `Sari Dewi {runId}`, tekan Enter
2. Klik `Transaction ID` pada baris `Sari Dewi {runId}`
3. Ubah toggle `Approval` pada baris `Excavator PC200 {runId}` menjadi `Reject`
4. Klik `[Submit]` pada halaman Review
5. Verifikasi pesan `Approval note must not be empty` tampil pada field `Approval Note` baris `Excavator PC200 {runId}`
6. Verifikasi halaman Review tetap terbuka dan dialog `Submit Approval` tidak tampil

### Reject dengan Approval Note menolak aset itu dan keputusannya tercatat di Assignment Log
7. Isi `Approval Note` pada baris `Excavator PC200 {runId}` dengan `Site work postponed`
8. Klik `[Submit]` pada halaman Review
9. Klik `[Submit]` pada dialog `Submit Approval`
10. Buka halaman `Transactions > Assignment`
11. Ketik Search `Sari Dewi {runId}`, tekan Enter
12. Klik `⋯` pada baris `Sari Dewi {runId}`
13. Klik `Detail`
14. Verifikasi `Status` pada baris `Excavator PC200 {runId}` bernilai `Rejected`
15. Klik `⋯` pada baris `Excavator PC200 {runId}`
16. Klik `Assignment Log`
17. Verifikasi dialog `Assignment Log` memuat node `Rejected by [Approver]` dengan Approver `Dewi Anggraini {runId}` dan Reason `Site work postponed`
18. Klik ikon silang pada dialog `Assignment Log`
19. Klik `⋯` pada baris `Toyota Avanza {runId}`
20. Klik `Assignment Log`
21. Verifikasi dialog `Assignment Log` memuat node `Approved by [Approver]` dengan Approver `Dewi Anggraini {runId}`

### Aset yang ditolak tidak membuat Draft baru
22. Klik ikon silang pada dialog `Assignment Log`
23. Buka halaman `Transactions > Assignment`
24. Klik tab `Drafts`
25. Ketik Search `Excavator PC200 {runId}`, tekan Enter
26. Verifikasi empty state `No results found` tampil karena tidak ada Draft yang memuat aset `Excavator PC200 {runId}` sesudah aset itu ditolak
