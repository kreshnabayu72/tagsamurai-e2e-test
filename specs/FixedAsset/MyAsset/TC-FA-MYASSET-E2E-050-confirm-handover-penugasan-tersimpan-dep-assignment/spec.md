---
id: TC-FA-MYASSET-E2E-050-confirm-handover-penugasan-tersimpan-dep-assignment
title: "Confirm Handover penugasan: aset tercentang menjadi Assigned dan Task hilang"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["T-MYA-01", "§1.2#r11", "§1.2#r68", "§1.2#r69", "§1.2#r70", "§1.2#r71", "§1.2#r72", "§2.1#r2", "§3#p7", "§4.2.2b#p1", "§4.2.5#p6", "§4.2.5#p7", "§4.4#r7", "§4.8#r4", "§7.3#r11", "§9.2#b4", "§9.2#r26", "§9.2#r27", "§9.6#r10", "§9.7#r6", "§9.7#r7", "§9.7#r9", "EB-FB-1@confirm-handover-assignment"]
smoke: ["EB-FB-1@confirm-handover-assignment"]
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "T-MYA-01": [6, 8, 10]
  "§1.2#r11": 6
  "§1.2#r68": [4, 6]
  "§1.2#r69": [10, 11, 12]
  "§1.2#r70": 12
  "§1.2#r71": [23, 26]
  "§1.2#r72": 19
  "§2.1#r2": [16, 21]
  "§3#p7": [6, 19, 21, 22, 23]
  "§4.2.2b#p1": [10, 17, 19]
  "§4.2.5#p6": [11, 16]
  "§4.2.5#p7": [16, 23]
  "§4.4#r7": [10, 17, 19]
  "§4.8#r4": 8
  "§7.3#r11": 16
  "§9.2#b4": 6
  "§9.2#r26": [21, 22]
  "§9.2#r27": [21, 22]
  "§9.6#r10": [18, 19, 30]
  "§9.7#r6": 6
  "§9.7#r7": 19
  "§9.7#r9": [21, 22]
  "EB-FB-1@confirm-handover-assignment": 16
anchor: [2]
coverage:
  web: automated
---

# Confirm Handover penugasan: aset tercentang menjadi Assigned dan Task hilang

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}` (karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`). Aktor Assignment `Rina Wijaya {runId}` (role `Asset Admin`, cakupan Group `Head Office`) hanya memicu sesi Handover.
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-050-1: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa Task lain dan tanpa penugasan lain.
  - DU-050-2: pengguna `Rina Wijaya {runId}`, role `Asset Admin`, cakupan Group `Head Office`, akun aktif.
  - DU-050-3: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, status `Waiting for Handover`, ada di entitas aktor.
  - DU-050-4: aset `Monitor Dell 24 inch {runId}`, Group `Head Office`, status `Waiting for Handover`, ada di entitas aktor.
  - DU-050-5: aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, status `Waiting for Handover`, ada di entitas aktor.
  - DU-050-6: penugasan dengan Assignee `Budi Santoso {runId}`, memuat DU-050-3, DU-050-4, dan DU-050-5, status `Waiting for Handover`, Need recipient confirmation `Yes`, belum ada sesi Handover berjalan.
- Kondisi:
  - Jendela konfirmasi sesi Handover DU-050-6 belum habis selama spec berjalan.

## Test Steps

### Task Confirm Handover belum ada sebelum sesi Handover dimulai
1. Klik tab `Assigned`
2. Verifikasi aset `Laptop Dell Latitude 5420 {runId}`, `Monitor Dell 24 inch {runId}`, dan `Printer HP LaserJet M404 {runId}` tampil dengan Status `Waiting for Handover`
3. Klik tab `Task`
4. Verifikasi `No tasks` tampil pada tab `Task` sebelum sesi Handover dimulai

### Task muncul saat sesi Handover penugasan dimulai
5. Aktor Assignment `Rina Wijaya {runId}` menekan `[Request Confirmation]` pada Handover penugasan DU-050-6
6. Verifikasi tepat satu baris Task dengan badge `Confirm Handover` tampil pada tab `Task` tanpa Muat ulang halaman

### Dialog Confirm Handover penugasan dibuka dari baris Task
7. Klik `⋯` pada baris Task
8. Verifikasi aksi `Confirm Handover` tampil pada menu baris Task
9. Klik `[Confirm Handover]` pada menu baris Task
10. Verifikasi dialog `Confirm Handover` tampil
11. Verifikasi checklist dialog memuat `Laptop Dell Latitude 5420 {runId}`, `Monitor Dell 24 inch {runId}`, dan `Printer HP LaserJet M404 {runId}`, ketiganya tercentang
12. Verifikasi tombol `[Confirm]` tampil pada footer dialog

### Confirm dengan satu aset tidak diterima
13. Hapus centang aset `Printer HP LaserJet M404 {runId}` pada checklist dialog
14. Centang pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
15. Klik `[Confirm]` pada footer dialog
16. Verifikasi toast sukses Confirm Handover tampil
17. Verifikasi dialog `Confirm Handover` tertutup

### Task hilang sesudah Confirm
18. Verifikasi tab `Task` aktif sesudah dialog tertutup
19. Verifikasi `No tasks` tampil pada tab `Task` sesudah Confirm

### Aset tercentang menjadi Assigned dan aset tidak tercentang tetap Waiting for Handover
20. Klik tab `Assigned`
21. Verifikasi aset `Laptop Dell Latitude 5420 {runId}` berstatus `Assigned`
22. Verifikasi aset `Monitor Dell 24 inch {runId}` berstatus `Assigned`
23. Verifikasi aset `Printer HP LaserJet M404 {runId}` tetap berstatus `Waiting for Handover`

### Assignment Log mencatat hasil konfirmasi
24. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
25. Klik `[Assignment Log]` pada menu baris
26. Verifikasi Assignment Log aset `Printer HP LaserJet M404 {runId}` memuat node `Confirmation not received`
27. Klik `✕` pada dialog Assignment Log
28. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
29. Klik `[Assignment Log]` pada menu baris
30. Verifikasi Assignment Log aset `Laptop Dell Latitude 5420 {runId}` memuat entri konfirmasi penerimaan aset
31. Klik `✕` pada dialog Assignment Log
