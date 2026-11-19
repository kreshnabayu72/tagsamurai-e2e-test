---
id: TC-FA-ASSIGN-E2E-015-create-assignment-division-dengan-pic
title: "Create Assignment untuk Division dengan PIC"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-ASSIGN-04", "FI-ASG-126", "FI-ASG-127"]
smoke: []
dependsOn: []
trace:
  "F-ASSIGN-04": [9, 30, 33, 36, 37]
  "FI-ASG-126": [6, 18]
  "FI-ASG-127": [20, 22]
anchor: [32]
coverage:
  web: automated
---

# Create Assignment untuk Division dengan PIC

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-015-1: Division `Finance`, Code `FIN`, memiliki anggota aktif dengan akun login.
  - DU-015-2: Division `Field Survey`, Code `FSV`, memiliki anggota aktif dengan akun login.
  - DU-015-3: Anggota Division `Finance` `Nadia Putri` (email `nadia.putri@example.com`, Position `Analyst`, Home Group `Head Office`), karyawan aktif dengan akun login.
  - DU-015-4: Anggota Division `Finance` `Dewi Anggraini` (email `dewi.anggraini@example.com`, Position `Staff`), karyawan aktif dengan akun login.
  - DU-015-5: Aset `Projector Epson EB-X49 {runId}`, Category `Projector`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-015-6: Purpose baris aset `Operasional keuangan`.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Require approval bernilai OFF untuk Category `Projector`.

## Test Steps

### Memilih Division membuka dialog Select User untuk PIC
1. Klik `[+ Assign]`
2. Klik pilihan `Division`
3. Klik `[Select Assignee]`
4. Pilih baris `Finance` pada dialog Select Assignee
5. Klik `[Select]`
6. Verifikasi dialog `Select User` langsung terbuka dengan keterangan `Active members of Finance who can sign in.`
7. Pilih baris `Nadia Putri`
8. Klik `[Select]`
9. Verifikasi field PIC menampilkan `Nadia Putri`

### Menambah aset lalu mengganti Assignee mengosongkan PIC
10. Klik `[+ Asset]`
11. Ketik Search `Projector Epson EB-X49 {runId}`, tekan Enter
12. Centang baris `Projector Epson EB-X49 {runId}`
13. Klik `[Select]`
14. Isi Purpose baris `Projector Epson EB-X49 {runId}` dengan `Operasional keuangan`

15. Klik tombol Assignee `Finance`
16. Pilih baris `Field Survey` pada dialog Select Assignee
17. Klik `[Select]`
18. Verifikasi dialog `Select User` terbuka dengan keterangan `Active members of Field Survey who can sign in.`
19. Klik `[Cancel]` pada dialog Select User
20. Verifikasi field PIC belum terisi dan tombol `[Select PIC]` tampil
21. Klik `[Submit]`
22. Verifikasi error `You must pick a PIC` tampil di bawah field PIC

### Submit Assignment Division dengan PIC
23. Klik tombol Assignee `Field Survey`
24. Pilih baris `Finance` pada dialog Select Assignee
25. Klik `[Select]`
26. Pilih baris `Nadia Putri` pada dialog Select User
27. Klik `[Select]`
28. Klik `[Submit]`
29. Klik `[Submit]` pada dialog `Submit Assignment`
30. Verifikasi halaman Assignment Detail ASG yang baru terbentuk menampilkan Assignee `Finance` dan PIC `Nadia Putri`

### Change PIC pada ASG Division yang berjalan
31. Klik `[Change PIC]` di bawah tabel Assets
32. Verifikasi baris `Dewi Anggraini` tampil pada dialog Select User
33. Verifikasi baris `Nadia Putri` tidak tampil pada dialog Select User
34. Pilih baris `Dewi Anggraini`
35. Klik `[Select]`
36. Verifikasi toast `Success, PIC has been changed to Dewi Anggraini.` tampil
37. Verifikasi PIC pada header Assignment Detail menampilkan `Dewi Anggraini`
