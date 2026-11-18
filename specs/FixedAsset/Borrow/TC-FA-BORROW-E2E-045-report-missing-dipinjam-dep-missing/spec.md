---
id: TC-FA-BORROW-E2E-045-report-missing-dipinjam-dep-missing
title: "Report Missing saat dipinjam menutup baris Returned dengan penanda Missing atau menunggu konfirmasi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["DM-BRW-13"]
smoke: []
dependsOn: ["Missing: dialog Report Missing dan keputusan laporan"]
trace:
  "DM-BRW-13": [9, 17, 20]
anchor: []
coverage:
  web: automated
---

# Report Missing saat dipinjam menutup baris Returned dengan penanda Missing atau menunggu konfirmasi

## Prerequisites
- Aktor: `Siti Rahma {runId}`, Group Manager (Aktor Borrow) pada Group `Head Office` dengan hak Aktor Missing; ia bukan Borrower maupun PIC pada BRW di spec ini. Aktor kedua: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office` tanpa hak Aktor Missing.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-045-1: BRW Group `Head Office`, Borrower `Indra Gunawan {runId}`, berisi baris `Borrowed` aset DU-045-2 dan DU-045-3.
  - DU-045-2: aset `Handycam Sony FDR {runId}`, baris `Borrowed`, Due date T0 + 3 hari.
  - DU-045-3: aset `Speaker JBL PartyBox {runId}`, baris `Borrowed`, Due date T0 + 3 hari.

## Test Steps

### Report Missing oleh Aktor Borrow dengan hak Aktor Missing menutup baris Returned dengan penanda Missing
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Indra Gunawan {runId}`, tekan Enter
4. Buka Borrow Detail BRW milik DU-045-1 dari tabel Transactions
5. Klik menu ⋯ pada baris aset DU-045-2
6. Klik `Report Missing`
7. Isi Reason dengan `Handycam tidak ditemukan saat pengecekan lapangan`
8. Kirim laporan pada dialog `Report Missing`
9. Verifikasi baris aset DU-045-2 berstatus `Returned` dengan penanda `Missing`

### Report Missing oleh Aktor Borrow tanpa hak Aktor Missing menunggu konfirmasi
10. Aktor kedua membuka Transactions > Borrow dan mengetik Search `Indra Gunawan {runId}`, tekan Enter
11. Aktor kedua membuka Borrow Detail BRW milik DU-045-1 dari tabel Transactions
12. Aktor kedua mengklik menu ⋯ pada baris aset DU-045-3
13. Aktor kedua mengklik `Report Missing`
14. Aktor kedua mengisi Reason dengan `Speaker tidak kembali dari lokasi acara`
15. Aktor kedua mengirim laporan pada dialog `Report Missing`
16. Muat ulang halaman Borrow Detail BRW milik DU-045-1 pada layar Aktor kedua
17. Verifikasi baris aset DU-045-3 berstatus `Borrowed` dengan badge `Reported Missing`

### Konfirmasi Aktor Missing menutup baris Returned dengan penanda Missing
18. Aktor pertama membuka menu Missing dan memilih laporan milik DU-045-3
19. Aktor pertama mengonfirmasi laporan milik DU-045-3
20. Verifikasi baris aset DU-045-3 berstatus `Returned` dengan penanda `Missing` di Borrow Detail BRW milik DU-045-1 setelah dimuat ulang
