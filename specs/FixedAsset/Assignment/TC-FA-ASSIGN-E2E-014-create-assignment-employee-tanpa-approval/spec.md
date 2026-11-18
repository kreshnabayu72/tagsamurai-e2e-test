---
id: TC-FA-ASSIGN-E2E-014-create-assignment-employee-tanpa-approval
title: "Create Assignment untuk Employee tanpa approval lalu Submit"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-ASSIGN-02", "§3#p3", "§3#p5", "§4.1#p1", "§4.4#r6", "TS-ASG-03", "EC-ASG-08"]
smoke: []
dependsOn: []
trace:
  "F-ASSIGN-02": [16, 27]
  "§3#p3": [2, 4, 16, 21]
  "§3#p5": [29, 37]
  "§4.1#p1": [8, 16]
  "§4.4#r6": [26, 27]
  "TS-ASG-03": 26
  "EC-ASG-08": [28, 29, 30]
anchor: [36]
coverage:
  web: automated
---

# Create Assignment untuk Employee tanpa approval lalu Submit

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-014-1: Aset `Laptop Dell Latitude 5420 {runId}`, Category `Laptop`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-014-2: Aset `Monitor LG 24 {runId}`, Category `Monitor`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-014-3: Aset `Printer HP M404 {runId}`, Category `Printer`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-014-4: Assignee Employee `Budi Santoso` (email `budi.santoso@example.com`, Position `Staff`, Division `IT`, Home Group `Head Office`), karyawan aktif dengan akun login.
  - DU-014-5: Purpose baris aset `Kerja harian`.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Require approval bernilai OFF untuk Category `Laptop`, `Monitor`, dan `Printer`.

## Test Steps

### Titik masuk [+ Assign] memilih tipe Assignee
1. Klik `[+ Assign]`
2. Verifikasi overlay `Assign to` menampilkan pilihan `Employee` dan `Division`
3. Klik pilihan `Employee`
4. Verifikasi form Assignment Request terbuka dengan Assignee Type `Employee`
5. Klik `[Cancel]` (form belum diubah, tanpa dialog Unsaved Changes)

### Titik masuk Quick Action
6. Klik `Quick Action` pada navbar
7. Klik `Assign`
8. Verifikasi form Assignment Request terbuka dengan tabel aset menampilkan empty state `No assets added`
9. Klik `[Cancel]` (form belum diubah, tanpa dialog Unsaved Changes)

### Assign dari Asset List dan tambah aset dari dialog Select Asset
10. Buka `Assets > Available`
11. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
12. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
13. Klik `Assign`
14. Pilih baris `Budi Santoso` pada dialog Select Assignee
15. Klik `[Select]`
16. Verifikasi form Assignment Request terbuka dengan Assignee `Budi Santoso` dan baris aset `Laptop Dell Latitude 5420 {runId}` sudah terisi
17. Klik `[+ Asset]`
18. Ketik Search `Monitor LG 24 {runId}`, tekan Enter
19. Centang baris `Monitor LG 24 {runId}`
20. Klik `[Select]`
21. Verifikasi baris `Monitor LG 24 {runId}` tampil di tabel aset
22. Isi Purpose baris `Laptop Dell Latitude 5420 {runId}` dengan `Kerja harian`
23. Isi Purpose baris `Monitor LG 24 {runId}` dengan `Kerja harian`

### Submit tanpa approval menghasilkan satu ASG Waiting for Handover
24. Klik `[Submit]`
25. Klik `[Submit]` pada dialog `Submit Assignment`
26. Verifikasi toast `Success, assignment [Transaction ID] is ready for handover.` tampil dengan Transaction ID ASG yang baru terbentuk
27. Verifikasi halaman Assignment Detail ASG yang baru terbentuk terbuka dan tabel Assets memuat baris `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 24 {runId}`
28. Verifikasi status header ASG `Waiting for Handover`
29. Verifikasi status baris `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 24 {runId}` keduanya `Waiting for Handover`
30. Verifikasi Approval kedua baris `Not required`

### Aset yang sudah diajukan tidak ditawarkan lagi
31. Buka `Transactions > Assignment`
32. Klik `[+ Assign]`
33. Klik pilihan `Employee`
34. Klik `[+ Asset]`
35. Ketik Search `{runId}`, tekan Enter
36. Verifikasi baris `Printer HP M404 {runId}` tampil pada dialog Select Asset
37. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 24 {runId}` tidak tampil pada dialog Select Asset
38. Klik `[Cancel]` pada dialog Select Asset
39. Klik `[Cancel]` pada form (form belum diubah, tanpa dialog Unsaved Changes)
