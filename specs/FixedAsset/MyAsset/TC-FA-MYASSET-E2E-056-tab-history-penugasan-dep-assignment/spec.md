---
id: TC-FA-MYASSET-E2E-056-tab-history-penugasan-dep-assignment
title: "Tab History pada data nyata penugasan: Type Assignment, status akhir, dan aksi Assignment Log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["§1.2#r18", "§1.2#r19", "§1.2#r75", "§1.2#r76", "§1.2#r80", "§1.2#r81", "§4.1c#r7", "§4.1c#r8", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r19", "§9.2#b12"]
smoke: []
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "§1.2#r18": [2, 3]
  "§1.2#r19": 4
  "§1.2#r75": [5, 6]
  "§1.2#r76": [7, 8]
  "§1.2#r80": [4, 5, 6, 7, 8]
  "§1.2#r81": [15, 16, 17, 18, 23, 24, 27, 28]
  "§4.1c#r7": [5, 6, 7, 8]
  "§4.1c#r8": 9
  "§4.1c#r11": 4
  "§4.1c#r12": 10
  "§4.1c#r13": [11, 12]
  "§4.1c#r19": [15, 20, 23, 27]
  "§9.2#b12": [11, 12, 13, 15, 16]
anchor: []
coverage:
  web: automated
---

# Tab History pada data nyata penugasan: Type Assignment, status akhir, dan aksi Assignment Log

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}` (karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`).
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-056-1: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa transaksi lain selain DU-056-6, DU-056-7, dan DU-056-8.
  - DU-056-2: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, pernah ditugaskan kepada `Budi Santoso {runId}` lalu dilepas (Unassigned), tanpa laporan lain.
  - DU-056-3: aset `Monitor Dell 24 inch {runId}`, Group `Head Office`, pernah ditugaskan kepada `Budi Santoso {runId}` dalam transaksi yang sama dengan DU-056-2 lalu dilepas (Unassigned), tanpa laporan lain.
  - DU-056-4: aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, penugasan kepada `Budi Santoso {runId}` ditolak (Rejected) sebelum diserahkan.
  - DU-056-5: aset `Projector Epson EB-X06 {runId}`, Group `Head Office`, penugasan kepada `Budi Santoso {runId}` dibatalkan (Canceled) sebelum diserahkan.
  - DU-056-6: transaksi penugasan `Budi Santoso {runId}` atas DU-056-2 dan DU-056-3, status akhir `Unassigned`, sudah diserahkan dan sudah ditutup.
  - DU-056-7: transaksi penugasan `Budi Santoso {runId}` atas DU-056-4, status akhir `Rejected`, tidak pernah diserahkan.
  - DU-056-8: transaksi penugasan `Budi Santoso {runId}` atas DU-056-5, status akhir `Canceled`, tidak pernah diserahkan.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24 jam`.

## Test Steps

### Baris penugasan yang ditutup tampil per aset dengan Type Assignment
1. Klik tab `History`
2. Verifikasi tepat empat baris tampil pada tab `History`, yaitu aset `Laptop Dell Latitude 5420 {runId}`, `Monitor Dell 24 inch {runId}`, `Printer HP LaserJet M404 {runId}`, dan `Projector Epson EB-X06 {runId}`
3. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` dan baris `Monitor Dell 24 inch {runId}` memiliki Transaction ID yang sama karena berasal dari satu transaksi dengan satu baris per aset
4. Verifikasi kolom `Type` keempat baris bernilai `Assignment`

### Status akhir dan nilai sel baris penugasan
5. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` adalah `Unassigned`
6. Verifikasi Status baris `Monitor Dell 24 inch {runId}` adalah `Unassigned`
7. Verifikasi Status baris `Printer HP LaserJet M404 {runId}` adalah `Rejected`
8. Verifikasi Status baris `Projector Epson EB-X06 {runId}` adalah `Canceled`
9. Verifikasi kolom `Holder` keempat baris bernilai `Me`
10. Verifikasi kolom `Transaction ID` baris `Laptop Dell Latitude 5420 {runId}` mengikuti format `ASG-YYYY-NNNN`
11. Verifikasi kolom `Handed Over At` baris `Laptop Dell Latitude 5420 {runId}` berisi Assigned Date dalam Date Format `dd/MM/yy` dan Time Format `24 jam`
12. Verifikasi kolom `Handed Over At` baris `Printer HP LaserJet M404 {runId}` dan `Projector Epson EB-X06 {runId}` bernilai `—`
13. Verifikasi kolom `Closed At` keempat baris terisi dalam Date Format `dd/MM/yy` dan Time Format `24 jam`

### Aksi baris Unassigned hanya Assignment Log
14. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
15. Verifikasi aksi `Assignment Log` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
16. Verifikasi aksi `Report Damaged` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
17. Verifikasi aksi `Report Missing` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
18. Verifikasi aksi `Unassign` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
19. Klik `[Assignment Log]` pada menu baris `Laptop Dell Latitude 5420 {runId}`
20. Verifikasi dialog Assignment Log aset `Laptop Dell Latitude 5420 {runId}` tampil
21. Klik `✕` pada dialog Assignment Log

### Aksi baris Rejected dan Canceled hanya Assignment Log
22. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
23. Verifikasi aksi `Assignment Log` tampil pada menu baris `Printer HP LaserJet M404 {runId}`
24. Verifikasi aksi `Report Damaged` tidak tampil pada menu baris `Printer HP LaserJet M404 {runId}`
25. Tutup menu baris `Printer HP LaserJet M404 {runId}`
26. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
27. Verifikasi aksi `Assignment Log` tampil pada menu baris `Projector Epson EB-X06 {runId}`
28. Verifikasi aksi `Report Damaged` tidak tampil pada menu baris `Projector Epson EB-X06 {runId}`
29. Tutup menu baris `Projector Epson EB-X06 {runId}`
