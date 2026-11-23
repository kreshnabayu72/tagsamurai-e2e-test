---
id: TC-FA-MYASSET-E2E-065-badge-maintenance-due-tab-borrowed-dep-maintenance-routine
title: "Badge Maintenance due di kolom Status tab Borrowed: tampil pada baris yang asetnya dipegang, tidak tampil pada baris Waiting, dan berubah saat task Maintenance Routine berubah"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1b#r7", "§1.2#r10", "§9.4.2#r37", "§9.4.2#r38", "§9.7#r14"]
smoke: []
dependsOn: ["Maintenance Routine: task Maintenance Routine pada aset yang dipinjam", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.1b#r7": [2, 3, 4, 5, 10, 12]
  "§1.2#r10": [2, 3, 4, 5, 7, 10, 12]
  "§9.4.2#r37": [2, 3, 4, 5]
  "§9.4.2#r38": [10, 12, 15]
  "§9.7#r14": [17, 20, 25]
anchor: [9, 11, 16, 21, 24]
coverage:
  web: automated
---

# Badge Maintenance due di kolom Status tab Borrowed: tampil pada baris yang asetnya dipegang, tidak tampil pada baris Waiting, dan berubah saat task Maintenance Routine berubah

## Prerequisites
- Aktor: Borrower `Budi Santoso {runId}`, pengguna karyawan ber-akun login tanpa role admin. Aktor Borrow `Rina Wulandari {runId}` dan Aktor Maintenance Routine `Maya Pratiwi {runId}` hanya memicu perubahan.
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-065-1: pengguna `Budi Santoso {runId}`, karyawan ber-akun login, tanpa role admin, cakupan Group `Head Office`.
  - DU-065-2: pengguna `Rina Wulandari {runId}`, role Asset Admin dengan hak Aktor Borrow, cakupan Group `Head Office`.
  - DU-065-3: pengguna `Dewi Lestari {runId}`, role Approver, cakupan Group `Head Office`.
  - DU-065-4: pengguna `Maya Pratiwi {runId}`, role Asset Admin dengan hak mengelola task Maintenance Routine, cakupan Group `Head Office`.
  - DU-065-5: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
  - DU-065-6: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Kamera Canon EOS 90D {runId}`, Group `Head Office`, Status `Overdue`, Duration `2 days`, Handed Over At `T0 − 5 hari`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
  - DU-065-7: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Tablet Lenovo Tab P11 {runId}`, Group `Head Office`, Status `Extension Request`, Duration `5 days`, Handed Over At `T0 − 2 hari`, pengajuan Extend menunggu review Aktor Borrow `Rina Wulandari {runId}`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
  - DU-065-8: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Tripod Manfrotto {runId}`, Group `Head Office`, Status `Extension Approval`, Duration `5 days`, Handed Over At `T0 − 3 hari`, Approval type `Any one approver` dengan approver `Dewi Lestari {runId}` yang belum Approve, pengajuan Extend sudah diteruskan Aktor Borrow `Rina Wulandari {runId}`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
  - DU-065-9: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Monitor Dell 24 inci {runId}`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`. Aset ini belum memiliki task Maintenance Routine.
  - DU-065-10: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Proyektor Epson EB-X06 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
  - DU-065-11: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Printer Canon G3010 {runId}`, Group `Head Office`, Status `Waiting for Approval`, Duration `3 days`, Approval type `Any one approver` dengan approver `Dewi Lestari {runId}` yang belum Approve. Aset ini memiliki task Maintenance Routine berstatus `To Do`.
- Kondisi:
  - Tab Borrowed `Budi Santoso {runId}` hanya berisi 7 baris aset, dari DU-065-5 sampai DU-065-11.

## Test Steps

### Badge Maintenance due tampil pada baris yang asetnya dipegang
1. Klik tab `Borrowed`
2. Verifikasi kolom Status baris `Laptop Dell Latitude 5420 {runId}` memuat badge `Borrowed` bersama badge `Maintenance due`
3. Verifikasi kolom Status baris `Kamera Canon EOS 90D {runId}` memuat badge `Overdue` bersama badge `Maintenance due`
4. Verifikasi kolom Status baris `Tablet Lenovo Tab P11 {runId}` memuat badge `Extension Request` bersama badge `Maintenance due`
5. Verifikasi kolom Status baris `Tripod Manfrotto {runId}` memuat badge `Extension Approval` bersama badge `Maintenance due`

### Badge Maintenance due hanya informasi tanpa aksi terkait
6. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
7. Verifikasi menu baris memuat tepat `Borrow Log`, `Request Extension`, `Report Damaged`, dan `Report Missing`, tanpa aksi terkait badge `Maintenance due`
8. Tekan `Esc` untuk menutup menu baris

### Badge Maintenance due tidak tampil pada baris Waiting
9. Verifikasi kolom Status baris `Proyektor Epson EB-X06 {runId}` bernilai `Waiting for Handover`
10. Verifikasi badge `Maintenance due` tidak tampil pada kolom Status baris `Proyektor Epson EB-X06 {runId}`
11. Verifikasi kolom Status baris `Printer Canon G3010 {runId}` bernilai `Waiting for Approval`
12. Verifikasi badge `Maintenance due` tidak tampil pada kolom Status baris `Printer Canon G3010 {runId}`

### Badge Maintenance due muncul setelah baris Waiting menjadi Borrowed
13. Aktor Borrow `Rina Wulandari {runId}` menyelesaikan serah terima aset `Proyektor Epson EB-X06 {runId}` kepada `Budi Santoso {runId}` sehingga pinjaman menjadi `Borrowed`
14. Muat ulang halaman
15. Verifikasi kolom Status baris `Proyektor Epson EB-X06 {runId}` memuat badge `Borrowed` bersama badge `Maintenance due`

### Badge Maintenance due muncul saat task Maintenance Routine menjadi To Do
16. Verifikasi kolom Status baris `Monitor Dell 24 inci {runId}` bernilai `Borrowed`
17. Verifikasi badge `Maintenance due` tidak tampil pada kolom Status baris `Monitor Dell 24 inci {runId}`
18. Aktor Maintenance Routine `Maya Pratiwi {runId}` membuat task Maintenance Routine berstatus `To Do` untuk aset `Monitor Dell 24 inci {runId}`
19. Muat ulang halaman
20. Verifikasi kolom Status baris `Monitor Dell 24 inci {runId}` memuat badge `Borrowed` bersama badge `Maintenance due`

### Badge Maintenance due hilang saat task Maintenance Routine berakhir
21. Verifikasi kolom Status baris `Kamera Canon EOS 90D {runId}` memuat badge `Maintenance due`
22. Aktor Maintenance Routine `Maya Pratiwi {runId}` mengakhiri task Maintenance Routine pada aset `Laptop Dell Latitude 5420 {runId}`
23. Muat ulang halaman
24. Verifikasi kolom Status baris `Laptop Dell Latitude 5420 {runId}` memuat badge `Borrowed`
25. Verifikasi badge `Maintenance due` tidak tampil pada kolom Status baris `Laptop Dell Latitude 5420 {runId}`
