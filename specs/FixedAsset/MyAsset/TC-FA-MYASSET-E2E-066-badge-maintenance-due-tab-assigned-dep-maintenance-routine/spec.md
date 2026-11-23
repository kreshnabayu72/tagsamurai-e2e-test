---
id: TC-FA-MYASSET-E2E-066-badge-maintenance-due-tab-assigned-dep-maintenance-routine
title: "Badge Maintenance due di kolom Status tab Assigned: tampil pada baris Assigned, tidak tampil pada baris Waiting, dan berubah saat task Maintenance Routine berubah"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-MYA-04", "§1.2#r10", "§9.4.2#r37", "§9.4.2#r38", "§9.7#r14"]
smoke: []
dependsOn: ["Maintenance Routine: task Maintenance Routine pada aset yang ditugaskan", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
trace:
  "T-MYA-04": [2, 3, 8, 10]
  "§1.2#r10": [2, 3, 5, 8, 10]
  "§9.4.2#r37": [2, 3]
  "§9.4.2#r38": [8, 10, 13]
  "§9.7#r14": [15, 18, 23]
anchor: [7, 9, 14, 19, 22]
coverage:
  web: automated
---

# Badge Maintenance due di kolom Status tab Assigned: tampil pada baris Assigned, tidak tampil pada baris Waiting, dan berubah saat task Maintenance Routine berubah

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}`, karyawan ber-akun login dengan role `Read Only`. Aktor Assignment `Rina Wijaya {runId}`, Approver `Dewi Lestari {runId}`, dan Aktor Maintenance Routine `Maya Pratiwi {runId}` hanya memicu perubahan.
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-066-1: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif.
  - DU-066-2: pengguna `Rina Wijaya {runId}`, role `Asset Admin` dengan hak Aktor Assignment, cakupan Group `Head Office`, akun aktif.
  - DU-066-3: pengguna `Dewi Lestari {runId}`, role `Approver`, cakupan Group `Head Office`, akun aktif.
  - DU-066-4: pengguna `Maya Pratiwi {runId}`, role `Asset Admin` dengan hak mengelola task Maintenance Routine, cakupan Group `Head Office`, akun aktif.
  - DU-066-5: penugasan untuk `Budi Santoso {runId}` atas aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Assigned`, diserahkan oleh `Rina Wijaya {runId}`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
  - DU-066-6: penugasan untuk `Budi Santoso {runId}` atas aset `Projector Epson EB-X06 {runId}`, Group `Head Office`, Status `Assigned`, diserahkan oleh `Rina Wijaya {runId}`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
  - DU-066-7: penugasan untuk `Budi Santoso {runId}` atas aset `Monitor LG 24MK430H {runId}`, Group `Head Office`, Status `Assigned`, diserahkan oleh `Rina Wijaya {runId}`. Aset ini belum memiliki task Maintenance Routine.
  - DU-066-8: penugasan untuk `Budi Santoso {runId}` atas aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, Status `Waiting for Handover`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
  - DU-066-9: penugasan untuk `Budi Santoso {runId}` atas aset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, Status `Waiting for Approval`, menunggu keputusan `Dewi Lestari {runId}`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
- Kondisi:
  - Tab Assigned `Budi Santoso {runId}` hanya berisi 5 baris aset, dari DU-066-5 sampai DU-066-9.

## Test Steps

### Badge Maintenance due tampil pada baris Assigned
1. Klik tab `Assigned`
2. Verifikasi kolom Status baris `Laptop Dell Latitude 5420 {runId}` memuat badge `Assigned` bersama badge `Maintenance due`
3. Verifikasi kolom Status baris `Projector Epson EB-X06 {runId}` memuat badge `Assigned` bersama badge `Maintenance due`

### Badge Maintenance due hanya informasi tanpa aksi terkait
4. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
5. Verifikasi menu baris memuat tepat `Assignment Log`, `Report Damaged`, dan `Report Missing`, tanpa aksi terkait badge `Maintenance due`
6. Tekan `Esc` untuk menutup menu baris

### Badge Maintenance due tidak tampil pada baris Waiting
7. Verifikasi kolom Status baris `Printer HP LaserJet M404 {runId}` bernilai `Waiting for Handover`
8. Verifikasi badge `Maintenance due` tidak tampil pada kolom Status baris `Printer HP LaserJet M404 {runId}`
9. Verifikasi kolom Status baris `Scanner Zebra DS2208 {runId}` bernilai `Waiting for Approval`
10. Verifikasi badge `Maintenance due` tidak tampil pada kolom Status baris `Scanner Zebra DS2208 {runId}`

### Badge Maintenance due muncul setelah baris Waiting menjadi Assigned
11. Aktor Assignment `Rina Wijaya {runId}` menyelesaikan serah terima aset `Printer HP LaserJet M404 {runId}` kepada `Budi Santoso {runId}` sehingga penugasan menjadi `Assigned`
12. Muat ulang halaman
13. Verifikasi kolom Status baris `Printer HP LaserJet M404 {runId}` memuat badge `Assigned` bersama badge `Maintenance due`

### Badge Maintenance due muncul saat task Maintenance Routine menjadi To Do
14. Verifikasi kolom Status baris `Monitor LG 24MK430H {runId}` bernilai `Assigned`
15. Verifikasi badge `Maintenance due` tidak tampil pada kolom Status baris `Monitor LG 24MK430H {runId}`
16. Aktor Maintenance Routine `Maya Pratiwi {runId}` membuat task Maintenance Routine berstatus `To Do` untuk aset `Monitor LG 24MK430H {runId}`
17. Muat ulang halaman
18. Verifikasi kolom Status baris `Monitor LG 24MK430H {runId}` memuat badge `Assigned` bersama badge `Maintenance due`

### Badge Maintenance due hilang saat task Maintenance Routine berakhir
19. Verifikasi kolom Status baris `Projector Epson EB-X06 {runId}` memuat badge `Maintenance due`
20. Aktor Maintenance Routine `Maya Pratiwi {runId}` mengakhiri task Maintenance Routine pada aset `Laptop Dell Latitude 5420 {runId}`
21. Muat ulang halaman
22. Verifikasi kolom Status baris `Laptop Dell Latitude 5420 {runId}` memuat badge `Assigned`
23. Verifikasi badge `Maintenance due` tidak tampil pada kolom Status baris `Laptop Dell Latitude 5420 {runId}`
