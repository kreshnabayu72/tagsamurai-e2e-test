---
id: TC-FA-ASSIGN-E2E-019-submit-melebihi-batas-aset-assignee
title: "Submit ditolak karena melebihi Max assets per assignee"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["EC-ASG-03"]
smoke: []
dependsOn: []
trace:
  "EC-ASG-03": [29, 35, 37]
anchor: [33]
coverage:
  web: automated
---

# Submit ditolak karena melebihi Max assets per assignee

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-019-1: Aset `Camera Sony A7 {runId}`, Category `Camera`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-019-2: Aset `Camera Canon EOS R6 {runId}`, Category `Camera`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-019-3: Aset `Camera Fujifilm X-T4 {runId}`, Category `Camera`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-019-4: Aset `Camera Nikon Z6 {runId}`, Category `Camera`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-019-5: Assignee Employee `Nadia Pratama {runId}` (email `nadia.pratama.{runId}@example.com`, Position `Accountant`, Division `Finance`, Home Group `Branch Surabaya`), karyawan aktif dengan akun login.
  - DU-019-6: Purpose baris aset `Dokumentasi kegiatan`.
  - ASG pertama berisi `2` aset.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Max assets per assignee efektif untuk Category `Camera` bernilai `3`, dihitung di Category itu.
  - Require approval bernilai OFF untuk Category `Camera`.

## Test Steps

### Dua baris aktif dari Submit pertama lalu Submit kedua melebihi batas ditolak
1. Klik `[+ Assign]`
2. Klik pilihan `Employee`
3. Klik `[Select Assignee]`
4. Pilih baris `Nadia Pratama {runId}` pada dialog Select Assignee
5. Klik `[Select]`
6. Klik `[+ Asset]`
7. Ketik Search `{runId}`, tekan Enter
8. Centang baris `Camera Sony A7 {runId}`
9. Centang baris `Camera Canon EOS R6 {runId}`
10. Klik `[Select]`
11. Isi Purpose baris `Camera Sony A7 {runId}` dengan `Dokumentasi kegiatan`
12. Isi Purpose baris `Camera Canon EOS R6 {runId}` dengan `Dokumentasi kegiatan`
13. Klik `[Submit]`
14. Klik `[Submit]` pada dialog `Submit Assignment`

15. Buka `Transactions > Assignment`
16. Klik `[+ Assign]`
17. Klik pilihan `Employee`
18. Klik `[Select Assignee]`
19. Pilih baris `Nadia Pratama {runId}` pada dialog Select Assignee
20. Klik `[Select]`
21. Klik `[+ Asset]`
22. Ketik Search `{runId}`, tekan Enter
23. Centang baris `Camera Fujifilm X-T4 {runId}`
24. Centang baris `Camera Nikon Z6 {runId}`
25. Klik `[Select]`
26. Isi Purpose baris `Camera Fujifilm X-T4 {runId}` dengan `Dokumentasi kegiatan`
27. Isi Purpose baris `Camera Nikon Z6 {runId}` dengan `Dokumentasi kegiatan`
28. Klik `[Submit]`
29. Verifikasi pesan `[Assignee] can hold up to 3 assets at a time.` tampil dengan `[Assignee]` berisi nama Assignee `Nadia Pratama {runId}`
30. Klik `[Cancel]` pada form
31. Klik `[Leave]` pada dialog Unsaved Changes

### Tidak ada ASG yang dibuat dari Submit kedua
32. Ketik Search `Camera Sony A7 {runId}`, tekan Enter
33. Verifikasi satu baris ASG dengan Assignee `Nadia Pratama {runId}` dan Total Asset `2` tampil
34. Ganti isi kotak search dengan `Camera Nikon Z6 {runId}`, tekan Enter
35. Verifikasi tidak ada baris ASG yang tampil dan empty state `No results found` tampil
36. Ganti isi kotak search dengan `Camera Fujifilm X-T4 {runId}`, tekan Enter
37. Verifikasi tidak ada baris ASG yang tampil dan empty state `No results found` tampil
