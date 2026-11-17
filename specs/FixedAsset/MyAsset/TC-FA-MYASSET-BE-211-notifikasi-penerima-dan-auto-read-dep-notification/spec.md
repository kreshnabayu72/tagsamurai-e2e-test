---
id: TC-FA-MYASSET-BE-211-notifikasi-penerima-dan-auto-read-dep-notification
title: "Notifikasi My Asset: penerima atas nama dan sinyal Auto-Read saat Task hilang"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§1.2#r48", "§9.8#p1"]
smoke: []
dependsOn: ["Notification: notifikasi Borrow dan Assignment yang bertautan ke My Asset", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "§1.2#r48": 2
  "§9.8#p1": [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
---

# Notifikasi My Asset: penerima atas nama dan sinyal Auto-Read saat Task hilang

## Prerequisites
- Aktor: Borrower dengan akun Dewi (DU-211-1), Borrower tanpa akun Rahmat (DU-211-2) beserta PIC Siti (DU-211-3), PIC Division Budi (DU-211-4), dan Aktor Borrow dan Aktor Assignment Rina (DU-211-5).
- Data:
  - DU-211-1: User: Name `Dewi Lestari {runId}`, Peran `Borrower tanpa hak lain`.
  - DU-211-2: Karyawan: Name `Rahmat Hidayat {runId}`, Akun login `tidak ada`, PIC `Siti Nurhaliza {runId}`.
  - DU-211-3: User: Name `Siti Nurhaliza {runId}`, Peran `PIC Borrower tanpa akun`.
  - DU-211-4: User: Name `Budi Santoso {runId}`, Peran `PIC Division Finance`.
  - DU-211-5: User: Name `Rina Wulandari {runId}`, Peran `Aktor Borrow dan Aktor Assignment pada Group Head Office`.
  - DU-211-6: Division: Name `Finance {runId}`, PIC `Budi Santoso {runId}`.
  - DU-211-7: Penugasan: Assigned To `Finance {runId}`, Aset `Laptop Lenovo ThinkPad T14 {runId}`, Status `Waiting for Handover`, Need recipient confirmation `Yes`, PIC `Budi Santoso {runId}`.
  - DU-211-8: Pinjaman: Name `Monitor Dell 24 Inci {runId}`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Dewi Lestari {runId}`.
  - DU-211-9: Pinjaman: Name `Printer HP M404 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Dewi Lestari {runId}`.
  - DU-211-10: Pinjaman: Name `Kamera Canon EOS 200D {runId}`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Dewi Lestari {runId}`.
  - DU-211-11: Pinjaman: Name `Drone DJI Mini 3 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Rahmat Hidayat {runId}`.
  - DU-211-12: Pinjaman: Name `Scanner Canon LiDE 300 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Rahmat Hidayat {runId}`.
  - DU-211-13: Pinjaman: Name `Proyektor Epson EB-X06 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Rahmat Hidayat {runId}`.

## Test Steps

### Notifikasi Assignment untuk Division dikirim ke PIC Division
1. Rina menekan `[Request Confirmation]` pada penugasan Division `Finance {runId}` atas aset `Laptop Lenovo ThinkPad T14 {runId}`
2. Verifikasi Budi, PIC Division `Finance {runId}`, menerima notifikasi Assignment atas penugasan itu

### Notifikasi Borrow untuk Borrower tanpa akun diterima PIC dan menjadi Read saat PIC mengonfirmasi
3. Rina memulai Handover pinjaman `Drone DJI Mini 3 {runId}` milik Borrower `Rahmat Hidayat {runId}`
4. Verifikasi Siti, PIC Borrower `Rahmat Hidayat {runId}` menerima notifikasi konfirmasi serah terima atas pinjaman `Drone DJI Mini 3 {runId}` dengan status `Unread`
5. Siti mengonfirmasi serah terima pinjaman `Drone DJI Mini 3 {runId}` atas nama Rahmat
6. Verifikasi notifikasi milik Siti menjadi `Read` oleh sinyal Auto-Read `borrow_confirmation_required` karena Task hilang saat PIC mengonfirmasi

### Notifikasi Borrower ber-akun menjadi Read saat Confirm
7. Rina memulai Handover pinjaman `Monitor Dell 24 Inci {runId}` milik Borrower `Dewi Lestari {runId}`
8. Verifikasi Dewi menerima notifikasi konfirmasi serah terima atas pinjaman `Monitor Dell 24 Inci {runId}` dengan status `Unread`
9. Dewi mengonfirmasi serah terima pinjaman `Monitor Dell 24 Inci {runId}`
10. Verifikasi notifikasi milik Dewi menjadi `Read` oleh sinyal Auto-Read `borrow_confirmation_required` karena Task hilang saat Confirm

### Notifikasi Borrower ber-akun menjadi Read saat admin menekan Cancel Request
11. Rina memulai Handover pinjaman `Printer HP M404 {runId}` milik Borrower `Dewi Lestari {runId}`
12. Verifikasi Dewi menerima notifikasi konfirmasi serah terima atas pinjaman `Printer HP M404 {runId}` dengan status `Unread`
13. Rina menekan `Cancel Request` pada sesi Handover pinjaman `Printer HP M404 {runId}`
14. Verifikasi notifikasi milik Dewi menjadi `Read` oleh sinyal Auto-Read `borrow_confirmation_required` karena Task hilang saat admin menekan `Cancel Request`

### Notifikasi Borrower ber-akun menjadi Read saat jendela konfirmasi habis
15. Rina memulai Handover pinjaman `Kamera Canon EOS 200D {runId}` milik Borrower `Dewi Lestari {runId}`
16. Verifikasi Dewi menerima notifikasi konfirmasi serah terima atas pinjaman `Kamera Canon EOS 200D {runId}` dengan status `Unread`
17. Waktu berlalu sampai melewati Expires At sesi Handover pinjaman `Kamera Canon EOS 200D {runId}`
18. Verifikasi notifikasi milik Dewi menjadi `Read` oleh sinyal Auto-Read `borrow_confirmation_required` karena Task hilang saat jendela konfirmasi habis

### Notifikasi PIC menjadi Read saat admin menekan Cancel Request atas pinjaman Borrower tanpa akun
19. Rina memulai Handover pinjaman `Scanner Canon LiDE 300 {runId}` milik Borrower `Rahmat Hidayat {runId}`
20. Verifikasi Siti, PIC Borrower `Rahmat Hidayat {runId}` menerima notifikasi konfirmasi serah terima atas pinjaman `Scanner Canon LiDE 300 {runId}` dengan status `Unread`
21. Rina menekan `Cancel Request` pada sesi Handover pinjaman `Scanner Canon LiDE 300 {runId}`
22. Verifikasi notifikasi milik Siti menjadi `Read` oleh sinyal Auto-Read `borrow_confirmation_required` karena Task hilang saat admin menekan `Cancel Request`

### Notifikasi PIC menjadi Read saat jendela konfirmasi habis atas pinjaman Borrower tanpa akun
23. Rina memulai Handover pinjaman `Proyektor Epson EB-X06 {runId}` milik Borrower `Rahmat Hidayat {runId}`
24. Verifikasi Siti, PIC Borrower `Rahmat Hidayat {runId}` menerima notifikasi konfirmasi serah terima atas pinjaman `Proyektor Epson EB-X06 {runId}` dengan status `Unread`
25. Waktu berlalu sampai melewati Expires At sesi Handover pinjaman `Proyektor Epson EB-X06 {runId}`
26. Verifikasi notifikasi milik Siti menjadi `Read` oleh sinyal Auto-Read `borrow_confirmation_required` karena Task hilang saat jendela konfirmasi habis
