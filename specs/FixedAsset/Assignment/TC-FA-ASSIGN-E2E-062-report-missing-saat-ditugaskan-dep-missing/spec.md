---
id: TC-FA-ASSIGN-E2E-062-report-missing-saat-ditugaskan-dep-missing
title: "Report Missing saat ditugaskan dan scan aset Missing"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [EC-ASG-33, EC-ASG-34, EC-ASG-39, F-ASSIGN-10.k1, "§9.7#r15", V-ASG-26]
smoke: []
dependsOn: ["Missing: Report Missing dan Mark as Found"]
trace:
  EC-ASG-33: [3, 5]
  EC-ASG-34: [15, 17, 18, 22]
  EC-ASG-39: [28, 29, 34, 41, 42]
  F-ASSIGN-10.k1: [5, 17]
  "§9.7#r15": [3, 15]
  V-ASG-26: [28, 41]
anchor: []
coverage:
  web: automated
---
# Report Missing saat ditugaskan dan scan aset Missing

## Prerequisites
- Aktor: Aktor Assignment (Asset Admin `Dewi Lestari {runId}`, DU-062-1).
- Layar awal: Transactions > Assignment.
- Data:
  - DU-062-1: Karyawan `Dewi Lestari {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`.
  - DU-062-2: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee semua ASG di bawah ini.
  - DU-062-3: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi aset `Laptop Acer Swift 3 {runId}` dengan laporan Missing `Waiting for Confirmation` milik pelapor `Budi Santoso {runId}`.
  - DU-062-4: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi dua aset: `Tablet Huawei MatePad {runId}` dan `Monitor AOC 24B2 {runId}`, tanpa laporan.
  - DU-062-5: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi aset `Kamera Fujifilm X-T30 {runId}`, tanpa laporan.
  - DU-062-6: Aset `Genset Honda EU20i {runId}` yang record Missing-nya berstatus Missing; baris penugasan sebelumnya sudah `Unassigned` dengan marker `Missing`.
  - DU-062-7: Laporan Missing baru untuk `Tablet Huawei MatePad {runId}` dengan Reason `Tablet tidak ditemukan setelah rapat di ruang lantai dua`.
  - DU-062-8: ASG `Waiting for Handover` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, Confirmation Rule `No`, Photo at start `OFF`, berisi aset `Speaker JBL PartyBox {runId}`.


## Test Steps

### Laporan Missing dari Assignee membuat baris tetap Assigned dengan badge Reported Missing
1. Buka tab Assigned Assets di halaman Transactions > Assignment
2. Ketik Search `Laptop Acer Swift 3 {runId}`, tekan Enter
3. Verifikasi baris aset `Laptop Acer Swift 3 {runId}` tetap berstatus `Assigned` dengan badge `Reported Missing`
4. Klik aksi `Assignment Log` pada baris aset `Laptop Acer Swift 3 {runId}`
5. Verifikasi node `Reported missing by [Actor]` dengan pelaku `Budi Santoso {runId}` dan Status `Waiting for Confirmation` tampil
6. Tutup dialog `Assignment Log`

### Report Missing oleh Aktor Assignment menutup baris tanpa scan
7. Ganti isi kotak search dengan `Tablet Huawei MatePad {runId}`, tekan Enter
8. Klik `⋯` pada baris aset `Tablet Huawei MatePad {runId}`
9. Klik `Report Missing`
10. Isi Reason `Tablet tidak ditemukan setelah rapat di ruang lantai dua` pada dialog `Report Missing`
11. Kirim dialog `Report Missing`
12. Buka tab History di halaman Transactions > Assignment
13. Buka sub-tab By Asset
14. Ketik Search `Tablet Huawei MatePad {runId}`, tekan Enter
15. Verifikasi baris aset `Tablet Huawei MatePad {runId}` berstatus `Unassigned` dengan marker `Missing`
16. Klik aksi `Assignment Log` pada baris aset `Tablet Huawei MatePad {runId}`
17. Verifikasi node `Reported missing by [Actor]` dengan pelaku `Dewi Lestari {runId}` tampil
18. Verifikasi node `Reported missing by [Actor]` memuat Reason `Tablet tidak ditemukan setelah rapat di ruang lantai dua`
19. Tutup dialog `Assignment Log`
20. Buka tab Assigned Assets di halaman Transactions > Assignment
21. Ketik Search `Monitor AOC 24B2 {runId}`, tekan Enter
22. Verifikasi baris aset `Monitor AOC 24B2 {runId}` tetap berstatus `Assigned`

### Scan aset Missing di halaman Unassign ditolak
23. Ganti isi kotak search dengan `Kamera Fujifilm X-T30 {runId}`, tekan Enter
24. Klik `⋯` pada baris aset `Kamera Fujifilm X-T30 {runId}`
25. Klik `Unassign`
26. Klik `[Verify Asset]`
27. Pindai TAG aset `Genset Honda EU20i {runId}`
28. Verifikasi toast `[Asset Name] is reported missing.` tampil dengan nama aset `Genset Honda EU20i {runId}` beserta tautan `[View Missing Log]`
29. Verifikasi daftar Unassign tidak berubah dan baris aset `Kamera Fujifilm X-T30 {runId}` berstatus `Unverified`
30. Klik `[Cancel]` pada form Unassign yang belum diubah
31. Buka tab History di halaman Transactions > Assignment
32. Buka sub-tab By Asset
33. Ketik Search `Genset Honda EU20i {runId}`, tekan Enter
34. Verifikasi baris aset `Genset Honda EU20i {runId}` tetap berstatus `Unassigned` dengan marker `Missing`

### Scan aset Missing di halaman Hand Over ditolak
35. Buka tab Transactions di halaman Transactions > Assignment
36. Ketik Search `Speaker JBL PartyBox {runId}`, tekan Enter
37. Klik `⋯` pada baris ASG untuk aset `Speaker JBL PartyBox {runId}`
38. Klik `Hand Over`
39. Klik `[Verify Asset]`
40. Pindai TAG aset `Genset Honda EU20i {runId}`
41. Verifikasi toast `[Asset Name] is reported missing.` tampil dengan nama aset `Genset Honda EU20i {runId}` beserta tautan `[View Missing Log]`
42. Verifikasi daftar Hand Over tidak berubah dan baris aset `Speaker JBL PartyBox {runId}` berstatus `Unverified`
