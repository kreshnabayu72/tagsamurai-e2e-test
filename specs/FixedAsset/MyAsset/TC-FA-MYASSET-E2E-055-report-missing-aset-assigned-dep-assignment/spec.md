---
id: TC-FA-MYASSET-E2E-055-report-missing-aset-assigned-dep-assignment
title: "Report Missing pada aset Assigned: badge Reported Missing dan baris tetap Assigned"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["ACT-MYA-01.<aksi>.<huruf>,ACT-MYA-02.<aksi>.<huruf>,ACT-MYA-04.<aksi>.<huruf>", "T-MYA-04", "§2.1#r8", "§3#p9", "§4.8#r9", "§9.2#r30", "§9.4.2#r57"]
smoke: []
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "ACT-MYA-01.<aksi>.<huruf>,ACT-MYA-02.<aksi>.<huruf>,ACT-MYA-04.<aksi>.<huruf>": [3, 5, 7, 8, 9, 10, 16, 17, 18]
  "T-MYA-04": [9, 10]
  "§2.1#r8": [7, 9]
  "§3#p9": [3, 5, 9, 10]
  "§4.8#r9": 3
  "§9.2#r30": [5, 7, 9]
  "§9.4.2#r57": 9
anchor: [12, 13]
coverage:
  web: automated
---

# Report Missing pada aset Assigned: badge Reported Missing dan baris tetap Assigned

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}` (karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`, tanpa hak Aktor Missing pada Group `Head Office`).
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-055-1: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa penugasan lain selain DU-055-3 dan DU-055-4.
  - DU-055-2: pengguna `Rina Wijaya {runId}`, role `Asset Admin`, cakupan Group `Head Office`, akun aktif, Aktor Assignment penyerah DU-055-3 dan DU-055-4.
  - DU-055-3: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, tanpa laporan Damaged dan tanpa laporan Missing.
  - DU-055-4: aset `Monitor Dell 24 inch {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, tanpa laporan Damaged dan tanpa laporan Missing.
  - DU-055-5: laporan atas DU-055-3 dari `Budi Santoso {runId}` dengan status `Waiting for Confirmation`, dibuat oleh langkah spec ini.

## Test Steps

### Aksi Report Missing tersedia pada baris Assigned
1. Klik tab `Assigned`
2. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi aksi `Report Missing` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
4. Klik `[Report Missing]` pada menu baris `Laptop Dell Latitude 5420 {runId}`

### Dialog Report Missing dari baris Assigned dan pengiriman laporan
5. Verifikasi dialog `Report Missing` tampil dengan aset `Laptop Dell Latitude 5420 {runId}`
6. Klik `[Report Missing]` pada footer dialog
7. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
8. Verifikasi dialog `Report Missing` tertutup

### Badge Reported Missing dan baris tetap Assigned
9. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil pada tab `Assigned` dengan badge `Reported Missing` pada kolom Status
10. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` tetap `Assigned`

### Aksi pada baris yang dilaporkan
11. Klik `⋯` pada baris `Monitor Dell 24 inch {runId}`
12. Verifikasi aksi `Report Damaged` tampil pada menu baris `Monitor Dell 24 inch {runId}`
13. Verifikasi aksi `Report Missing` tampil pada menu baris `Monitor Dell 24 inch {runId}`
14. Tutup menu baris `Monitor Dell 24 inch {runId}`
15. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
16. Verifikasi aksi `Cancel Missing Report` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
17. Verifikasi aksi `Report Missing` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
18. Verifikasi aksi `Report Damaged` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
19. Tutup menu baris `Laptop Dell Latitude 5420 {runId}`
