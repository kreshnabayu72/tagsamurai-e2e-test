---
id: TC-FA-MYASSET-E2E-020-report-damaged-pinjaman-dep-borrow
title: "Report Damaged pada pinjaman: badge Reported Damaged dan aksi Extend tidak tampil lagi"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r7", "§4.1b#r40", "§4.1b#r43", "§4.1b#r44", "§4.1b#r45", "§4.1b#r46", "§4.1b#r47", "§4.1b#r48", "§4.4#r9", "§4.8#r8", "§7.3#r6", "§9.2#r15", "§9.2#r16", "§9.2#r17", "§9.6#r8", "§9.7#r12", "EB-FB-1@report-damaged"]
smoke: ["EB-FB-1@report-damaged"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§2.1#r7": [3, 13]
  "§4.1b#r40": [3]
  "§4.1b#r43": [5]
  "§4.1b#r44": [6, 7, 9]
  "§4.1b#r45": [13]
  "§4.1b#r46": [16]
  "§4.1b#r47": [20, 21]
  "§4.1b#r48": [32, 35]
  "§4.4#r9": [5, 13, 16]
  "§4.8#r8": [3]
  "§7.3#r6": [13]
  "§9.2#r15": [16]
  "§9.2#r16": [17]
  "§9.2#r17": [20]
  "§9.6#r8": [13, 16]
  "§9.7#r12": [16]
  "EB-FB-1@report-damaged": [13]
anchor: [19, 24, 26, 31, 34]
coverage:
  web: automated
---

# Report Damaged pada pinjaman: badge Reported Damaged dan aksi Extend tidak tampil lagi

## Prerequisites
- Aktor: Borrower, karyawan ber-akun login, pemilik pinjaman di Data.
- Layar awal: My Asset, tab Borrowed.
- Data:
  - DU-020-1: pinjaman Borrowed milik aktor, Name `Laptop Dell Latitude 5420 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `4 days`, Due Date `T0 + 4 hari`, Handed Over At `T0`, tanpa Damage Report.
  - DU-020-3: pinjaman milik aktor dengan pengajuan Extend yang menunggu review, Name `Proyektor Epson EB-X06 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Extension Request`, Borrower `Me`, Source `Admin`, Duration `5 days`, Due Date `T0 + 5 hari`, Handed Over At `T0`, tanpa Damage Report.

## Test Steps

### Report Damaged ditolak tanpa isian wajib dan berhasil dengan isian lengkap
1. Ketik Search `{runId}`, tekan Enter
2. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi aksi `Request Extension` dan `Report Damaged` tampil di menu baris
4. Klik `Report Damaged`
5. Verifikasi dialog `Report Damaged` tampil
6. Verifikasi field `Damaged Photo` ditandai wajib
7. Verifikasi field `What happened` ditandai wajib
8. Klik `[Report Damaged]` tanpa mengisi field apa pun
9. Verifikasi dialog `Report Damaged` tetap tampil
10. Isi `Damaged Photo` dengan berkas `kerusakan-laptop.jpg`
11. Isi `What happened` dengan `Layar laptop retak setelah terjatuh dari meja rapat`
12. Klik `[Report Damaged]`
13. Verifikasi toast `Success, damage report has been sent to the Asset Admin.` tampil

### Badge Reported Damaged dan aksi menu sesudah Report Damaged
14. Muat ulang halaman
15. Ketik Search `{runId}`, tekan Enter
16. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memiliki badge `Reported Damaged` di kolom Status
17. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tetap berstatus `Borrowed`
18. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
19. Verifikasi aksi `Borrow Log` tampil di menu baris sesudah laporan kerusakan dikirim
20. Verifikasi aksi `Request Extension` tidak tampil di menu baris sesudah Report Damaged
21. Verifikasi aksi `Report Damaged` tidak tampil di menu baris sesudah Report Damaged
22. Tekan `Esc` untuk menutup menu baris

### Pengajuan Extend yang menunggu ditutup saat Report Damaged
23. Ganti isi kotak search dengan `Proyektor Epson EB-X06 {runId}`, tekan Enter
24. Verifikasi baris `Proyektor Epson EB-X06 {runId}` berstatus `Extension Request` sebelum Report Damaged
25. Klik menu `⋯` pada baris `Proyektor Epson EB-X06 {runId}`
26. Verifikasi aksi `Cancel Extension Request` tampil di menu baris
27. Klik `Report Damaged`
28. Isi `Damaged Photo` dengan berkas `kerusakan-proyektor.jpg`
29. Isi `What happened` dengan `Lensa proyektor pecah saat dipindahkan`
30. Klik `[Report Damaged]`
31. Verifikasi baris `Proyektor Epson EB-X06 {runId}` memiliki badge `Reported Damaged` di kolom Status sesudah Report Damaged
32. Verifikasi badge `Extension Request` tidak tampil pada baris `Proyektor Epson EB-X06 {runId}` sesudah Report Damaged
33. Klik menu `⋯` pada baris `Proyektor Epson EB-X06 {runId}`
34. Verifikasi aksi `Borrow Log` tampil di menu baris sesudah laporan kerusakan dikirim
35. Verifikasi aksi `Cancel Extension Request` tidak tampil di menu baris sesudah Report Damaged
36. Tekan `Esc` untuk menutup menu baris
