---
id: TC-FA-MYASSET-BE-210-status-berbasis-waktu-dep-borrow
title: "Perubahan berbasis waktu: baris menjadi Overdue dan Task hilang saat jendela konfirmasi lewat"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r12", "§1.2#r72", "§9.4.2#r87", "§9.4.2#r90", "§9.7#r2", "§9.7#r16"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "§1.2#r12": [1, 5]
  "§1.2#r72": [2, 8, 9]
  "§9.4.2#r87": [3, 11, 13, 15]
  "§9.4.2#r90": [5, 8]
  "§9.7#r2": [5, 6]
  "§9.7#r16": [5, 8, 11, 15]
---

# Perubahan berbasis waktu: baris menjadi Overdue dan Task hilang saat jendela konfirmasi lewat

## Prerequisites
- Aktor: Borrower dan Assignee Dewi (DU-210-1) dan Aktor Borrow dan Aktor Assignment Rina (DU-210-2) yang memulai sesi Handover.
- Data:
  - DU-210-1: User: Name `Dewi Lestari {runId}`, Peran `Borrower dan Assignee tanpa hak lain`.
  - DU-210-2: User: Name `Rina Wulandari {runId}`, Peran `Aktor Borrow dan Aktor Assignment pada Group Head Office`.
  - DU-210-3: Pinjaman: Name `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Dewi Lestari {runId}`, Sesi Handover `aktif, menunggu konfirmasi Dewi Lestari {runId}`.
  - DU-210-4: Penugasan: Name `Keyboard Logitech MX Keys {runId}`, Group `Head Office`, Status `Waiting for Handover`, Assignee `Dewi Lestari {runId}`, Need recipient confirmation `Yes`, Sesi Handover `aktif, menunggu konfirmasi Dewi Lestari {runId}`.
  - DU-210-5: Pinjaman: Name `Kamera Canon EOS 200D {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Satuan `Days`, Due Date `T0 + 3 hari`.
  - DU-210-6: Pinjaman: Name `Drone DJI Mini 3 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Satuan `Hours`, Due Date `T0 + 4 jam`.
- Kondisi:
  - Waktu T0 adalah saat spec ini mulai; nilai Due Date dihitung relatif terhadap T0.
  - Expires At sesi Handover `Laptop Lenovo ThinkPad T14 {runId}` (DU-210-3) dan `Keyboard Logitech MX Keys {runId}` (DU-210-4) jatuh lebih awal daripada Due Date `T0 + 4 jam` pinjaman `Drone DJI Mini 3 {runId}` (DU-210-6), Due Date paling awal di antara data ini, sehingga jendela konfirmasi habis sebelum waktu dimajukan ke Due Date mana pun.

## Test Steps

### Keadaan sebelum waktu berlalu: kedua Task masih ada dan pinjaman Hours masih Borrowed
1. Verifikasi Task Confirm Handover pinjaman `Laptop Lenovo ThinkPad T14 {runId}` ada di My Asset Dewi selama jendela konfirmasi berjalan
2. Verifikasi Task Confirm Handover penugasan `Keyboard Logitech MX Keys {runId}` ada di My Asset Dewi selama jendela konfirmasi berjalan
3. Verifikasi baris pinjaman `Drone DJI Mini 3 {runId}` berstatus `Borrowed` sebelum Due Date

### Task Confirm Handover pinjaman hilang saat jendela konfirmasi habis
4. Waktu berlalu sampai melewati Expires At sesi Handover pinjaman `Laptop Lenovo ThinkPad T14 {runId}`
5. Verifikasi Task pinjaman `Laptop Lenovo ThinkPad T14 {runId}` hilang dari My Asset Dewi
6. Verifikasi baris pinjaman `Laptop Lenovo ThinkPad T14 {runId}` tetap `Waiting for Handover` dan tidak menjadi `Borrowed`

### Task Confirm Handover penugasan hilang saat jendela konfirmasi habis
7. Waktu berlalu sampai melewati Expires At sesi Handover penugasan `Keyboard Logitech MX Keys {runId}`
8. Verifikasi Task penugasan `Keyboard Logitech MX Keys {runId}` hilang dari My Asset Dewi
9. Verifikasi baris penugasan `Keyboard Logitech MX Keys {runId}` tetap `Waiting for Handover`

### Pinjaman Hours menjadi Overdue saat Due Date terlewati
10. Waktu berlalu sampai melewati Due Date pinjaman `Drone DJI Mini 3 {runId}`, yaitu T0 + 4 jam
11. Verifikasi baris pinjaman `Drone DJI Mini 3 {runId}` menjadi `Overdue`

### Pinjaman Days menjadi Overdue pada H+1
12. Waktu berlalu sampai hari Due Date pinjaman `Kamera Canon EOS 200D {runId}`
13. Verifikasi baris pinjaman `Kamera Canon EOS 200D {runId}` masih `Borrowed` pada hari Due Date
14. Waktu berlalu sampai hari sesudah Due Date, yaitu H+1
15. Verifikasi baris pinjaman `Kamera Canon EOS 200D {runId}` menjadi `Overdue`
