---
id: TC-FA-BORROW-E2E-044-report-damaged-dipinjam-dep-damaged
title: "Report Damaged saat dipinjam membuat laporan Waiting for Confirmation dan memblok Extend sampai laporan selesai"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["DM-BRW-11"]
smoke: []
dependsOn: ["Damaged: dialog Report Damaged dan keputusan laporan"]
trace:
  "DM-BRW-11": [10, 11, 13, 15, 19]
anchor: []
coverage:
  web: automated
---

# Report Damaged saat dipinjam membuat laporan Waiting for Confirmation dan memblok Extend sampai laporan selesai

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office` tanpa hak Aktor Damaged; ia bukan Borrower maupun PIC pada BRW di spec ini. Aktor kedua: `Siti Rahma {runId}`, Group Manager pada Group `Head Office` dengan hak Aktor Damaged; ia memutuskan laporan di layar kedua.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-044-1: BRW Group `Head Office`, Borrower `Hendra Kusuma {runId}`, berisi baris `Borrowed` aset DU-044-2.
  - DU-044-2: aset `Kamera Canon EOS R6 {runId}`, baris `Borrowed`, Due date T0 + 3 hari.

## Test Steps

### Report Damaged dari Borrow Detail membuat laporan Waiting for Confirmation
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
4. Buka Borrow Detail BRW milik DU-044-1 dari tabel Transactions
5. Klik menu ⋯ pada baris aset DU-044-2
6. Klik `Report Damaged`
7. Unggah foto `lensa-retak.jpg` pada dialog `Report Damaged`
8. Isi What happened dengan `Lensa kamera retak terkena benturan`
9. Kirim laporan pada dialog `Report Damaged`
10. Verifikasi toast `Success, damage report has been sent to the Asset Admin.` tampil
11. Verifikasi baris aset DU-044-2 berstatus `Borrowed` dengan badge `Reported Damaged`

### Laporan menunggu keputusan Aktor Damaged dan Extend diblokir
12. Aktor kedua membuka menu Damaged dan memilih laporan milik DU-044-3
13. Verifikasi laporan milik DU-044-3 berstatus `Waiting for Confirmation` di layar Aktor Damaged
14. Klik menu ⋯ pada baris aset DU-044-2 di Borrow Detail BRW milik DU-044-1 pada layar Aktor Borrow
15. Verifikasi alasan `This asset has a damage report. Return it first.` tersampaikan pada aksi `Request Extension` yang disabled

### Laporan yang ditolak Aktor Damaged membuka kembali Extend
16. Aktor kedua menolak laporan milik DU-044-3
17. Muat ulang halaman Borrow Detail BRW milik DU-044-1 pada layar Aktor Borrow
18. Klik menu ⋯ pada baris aset DU-044-2
19. Verifikasi aksi `Request Extension` pada baris aset DU-044-2 aktif kembali
