---
id: TC-FA-MYASSET-E2E-026-keputusan-laporan-missing-dep-missing
title: "Keputusan laporan Missing tercermin di My Asset: baris Returned bermarker Missing atau badge hilang"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["§4.1b#r55", "§9.2#r14", "§9.7#r13"]
smoke: []
dependsOn: ["Missing: keputusan laporan Missing oleh Aktor Missing", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.1b#r55": [13, 16]
  "§9.2#r14": [13, 16]
  "§9.7#r13": [7, 13, 16]
anchor: [2, 6, 8, 12]
coverage:
  web: automated
---

# Keputusan laporan Missing tercermin di My Asset: baris Returned bermarker Missing atau badge hilang

## Prerequisites
- Aktor: Borrower, karyawan ber-akun login, pemilik pinjaman dan pelapor laporan Missing di Data. Aktor Missing memicu keputusan laporan Missing dan tidak diamati layarnya.
- Layar awal: My Asset, tab Borrowed.
- Data:
  - DU-026-1: pinjaman Borrowed milik aktor, Name `Laptop Dell Latitude 5420 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `4 days`, Due Date `T0 + 4 hari`, Handed Over At `T0`, dengan laporan Missing berstatus `Waiting for Confirmation` yang dilaporkan aktor sendiri.
  - DU-026-2: pinjaman Borrowed milik aktor, Name `Proyektor Epson EB-X06 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `5 days`, Due Date `T0 + 5 hari`, Handed Over At `T0`, dengan laporan Missing berstatus `Waiting for Confirmation` yang dilaporkan aktor sendiri.

## Test Steps

### Aktor Missing menolak laporan: badge hilang dan baris tetap Borrowed
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Proyektor Epson EB-X06 {runId}` memiliki badge `Reported Missing` di kolom Status sebelum keputusan Aktor Missing
3. Aktor Missing menolak laporan Missing milik DU-026-2
4. Muat ulang halaman
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris `Proyektor Epson EB-X06 {runId}` tampil dengan status `Borrowed`
7. Verifikasi badge `Reported Missing` tidak tampil pada baris `Proyektor Epson EB-X06 {runId}`

### Aktor Missing mengonfirmasi laporan: baris Returned bermarker Missing di tab History
8. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` memiliki badge `Reported Missing` di kolom Status sebelum keputusan Aktor Missing
9. Aktor Missing mengonfirmasi laporan Missing milik DU-026-1
10. Muat ulang halaman
11. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
12. Verifikasi empty state `No results found` tampil di tab Borrowed sesudah konfirmasi Aktor Missing
13. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak tampil di tab Borrowed
14. Klik tab `History`
15. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
16. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berpindah ke tab History dengan badge `Returned` dan badge marker `Missing` di kolom Status
