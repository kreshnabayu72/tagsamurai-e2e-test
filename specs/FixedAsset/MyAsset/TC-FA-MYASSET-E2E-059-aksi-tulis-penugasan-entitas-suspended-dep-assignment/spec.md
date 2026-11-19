---
id: TC-FA-MYASSET-E2E-059-aksi-tulis-penugasan-entitas-suspended-dep-assignment
title: "Entitas Suspended: aksi tulis penugasan di My Asset ditolak dan baris tetap tampil"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.4.1#r1", "§9.4.2#r81", "§9.4.2#r82", "EB-AKS-7"]
smoke: []
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "§9.4.1#r1": [7, 9, 16, 18, 23, 25, 30, 32, 36, 38]
  "§9.4.2#r81": [7, 16, 23, 30, 36]
  "§9.4.2#r82": [9, 18, 25, 32, 38]
  "EB-AKS-7": [1, 2, 7, 9, 16, 18, 19, 23, 25, 26, 30, 32, 36, 38]
anchor: []
coverage:
  web: automated
---

# Entitas Suspended: aksi tulis penugasan di My Asset ditolak dan baris tetap tampil

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}` (karyawan ber-akun login di entitas khusus spec ini, role `Read Only`, cakupan Group `Head Office`).
- Layar awal: halaman My Asset, tab Task.
- Data:
  - Spec ini memakai entitas khusus yang tidak dipakai spec lain, karena yang diasersi adalah status seluruh entitas (Suspended).
  - DU-059-1: entitas `Client` bernama `PT Sinar Harapan {runId}`, status `Suspended`, berisi seluruh data DU-059-2 sampai DU-059-8 yang dibentuk sebelum entitas di-Suspend.
  - DU-059-2: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa Task dan tanpa penugasan lain selain DU-059-3 sampai DU-059-8.
  - DU-059-3: aset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, penugasan kepada `Budi Santoso {runId}` berstatus `Waiting for Handover` dengan sesi Handover berjalan dan Task Confirm Handover aktif untuk `Budi Santoso {runId}`.
  - DU-059-4: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, tanpa laporan.
  - DU-059-5: aset `Monitor Dell 24 inch {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, tanpa laporan.
  - DU-059-6: aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, dengan Damage Report `Waiting for Confirmation` dari `Budi Santoso {runId}` (badge `Reported Damaged`).
  - DU-059-7: aset `Projector Epson EB-X06 {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, dengan laporan Missing `Waiting for Confirmation` dari `Budi Santoso {runId}` (badge `Reported Missing`).
  - DU-059-8: isian dialog Report Damaged atas DU-059-4: What happened `Layar laptop retak sesudah terjatuh dari meja` dan Damaged Photo `laptop-layar-retak.jpg`.
- Kondisi:
  - Status entitas aktor bernilai `Suspended` selama spec berjalan.

## Test Steps

### Halaman My Asset tetap terbuka dan terbaca pada entitas Suspended
1. Verifikasi tepat satu baris Task dengan badge `Confirm Handover` tampil pada tab `Task`
2. Verifikasi halaman My Asset tetap terbuka tanpa redirect

### Confirm Handover ditolak
3. Klik `⋯` pada baris Task
4. Klik `[Confirm Handover]` pada menu baris Task
5. Centang pernyataan tanggung jawab pada dialog `Confirm Handover`
6. Klik `[Confirm]` pada footer dialog
7. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
8. Muat ulang halaman
9. Verifikasi baris Task dengan badge `Confirm Handover` masih tampil pada tab `Task` sesudah penolakan

### Report Damaged ditolak
10. Klik tab `Assigned`
11. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
12. Klik `[Report Damaged]` pada menu baris `Laptop Dell Latitude 5420 {runId}`
13. Isi `What happened` dengan `Layar laptop retak sesudah terjatuh dari meja`
14. Unggah foto `laptop-layar-retak.jpg` pada `Damaged Photo`
15. Klik `[Report Damaged]` pada footer dialog
16. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
17. Muat ulang halaman
18. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` masih tampil pada tab `Assigned` dengan Status `Assigned`
19. Verifikasi badge `Reported Damaged` tidak tampil pada baris `Laptop Dell Latitude 5420 {runId}`

### Report Missing ditolak
20. Klik `⋯` pada baris `Monitor Dell 24 inch {runId}`
21. Klik `[Report Missing]` pada menu baris `Monitor Dell 24 inch {runId}`
22. Klik `[Report Missing]` pada footer dialog
23. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
24. Muat ulang halaman
25. Verifikasi baris `Monitor Dell 24 inch {runId}` masih tampil pada tab `Assigned` dengan Status `Assigned`
26. Verifikasi badge `Reported Missing` tidak tampil pada baris `Monitor Dell 24 inch {runId}`

### Cancel Damage Report ditolak
27. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
28. Klik `[Cancel Damage Report]` pada menu baris `Printer HP LaserJet M404 {runId}`
29. Klik tombol konfirmasi pada dialog pembatalan laporan
30. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
31. Muat ulang halaman
32. Verifikasi baris `Printer HP LaserJet M404 {runId}` masih tampil dengan badge `Reported Damaged` pada kolom Status

### Cancel Missing Report ditolak
33. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
34. Klik `[Cancel Missing Report]` pada menu baris `Projector Epson EB-X06 {runId}`
35. Klik tombol konfirmasi pada dialog pembatalan laporan
36. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
37. Muat ulang halaman
38. Verifikasi baris `Projector Epson EB-X06 {runId}` masih tampil dengan badge `Reported Missing` pada kolom Status
