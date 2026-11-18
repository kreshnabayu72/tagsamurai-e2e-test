---
id: TC-FA-MYASSET-E2E-025-keputusan-damage-report-dep-damaged
title: "Keputusan Damage Report tercermin di tab Borrowed: badge Damaged dan aksi yang tersedia"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r35", "§4.1b#r50", "§4.1b#r67", "§9.7#r12"]
smoke: []
dependsOn: ["Damaged: keputusan Damage Report oleh Aktor Damaged", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r35": [6, 11, 14, 16, 17, 23, 25]
  "§4.1b#r50": [6, 14, 25]
  "§4.1b#r67": [15]
  "§9.7#r12": [11, 12, 23]
anchor: [2, 3, 5, 22]
coverage:
  web: automated
---

# Keputusan Damage Report tercermin di tab Borrowed: badge Damaged dan aksi yang tersedia

## Prerequisites
- Aktor: Borrower, karyawan ber-akun login, pemilik pinjaman dan pelapor Damage Report di Data. Aktor Damaged memicu keputusan Damage Report dan tidak diamati layarnya.
- Layar awal: My Asset, tab Borrowed.
- Data:
  - DU-025-1: pinjaman Borrowed milik aktor, Name `Laptop Dell Latitude 5420 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `4 days`, Due Date `T0 + 4 hari`, Handed Over At `T0`, dengan Damage Report berstatus `Waiting for Confirmation` yang dilaporkan aktor sendiri.
  - DU-025-2: pinjaman Borrowed milik aktor, Name `Proyektor Epson EB-X06 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `5 days`, Due Date `T0 + 5 hari`, Handed Over At `T0`, dengan Damage Report berstatus `Waiting for Confirmation` yang dilaporkan aktor sendiri.

## Test Steps

### Damage Report menunggu konfirmasi: Report Missing tidak tersedia
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memiliki badge `Reported Damaged` di kolom Status sebelum keputusan Aktor Damaged
3. Verifikasi baris `Proyektor Epson EB-X06 {runId}` memiliki badge `Reported Damaged` di kolom Status sebelum keputusan Aktor Damaged
4. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
5. Verifikasi aksi `Cancel Damage Report` tampil di menu baris
6. Verifikasi aksi `Report Missing` tidak tampil di menu baris selama Damage Report menunggu konfirmasi
7. Tekan `Esc` untuk menutup menu baris

### Aktor Damaged mengonfirmasi laporan: badge Damaged dan aksi menyesuaikan
8. Aktor Damaged mengonfirmasi Damage Report milik DU-025-1
9. Muat ulang halaman
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memiliki badge `Damaged` di kolom Status
12. Verifikasi badge `Reported Damaged` tidak tampil pada baris `Laptop Dell Latitude 5420 {runId}`
13. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
14. Verifikasi aksi `Report Missing` tampil di menu baris
15. Verifikasi aksi `Cancel Damage Report` tidak tampil di menu baris
16. Verifikasi aksi `Request Extension` tidak tampil di menu baris sesudah keputusan Damaged
17. Verifikasi aksi `Report Damaged` tidak tampil di menu baris sesudah keputusan Damaged
18. Tekan `Esc` untuk menutup menu baris

### Aktor Damaged menolak laporan: badge hilang dan aksi tampil lagi
19. Aktor Damaged menolak Damage Report milik DU-025-2
20. Muat ulang halaman
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi baris `Proyektor Epson EB-X06 {runId}` berstatus `Borrowed`
23. Verifikasi badge `Reported Damaged` tidak tampil pada baris `Proyektor Epson EB-X06 {runId}`
24. Klik menu `⋯` pada baris `Proyektor Epson EB-X06 {runId}`
25. Verifikasi aksi `Request Extension`, `Report Damaged`, dan `Report Missing` tampil di menu baris
26. Tekan `Esc` untuk menutup menu baris
