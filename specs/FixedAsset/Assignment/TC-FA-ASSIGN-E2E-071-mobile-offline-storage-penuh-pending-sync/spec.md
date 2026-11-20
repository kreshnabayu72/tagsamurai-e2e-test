---
id: TC-FA-ASSIGN-E2E-071-mobile-offline-storage-penuh-pending-sync
title: "Mobile offline: langkah Handover dan Unassign ditolak Storage penuh saat sinkron tetap Pending sync"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceRules: ["ASSIGN-LOGIC-21g", "ASSIGN-LOGIC-21h", "ASSIGN-LOGIC-21l", "TS-ASG-36", "EC-ASG-125"]
smoke: []
dependsOn: []
trace:
  "ASSIGN-LOGIC-21g": [7, 19]
  "ASSIGN-LOGIC-21h": [10, 11]
  "ASSIGN-LOGIC-21l": [5, 6, 7, 17, 18, 19]
  "TS-ASG-36": [5, 17]
  "EC-ASG-125": [5, 6, 7, 17, 18, 19]
anchor: [3, 15]
coverage:
  android: manual
---

# Mobile offline: langkah Handover dan Unassign ditolak Storage penuh saat sinkron tetap Pending sync

## Prerequisites
- Aktor: Asset Admin `Adi Pratama {runId}` (DU-071-1) pada aplikasi native Android, di entitas khusus yang Storage-nya penuh dan tidak dipakai spec lain.
- Layar awal: Menu Scan pada aplikasi Android.
- Data:
  - DU-071-1: User (Aktor Asset Admin), Name `Adi Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-071-2: User (Assignee Employee), Name `Budi Santoso {runId}`, Tampil sebagai `Budi S`.
  - DU-071-3: Assignment (ASG Waiting for Handover), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}` ber-TAG `QR`, Need recipient confirmation `No`, Photo at start `ON`, Approval `Not required`.
  - DU-071-4: Assignment (ASG Assigned), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Camera Sony A7 {runId}` ber-TAG `QR`, Photo at end `ON`, Approval `Not required`.
- Kondisi:
  - Aplikasi native Android terpasang di perangkat dan akun `Adi Pratama {runId}` aktif.
  - Storage client penuh: Total Used `50.0 GB` dan Storage Quota `50.0 GB`.

## Test Steps

### Handover berfoto yang diambil offline ditolak saat sinkron
1. Perangkat berada dalam keadaan offline
2. Scan TAG aset `Printer HP M404 {runId}` pada halaman Handover dan ambil foto Handover
3. Verifikasi hasil scan dan foto tersimpan lokal dengan status `Pending sync`
4. Perangkat kembali online dan sinkronisasi berjalan
5. Verifikasi aktor diberi tahu lewat toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` pada pemberitahuan sinkron
6. Verifikasi langkah Handover aset `Printer HP M404 {runId}` tetap di perangkat dengan status `Pending sync` dan alasan `Storage is full`
7. Verifikasi aset `Printer HP M404 {runId}` berstatus `Waiting for Handover` pada daftar penugasan di aplikasi Android

### Kirim ulang langkah Handover setelah kuota ditambah
8. Kuota Storage client ditambah sehingga pemakaian berada di bawah kuota
9. Kirim ulang langkah Handover aset `Printer HP M404 {runId}` yang tertunda dari perangkat
10. Verifikasi aset `Printer HP M404 {runId}` berstatus `Assigned` pada daftar penugasan di aplikasi Android
11. Verifikasi langkah Handover aset `Printer HP M404 {runId}` tidak lagi berstatus `Pending sync`

### Unassign berfoto yang diambil offline ditolak saat sinkron
12. Pemakaian Storage client kembali sama dengan kuota karena unggahan file lain
13. Perangkat berada dalam keadaan offline
14. Scan TAG aset `Camera Sony A7 {runId}` pada halaman Unassign dan ambil foto Unassign
15. Verifikasi hasil scan dan foto Unassign tersimpan lokal dengan status `Pending sync`
16. Perangkat kembali online dan sinkronisasi berjalan
17. Verifikasi aktor diberi tahu lewat toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` pada pemberitahuan sinkron
18. Verifikasi langkah Unassign aset `Camera Sony A7 {runId}` tetap di perangkat dengan status `Pending sync` dan alasan `Storage is full`
19. Verifikasi aset `Camera Sony A7 {runId}` berstatus `Assigned` pada daftar penugasan di aplikasi Android
