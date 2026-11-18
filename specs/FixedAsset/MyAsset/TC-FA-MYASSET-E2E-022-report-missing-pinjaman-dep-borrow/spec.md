---
id: TC-FA-MYASSET-E2E-022-report-missing-pinjaman-dep-borrow
title: "Report Missing pada pinjaman oleh pemegang: badge Reported Missing dan baris tetap Borrowed"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r8", "§4.1b#r49", "§4.1b#r51", "§4.1b#r52", "§4.1b#r53", "§4.1b#r54", "§4.4#r10", "§4.8#r9", "§7.3#r7", "§9.2#r10", "§9.2#r12", "§9.4.3#b6", "§9.6#r5", "§9.7#r13", "EB-FB-1@report-missing"]
smoke: ["EB-FB-1@report-missing"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§2.1#r8": [3, 7]
  "§4.1b#r49": [3]
  "§4.1b#r51": [5]
  "§4.1b#r52": [7]
  "§4.1b#r53": [10, 34]
  "§4.1b#r54": [14, 15, 16, 24, 27]
  "§4.4#r10": [5, 7]
  "§4.8#r9": [3]
  "§7.3#r7": [7]
  "§9.2#r10": [10]
  "§9.2#r12": [11, 30, 35]
  "§9.4.3#b6": [11]
  "§9.6#r5": [7, 10]
  "§9.7#r13": [10]
  "EB-FB-1@report-missing": [7]
anchor: [13, 19, 23, 26]
coverage:
  web: automated
---

# Report Missing pada pinjaman oleh pemegang: badge Reported Missing dan baris tetap Borrowed

## Prerequisites
- Aktor: Borrower, karyawan ber-akun login yang tidak memegang hak Aktor Missing pada Group aset, pemilik pinjaman di Data.
- Layar awal: My Asset, tab Borrowed.
- Data:
  - DU-022-1: pinjaman Borrowed milik aktor, Name `Laptop Dell Latitude 5420 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `4 days`, Due Date `T0 + 4 hari`, Handed Over At `T0`, tanpa laporan Missing.
  - DU-022-2: pinjaman milik aktor dengan pengajuan Extend yang menunggu review, Name `Proyektor Epson EB-X06 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Extension Request`, Borrower `Me`, Source `Admin`, Duration `5 days`, Due Date `T0 + 5 hari`, Handed Over At `T0`, tanpa laporan Missing.
  - DU-022-3: pinjaman Overdue milik aktor, Name `Kamera Mirrorless Sony A6400 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Overdue`, Borrower `Me`, Source `Admin`, Duration `2 days`, Due Date `T0 - 3 hari`, Handed Over At `T0 - 5 hari`, tanpa laporan Missing.

## Test Steps

### Report Missing oleh pemegang berhasil dengan toast
1. Ketik Search `{runId}`, tekan Enter
2. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi aksi `Report Missing` tampil di menu baris
4. Klik `Report Missing`
5. Verifikasi dialog `Report Missing` tampil
6. Klik `[Report Missing]`
7. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Badge Reported Missing dan baris tetap Borrowed
8. Muat ulang halaman
9. Ketik Search `{runId}`, tekan Enter
10. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memiliki badge `Reported Missing` di kolom Status
11. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tetap berstatus `Borrowed` di tab Borrowed
12. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
13. Verifikasi aksi `Borrow Log` tampil di menu baris sesudah laporan kehilangan dikirim
14. Verifikasi aksi `Request Extension` tidak tampil di menu baris sesudah Report Missing
15. Verifikasi aksi `Report Damaged` tidak tampil di menu baris sesudah Report Missing
16. Verifikasi aksi `Report Missing` tidak tampil di menu baris sesudah Report Missing
17. Tekan `Esc` untuk menutup menu baris

### Pengajuan Extend yang menunggu ditutup saat Report Missing
18. Ganti isi kotak search dengan `Proyektor Epson EB-X06 {runId}`, tekan Enter
19. Verifikasi baris `Proyektor Epson EB-X06 {runId}` berstatus `Extension Request` sebelum Report Missing
20. Klik menu `⋯` pada baris `Proyektor Epson EB-X06 {runId}`
21. Klik `Report Missing`
22. Klik `[Report Missing]`
23. Verifikasi baris `Proyektor Epson EB-X06 {runId}` memiliki badge `Reported Missing` di kolom Status sesudah Report Missing
24. Verifikasi badge `Extension Request` tidak tampil pada baris `Proyektor Epson EB-X06 {runId}` sesudah Report Missing
25. Klik menu `⋯` pada baris `Proyektor Epson EB-X06 {runId}`
26. Verifikasi aksi `Borrow Log` tampil di menu baris sesudah laporan kehilangan dikirim
27. Verifikasi aksi `Cancel Extension Request` tidak tampil di menu baris sesudah Report Missing
28. Tekan `Esc` untuk menutup menu baris

### Report Missing pada pinjaman Overdue: baris tetap Overdue
29. Ganti isi kotak search dengan `Kamera Mirrorless Sony A6400 {runId}`, tekan Enter
30. Verifikasi baris `Kamera Mirrorless Sony A6400 {runId}` berstatus `Overdue` sebelum Report Missing
31. Klik menu `⋯` pada baris `Kamera Mirrorless Sony A6400 {runId}`
32. Klik `Report Missing`
33. Klik `[Report Missing]`
34. Verifikasi baris `Kamera Mirrorless Sony A6400 {runId}` memiliki badge `Reported Missing` di kolom Status sesudah Report Missing
35. Verifikasi baris `Kamera Mirrorless Sony A6400 {runId}` tetap berstatus `Overdue` di tab Borrowed sesudah Report Missing
