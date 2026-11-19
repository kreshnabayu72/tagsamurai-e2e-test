---
id: TC-FA-ASSIGN-E2E-057-transaction-log-aset-di-asset-detail-dep-asset-detail
title: "Transaction log aset di Asset Detail"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.1a#p1", "§8.1a#p2", "§9.7#r20", ASSIGN-LOGIC-06s]
smoke: []
dependsOn: ["Asset Detail: tab Transaction log dan Changelog Asset"]
trace:
  "§8.1a#p1": [4, 5, 6, 8, 39]
  "§8.1a#p2": [10, 11]
  "§9.7#r20": [6, 20, 28]
  ASSIGN-LOGIC-06s: [14, 15, 33]
anchor: [38]
coverage:
  web: automated
---
# Transaction log aset di Asset Detail

## Prerequisites
- Aktor: Aktor Assignment (Asset Admin `Dewi Lestari {runId}`, DU-057-1).
- Layar awal: Asset List.
- Data:
  - DU-057-1: Karyawan `Dewi Lestari {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`, dengan hak Aktor Missing di Group `Head Office`.
  - DU-057-2: Karyawan `Hendra Kusuma {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, anggota Division `Finance {runId}`.
  - DU-057-3: Division `Finance {runId}` dengan PIC `Hendra Kusuma {runId}`.
  - DU-057-4: Division `Operations {runId}`, Division aset `Laptop Acer Aspire 5 {runId}` sebelum ditugaskan.
  - DU-057-5: Aset `Laptop Acer Aspire 5 {runId}`, Group `Head Office`, dengan riwayat satu ASG Assignee Division `Finance {runId}` dan PIC `Hendra Kusuma {runId}`: sudah `Handed over by` `Dewi Lestari {runId}` sehingga Division aset menjadi `Finance {runId}`, lalu `Unassigned by` `Dewi Lestari {runId}` sehingga Division aset kembali `Operations {runId}`. Transaction ID ASG itu milik DU-057-5.
  - DU-057-6: Aset `Monitor LG UltraWide {runId}`, Group `Head Office`, Custody `Available` dengan satu ASG `Waiting for Handover` untuk Assignee `Budi Santoso {runId}`.
  - DU-057-7: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login.
  - DU-057-8: Aset `Tablet Lenovo Tab M10 {runId}`, Group `Head Office`, dengan riwayat satu ASG Assignee Division `Finance {runId}` dan PIC `Hendra Kusuma {runId}`: sudah `Handed over by` `Dewi Lestari {runId}` sehingga Division aset menjadi `Finance {runId}`, lalu baris ditutup lewat Report Missing oleh `Dewi Lestari {runId}` sehingga Division aset kembali `Operations {runId}`.
  - DU-057-9: Aset `Printer Epson L3250 {runId}`, Group `Head Office`, Custody `Available`, dengan riwayat satu ASG Assignee `Budi Santoso {runId}` yang sudah `Assigned` lalu `Unassigned`, dan ada di satu Draft untuk Assignee `Maya Putri {runId}`.
  - DU-057-10: Karyawan `Maya Putri {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login.

## Test Steps

### Transaction log aset memuat kolom dan peristiwa Assignment
1. Ketik Search `Laptop Acer Aspire 5 {runId}`, tekan Enter
2. Buka halaman detail aset `Laptop Acer Aspire 5 {runId}`
3. Buka tab `Transaction log`
4. Verifikasi kolom Assignment `Date`, `Transaction ID`, `Status`, `Reader name`, `Group`, `PIC`, dan `Assignee` tampil
5. Verifikasi baris berstatus `Assigned` tampil dengan Group `Head Office`, PIC `Hendra Kusuma {runId}`, dan Assignee `Finance {runId}`
6. Verifikasi baris berstatus `Unassigned` tampil dengan Group `Head Office`, PIC `Hendra Kusuma {runId}`, dan Assignee `Finance {runId}`
7. Klik Transaction ID pada baris berstatus `Assigned`
8. Verifikasi Assignment Detail terbuka untuk Transaction ID milik DU-057-5

### Satu peristiwa tampil sama di Assignment Log dan Transaction log aset
9. Klik aksi `Assignment Log` pada baris aset `Laptop Acer Aspire 5 {runId}`
10. Verifikasi node `Handed over by [Giver]` tampil dengan pelaku `Dewi Lestari {runId}` di dialog `Assignment Log`
11. Verifikasi node `Unassigned by [Receiver]` tampil dengan pelaku `Dewi Lestari {runId}` di dialog `Assignment Log`

### Changelog Asset mencatat perubahan field Division dengan pelaku Handover dan Unassign
12. Buka halaman detail aset `Laptop Acer Aspire 5 {runId}`
13. Buka tab `Changelog`
14. Verifikasi entri Field `Division` dari `Operations {runId}` menjadi `Finance {runId}` tampil dengan pelaku `Dewi Lestari {runId}` sebagai pelaku Handover
15. Verifikasi entri Field `Division` dari `Finance {runId}` menjadi `Operations {runId}` tampil dengan pelaku `Dewi Lestari {runId}` sebagai pelaku Unassign

### Peristiwa baru langsung tercermin di Transaction log aset
16. Kembali ke daftar aset
17. Ketik Search `Monitor LG UltraWide {runId}`, tekan Enter
18. Buka halaman detail aset `Monitor LG UltraWide {runId}`
19. Buka tab `Transaction log`
20. Verifikasi baris berstatus `Waiting for Handover` tampil dengan Assignee `Budi Santoso {runId}`
21. Buka halaman Transactions > Assignment
22. Ketik Search `Budi Santoso {runId}`, tekan Enter
23. Klik `⋯` pada baris ASG milik Assignee `Budi Santoso {runId}`
24. Klik `Cancel Assignment`
25. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
26. Buka halaman detail aset `Monitor LG UltraWide {runId}`
27. Buka tab `Transaction log`
28. Verifikasi baris berstatus `Canceled` tampil dengan Assignee `Budi Santoso {runId}` sebagai baris baru

### Changelog Asset mencatat penutupan baris lewat Report Missing
29. Kembali ke daftar aset
30. Ketik Search `Tablet Lenovo Tab M10 {runId}`, tekan Enter
31. Buka halaman detail aset `Tablet Lenovo Tab M10 {runId}`
32. Buka tab `Changelog`
33. Verifikasi entri Field `Division` dari `Finance {runId}` menjadi `Operations {runId}` tampil dengan pelaku `Dewi Lestari {runId}` sebagai pelaku penutupan baris lewat Report Missing

### Aset yang ada di Draft tidak menghasilkan baris Transaction log
34. Kembali ke daftar aset
35. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
36. Buka halaman detail aset `Printer Epson L3250 {runId}`
37. Buka tab `Transaction log`
38. Verifikasi baris berstatus `Unassigned` tampil dengan Assignee `Budi Santoso {runId}`
39. Verifikasi tidak ada baris dengan Assignee `Maya Putri {runId}`
