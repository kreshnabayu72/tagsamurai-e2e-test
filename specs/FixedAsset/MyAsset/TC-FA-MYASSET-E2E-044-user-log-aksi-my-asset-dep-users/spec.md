---
id: TC-FA-MYASSET-E2E-044-user-log-aksi-my-asset-dep-users
title: "Aksi My Asset terbaca di User Detail > User Log > Borrow"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§8#p1", "§8#r3"]
smoke: []
dependsOn: ["Users: Borrower tanpa akun beserta PIC-nya, dan User Detail > User Log", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§8#p1": [14, 15]
  "§8#r3": 14
anchor: []
coverage:
  web: automated
---

# Aksi My Asset terbaca di User Detail > User Log > Borrow

## Prerequisites
- Aktor: Total Control `Eko Prasetyo {runId}` (DU-044-1), yang juga Borrower atas pinjamannya sendiri.
- Layar awal: halaman masuk Fixed Asset.
- Data:
  - DU-044-1: pengguna `Eko Prasetyo {runId}`, role `Total Control`, Group `Head Office`.
  - DU-044-2: pinjaman aset `Headset Jabra Evolve2 {runId}`, Group `Head Office`, Status `Waiting for Approval`, Source `Admin`, Borrower `Me`. User Log Borrow aktor untuk pinjaman ini memuat 1 entri dengan Activity `Borrow requested`.
- Kondisi:
  - Tab Borrowed aktor memuat 1 baris, yaitu DU-044-2.

## Test Steps

### Cancel Borrow dari My Asset tercatat di User Log Borrow
1. Masuk sebagai Total Control `Eko Prasetyo {runId}`
2. Buka User Detail `Eko Prasetyo {runId}` dari Users
3. Klik tab `User Log`
4. Klik sub-tab `Borrow`
5. Catat jumlah entri User Log Borrow untuk pinjaman `Headset Jabra Evolve2 {runId}`
6. Buka `My Asset` dari menu profil pada navbar
7. Klik tab `Borrowed`
8. Buka menu `⋯` pada baris `Headset Jabra Evolve2 {runId}`
9. Klik `Cancel Borrow`
10. Klik `[Cancel Borrow]` pada dialog `Cancel Borrow`
11. Buka User Detail `Eko Prasetyo {runId}` dari Users
12. Klik tab `User Log`
13. Klik sub-tab `Borrow`
14. Verifikasi User Log Borrow memuat entri baru dengan Activity `Canceled` untuk pinjaman `Headset Jabra Evolve2 {runId}`, sehingga jumlah entri untuk pinjaman itu bertambah satu dari jumlah yang dicatat pada langkah 5
15. Verifikasi entri dengan Activity `Borrow requested` untuk pinjaman `Headset Jabra Evolve2 {runId}` tetap tampil
