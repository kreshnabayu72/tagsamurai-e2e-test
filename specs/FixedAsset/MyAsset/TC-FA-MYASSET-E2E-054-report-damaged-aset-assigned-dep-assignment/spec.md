---
id: TC-FA-MYASSET-E2E-054-report-damaged-aset-assigned-dep-assignment
title: "Report Damaged pada aset Assigned: badge Reported Damaged dan aksi Report Damaged tidak tampil lagi"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["ACT-MYA-01.<aksi>.<huruf>,ACT-MYA-02.<aksi>.<huruf>,ACT-MYA-04.<aksi>.<huruf>", "T-MYA-04", "§2.1#r7", "§3#p9", "§4.4#r8", "§4.8#r8", "§7.3#r12", "§9.2#r28", "§9.2#r29", "§9.4.2#r61", "§9.4.2#r62"]
smoke: []
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "ACT-MYA-01.<aksi>.<huruf>,ACT-MYA-02.<aksi>.<huruf>,ACT-MYA-04.<aksi>.<huruf>": [3, 5, 6, 7, 8, 9, 10, 14, 15, 16, 23, 24, 28, 31, 33, 35, 36]
  "T-MYA-04": [16, 17, 18, 30, 33]
  "§2.1#r7": [14, 16]
  "§3#p9": [3, 5, 16, 24]
  "§4.4#r8": [5, 16]
  "§4.8#r8": 3
  "§7.3#r12": 14
  "§9.2#r28": 5
  "§9.2#r29": [17, 18]
  "§9.4.2#r61": 16
  "§9.4.2#r62": 24
anchor: [20, 32]
coverage:
  web: automated
---

# Report Damaged pada aset Assigned: badge Reported Damaged dan aksi Report Damaged tidak tampil lagi

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}` (karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`).
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-054-1: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa penugasan lain selain DU-054-3 dan DU-054-4.
  - DU-054-2: pengguna `Rina Wijaya {runId}`, role `Asset Admin`, cakupan Group `Head Office`, akun aktif, Aktor Assignment penyerah DU-054-3 dan DU-054-4.
  - DU-054-3: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, tanpa Damage Report dan tanpa laporan lain.
  - DU-054-4: aset `Monitor Dell 24 inch {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, tanpa Damage Report dan tanpa laporan lain.
  - DU-054-5: laporan atas DU-054-3 dengan What happened `Layar laptop retak sesudah terjatuh dari meja` dan Damaged Photo `laptop-layar-retak.jpg`, dibuat oleh langkah spec ini lalu dibatalkan pelapor.

## Test Steps

### Aksi Report Damaged tersedia pada baris Assigned
1. Klik tab `Assigned`
2. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi aksi `Report Damaged` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
4. Klik `[Report Damaged]` pada menu baris `Laptop Dell Latitude 5420 {runId}`

### Dialog Report Damaged dari baris Assigned dan pengiriman laporan
5. Verifikasi dialog `Report Damaged` tampil dengan aset `Laptop Dell Latitude 5420 {runId}`
6. Verifikasi field `What happened` tampil pada dialog
7. Verifikasi field `Damaged Photo` tampil pada dialog
8. Verifikasi field `What happened` ditandai wajib
9. Verifikasi field `Damaged Photo` ditandai wajib
10. Verifikasi kotak dampak tidak tampil pada dialog
11. Isi `What happened` dengan `Layar laptop retak sesudah terjatuh dari meja`
12. Unggah foto `laptop-layar-retak.jpg` pada `Damaged Photo`
13. Klik `[Report Damaged]` pada footer dialog
14. Verifikasi toast sukses tampil untuk laporan yang dikirim
15. Verifikasi dialog `Report Damaged` tertutup

### Badge Reported Damaged dan baris tetap Assigned milik Assignee
16. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil pada tab `Assigned` dengan badge `Reported Damaged` pada kolom Status
17. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` tetap `Assigned`
18. Verifikasi kolom `Assigned To` baris `Laptop Dell Latitude 5420 {runId}` tetap `Me`

### Aksi Report Damaged tidak tampil lagi pada baris yang dilaporkan
19. Klik `⋯` pada baris `Monitor Dell 24 inch {runId}`
20. Verifikasi aksi `Report Damaged` tampil pada menu baris `Monitor Dell 24 inch {runId}`
21. Tutup menu baris `Monitor Dell 24 inch {runId}`
22. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
23. Verifikasi aksi `Cancel Damage Report` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
24. Verifikasi aksi `Report Damaged` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
25. Tutup menu baris `Laptop Dell Latitude 5420 {runId}`

### Cancel Damage Report pada baris Assigned memulihkan aksi Report Damaged
26. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
27. Klik `[Cancel Damage Report]` pada menu baris `Laptop Dell Latitude 5420 {runId}`
28. Verifikasi dialog `Cancel Report` tampil untuk aset `Laptop Dell Latitude 5420 {runId}`
29. Konfirmasi pembatalan laporan pada dialog `Cancel Report`
30. Verifikasi toast sukses `Success, report has been canceled.` tampil
31. Verifikasi dialog `Cancel Report` tertutup
32. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` adalah `Assigned`
33. Verifikasi badge `Reported Damaged` tidak tampil pada kolom Status baris `Laptop Dell Latitude 5420 {runId}`
34. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
35. Verifikasi aksi `Report Damaged` tampil lagi pada menu baris `Laptop Dell Latitude 5420 {runId}`
36. Verifikasi aksi `Cancel Damage Report` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
37. Tutup menu baris `Laptop Dell Latitude 5420 {runId}`
