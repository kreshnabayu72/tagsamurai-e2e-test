---
id: TC-FA-FATR-E2E-054-efek-notification-dep-notification
title: "Notifikasi akibat setting transaksi"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r4", "§9.2#r11", "§9.2#b229", "§9.2#b388", "§9.2#b484", "§9.7#r12", "§11#r13"]
smoke: ["§9.2#b229", "§9.2#b388", "§9.2#b484", "§9.7#r12", "§11#r13"]
dependsOn:
  - "Notification: notifikasi in-app dan email"
trace:
  "§Aturan Logika Modul#r4": 17
  "§9.2#r11": [9, 10]
  "§9.2#b229": 25
  "§9.2#b388": 22
  "§9.2#b484": 10
  "§9.7#r12": 9
  "§11#r13": [9, 22, 25]
anchor: []
coverage:
  web: automated
---

# Notifikasi akibat setting transaksi

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update) di entitas khusus; `Wulan Kusuma {runId}` sebagai Borrower dan pengaju.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-054-1: Entitas Name `Entitas Notifikasi {runId}`, Require approval Assign `OFF`; entitas khusus spec ini, tanpa Role Transaksi Approver untuk Assign dan dengan Require approval Assign bernilai OFF.
  - DU-054-2: Group Name `Logistics Team {runId}`; Group tanpa Division.
  - DU-054-3: User Name `Wulan Kusuma {runId}`, Role `Employee`, Group `Logistics Team {runId}`; akun aktif Borrower dan pengaju.
  - DU-054-4: Asset Name `Welding Machine WM30 {runId}`, Group `Logistics Team {runId}`, Status `Borrowed`; aset dengan pinjaman Borrowed yang Due date-nya kemarin.
  - DU-054-5: Asset Name `Air Compressor AC10 {runId}`, Group `Logistics Team {runId}`, Status `Waiting for Approval`; aset dengan pengajuan yang tersisa 1 hari sebelum batas Transaction timeout.
  - DU-054-6: Borrow Asset `Welding Machine WM30 {runId}`, Borrower `Wulan Kusuma {runId}`, Status `Borrowed`, Due date `T0 − 1 hari`; pinjaman Borrowed yang Overdue mulai H+1.
  - DU-054-7: Borrow Asset `Air Compressor AC10 {runId}`, Borrower `Wulan Kusuma {runId}`, Status `Waiting for Approval`, Sisa batas `1 hari`; pengajuan yang tersisa 1 hari sebelum batas Transaction timeout.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Notifikasi {runId}` yang tidak dipakai spec lain, karena yang diubah adalah setting tingkat entitas.
  - Role Transaksi `Approver` untuk transaksi `Assign` belum ditugaskan ke user mana pun di Group mana pun di entitas khusus ini, dan Require approval pada `Assign` bernilai `OFF`.
  - Akun `Wulan Kusuma {runId}` aktif dan kredensialnya tersedia untuk login.

## Test Steps

### Save konfigurasi Approval tanpa Approver memicu notifikasi approver_required
1. Masuk sebagai Default User
2. Buka daftar Notification
3. Catat jumlah notifikasi `approver_required`
4. Buka tab `Assign` pada node All categories di Fixed Asset > Settings > Transaction Settings
5. Pilih nilai `ON` pada field Require approval
6. Klik `[Save]`
7. Klik `[Save]` pada dialog Save Changes
8. Buka daftar Notification
9. Verifikasi jumlah notifikasi `approver_required` bertambah satu dari jumlah yang dicatat
10. Verifikasi notifikasi `approver_required` terbaru memuat Title, Body, dan Click-path

### Perubahan Settings tanpa approval tidak memicu notifikasi
11. Catat jumlah notifikasi pada daftar Notification
12. Buka tab `Borrow` pada node All categories di Fixed Asset > Settings > Transaction Settings
13. Isi Max duration dengan `10`
14. Klik `[Save]`
15. Klik `[Save]` pada dialog Save Changes
16. Buka daftar Notification
17. Verifikasi jumlah notifikasi sama dengan jumlah yang dicatat sebelum Save

### Pinjaman yang Overdue memicu satu notifikasi borrow_overdue
18. Masuk sebagai `Wulan Kusuma {runId}`
19. Catat jumlah notifikasi `borrow_overdue` pada daftar Notification
20. Job Overdue Borrow berjalan
21. Buka daftar Notification
22. Verifikasi satu notifikasi `borrow_overdue` baru diterima untuk pinjaman aset `Welding Machine WM30 {runId}`

### Pengajuan yang hampir melewati batas memicu notifikasi peringatan
23. Job peringatan Transaction timeout berjalan
24. Buka daftar Notification
25. Verifikasi notifikasi `*_almost_timeout` diterima untuk pengajuan aset `Air Compressor AC10 {runId}`
