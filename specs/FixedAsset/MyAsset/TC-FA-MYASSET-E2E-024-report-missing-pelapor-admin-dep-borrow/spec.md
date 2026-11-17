---
id: TC-FA-MYASSET-E2E-024-report-missing-pelapor-admin-dep-borrow
title: "Report Missing oleh pemegang yang memegang hak Aktor Missing: baris langsung ditutup ke tab History"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["§4.1b#r52", "§4.1b#r53", "§4.4#r10", "§7.3#r8", "§9.2#r11"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.1b#r52": [6]
  "§4.1b#r53": [14]
  "§4.4#r10": [4, 6]
  "§7.3#r8": [6]
  "§9.2#r11": [10, 13]
anchor: [9]
coverage:
  web: automated
---

# Report Missing oleh pemegang yang memegang hak Aktor Missing: baris langsung ditutup ke tab History

## Prerequisites
- Aktor: Borrower, karyawan ber-akun login yang juga memegang hak Aktor Missing pada Group aset, pemilik pinjaman di Data.
- Layar awal: My Asset, tab Borrowed.
- Data:
  - DU-024-1: pinjaman Borrowed milik aktor, Name `Laptop Dell Latitude 5420 {runId}` (Name yang tampil memuat Increment bentukan server), Group `Head Office`, Brand `—`, Model/Type `—`, Status `Borrowed`, Borrower `Me`, Source `Admin`, Duration `4 days`, Due Date `T0 + 4 hari`, Handed Over At `T0`, tanpa laporan Missing.

## Test Steps

### Report Missing oleh pelapor admin berhasil dengan toast
1. Ketik Search `{runId}`, tekan Enter
2. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Klik `Report Missing`
4. Verifikasi dialog `Report Missing` tampil
5. Klik `[Report Missing]`
6. Verifikasi toast sukses dengan awalan `Success,` tampil

### Baris ditutup ke tab History tanpa badge Reported Missing
7. Muat ulang halaman
8. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
9. Verifikasi empty state `No results found` tampil di tab Borrowed sesudah Report Missing oleh pelapor admin
10. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak tampil di tab Borrowed
11. Klik tab `History`
12. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
13. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berpindah ke tab History dengan badge `Returned` dan badge marker `Missing` di kolom Status
14. Verifikasi badge `Reported Missing` tidak tampil pada baris `Laptop Dell Latitude 5420 {runId}`
