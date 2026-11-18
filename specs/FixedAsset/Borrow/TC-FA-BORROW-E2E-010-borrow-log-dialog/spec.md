---
id: TC-FA-BORROW-E2E-010-borrow-log-dialog
title: "Dialog Borrow Log menampilkan riwayat satu aset di dalam satu BRW"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§5#r8", "§8#p1", "§8#r1", "§8#r2", "§8#r3", "§8#r4", "§8.1#p1", "§8.1#r1", "§8.1#r2", "§8.1#r3", "§8.1#r4", "§8.1#r5", "§8.1#b1", "§8.1#b2", "§8.1#b3"]
smoke: []
dependsOn: []
trace:
  "§5#r8": [1]
  "§8#p1": [17]
  "§8#r1": [11]
  "§8#r2": [1]
  "§8#r3": [1]
  "§8#r4": [15]
  "§8.1#p1": [11, 12, 13]
  "§8.1#r1": [7]
  "§8.1#r2": [7]
  "§8.1#r3": [8]
  "§8.1#r4": [9, 26]
  "§8.1#r5": [10]
  "§8.1#b1": [24]
  "§8.1#b2": [16, 19]
  "§8.1#b3": [14]
anchor: []
coverage:
  web: automated
---

# Dialog Borrow Log menampilkan riwayat satu aset di dalam satu BRW

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-010-1), cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-010-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client.
  - Pelaku riwayat: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`) sebagai pengaju, pemberi saat handover, pengaju Extend, dan penerima Return; `Siti Rahmawati` (Group Manager, Group binaan `Head Office`) sebagai approver dengan mode `Any one`; `Rina Wijaya` (Asset Admin, Group penugasan `Head Office`) sebagai PIC.
  - DU-010-2: BRW Returned, Borrower `Oscar Wijaya` (tampil `Oscar W`), Group `Head Office`, pengaju `Agus Pratama`, dengan tiga aset: `Gimbal DJI RS 3 {runId}`, `Kamera Sony ZV-1 {runId}`, dan `Mikrofon Rode VideoMic {runId}`. Aset `Kamera Sony ZV-1 {runId}` berstatus Returned dengan riwayat berurutan dari yang paling awal: Borrow requested (Duration `3 Day(s)`, Purpose `Client presentation`), Approved by `Siti Rahmawati` (Approved duration `3 Day(s)`, Mode `Any one`), Handed over oleh `Agus Pratama` (Duration `3 Day(s)`, Condition `Normal`), Extension requested oleh `Agus Pratama` (Extend duration `2 Day(s)`), Extension approved oleh `Siti Rahmawati` (Due date `T0 − 3 hari → T0 − 1 hari`, Extension `1 of 2`), dan Returned ke `Agus Pratama` (Condition `Normal`). Aset `Gimbal DJI RS 3 {runId}` dan `Mikrofon Rode VideoMic {runId}` memiliki riwayat sendiri.
  - DU-010-3: BRW Borrowed, Borrower `Nico Prasetyo` (karyawan tanpa akun login, PIC `Rina Wijaya`), Group `Head Office`, pengaju `Agus Pratama`, satu aset `Proyektor Epson EB-X49 {runId}` yang sudah diserahkan oleh `Agus Pratama` dan dikonfirmasi oleh `Rina Wijaya` atas nama `Nico Prasetyo`.
- Kondisi:
  - Date Format di General Settings entitas berlaku untuk tampilan tanggal.

## Test Steps

### Modul tidak memakai Changelog
1. Verifikasi toolbar tabel Transactions memuat `Search` dan `Download` dan tidak memuat `Changelog`

### Borrow Log satu aset dalam satu BRW
2. Klik tab `History`
3. Ketik Search `{runId}`, tekan Enter
4. Klik Transaction ID baris Borrower `Oscar W`
5. Klik `⋯` pada baris aset `Kamera Sony ZV-1 {runId}`
6. Klik `Borrow Log`
7. Verifikasi dialog `Borrow Log` terbuka dengan Transaction ID BRW milik DU-010-2
8. Verifikasi dialog memuat aset lain di BRW yang sama berurutan seperti tabel Assets: `Gimbal DJI RS 3 {runId}` lalu `Mikrofon Rode VideoMic {runId}`
9. Verifikasi dialog menampilkan Requested By `Agus Pratama` dan Borrower `Oscar Wijaya`
10. Verifikasi dialog menampilkan badge status baris `Returned`
11. Verifikasi urutan node dari atas ke bawah: `Returned to Agus Pratama`, `Extension approved by Siti Rahmawati`, `Extension requested by Agus Pratama`, `Handed over by Agus Pratama`, `Approved by Siti Rahmawati`, lalu `Borrow requested by Agus Pratama`
12. Verifikasi dialog hanya memuat riwayat aset `Kamera Sony ZV-1 {runId}` dan tidak memuat node milik aset `Gimbal DJI RS 3 {runId}`
13. Verifikasi node `Borrow requested by Agus Pratama` memuat `Duration: 3 Day(s)` dan `Purpose: Client presentation`
14. Verifikasi node `Approved by Siti Rahmawati` memuat nama approver, `Approved duration: 3 Day(s)`, dan `Mode: Any one`
15. Verifikasi node `Extension approved by Siti Rahmawati` memuat baris detail Due date dari nilai lama ke nilai baru `T0 − 3 hari → T0 − 1 hari` dan `Extension: 1 of 2`
16. Verifikasi node `Returned to Agus Pratama` mencatat penerima Return dan memuat `Condition: Normal`
17. Verifikasi dialog Borrow Log tidak menyediakan aksi untuk mengubah atau menghapus entri
18. Tutup dialog Borrow Log
19. Verifikasi tabel Assets tidak memiliki kolom `Received By`

### Pelaku atas nama PIC pada Borrow Log
20. Klik tab `Borrowed Assets`
21. Ketik Search `{runId}`, tekan Enter
22. Klik `⋯` pada baris aset `Proyektor Epson EB-X49 {runId}`
23. Klik `Borrow Log`
24. Verifikasi node `Handed over by Agus Pratama` memuat `Confirmation: Confirmed by Rina Wijaya on behalf of Nico Prasetyo`
25. Arahkan kursor ke ikon tautan di samping Borrower `Nico Prasetyo`
26. Verifikasi tooltip `On behalf of: Rina Wijaya (PIC)` tampil
